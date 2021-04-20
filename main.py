from tkinter import *
import pandas as pd
import random

BACKGROUND = "#B1DDC6"
CANVAS_BACKGROUND = "#FFFFFF"
CARD_TITLE_FONT = "Rubik", 40, "italic"
CARD_WORD_LOOK = "Rubik", 60, "bold"

df = pd.read_csv("data/french_words.csv")
to_learn = df.to_dict(orient="records")
current_card = {}


def next_card():
    # data = {row.French: row.English for (index, row) in df.iterrows()}
    global current_card, TIMER
    window.after_cancel(TIMER)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    TIMER = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard Capstone Project")
window.config(padx=50, pady=50, background=BACKGROUND)

TIMER = window.after(3000, func=flip_card)

# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526,
                background=BACKGROUND, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(
    400, 150, text="", font=CARD_TITLE_FONT)
card_word = canvas.create_text(
    400, 263, text="", font=CARD_WORD_LOOK)

# Buttons
wrong_mark = Button(image=wrong_image, highlightthickness=0,
                    command=next_card)
wrong_mark.grid(column=0, row=1)
wrong_mark.config(padx=50, pady=50)

right_mark = Button(image=right_image, highlightthickness=0,
                    command=next_card)
right_mark.grid(column=1, row=1)
right_mark.config(padx=50, pady=50)

next_card()


window.mainloop()
