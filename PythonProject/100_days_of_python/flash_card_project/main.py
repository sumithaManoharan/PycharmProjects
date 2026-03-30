from tkinter import *
import pandas as pd
import random


# ---------------------------- CONSTANTS & SETUP ----------------------- #
BACKGROUND_COLOR = "#B1DDC6"
SESSION_SIZE = 10  # Change this to however many cards you want to see
current_card = {}
to_learn_this_session = []  # Words you got wrong today

# Load Data
try:
    data = pd.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    print("Error: french_words.csv not found in data folder.")
    exit()

# Shuffle the entire deck and take a small sample for this session
full_list = data.to_dict(orient="records")
session_list = random.sample(full_list, SESSION_SIZE)


# ---------------------------- LOGIC ---------------------------------- #
def restart_game():
    global session_list, to_learn_this_session

    # 1. Reshuffle and get new cards
    session_list = random.sample(full_list, SESSION_SIZE)
    to_learn_this_session = []

    # 2. Put the buttons back
    unknown_button.grid(row=2, column=0)
    known_button.grid(row=2, column=1)

    # 3. Hide the restart button
    restart_button.grid_forget()

    # 4. Start the first card
    create_card()

def update_progress():
    # Calculate width: (Items done / Total items) * Total Pixel Width
    items_done = SESSION_SIZE - len(session_list)
    new_width = (items_done / SESSION_SIZE) * 800
    progress_bg.coords(progress_bar, 0, 0, new_width, 10)

def create_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    update_progress()

    if len(session_list) > 0:
        current_card = session_list.pop()  # Take the last card out of the session

        canvas.itemconfig(card_background, image=card_f)
        canvas.itemconfig(lang_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=current_card["French"], fill="black")

        flip_timer = window.after(3000, func=flip_card)
    else:
        show_results()


def flip_card():
    canvas.itemconfig(card_background, image=card_b)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    # If they know it, we just move on. It's already removed from session_list via .pop()
    if current_card in full_list:
        full_list.remove(current_card)
    create_card()


def is_unknown():
    # If they don't know it, save it to the "to_learn" list
    to_learn_this_session.append(current_card)
    create_card()


def show_results():
    # 1. STOP THE TIMER
    # This prevents the English flip from hijacking the screen while you read results
    window.after_cancel(flip_timer)

    # 2. SAVE THE DATA
    # Update the master list CSV (removes all words you got right during this session)
    df_master = pd.DataFrame(full_list)
    df_master.to_csv("data/french_words_to_learn.csv", index=False)

    # 3. CONSTRUCT THE MESSAGE
    if to_learn_this_session:
        # Save only the words you missed today for quick review
        df_session = pd.DataFrame(to_learn_this_session)
        df_session.to_csv("data/needs_review.csv", index=False)
        msg = f"Session Over!\n{len(to_learn_this_session)} words missed.\nProgress saved to Master list."
    else:
        msg = "Perfect Score!\nMaster list updated!"

    # 4. UPDATE THE UI
    # Hide the Tick/Cross buttons
    unknown_button.grid_forget()
    known_button.grid_forget()

    # Show the Restart button (make sure it spans both columns)
    restart_button.grid(row=2, column=0, columnspan=2, pady=20)

    # Update the main card to show the final message
    canvas.itemconfig(card_background, image=card_f)
    canvas.itemconfig(lang_text, text="Results", fill="black")
    canvas.itemconfig(word_text, text=msg, font=("Ariel", 20, "bold"), fill="black")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy - Session Mode")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_f = PhotoImage(file="images/card_front.png")
card_b = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_f)
lang_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=is_unknown,borderwidth=0,bg=BACKGROUND_COLOR,border=0,activebackground=BACKGROUND_COLOR)
unknown_button.grid(row=1, column=0)

# Restart Button (hidden at start)
restart_button = Button(text="Play Again", font=("Ariel", 15, "bold"),command=restart_game, bg="white", highlightthickness=0)
# We don't .grid() it yet because it only appears at the end
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known,borderwidth=0,bg=BACKGROUND_COLOR,border=0,activebackground=BACKGROUND_COLOR)
known_button.grid(row=1, column=1)
known_button.grid(row=1, column=1)

# 1. Progress Bar in Row 0
progress_bg = Canvas(width=800, height=10, bg="white", highlightthickness=0)
progress_bg.grid(row=0, column=0, columnspan=2, pady=(0, 20)) # Added columnspan and padding

# 2. Main Card Canvas moves to Row 1
canvas.grid(row=1, column=0, columnspan=2)

# 3. Buttons move to Row 2
unknown_button.grid(row=2, column=0)
known_button.grid(row=2, column=1)

# The actual moving bar (starts at width 0)
progress_bar = progress_bg.create_rectangle(0, 0, 0, 10, fill="#4AA96C", outline="")


create_card()
window.mainloop()