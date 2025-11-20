from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    get_password_textbox = password_textbox.get()

    random_letter = random.choices(string.ascii_letters, k=5)
    random_numbers = random.choices(string.digits, k=3)
    random_symbols = random.choices(string.punctuation, k=2)

    password_list = random_letter + random_numbers + random_symbols

    random.shuffle(password_list)

    final_password = "".join(password_list)
    print(final_password)

    password_textbox.insert(0, final_password)

    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_file():
    get_website_name = website_textbox.get().title()
    get_username = username_textbox.get()
    get_password = password_textbox.get()

    # 3. Confirmation Pop-up (using askokcancel)
    is_ok = messagebox.askokcancel(
        title=get_website_name,
        message=f"These are the details entered:\nEmail: {get_username}\nPassword: {get_password}\n\nIs it okay to save?",
    )

    if is_ok:
        with open("password_manager.txt", "a") as file:
            file.write("------------------------------")
            file.write(
                f"\nWebsite: {get_website_name}\nUsername/Email: {get_username}\nPassword: {get_password}\n"
            )
            file.write("------------------------------")
            print("New website and password have been added!")

        website_textbox.delete(0, END)
        password_textbox.delete(0, END)
        website_textbox.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=1)

# ---------------
title_text = Label(text="", font=("helvetica", 15))
title_text.grid(column=1, row=0)


# ---------------
website_text = Label(text="Website")
website_text.grid(column=0, row=2)

website_textbox = Entry(width=35)
website_textbox.focus()
website_textbox.grid(column=1, row=2, columnspan=2)

# ---------------
username_text = Label(text="Email/Username")
username_text.grid(column=0, row=3)

username_textbox = Entry(width=35)
username_textbox.insert(0, "naz@gmail.com")
username_textbox.grid(column=1, row=3, columnspan=2)

# ---------------
password_text = Label(text="Password")
password_text.grid(column=0, row=4)

password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=4)

password_generator_btn = Button(text="Generate Password", command=gen_password)
password_generator_btn.grid(column=2, row=4)
# ---------------

add_btn = Button(text="Add", width=36, command=create_file)
add_btn.grid(column=1, row=5, columnspan=2)
# ########################
window.mainloop()
