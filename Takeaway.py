from tkinter import *
from tkinter.tix import *
import re
from PIL import ImageTk, Image
from random import *


def clear():
    """Clears all widgets on the screen"""
    for widgets in top_frame.winfo_children():
        widgets.destroy()
    for widgets in frame.winfo_children():
        widgets.destroy()
    for widgets in bottom_frame.winfo_children():
        widgets.destroy()


class MainPage:
    """The main shopping menu with item images, names and prices"""
    def __init__(self):
        """Grid 6 images with quantity buttons and names underneath"""
        clear()
        # makes these variables accesssable from all functions
        global image_1, image_2, image_3, image_4, image_5, image_6
        global number_of_beef_burger, number_of_chicken_burger
        global number_of_ham_burger, number_of_breakfast_burger
        global number_of_fish_burger, number_of_vege_burger
        global number_of_burgers

        title = Label(top_frame, text="McHacker Menu",
                      font=("Times New Roman", 40))
        title.grid(sticky="nsew")

        # locates the image location and holds it as an image
        image_1 = ImageTk.PhotoImage(Image.open("Images\Beef burger.png"))
        frame_1 = Frame(frame, width=140, height=140)
        self.panel_1 = Label(frame_1, image=image_1)
        frame_1.grid_propagate(False)  # prevent auto resizing within the frame
        frame_1.grid(row=0, column=0, pady=10)
        self.panel_1.grid(sticky="nsew")  # fills the frame with the image

        # turns the variable into an integer that tkinter can manage
        number_of_beef_burger = IntVar()
        frame_2 = Frame(frame, width=140, height=140)
        frame_2_bottom = Frame(frame_2, width=140)
        self.burger_1 = Label(frame_2, text="Beef Burger",
                              font=("Times New Roman", 15))
        self.price_1 = Label(frame_2, text="$8",
                             font=("Times New Roman", 12))
        self.quantity_1 = Label(frame_2_bottom, width=10,
                                textvariable=number_of_beef_burger,
                                font=("Times New Roman", 10))
        self.up_button_1 = Button(frame_2_bottom, text="+", width=2,
                                  font=("Times New Roman", 10),
                                  command=self.increase_1)
        self.down_button_1 = Button(frame_2_bottom, text="-", width=2,
                                    font=("Times New Roman", 10),
                                    command=self.decrease_1)
        frame_2.grid_propagate(False)  # prevent auto resizing within the frame
        frame_2.columnconfigure((0, 1, 2), weight=1)
        frame_2.rowconfigure((0, 1, 2), weight=1)
        frame_2.grid(row=0, column=1)
        self.burger_1.grid(row=0, column=1)
        self.price_1.grid(row=1, column=1)
        frame_2_bottom.grid(row=2, column=1)
        self.down_button_1.grid(row=0, column=0)
        self.quantity_1.grid(row=0, column=1)
        self.up_button_1.grid(row=0, column=2)

        # locates the image location and holds it as an image
        image_2 = ImageTk.PhotoImage(Image.open("Images\Chicken burger.png"))
        frame_3 = Frame(frame, width=140, height=140)
        self.panel_2 = Label(frame_3, image=image_2)
        frame_3.grid_propagate(False)  # prevent auto resizing within the frame
        frame_3.grid(row=0, column=2)
        self.panel_2.grid(sticky="nsew")  # fills the frame with the image

        # turns the variable into an integer that tkinter can manage
        number_of_chicken_burger = IntVar()
        frame_4 = Frame(frame, width=140, height=140)
        frame_4_bottom = Frame(frame_4, width=140)
        self.burger_2 = Label(frame_4, text="Chicken Burger",
                              font=("Times New Roman", 15))
        self.price_2 = Label(frame_4, text="$8",
                             font=("Times New Roman", 12))
        self.quantity_2 = Label(frame_4_bottom, width=10,
                                textvariable=number_of_chicken_burger,
                                font=("Times New Roman", 10))
        self.upbutton_2 = Button(frame_4_bottom, text="+", width=2,
                                 font=("Times New Roman", 10),
                                 command=self.increase_2)
        self.downbutton2 = Button(frame_4_bottom, text="-", width=2,
                                  font=("Times New Roman", 10),
                                  command=self.decrease_2)
        frame_4.grid_propagate(False)  # prevent auto resizing within the frame
        frame_4.columnconfigure((0, 1, 2), weight=1)
        frame_4.rowconfigure((0, 1, 2), weight=1)
        frame_4.grid(row=0, column=3)
        self.burger_2.grid(row=0, column=1)
        self.price_2.grid(row=1, column=1)
        frame_4_bottom.grid(row=2, column=1)
        self.downbutton2.grid(row=0, column=0)
        self.quantity_2.grid(row=0, column=1)
        self.upbutton_2.grid(row=0, column=2)

        # locates the image location and holds it as an image
        image_3 = ImageTk.PhotoImage(Image.open("Images\Ham burger.png"))
        frame_5 = Frame(frame, width=140, height=140)
        self.panel_3 = Label(frame_5, image=image_3)
        frame_5.grid_propagate(False)  # prevent auto resizing within the frame
        frame_5.grid(row=0, column=4)
        self.panel_3.grid(sticky="nsew")  # fills the frame with the image

        # turns the variable into an integer that tkinter can manage
        number_of_ham_burger = IntVar()
        frame_6 = Frame(frame, width=140, height=140)
        frame_6_bottom = Frame(frame_6, width=140)
        self.burger_3 = Label(frame_6, text="Ham Burger",
                              font=("Times New Roman", 15))
        self.price_3 = Label(frame_6, text="$8",
                             font=("Times New Roman", 12))
        self.quantity_3 = Label(frame_6_bottom, width=10,
                                textvariable=number_of_ham_burger,
                                font=("Times New Roman", 10))
        self.up_button_3 = Button(frame_6_bottom, text="+", width=2,
                                  font=("Times New Roman", 10),
                                  command=self.increase_3)
        self.down_button_3 = Button(frame_6_bottom, text="-", width=2,
                                    font=("Times New Roman", 10),
                                    command=self.decrease_3)
        frame_6.grid_propagate(False)  # prevent auto resizing within the frame
        frame_6.columnconfigure((0, 1, 2), weight=1)
        frame_6.rowconfigure((0, 1, 2), weight=1)
        frame_6.grid(row=0, column=5)
        self.burger_3.grid(row=0, column=1)
        self.price_3.grid(row=1, column=1)
        frame_6_bottom.grid(row=2, column=1)
        self.down_button_3.grid(row=0, column=0)
        self.quantity_3.grid(row=0, column=1)
        self.up_button_3.grid(row=0, column=2)

        # locates the image location and holds it as an image
        image_4 = ImageTk.PhotoImage(Image.open("Images\Breakfast burger.png"))
        frame_7 = Frame(frame, width=140, height=140)
        self.panel_4 = Label(frame_7, image=image_4)
        frame_7.grid_propagate(False)  # prevent auto resizing within the frame
        frame_7.grid(row=1, column=0, pady=10)
        self.panel_4.grid(sticky="nsew")  # fills the frame with the image

        # turns the variable into an integer that tkinter can manage
        number_of_breakfast_burger = IntVar()
        frame_8 = Frame(frame, width=140, height=140)
        frame_8_bottom = Frame(frame_8, width=140)
        self.burger_4 = Label(frame_8, text="Breakfast Burger",
                              font=("Times New Roman", 15))
        self.price_4 = Label(frame_8, text="$5",
                             font=("Times New Roman", 12))
        self.quantity_4 = Label(frame_8_bottom, width=10,
                                textvariable=number_of_breakfast_burger,
                                font=("Times New Roman", 10))
        self.up_button_4 = Button(frame_8_bottom, text="+", width=2,
                                  font=("Times New Roman", 10),
                                  command=self.increase_4)
        self.down_button_4 = Button(frame_8_bottom, text="-", width=2,
                                    font=("Times New Roman", 10),
                                    command=self.decrease_4)
        frame_8.grid_propagate(False)  # prevent auto resizing within the frame
        frame_8.columnconfigure((0, 1, 2), weight=1)
        frame_8.rowconfigure((0, 1, 2), weight=1)
        frame_8.grid(row=1, column=1)
        self.burger_4.grid(row=0, column=1)
        self.price_4.grid(row=1, column=1)
        frame_8_bottom.grid(row=2, column=1)
        self.down_button_4.grid(row=0, column=0)
        self.quantity_4.grid(row=0, column=1)
        self.up_button_4.grid(row=0, column=2)

        # locates the image location and holds it as an image
        image_5 = ImageTk.PhotoImage(Image.open("Images\Fish burger.png"))
        frame_9 = Frame(frame, width=140, height=140)
        self.panel_5 = Label(frame_9, image=image_5)
        frame_9.grid_propagate(False)  # prevent auto resizing within the frame
        frame_9.grid(row=1, column=2)
        self.panel_5.grid(sticky="nsew")  # fills the frame with the image

        # turns the variable into an integer that tkinter can manage
        number_of_fish_burger = IntVar()
        frame_10 = Frame(frame, width=140, height=140)
        frame_10_bottom = Frame(frame_10, width=140)
        self.burger_5 = Label(frame_10, text="Fish Burger",
                              font=("Times New Roman", 15))
        self.price_5 = Label(frame_10, text="$5",
                             font=("Times New Roman", 12))
        self.quantity_5 = Label(frame_10_bottom, width=10,
                                textvariable=number_of_fish_burger,
                                font=("Times New Roman", 10))
        self.up_button_5 = Button(frame_10_bottom, text="+", width=2,
                                  font=("Times New Roman", 10),
                                  command=self.increase_5)
        self.down_button_5 = Button(frame_10_bottom, text="-", width=2,
                                    font=("Times New Roman", 10),
                                    command=self.decrease_5)
        frame_10.grid_propagate(False)  # prevent auto resizing in the frame
        frame_10.columnconfigure((0, 1, 2), weight=1)
        frame_10.rowconfigure((0, 1, 2), weight=1)
        frame_10.grid(row=1, column=3)
        self.burger_5.grid(row=0, column=1)
        self.price_5.grid(row=1, column=1)
        frame_10_bottom.grid(row=2, column=1)
        self.down_button_5.grid(row=0, column=0)
        self.quantity_5.grid(row=0, column=1)
        self.up_button_5.grid(row=0, column=2)

        # locates the image location and holds it as an image
        image_6 = ImageTk.PhotoImage(Image.open("Images\Vege burger.png"))
        frame_11 = Frame(frame, width=140, height=140)
        self.panel_6 = Label(frame_11, image=image_6)
        frame_11.grid_propagate(False)  # prevent auto resizing in the frame
        frame_11.grid(row=1, column=4)
        self.panel_6.grid(sticky="nsew")  # fills the frame with the image

        # turns the variable into an integer that tkinter can manage
        number_of_vege_burger = IntVar()
        frame_12 = Frame(frame, width=140, height=140)
        frame_12_bottom = Frame(frame_12, width=140)
        self.burger_6 = Label(frame_12, text="Vege Burger",
                              font=("Times New Roman", 15))
        self.price_6 = Label(frame_12, text="$5",
                             font=("Times New Roman", 12))
        self.quantity_6 = Label(frame_12_bottom, width=10,
                                textvariable=number_of_vege_burger,
                                font=("Times New Roman", 10))
        self.up_button_6 = Button(frame_12_bottom, text="+", width=2,
                                  font=("Times New Roman", 10),
                                  command=self.increase_6)
        self.down_button_6 = Button(frame_12_bottom, text="-",
                                    width=2, font=("Times New Roman", 10),
                                    command=self.decrease_6)
        frame_12.grid_propagate(False)  # prevent auto resizing in the frame
        frame_12.columnconfigure((0, 1, 2), weight=1)
        frame_12.rowconfigure((0, 1, 2), weight=1)
        frame_12.grid(row=1, column=5)
        self.burger_6.grid(row=0, column=1)
        self.price_6.grid(row=1, column=1)
        frame_12_bottom.grid(row=2, column=1)
        self.down_button_6.grid(row=0, column=0)
        self.quantity_6.grid(row=0, column=1)
        self.up_button_6.grid(row=0, column=2)

        self.submit = Button(bottom_frame, text="Order",
                             font=("Times New Roman", 20),
                             command=self.open_popup)
        self.submit.pack(pady=20)

        # keeps track of the number of each type of burger ordered
        number_of_burgers = {"beef": 0, "chicken": 0, "ham": 0,
                             "breakfast": 0, "fish": 0, "vege": 0}

    def increase_1(self):
        """Increase the quantity by 1"""
        number_of_burgers["beef"] += 1
        number_of_beef_burger.set(number_of_burgers["beef"])

    def decrease_1(self):
        """Decrease the quantity by 1 if the quantity is not 0"""
        if number_of_beef_burger.get() == 0:
            return
        number_of_burgers["beef"] -= 1
        number_of_beef_burger.set(number_of_burgers["beef"])

    def increase_2(self):
        """Increase the quantity by 1"""
        number_of_burgers["chicken"] += 1
        number_of_chicken_burger.set(number_of_burgers["chicken"])

    def decrease_2(self):
        """Decrease the quantity by 1 if the quantity is not 0"""
        if number_of_chicken_burger.get() == 0:
            return
        number_of_burgers["chicken"] -= 1
        number_of_chicken_burger.set(number_of_burgers["chicken"])

    def increase_3(self):
        """Increase the quantity by 1"""
        number_of_burgers["ham"] += 1
        number_of_ham_burger.set(number_of_burgers["ham"])

    def decrease_3(self):
        """Decrease the quantity by 1 if the quantity is not 0"""
        if number_of_ham_burger.get() == 0:
            return
        number_of_burgers["ham"] -= 1
        number_of_ham_burger.set(number_of_burgers["ham"])

    def increase_4(self):
        """Increase the quantity by 1"""
        number_of_burgers["breakfast"] += 1
        number_of_breakfast_burger.set(number_of_burgers["breakfast"])

    def decrease_4(self):
        """Decrease the quantity by 1 if the quantity is not 0"""
        if number_of_breakfast_burger.get() == 0:
            return
        number_of_burgers["breakfast"] -= 1
        number_of_breakfast_burger.set(number_of_burgers["breakfast"])

    def increase_5(self):
        """Increase the quantity by 1"""
        number_of_burgers["fish"] += 1
        number_of_fish_burger.set(number_of_burgers["fish"])

    def decrease_5(self):
        """Decrease the quantity by 1 if the quantity is not 0"""
        if number_of_fish_burger.get() == 0:
            return
        number_of_burgers["fish"] -= 1
        number_of_fish_burger.set(number_of_burgers["fish"])

    def increase_6(self):
        """Increase the quantity by 1"""
        number_of_burgers["vege"] += 1
        number_of_vege_burger.set(number_of_burgers["vege"])

    def decrease_6(self):
        """Decrease the quantity by 1 if the quantity is not 0"""
        if number_of_vege_burger.get() == 0:
            return
        number_of_burgers["vege"] -= 1
        number_of_vege_burger.set(number_of_burgers["vege"])

    def open_popup(self):
        """open a new popup for the receipt"""
        return_check = 0
        for i in number_of_burgers:
            if number_of_burgers[i] == 0:
                return_check += 1
        if return_check == 6:
            return

        # creates the popup
        popup = Toplevel(window)
        popup.geometry("250x500")
        popup.resizable(width=False, height=False)
        popup.title("Receipt")
        # disables the main window when on the popup
        popup.grab_set()
        self.order_title = Label(popup, font=("Times New Roman", 15),
                                 text="You ordered:")
        self.order_title.pack()

        # creates the frame within the popup and configures it
        middle_frame = Frame(popup, width=250, height=350)
        middle_frame.grid_propagate(False)
        middle_frame.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
        middle_frame.grid_columnconfigure([0, 1], weight=1)
        middle_frame.pack()

        row_counter = 0
        for i in number_of_burgers:
            if number_of_burgers[i] != 0:
                burger_order = Label(middle_frame, text=i + " burger",
                                     font=("Times New Roman", 12))
                burger_quantity = Label(middle_frame, text="x" +
                                        str(number_of_burgers[i]),
                                        font=("Times New Roman", 12))
                burger_order.grid(row=row_counter, column=0,
                                  padx=10, sticky="w")
                burger_quantity.grid(row=row_counter, column=1,
                                     padx=10, sticky="e")
                row_counter += 1
            else:
                continue

        self.total_label = Label(popup, font=("Times New Roman", 15),
                                 text="Total price: $" + str(
                                 8*(number_of_beef_burger.get() +
                                    number_of_chicken_burger.get() +
                                    number_of_ham_burger.get()) +
                                 5*(number_of_breakfast_burger.get() +
                                    number_of_fish_burger.get() +
                                    number_of_vege_burger.get())))
        self.thank_you_message = Label(popup, font=("Times New Roman", 15),
                                       text="Thank you for ordering \n "
                                            "at McHacker!")
        self.total_label.pack()
        self.thank_you_message.pack()


