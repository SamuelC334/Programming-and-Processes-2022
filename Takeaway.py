import tkinter as tk
import re
from PIL import ImageTk, Image
from random import *


def clear():
    """Clears all widgets on the screen"""
    for widgets in topframe.winfo_children():
        widgets.destroy()
    for widgets in frame.winfo_children():
        widgets.destroy()
    for widgets in bottomframe.winfo_children():
        widgets.destroy()


class MainPage:
    """The main shopping menu with item images, names and prices"""
    def __init__(self):
        """Grid 6 images with quantity buttons and names underneath"""
        clear()
        global image_1, image_2, image_3, image_4, image_5, image_6
        global counter_1, counter_2, counter_3, counter_4, counter_5, counter_6

        title = tk.Label(topframe, text="McHacker Menu",
                         font=("Times New Roman", 40))
        title.grid(sticky="nsew")

        image_1 = ImageTk.PhotoImage(Image.open("Images\Beef burger.png"))
        frame_1 = tk.Frame(frame, width=140, height=140)
        self.panel_1 = tk.Label(frame_1, image=image_1)
        frame_1.grid_propagate(False)
        frame_1.grid(row=0, column=0, pady=10)
        self.panel_1.grid(sticky="nsew")

        counter_1 = tk.IntVar()
        frame_2 = tk.Frame(frame, width=140, height=140)
        frame_2_bottom = tk.Frame(frame_2, width=140)
        self.burger_1 = tk.Label(frame_2, text="Beef Burger",
                                font=("Times New Roman", 15))
        self.price_1 = tk.Label(frame_2, text="$8", font=("Times New Roman", 12))
        self.quantity_1 = tk.Label(frame_2_bottom, textvariable=counter_1,
                                  width=10, font=("Times New Roman", 10))
        self.up_button_1 = tk.Button(frame_2_bottom, text="+", width=2,
                                   font=("Times New Roman", 10),
                                   command=self.increase_1)
        self.down_button_1 = tk.Button(frame_2_bottom, text="-", width=2,
                                     font=("Times New Roman", 10),
                                     command=self.decrease_1)
        frame_2.grid_propagate(False)
        frame_2.columnconfigure((0, 1, 2), weight=1)
        frame_2.rowconfigure((0, 1, 2), weight=1)
        frame_2.grid(row=0, column=1)
        self.burger_1.grid(row=0, column=1)
        self.price_1.grid(row=1, column=1)
        frame_2_bottom.grid(row=2, column=1)
        self.down_button_1.grid(row=0, column=0)
        self.quantity_1.grid(row=0, column=1)
        self.up_button_1.grid(row=0, column=2)

        image_2 = ImageTk.PhotoImage(Image.open("Images\Chicken burger.png"))
        frame_3 = tk.Frame(frame, width=140, height=140)
        self.panel_2 = tk.Label(frame_3, image=image_2)
        frame_3.grid_propagate(False)
        frame_3.grid(row=0, column=2)
        self.panel_2.grid(sticky="nsew")

        counter_2 = tk.IntVar()
        frame_4 = tk.Frame(frame, width=140, height=140)
        frame_4_bottom = tk.Frame(frame_4, width=140)
        self.burger_2 = tk.Label(frame_4, text="Chicken Burger",
                                font=("Times New Roman", 15))
        self.price_2 = tk.Label(frame_4, text="$8", font=("Times New Roman", 12))
        self.quantity_2 = tk.Label(frame_4_bottom, textvariable=counter_2,
                                  width=10, font=("Times New Roman", 10))
        self.upbutton_2 = tk.Button(frame_4_bottom, text="+", width=2,
                                   font=("Times New Roman", 10),
                                   command=self.increase_2)
        self.downbutton2 = tk.Button(frame_4_bottom, text="-", width=2,
                                     font=("Times New Roman", 10),
                                     command=self.decrease_2)
        frame_4.grid_propagate(False)
        frame_4.columnconfigure((0, 1, 2), weight=1)
        frame_4.rowconfigure((0, 1, 2), weight=1)
        frame_4.grid(row=0, column=3)
        self.burger_2.grid(row=0, column=1)
        self.price_2.grid(row=1, column=1)
        frame_4_bottom.grid(row=2, column=1)
        self.downbutton2.grid(row=0, column=0)
        self.quantity_2.grid(row=0, column=1)
        self.upbutton_2.grid(row=0, column=2)

        image_3 = ImageTk.PhotoImage(Image.open("Images\Ham burger.png"))
        frame_5 = tk.Frame(frame, width=140, height=140)
        self.panel_3 = tk.Label(frame_5, image=image_3)
        frame_5.grid_propagate(False)
        frame_5.grid(row=0, column=4)
        self.panel_3.grid(sticky="nsew")

        counter_3 = tk.IntVar()
        frame_6 = tk.Frame(frame, width=140, height=140)
        frame_6_bottom = tk.Frame(frame_6, width=140)
        self.burger_3 = tk.Label(frame_6, text="Ham Burger",
                                font=("Times New Roman", 15))
        self.price_3 = tk.Label(frame_6, text="$8", font=("Times New Roman", 12))
        self.quantity_3 = tk.Label(frame_6_bottom, textvariable=counter_3,
                                  width=10, font=("Times New Roman", 10))
        self.up_button_3 = tk.Button(frame_6_bottom, text="+", width=2,
                                   font=("Times New Roman", 10),
                                   command=self.increase_3)
        self.down_button_3 = tk.Button(frame_6_bottom, text="-", width=2,
                                     font=("Times New Roman", 10),
                                     command=self.decrease_3)
        frame_6.grid_propagate(False)
        frame_6.columnconfigure((0, 1, 2), weight=1)
        frame_6.rowconfigure((0, 1, 2), weight=1)
        frame_6.grid(row=0, column=5)
        self.burger_3.grid(row=0, column=1)
        self.price_3.grid(row=1, column=1)
        frame_6_bottom.grid(row=2, column=1)
        self.down_button_3.grid(row=0, column=0)
        self.quantity_3.grid(row=0, column=1)
        self.up_button_3.grid(row=0, column=2)

        image_4 = ImageTk.PhotoImage(Image.open("Images\Bacon egg burger.png"))
        frame_7 = tk.Frame(frame, width=140, height=140)
        self.panel_4 = tk.Label(frame_7, image=image_4)
        frame_7.grid_propagate(False)
        frame_7.grid(row=1, column=0, pady=10)
        self.panel_4.grid(sticky="nsew")

        counter_4 = tk.IntVar()
        frame_8 = tk.Frame(frame, width=140, height=140)
        frame_8_bottom = tk.Frame(frame_8, width=140)
        self.burger_4 = tk.Label(frame_8, text="Bacon egg Burger",
                                font=("Times New Roman", 15))
        self.price_4 = tk.Label(frame_8, text="$5", font=("Times New Roman", 12))
        self.quantity_4 = tk.Label(frame_8_bottom, textvariable=counter_4,
                                  width=10, font=("Times New Roman", 10))
        self.up_button_4 = tk.Button(frame_8_bottom, text="+", width=2,
                                   font=("Times New Roman", 10),
                                   command=self.increase_4)
        self.down_button_4 = tk.Button(frame_8_bottom, text="-", width=2,
                                     font=("Times New Roman", 10),
                                     command=self.decrease_4)
        frame_8.grid_propagate(False)
        frame_8.columnconfigure((0, 1, 2), weight=1)
        frame_8.rowconfigure((0, 1, 2), weight=1)
        frame_8.grid(row=1, column=1)
        self.burger_4.grid(row=0, column=1)
        self.price_4.grid(row=1, column=1)
        frame_8_bottom.grid(row=2, column=1)
        self.down_button_4.grid(row=0, column=0)
        self.quantity_4.grid(row=0, column=1)
        self.up_button_4.grid(row=0, column=2)

        image_5 = ImageTk.PhotoImage(Image.open("Images\Fish burger.png"))
        frame_9 = tk.Frame(frame, width=140, height=140)
        self.panel_5 = tk.Label(frame_9, image=image_5)
        frame_9.grid_propagate(False)
        frame_9.grid(row=1, column=2)
        self.panel_5.grid(sticky="nsew")

        counter_5 = tk.IntVar()
        frame_10 = tk.Frame(frame, width=140, height=140)
        frame_10_bottom = tk.Frame(frame_10, width=140)
        self.burger_5 = tk.Label(frame_10, text="Fish Burger",
                                font=("Times New Roman", 15))
        self.price_5 = tk.Label(frame_10, text="$5",
                               font=("Times New Roman", 12))
        self.quantity_5 = tk.Label(frame_10_bottom, textvariable=counter_5,
                                  width=10, font=("Times New Roman", 10))
        self.up_button_5 = tk.Button(frame_10_bottom, text="+", width=2,
                                   font=("Times New Roman", 10),
                                   command=self.increase_5)
        self.down_button_5 = tk.Button(frame_10_bottom, text="-", width=2,
                                     font=("Times New Roman", 10),
                                     command=self.decrease_5)
        frame_10.grid_propagate(False)
        frame_10.columnconfigure((0, 1, 2), weight=1)
        frame_10.rowconfigure((0, 1, 2), weight=1)
        frame_10.grid(row=1, column=3)
        self.burger_5.grid(row=0, column=1)
        self.price_5.grid(row=1, column=1)
        frame_10_bottom.grid(row=2, column=1)
        self.down_button_5.grid(row=0, column=0)
        self.quantity_5.grid(row=0, column=1)
        self.up_button_5.grid(row=0, column=2)

        image_6 = ImageTk.PhotoImage(Image.open("Images\Vege burger.png"))
        frame_11 = tk.Frame(frame, width=140, height=140)
        self.panel_6 = tk.Label(frame_11, image=image_6)
        frame_11.grid_propagate(False)
        frame_11.grid(row=1, column=4)
        self.panel_6.grid(sticky="nsew")

        counter_6 = tk.IntVar()
        frame_12 = tk.Frame(frame, width=140, height=140)
        frame_12_bottom = tk.Frame(frame_12, width=140)
        self.burger_6 = tk.Label(frame_12, text="Vege Burger",
                                font=("Times New Roman", 15))
        self.price_6 = tk.Label(frame_12, text="$5",
                               font=("Times New Roman", 12))
        self.quantity_6 = tk.Label(frame_12_bottom, textvariable=counter_6,
                                  width=10, font=("Times New Roman", 10))
        self.up_button_6 = tk.Button(frame_12_bottom, text="+", width=2,
                                   font=("Times New Roman", 10),
                                   command=self.increase_6)
        self.down_button_6 = tk.Button(frame_12_bottom, text="-",
                                     width=2, font=("Times New Roman", 10),
                                     command=self.decrease_6)
        frame_12.grid_propagate(False)
        frame_12.columnconfigure((0, 1, 2), weight=1)
        frame_12.rowconfigure((0, 1, 2), weight=1)
        frame_12.grid(row=1, column=5)
        self.burger_6.grid(row=0, column=1)
        self.price_6.grid(row=1, column=1)
        frame_12_bottom.grid(row=2, column=1)
        self.down_button_6.grid(row=0, column=0)
        self.quantity_6.grid(row=0, column=1)
        self.up_button_6.grid(row=0, column=2)

        self.submit = tk.Button(bottomframe, text="Submit",
                                font=("Times New Roman", 20),
                                command=self.open_popup)
        self.submit.pack(pady=20)

    def increase_1(self):
        counter_1.set(counter_1.get() + 1)

    def decrease_1(self):
        if counter_1.get() == 0:
            return
        counter_1.set(counter_1.get() - 1)

    def increase_2(self):
        counter_2.set(counter_2.get() + 1)

    def decrease_2(self):
        if counter_2.get() == 0:
            return
        counter_2.set(counter_2.get() - 1)

    def increase_3(self):
        counter_3.set(counter_3.get() + 1)

    def decrease_3(self):
        if counter_3.get() == 0:
            return
        counter_3.set(counter_3.get() - 1)

    def increase_4(self):
        counter_4.set(counter_4.get() + 1)

    def decrease_4(self):
        if counter_4.get() == 0:
            return
        counter_4.set(counter_4.get() - 1)

    def increase_5(self):
        counter_5.set(counter_5.get() + 1)

    def decrease_5(self):
        if counter_5.get() == 0:
            return
        counter_5.set(counter_5.get() - 1)

    def increase_6(self):
        counter_6.set(counter_6.get() + 1)

    def decrease_6(self):
        if counter_6.get() == 0:
            return
        counter_6.set(counter_6.get() - 1)

    def open_popup(self):
        popup = tk.Toplevel(window)
        popup.geometry("250x500")
        popup.title("Receipt")
        popup.grab_set()
        order_title = tk.Label(popup, font=("Times New Roman", 20),
                              text="Your order number:")
        order_title.pack()
        order_number = tk.Label(popup, font=("Times New Roman", 20),
                               text=randint(100000, 999999))
        order_number.pack()
        price = tk.Label(popup, font=("Times New Roman", 20), text="$" + str(
                         8*(counter_1.get()+counter_2.get()+counter_3.get()) +
                         5*(counter_4.get()+counter_5.get()+counter_6.get())))
        price.pack(side=tk.BOTTOM)


