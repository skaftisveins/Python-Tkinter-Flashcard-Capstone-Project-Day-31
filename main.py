from tkinter import *
import pandas as pd
import random

BACKGROUND = "#B1DDC6"
CANVAS_BACKGROUND = "#FFFFFF"
CARD_TITLE_FONT = "Rubik", 40, "italic"
CARD_WORD_FONT = "Rubik", 60, "bold"
current_card = {}
to_learn = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    existing_data = pd.read_csv("data/french_words.csv")
    to_learn = existing_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


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


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    learn_data = pd.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


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
    400, 263, text="", font=CARD_WORD_FONT)

# Buttons
unknown_card = Button(image=wrong_image, highlightthickness=0,
                      command=next_card)
unknown_card.grid(column=0, row=1)
unknown_card.config(padx=50, pady=50)

known_card = Button(image=right_image, highlightthickness=0,
                    command=is_known)
known_card.grid(column=1, row=1)
known_card.config(padx=50, pady=50)

next_card()

window.mainloop()
