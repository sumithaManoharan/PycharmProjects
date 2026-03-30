from tkinter import *
from tkinter import messagebox
import pygame, os, random, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#E83C91"
RED = "#BF1A1A"
GREEN = "#5C6F2B"
YELLOW = "#f7f5dd"
BROWN = "#9E3B3B"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
flags = ""
timer = None
is_muted =False
# ----------------------------MUSIC LOGIC----------------------------------#
# Add specific arguments to init to help Ubuntu audio sync
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()


def play_music():
    folder_path = os.path.join(os.getcwd(), "musics") # Removed trailing slash for os.path.join

    # Verify the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} not found.")
        return

    songs = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

    if songs:
        random_song = random.choice(songs)
        full_path = os.path.join(folder_path, random_song)

        try:
            pygame.mixer.music.load(full_path)
            pygame.mixer.music.set_volume(0.7)  # Ensure volume is up
            pygame.mixer.music.play()
            music_label.config(text=f"🎵{random_song}",fg=BROWN)
            print(f"Now playing: {random_song}")  # Debug print to console
        except pygame.error as e:
            print(f"Pygame error: {e}")
    else:
        print("No MP3 files found in the directory.")

def toggle_mute():
    global is_muted
    if not is_muted:
        pygame.mixer.music.set_volume(0.0)
        mute_button.config(text="🔇 Muted")
        is_muted = True
    else:
        pygame.mixer.music.set_volume(0.7)
        mute_button.config(text="🔊 Mute")
        is_muted = False


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer, flags, reps

    sessions_completed = len(flags)
    total_work_min = sessions_completed * WORK_MIN

    stats_msg = f"Session Completed: {sessions_completed}\nTotal Work Time: {total_work_min}"
    if sessions_completed >= 4:
        stats_msg += "\n\n🌟 Amazing job! You're in the flow state. Keep that momentum going!"
    elif sessions_completed > 0:
        stats_msg += "\n\nGood start! Every minute counts toward your goals. 🚀"
    else:
        stats_msg = "No sessions completed yet. Let's get to work! 💪"

        # 3. Show the Pop-up BEFORE resetting the variables
    messagebox.showinfo(title="Session Summary", message=stats_msg)
    #reset

    window.after_cancel(timer)
    pygame.mixer.music.stop()


    # Reset Variables

    reps = 0
    flags = ""

    #label reset

    start_button.config(text="Start", state="active")
    canvas.itemconfig(time_text, text=f"{00:02d}:{00:02d}")
    left_icon.config(image=pomodoro_img)
    right_icon.config(image=pomodoro_img)
    flag_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    music_label.config(text="🎵 Music: Off")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def icon_change(img):
    left_icon.config(image=img)
    right_icon.config(image=img)

def pop_up():
    window.lift()
    window.attributes('-topmost', True)
    window.after(1, window.attributes, '-topmost', False)
    messagebox.showinfo(title="Break Time!", message="Step away from your screen and relax 😉!")


def start_timer():
    global reps
    global flags
    reps += 1
    start_button.config(text="Start", state="disabled")

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break!", fg=RED)
        icon_change(brk_img)  # Works perfectly now!
        flag_label.config(text="")
        play_music()
        pop_up()

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break Time!", fg=PINK)
        icon_change(brk_img)
        play_music()
        pop_up()
    else:
        # Work mode
        # window.attributes("-alpha", 0.3)
        pygame.mixer.music.fadeout(1000)
        music_label.config(text="🎵 Music: Off")
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work Time!", fg=GREEN)
        icon_change(work_img)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global flags
    global timer
    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(time_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
       timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            flags += "🚩"
            flag_label.config(text=flags)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.configure(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato= PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 112, image=tomato)
time_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME,20,"bold"), fill="white")
canvas.grid(row=1, column=1)

work_img = PhotoImage(file=resource_path("img_wrk.png"))
brk_img = PhotoImage(file=resource_path("img_br.png"))
pomodoro_img = PhotoImage(file=resource_path("pomo.png"))

#labels
left_icon = Label(bg=YELLOW,image=pomodoro_img)
left_icon.grid(row=0, column=0, sticky="e")

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME,30,"bold"),padx=10,pady=10)
timer_label.grid(row=0, column=1)

right_icon = Label(bg=YELLOW,image=pomodoro_img)
right_icon.grid(row=0, column=2, sticky="w")

flag_label = Label(text="", bg=YELLOW, fg=GREEN)
flag_label.grid(row=3, column=0, columnspan=3)

music_label = Label(text="🎵 Music: Off", bg=YELLOW, fg=RED, font=(FONT_NAME, 10, "italic"))
music_label.grid(row=4, column=0, columnspan=3, pady=5)

#buttons
start_button = Button(text="start", font=(FONT_NAME,10,"bold"), command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="reset", font=(FONT_NAME,10,"bold"),command=reset_timer)
reset_button.grid(row=2, column=2)
mute_button = Button(text="🔊 Mute", font=(FONT_NAME, 8, "bold"), command=toggle_mute)
mute_button.grid(row=5, column=1, pady=10)


window.mainloop()