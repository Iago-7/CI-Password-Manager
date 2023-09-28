from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


FONT_NAME = "Arial"
FONT_SIZE = 20


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letter_list = [choice(letters) for _ in range(randint(8, 12))]
    pw_symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    pw_number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_char_list = pw_letter_list + pw_symbol_list + pw_number_list

    shuffle(password_char_list)

    password = "".join(password_char_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


def save_login_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Oops", detail="Please don't leave any fields empty!")
    else:
        try:
            with open("login_storage.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("login_storage.json", "w") as file:
                json.dump(new_entry, file, indent=4)
        else:
            data.update(new_entry)

            with open("login_storage.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


window = Tk()
window.title("CI Password Manager")
window.config(bg="white")

canvas = Canvas(width=202, height=320, highlightthickness=0, highlightbackground="white")
logo_img = PhotoImage(file="CI-PW-Logo.png")
canvas.create_image(101, 160, image=logo_img)
canvas.grid(row=0, column=1, pady=(10, 0))

website_label = Label(text="Website:", bg="white", font=(FONT_NAME, FONT_SIZE))
website_label.grid(row=1, column=0, sticky=E)

username_label = Label(text="Email/Username:", bg="white", font=(FONT_NAME, FONT_SIZE))
username_label.grid(row=2, column=0, sticky=E, padx=(10, 0))

password_label = Label(text="Password:", bg="white", font=(FONT_NAME, FONT_SIZE))
password_label.grid(row=3, column=0, sticky=E)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW, padx=(0, 17))
website_entry.focus()

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW, padx=(0, 17))

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky=EW, padx=(0, 17))

generate_password_button = Button(text="Generate Password", highlightthickness=0, highlightbackground="white",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2, padx=(0, 17))

add_button = Button(text="Add", highlightthickness=0, highlightbackground="white", activebackground="blue",
                    command=save_login_info)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, padx=(0, 17), pady=(0, 17))

window.mainloop()

# TODO: Fix buttons so when they are clicked they turn blue.
# TODO: Better databasing - CSV
# TODO: Require password to get in to program
# TODO: Update UI
# TODO: Add README