class StartupPage:
    """The initial page with a signup and login button"""
    def __init__(self):
        """Create signup and login buttons"""
        clear()
        self.title = Label(frame, text="McHacker",
                           font=("Times New Roman", 50))
        self.title.pack(pady=50)

        self.question_1 = Label(frame, text="Welcome to McHacker! \n "
                                "would you like to log in or sign up?",
                                font=("Times New Roman", 25))
        self.question_1.pack(pady=50)

        self.button_1 = Button(bottom_frame, text="Sign up",
                               command=SignupPage,
                               font=("Times New Roman", 20))
        self.button_1.grid(row=0, column=0, padx=100)

        self.button_2 = Button(bottom_frame, text="Login",
                               command=LoginPage,
                               font=("Times New Roman", 20))
        self.button_2.grid(row=0, column=1, padx=100)


class LoginPage:
    """The login page with input boxes, and a register and submit button"""
    def __init__(self):
        """Create username and password input boxes with labels on top,
        create submit button and signup button and an error message label"""
        clear()
        global error_message

        self.login_text = Label(frame, text="Login to your account",
                                font=("Times New Roman", 25))
        self.login_text.pack(pady=25)

        self.username_text = Label(frame, text="username",
                                   font=("Times New Roman", 20))
        self.username_text.pack()

        self.username = Entry(frame, font=("Times New Roman", 20))
        self.username.pack()

        self.password_text = Label(frame, text="password",
                                   font=("Times New Roman", 20))
        self.password_text.pack()

        self.password = Entry(frame, show="*", font=("Times New Roman", 20))
        self.password.pack()

        error_message = StringVar()
        error_message.set("")

        self.error_message = Label(frame, font=("Times New Roman", 20),
                                   textvariable=error_message)
        self.error_message.pack(pady=56)

        self.signup = Button(bottom_frame, text="don't have an account",
                             font=("Times New Roman", 20),
                             width=18, command=SignupPage)
        self.signup.grid(row=1, column=1, padx=100)

        self.submit = Button(bottom_frame, text="submit",
                             font=("Times New Roman", 20),
                             command=self.login_test)
        self.submit.grid(row=1, column=2, padx=100)

    def login_test(self):
        """Search the external accounts file for matching credentials"""
        with open("Accounts.txt") as f:
            lines = f.readlines()
            for line in lines:
                if self.username.get().lower() == line[:line.index("|")]:
                    if self.password.get() == line[line.index("|")+1:-1]:
                        MainPage()
                        break
                    else:
                        continue
                else:
                    continue
            error_message.set("Username or password is incorrect,"
                              " please try again")
            return


