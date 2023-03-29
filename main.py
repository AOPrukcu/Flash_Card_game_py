BACKGROUND_COLOR = "#B1DDC6"
import  pandas
from tkinter import messagebox
from tkinter import  *
import random

new_key = {}
to_learn_dic = {}

try:
    file = pandas.read_csv("data/worlds_to_learn.csv.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn_dic = original_data.to_dict(orient="records")

else:
    to_learn_dic = file.to_dict(orient="records")



new_key = {}

def next_card():
    global new_key,flip_timer,used_word
    window.after_cancel(flip_timer)
    new_key = random.choice(to_learn_dic)
    new_word = new_key["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=new_word, fill="black")
    canvas.itemconfig(canvas_image,image= card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn_dic.remove(new_key)
    print(len(to_learn_dic))
    data = pandas.DataFrame(to_learn_dic)
    data.to_csv("data/worlds_to_learn.csv",index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=new_key["English"],fill="white")
    canvas.itemconfig(canvas_image,image=card_back_image)





window = Tk()
window.title = ("Flashy")
window.config(padx=50,pady=50,highlightthickness=0,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file="images/card_front.png")
# canvas first values is coordinates
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image= card_front_image)
card_title = canvas.create_text(400,150,text="", font=("Ariel", 40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel", 60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)


# cross button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(column=0, row=1)

# right button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(column=1, row=1)

next_card()



window.mainloop()