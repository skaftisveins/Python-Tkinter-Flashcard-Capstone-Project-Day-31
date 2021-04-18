from tkinter import *

BACKGROUND = "#B1DDC6"
CANVAS_BACKGROUND = "#FFFFFF"
UPPER_FONT_LOOK = "Rubik", 40, "italic"
LOWER_FONT_LOOK = "Rubik", 60, "bold"


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
canvas.create_text(400, 150, text="Title", font=(UPPER_FONT_LOOK))
canvas.create_text(400, 263, text="word", font=(LOWER_FONT_LOOK))

# Buttons
wrong_mark = Button(image=wrong_image, highlightthickness=0)
wrong_mark.grid(column=0, row=1)
wrong_mark.config(padx=50, pady=50)

right_mark = Button(image=right_image, highlightthickness=0)
right_mark.grid(column=1, row=1)
right_mark.config(padx=50, pady=50)

window.mainloop()