class StartUpPage:
    """The initial page with a signup and login button"""
    def __init__(self):
        """Create signup and login buttons"""
        clear()
        self.title = tk.Label(frame, text="McHacker",
                              font=("Times New Roman", 50))
        self.title.pack(pady=50)

        self.question1 = tk.Label(frame, text="Welcome to McHacker! \n "
                                  "would you like to log in or sign up?",
                                  font=("Times New Roman", 25))
        self.question1.pack(pady=50)

        self.button1 = tk.Button(bottomframe, text="Sign up",
                                 command=SignUpPage,
                                 font=("Times New Roman", 20))
        self.button1.grid(row=0, column=0, padx=100)

        self.button2 = tk.Button(bottomframe, text="Login",
                                 command=LoginPage,
                                 font=("Times New Roman", 20))
        self.button2.grid(row=0, column=1, padx=100)


class LoginPage:
    """The login page with input boxes, and a register and submit button"""
    def __init__(self):
        """Create username and password input boxes with labels on top,
        create submit button and signup button and an error message label"""
        clear()
        global errormessage

        self.logintext = tk.Label(frame, text="Login to your account",
                                  font=("Times New Roman", 25))
        self.logintext.pack(pady=25)

        self.usernametext = tk.Label(frame, text="username",
                                     font=("Times New Roman", 20))
        self.usernametext.pack()

        self.username = tk.Entry(frame,
                                 font=("Times New Roman", 20))
        self.username.pack()

        self.passwordtext = tk.Label(frame, text="password",
                                     font=("Times New Roman", 20))
        self.passwordtext.pack()

        self.password = tk.Entry(frame, show="*", font=("Times New Roman", 20))
        self.password.pack()

        errormessage = tk.StringVar()
        errormessage.set("")

        self.errormessage = tk.Label(frame, font=("Times New Roman", 20),
                                     textvariable=errormessage)
        self.errormessage.pack(pady=56)

        self.signup = tk.Button(bottomframe, text="don't have an account",
                                font=("Times New Roman", 20),
                                width=18, command=SignUpPage)
        self.signup.grid(row=1, column=1, padx=100)

        self.submit = tk.Button(bottomframe, text="submit",
                                font=("Times New Roman", 20),
                                command=self.login_test)
        self.submit.grid(row=1, column=2, padx=100)

    def login_test(self):
        """Search the external accounts file for matching credentials"""
        with open("Accounts.txt") as f:
            lines = f.readlines()
            for line in lines:
                if self.username.get() == line[:line.index("|")]:
                    if self.password.get() == line[line.index("|")+1:-1]:
                        MainPage()

            errormessage.set("Username or password is incorrect,"
                             " please try again")
            return


