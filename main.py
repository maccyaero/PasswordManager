import tkinter
import pandas as pd
import random
import json
from tkinter import messagebox
header_written = False
website_name = " "
email = " "
password = " "


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    global password
    password = ''
    print(password)
    password_input.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [random.choice(letters) for char in range(nr_letters)]
    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]
    password_list.extend(letters_list)
    password_list.extend(symbols_list)
    password_list.extend(numbers_list)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    global website_name
    global email
    global password
    global header_written
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # Write to JSON
    new_data = {website_name: {
        "email": email,
        "password": password
    }}

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open('data.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)

        website_input.delete(0, len(website_name))
        email_input.delete(0, len(email))
        password_input.delete(0, len(password))
    # Write to CSV

    # d = {'Website': [website_name], 'Username': [email], 'Password': [password]}
    # df = pd.DataFrame(data=d)
    # print(df)
    # df.to_csv('out.csv', index=False, mode='a', header=False)
    # Empty all Entry fields after submitting to get them ready for the next input


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    global website_name
    global email
    website_name = website_input.get()
    email = email_input.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}
        with open('data.json', 'w') as data_file:
            json.dump(data, data_file, )
            print("Error No File found new file created")
            tkinter.messagebox.showinfo(title="ERROR", message="Error No File found new file created")

    else:
        if website_name in data:
            new_data = data[website_name]
            print(new_data["email"])
            print(email)
            if data[website_name]['email'] == email:
                tkinter.messagebox.showinfo(title=website_name, message=f"Password is {new_data['password']}")

        else:
            tkinter.messagebox.showinfo(title=website_name, message=f"{website_name} was not found")

    website_input.delete(0, len(website_name))
    email_input.delete(0, len(email))


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
website_input = tkinter.Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email Label
Email_label = tkinter.Label(text="Email", )
Email_label.grid(column=0, row=2)

# Email Input
email_input = tkinter.Entry(width=36)
email_input.grid(column=1, row=2, columnspan=2)

# Password Label
Password_label = tkinter.Label(text="Password", )
Password_label.grid(column=0, row=3)
# Password Input
password_input = tkinter.Entry(width=19)
password_input.grid(column=1, row=3)

# Generate Password Button
Password_button = tkinter.Button(text="Generate Password", highlightthickness=0, command=password_generator)
Password_button.grid(column=2, row=3)
# Add Button
Add_button = tkinter.Button(text="Add", highlightthickness=0, width=36, command=save_password)
Add_button.grid(column=1, row=4, columnspan=2, )
# Save Password Button
Save_button = tkinter.Button(text="Search Password", highlightthickness=0, bd=10, command=search_password)
Save_button.grid(column=2, row=1)

window.mainloop()
