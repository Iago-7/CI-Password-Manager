from tkinter import *
from tkinter import messagebox


FONT_NAME = "Arial"
FONT_SIZE = 20


def generate_password():
    password_entry.insert(END, string="TEST")


def save_login_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Oops", detail="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="", message=website, detail=f"These are the details entered:"
                                                                         f"\nUsername/Email: {username}\n"
                                                                         f"Password: {password}\nIs it ok to save?")

    if is_ok:
        with open("login_storage.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


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