class SignUpPage:
    """The signup page with input boxes, and a login and submit button"""
    def __init__(self):
        """Create username, password and confirm input boxes with labels on top,
        create submit button and signup button and an error message label"""
        clear()
        global errormessage

        self.signuptext = tk.Label(frame, text="Signup for an account",
                                   font=("Times New Roman", 25))
        self.signuptext.pack(pady=25)

        self.usernametext = tk.Label(frame, text="username",
                                     font=("Times New Roman", 20))
        self.usernametext.pack()

        self.username = tk.Entry(frame, font=("Times New Roman", 20))
        self.username.pack()

        self.passwordtext = tk.Label(frame, text="password",
                                     font=("Times New Roman", 20))
        self.passwordtext.pack()

        self.password = tk.Entry(frame, font=("Times New Roman", 20))
        self.password.pack()

        self.confirmpasswordtext = tk.Label(frame, text="confirm password",
                                            font=("Times New Roman", 20))
        self.confirmpasswordtext.pack()

        self.confirmpassword = tk.Entry(frame, font=("Times New Roman", 20))
        self.confirmpassword.pack()

        errormessage = tk.StringVar()
        errormessage.set("")

        self.errormessage = tk.Label(frame, textvariable=errormessage,
                                     font=("Times New Roman", 20))
        self.errormessage.pack(pady=20)

        self.login = tk.Button(bottomframe, text="already have an account",
                               font=("Times New Roman", 20),
                               width=18, command=LoginPage)
        self.login.grid(row=0, column=0, padx=100)

        self.submit = tk.Button(bottomframe, text="submit",
                                font=("Times New Roman", 20),
                                command=self.sign_up_test)
        self.submit.grid(row=0, column=1, padx=100)

    def sign_up_test(self):
        """Check validity of username and password"""
        with open("Accounts.txt") as f:
            lines = f.readlines()
            for line in lines:
                if self.username.get() == line[:line.index("|")]:
                    errormessage.set("Username has already been taken")
                    return

        if len(self.username.get()) < 3:
            errormessage.set("Username must contain at least 3 characters")
            return

        elif self.password.get() != self.confirmpassword.get():
            errormessage.set("Password does not match")
            return

        elif len(self.password.get()) < 8:
            errormessage.set("Password must contain at least 8 characters")
            return

        elif re.search('[A-Z]', self.password.get()) is None:
            errormessage.set("Password must contain at least 1 capital letter")
            return

        elif re.search('[0-9]', self.password.get()) is None:
            errormessage.set("Password must contain at least 1 number")
            return

        elif re.search('[|]', self.password.get()) is not None:
            errormessage.set("You are not allowed to use pipes ( | )")
            return

        elif re.search('[|]', self.username.get()) is not None:
            errormessage.set("You are not allowed to use pipes ( | )")
            return

        else:
            with open("Accounts.txt", 'a+') as f:
                f.write(self.username.get() + "|" + self.password.get() + "\n")
            LoginPage()


window = tk.Tk()
window.title("McHacker Burger")

topframe = tk.Frame(window)
topframe.pack(padx=20)

frame = tk.Frame(window)
frame.pack(padx=20)

bottomframe = tk.Frame(window)
bottomframe.pack(padx=20)

startup = MainPage()

window.minsize(width=880, height=500)
window.resizable(width=False, height=False)

window.mainloop()