class SignupPage:
    """The signup page with input boxes, and a login and submit button"""
    def __init__(self):
        """Create username, password and confirm input boxes with labels on top,
        create submit button and signup button and an error message label"""
        clear()
        global error_message

        self.signup_text = Label(frame, text="Signup for an account",
                                 font=("Times New Roman", 25))
        self.signup_text.pack(pady=25)

        self.username_text = Label(frame, text="username",
                                   font=("Times New Roman", 20))
        self.username_text.pack()

        self.username = Entry(frame, font=("Times New Roman", 20))
        self.username.pack()

        # creates a tool tip that appears when the widget is hovered over
        self.username_tip = Balloon(window)
        self.username_tip.bind_widget(self.username,
                                      balloonmsg="Username must contain:\n"
                                                 " - 3 characters")

        self.password_text = Label(frame, text="password",
                                   font=("Times New Roman", 20))
        self.password_text.pack()

        self.password = Entry(frame, font=("Times New Roman", 20))
        self.password.pack()

        # creates a tool tip that appears when the widget is hovered over
        self.password_tip = Balloon(window)
        self.password_tip.bind_widget(self.password,
                                      balloonmsg="Password must contain:\n"
                                      " - 8 characters \n"
                                      " - 1 numeral \n"
                                      " - 1 capital letter \n"
                                      " - 1 lower case letter \n"
                                      "Password cannot contain:\n"
                                      " - pipes ( | )")

        self.confirm_password_text = Label(frame, text="confirm password",
                                           font=("Times New Roman", 20))
        self.confirm_password_text.pack()

        self.confirm_password = Entry(frame, font=("Times New Roman", 20))
        self.confirm_password.pack()

        # creates a tool tip that appears when the widget is hovered over
        self.confirm_tip = Balloon(window)
        self.confirm_tip.bind_widget(self.confirm_password,
                                     balloonmsg="Password must match")

        # turns the variable into an string that tkinter can manage
        error_message = StringVar()
        error_message.set("Hover over a box for more info")

        self.error_message = Label(frame, textvariable=error_message,
                                   font=("Times New Roman", 20))
        self.error_message.pack(pady=20)

        self.login = Button(bottom_frame, text="already have an account",
                            font=("Times New Roman", 20),
                            width=18, command=LoginPage)
        self.login.grid(row=0, column=0, padx=100)

        self.submit = Button(bottom_frame, text="submit",
                             font=("Times New Roman", 20),
                             command=self.sign_up_test)
        self.submit.grid(row=0, column=1, padx=100)

    def sign_up_test(self):
        """Check validity of username and password"""
        # opens an external file and read from it
        with open("Accounts.txt") as f:
            lines = f.readlines()
            for line in lines:
                if self.username.get() == line[:line.index("|")]:
                    error_message.set("Username has already been taken")
                    return

        if len(self.username.get()) < 3:
            error_message.set("Username must have at least 3 characters")
            return

        elif self.password.get() != self.confirm_password.get():
            error_message.set("Password does not match")
            return

        elif len(self.password.get()) < 8:
            error_message.set("Password must have at least 8 characters")
            return

        # uses the re import to search the string for capital letters
        elif re.search('[A-Z]', self.password.get()) is None:
            error_message.set("Password must have at least 1 uppercase letter")
            return

        # uses re to search the string for lower case letters
        elif re.search('[a-z]', self.password.get()) is None:
            error_message.set("Password must have at least 1 lowercase letter")
            return

        # uses the re import to search the string for numbers
        elif re.search('[0-9]', self.password.get()) is None:
            error_message.set("Password must have at least 1 number")
            return

        # uses the re import to search the string for pipes
        elif re.search('[|]', self.password.get()) is not None:
            error_message.set("You are not allowed to use pipes ( | )")
            return

        # uses the re import to search the string for pipes
        elif re.search('[|]', self.username.get()) is not None:
            error_message.set("You are not allowed to use pipes ( | )")
            return

        else:
            # opens an external file and writes to it
            with open("Accounts.txt", 'a+') as f:
                f.write(self.username.get().lower() + "|" +
                        self.password.get() + "\n")
            LoginPage()


window = Tk()
window.title("McHacker Burger")

top_frame = Frame(window)
top_frame.pack(padx=20)

frame = Frame(window)
frame.pack(padx=20)

bottom_frame = Frame(window)
bottom_frame.pack(padx=20)

startup = StartupPage()

window.minsize(width=880, height=500)
window.resizable(width=False, height=False)

window.mainloop()
