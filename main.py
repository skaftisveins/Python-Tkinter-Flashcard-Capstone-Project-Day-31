from tkinter import *
import pandas as pd
import random

BACKGROUND = "#B1DDC6"
CANVAS_BACKGROUND = "#FFFFFF"
UPPER_FONT_LOOK = "Rubik", 40, "italic"
LOWER_FONT_LOOK = "Rubik", 60, "bold"


# --------------------- GENERATE A RANDOM WORD  ----------------------- #

def generate_random_word():
    df = pd.read_csv("data/french_words.csv")
    data = {row.French: row.English for (index, row) in df.iterrows()}
    random_french_word = random.choice(list(data.items()))
    canvas.itemconfig(upper_text, text=random_french_word[0])
    canvas.itemconfig(lower_text, text=random_french_word[1])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard Capstone Project")
window.config(padx=50, pady=50, background=BACKGROUND)

# Images
card_front_img = PhotoImage(file="images/card_front.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526,
                background=BACKGROUND, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
upper_text = canvas.create_text(
    400, 150, text="Title", font=(UPPER_FONT_LOOK))
lower_text = canvas.create_text(
    400, 263, text="text", font=(LOWER_FONT_LOOK))

# Buttons
wrong_mark = Button(image=wrong_image, highlightthickness=0,
                    command=generate_random_word)
wrong_mark.grid(column=0, row=1)
wrong_mark.config(padx=50, pady=50)

right_mark = Button(image=right_image, highlightthickness=0,
                    command=generate_random_word)
right_mark.grid(column=1, row=1)
right_mark.config(padx=50, pady=50)

generate_random_word()


window.mainloop()
