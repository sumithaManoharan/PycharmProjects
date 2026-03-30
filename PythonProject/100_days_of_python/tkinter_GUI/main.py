from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)

# 1. Label
my_label = Label(text="is equal to", font=("courier", 10, "bold"))
miles = Label(text="Miles", font=("courier", 10, "bold"))
km = Label(text="KM", font=("courier", 10, "bold"))
converted = Label(text="0", font=("courier", 10, "bold"))
converted.grid(row=2, column=2,padx=5,pady=5)
miles.grid(row=1, column=3,padx=5,pady=5)
km.grid(row=2, column=3,padx=5,pady=5)
my_label.grid(row=2,column=1,padx=5,pady=5)

# 2. Entry (Input) - Define this BEFORE the button so the button can use it
my_input = Entry(width=10)
my_input.grid(row=1,column=2,padx=5,pady=5)

# 3. Button Function
def clicked():
    # Get the text currently typed in the input box
    text = float(my_input.get())*1.6
    new_text = round(text, 2)
    # Update the label with that text
    converted.config(text=new_text)

# 4. Button
button = Button(text="Calculate", command=clicked,padx=5,pady=5)
button.grid(row=3, column=2)
# new_button = Button(text="new me", command=clicked)
# new_button.grid(row=2, column=1)
# 5. The Loop - This MUST be at the very end
window.mainloop()