from tkinter import *
from tkinter import messagebox
import string,random,pyperclip
import os, sys, json



def get_resource_path(relative_path):
    """ Used for IMAGES (Read-only bundle folder) """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_data_path(filename):
    """ Used for JSON (Writeable app folder) """
    if getattr(sys, 'frozen', False):
        # Path to the folder where the binary sits
        base_path = os.path.dirname(sys.executable)
    else:
        # Path to the script folder
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, filename)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entries.get()
    with open(get_data_path("data.json"), "r") as file:
        data = json.load(file)
        if website in data:
            email = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=f"Details for {website}",
                message=f"Account: {website}\n"
                        f"{'-' * 30}\n"  # A simple visual separator line
                        f"👤 Username:  {email}\n"
                        f"🔑 Password:  {password}\n\n"
                        f"Result: Copied to clipboard!"
            )
        else:
            messagebox.showerror("Error","No saved password for this website, create a new one")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = "`!@#$%^&*()_+-=[]{}"

    sl = random.randint(4,5)
    cl = random.randint(4,5)
    num = random.randint(2,4)
    sym = random.randint(2,4)

    lower = [random.choice(small_letters) for _ in range(sl)]
    upper = [random.choice(capital_letters) for _ in range(cl)]
    numb = [random.choice(numbers) for _ in range(num)]
    symc = [random.choice(symbols) for _ in range(sym)]

    password_letters = lower + upper + numb + symc
    random.shuffle(password_letters)

    password = "".join(password_letters)
    pyperclip.copy(password)
    password_entries.insert(END,string=pyperclip.paste())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entries.get()
    username = username_entries.get()
    password = password_entries.get()
    if website == "" or username == "" or password == "":
        messagebox.showerror("Error","Please fill all fields")
    else:
        new_entry = {website:{"username":username,"password":password}}
        try:
            with open(get_data_path("data.json"), "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = new_entry
        else:
            data.update(new_entry)
        with open(get_data_path("data.json"), "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Password Manager","Password has been saved")
        website_entries.delete(0, END)
        password_entries.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(background="white", width=500,height=500,padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white",highlightthickness=0)
lock = PhotoImage(file=get_resource_path("logo.png"))
canvas.create_image(100,100, image=lock)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(row=1, column=0,pady=5,padx=5)

username_label = Label(text="Email/Username:", bg="white", fg="black")
username_label.grid(row=2, column=0,pady=5,padx=5)

password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(row=3, column=0,pady=5,padx=5)

#entries

website_entries = Entry(width=24, bg="white", fg="black")
website_entries.grid(row=1, column=1,pady=5,padx=5)

username_entries = Entry(width=40, bg="white", fg="black")
username_entries.insert(END,"sumithamanoharan76@gmail.com")
username_entries.grid(row=2, column=1, columnspan=3,pady=5,padx=5)

password_entries = Entry(width=24, bg="white", fg="black")
password_entries.grid(row=3, column=1,pady=5,padx=5)

#button
password_button = Button(text="Generate password",width=14,pady=5,padx=5,command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add",width=38,command=save_password)
add_button.grid(row=4, column=1, columnspan=3,pady=5,padx=5)

search_button = Button(text="Search",width = 14,pady=5,padx=5, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()


