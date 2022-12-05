import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website Label
Website_label = tkinter.Label(text="Website", )
Website_label.grid(column=0, row=1, )
# Website Input
website_input = tkinter.Entry( width=36)
website_input.grid(column=1, row=1, columnspan=2)

# Email Label
Email_label = tkinter.Label(text="Email", )
Email_label.grid(column=0, row=2)

# Email Input
email_input = tkinter.Entry( width=36)
email_input.grid(column=1, row=2, columnspan=2)

# Password Label
Password_label = tkinter.Label(text="Password", )
Password_label.grid(column=0, row=3)
# Password Input
password_input = tkinter.Entry( width=19)
password_input.grid(column=1, row=3)

# Generate Password Button
Password_button = tkinter.Button(text="Generate Password", highlightthickness=0,)
Password_button.grid(column=2, row=3)
# Add Button
Add_button = tkinter.Button(text="Add", highlightthickness=0, width=36)
Add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
