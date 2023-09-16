from tkinter import *

FONT_NAME = "Arial"
FONT_SIZE = 20


def generate_password():
    password_entry.insert(END, string="TEST")


window = Tk()
window.title("CI Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=202, height=320, highlightthickness=0, highlightbackground="white")
logo_img = PhotoImage(file="CI-PW-Logo.png")
canvas.create_image(101, 160, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white", font=(FONT_NAME, FONT_SIZE))
website_label.grid(row=1, column=0, sticky=E)

username_label = Label(text="Email/Username:", bg="white", font=(FONT_NAME, FONT_SIZE))
username_label.grid(row=2, column=0, sticky=E)

password_label = Label(text="Password:", bg="white", font=(FONT_NAME, FONT_SIZE))
password_label.grid(row=3, column=0, sticky=E)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)

username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky=EW)

generate_password_button = Button(text="Generate Password", highlightthickness=0, highlightbackground="white",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=0, highlightbackground="white")
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
