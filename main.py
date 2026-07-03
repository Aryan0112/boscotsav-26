from logging import root
import tkinter
import customtkinter
from tkinter import *
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("1920x1080")
app.title("Condenzaaaa")
login = customtkinter.CTkImage(light_image=Image.open('lal.png'),size=(1920,1080)) # WidthxHeight
bg_label = customtkinter.CTkLabel(app, text="", image=login)
bg_label.pack()


def print_btn():
    print("Button Clicked!")
button = CTkButton(
    master=app,
    text="Login",
    font=("Lato", 20),
    corner_radius=50,
    text_color="White",
    command=print_btn,
    fg_color="Blue",
    hover_color="#D3D3D3",
    width=400.5,
    height=70,
    bg_color="White"      # <-- transparent ki jagah same background color do
)
button.place(relx=0.745, rely=0.65, anchor=CENTER)

email_entry = customtkinter.CTkEntry(
    master=app,
    corner_radius=50,
    placeholder_text="Enter your email id",
    fg_color="White",       # Makes the text background transparent
    border_color="Gray",   # Removes the outer border line
    text_color="Black",           # Color of the typed text
    placeholder_text_color="gray",# Color of the placeholder text
    width=391,
    height=71,
    bg_color="White"      # <-- transparent ki jagah same background color do
)

email_entry.place(relx=0.745, rely=0.456, anchor=CENTER)

password = customtkinter.CTkEntry(
    master=app,
    corner_radius=50,
    placeholder_text="Enter your password",
    fg_color="White",       # Makes the text background transparent
    border_color="Gray",   # Removes the outer border line
    text_color="Black",           # Color of the typed text
    placeholder_text_color="gray",# Color of the placeholder text
    width=391,
    height=71,
    bg_color="White"      # <-- transparent ki jagah same background color do
)

password.place(relx=0.745, rely=0.559, anchor=CENTER)

app.mainloop()