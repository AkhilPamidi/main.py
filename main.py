from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, shuffle, choice

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_charecters = ["!", "@", "#", "$", "%", "^", "&", "*"]


def for_password():
    """it is to generate password"""
    password_letters = [choice(alphabets) for _ in range(randint(3, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 3))]
    password_charecters = [choice(special_charecters) for _ in range(randint(2, 3))]
    password_list = password_numbers + password_letters + password_charecters
    shuffle(password_list)
    Gpassword = "".join(password_list)
    password.delete(0, END)
    password.insert(0, Gpassword)
    pyperclip.copy(Gpassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_file():
    """to save the data"""
    we = web_entry.get()
    pa = password.get()
    em = email.get()
    new_data = {
        we: {
            "email": em,
            "password": pa,
        }
    }
    if len(we) == 0 or len(pa) == 0 or em == 0:
        messagebox.showwarning(title="Oops!", message="credentials are missing")
    else:
        try:
            with open("data.jason", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.jason", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.jason", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.jason", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password.delete(0, END)


# ----------------------------gor SEARCH BUTTON_________________#


def for_search():
    with open("data.jason", "r") as data_file:
        data = json.load(data_file)
        website=web_entry.get()
        if website in data:
            email.delete(0,END)
            ema = data[web_entry.get()]["email"]
            pas = data[web_entry.get()]["password"]
            email.insert(0, ema)
            password.insert(0, pas)
        else:
            messagebox.askyesno(title="website not found",message="add the website into the data")


# _____________________for GUI SETUP_____________________#
windows = Tk()
windows.title("PASSWORD MANAGER")
windows.configure(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.configure(bg="white")
canvas.grid(row=0, column=2)
label1 = Label(text="Website")
label1.grid(row=1, column=1)
label2 = Label(text="Email/Username")
label2.grid(row=2, column=1)
label3 = Label(text="Password")
label3.grid(row=3, column=1)
web_entry = Entry()
web_entry.grid(row=1, column=2)
web_entry.configure(width=33)
web_entry.focus()

email = Entry()
email.grid(row=2, column=2, columnspan=2)
email.configure(width=53)

password = Entry()
password.grid(row=3, column=2)

password.configure(width=33)
generate = Button(text="Generate Password", command=for_password)
generate.grid(row=3, column=3)

add = Button(text="ADD", bd=2, command=save_data_file)
add.configure(width=39)
add.grid(row=4, column=2, columnspan=2)

search = Button(text="search", bd=2, command=for_search)
search.configure(width=16)
search.grid(row=1, column=3)

windows.mainloop()
