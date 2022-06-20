import tkinter as tk
import re
from PIL import ImageTk, Image


def clear():
    """Clears all widgets on the screen"""
    for widgets in frame.winfo_children():
        widgets.destroy()
    for widgets in bottomframe.winfo_children():
        widgets.destroy()


class mainpage:
    """The main shopping menu with item images, names and prices"""
    def __init__(self):
        """Grid 6 images with quantity buttons and names underneath"""
        clear()
        global image1, image2, image3, image4, image5, image6

        image1 = ImageTk.PhotoImage(Image.open("Images\Beef burger.png"))
        frame1 = tk.Frame(frame, width=140, height=140)
        self.panel1 = tk.Label(frame1, image=image1)
        frame1.grid_propagate(False)
        frame1.columnconfigure(0, weight=1)
        frame1.rowconfigure(0,weight=1)
        frame1.grid(row=0, column=0)
        self.panel1.grid(sticky="nsew")

        frame2 = tk.Frame(frame, width=140, height=140)
        burger1 = tk.Label(frame2, text="Beef Burger", font=("Times New Roman", 10))
        frame2.grid_propagate(False)
        frame2.columnconfigure(0, weight=1)
        frame2.rowconfigure(0,weight=1)
        frame2.grid(row=0, column=1)
        burger1.grid(sticky="nsew")

        image2 = ImageTk.PhotoImage(Image.open("Images\Chicken burger.png"))
        frame3 = tk.Frame(frame, width=140, height=140)
        self.panel2 = tk.Label(frame3, image=image2)
        frame3.grid_propagate(False)
        frame3.columnconfigure(0, weight=1)
        frame3.rowconfigure(0,weight=1)
        frame3.grid(row=0, column=2)
        self.panel2.grid(sticky="nsew")

        frame4 = tk.Frame(frame, width=140, height=140)
        burger2 = tk.Label(frame4, text="Chicken Burger", font=("Times New Roman", 10))
        frame4.grid_propagate(False)
        frame4.columnconfigure(0, weight=1)
        frame4.rowconfigure(0,weight=1)
        frame4.grid(row=0, column=3)
        burger2.grid(sticky="nsew")

        image3 = ImageTk.PhotoImage(Image.open("Images\Ham burger.png"))
        frame5 = tk.Frame(frame, width=140, height=140)
        self.panel3 = tk.Label(frame5, image=image3)
        frame5.grid_propagate(False)
        frame5.columnconfigure(0, weight=1)
        frame5.rowconfigure(0,weight=1)
        frame5.grid(row=0, column=4)
        self.panel3.grid(sticky="nsew")

        frame6 = tk.Frame(frame, width=140, height=140)
        burger3 = tk.Label(frame6, text="Ham Burger", font=("Times New Roman", 10))
        frame6.grid_propagate(False)
        frame6.columnconfigure(0, weight=1)
        frame6.rowconfigure(0,weight=1)
        frame6.grid(row=0, column=5)
        burger3.grid(sticky="nsew")

        image4 = ImageTk.PhotoImage(Image.open("Images\Bacon egg burger.png"))
        frame7 = tk.Frame(frame, width=140, height=140)
        self.panel4 = tk.Label(frame7, image=image4)
        frame7.grid_propagate(False)
        frame7.columnconfigure(0, weight=1)
        frame7.rowconfigure(0,weight=1)
        frame7.grid(row=1, column=0)
        self.panel4.grid(sticky="nsew")

        frame8 = tk.Frame(frame, width=140, height=140)
        burger4 = tk.Label(frame8, text="Bacon egg Burger", font=("Times New Roman", 10))
        frame8.grid_propagate(False)
        frame8.columnconfigure(0, weight=1)
        frame8.rowconfigure(0,weight=1)
        frame8.grid(row=1, column=1)
        burger4.grid(sticky="nsew")

        image5 = ImageTk.PhotoImage(Image.open("Images\Fish burger.png"))
        frame9 = tk.Frame(frame, width=140, height=140)
        self.panel5 = tk.Label(frame9, image=image5)
        frame9.grid_propagate(False)
        frame9.columnconfigure(0, weight=1)
        frame9.rowconfigure(0,weight=1)
        frame9.grid(row=1, column=2)
        self.panel5.grid(sticky="nsew")

        frame10 = tk.Frame(frame, width=140, height=140)
        burger5 = tk.Label(frame10, text="Fish Burger", font=("Times New Roman", 10))
        frame10.grid_propagate(False)
        frame10.columnconfigure(0, weight=1)
        frame10.rowconfigure(0,weight=1)
        frame10.grid(row=1, column=3)
        burger5.grid(sticky="nsew")

        image6 = ImageTk.PhotoImage(Image.open("Images\Vege burger.png"))
        frame11 = tk.Frame(frame, width=140, height=140)
        self.panel6 = tk.Label(frame11, image=image6)
        frame11.grid_propagate(False)
        frame11.columnconfigure(0, weight=1)
        frame11.rowconfigure(0,weight=1)
        frame11.grid(row=1, column=4)
        self.panel6.grid(sticky="nsew")

        frame12 = tk.Frame(frame, width=140, height=140)
        burger6 = tk.Label(frame12, text="Vege Burger", font=("Times New Roman", 10))
        frame12.grid_propagate(False)
        frame12.columnconfigure(0, weight=1)
        frame12.rowconfigure(0,weight=1)
        frame12.grid(row=1, column=5)
        burger6.grid(sticky="nsew")


class startuppage:
    """The initial page with a signup and login button"""
    def __init__(self):
        """Create signup and login buttons"""
        clear()
        self.title = tk.Label(frame, text="McHacker", font=("Times New Roman", 50))
        self.title.pack(pady=50)

        self.question1 = tk.Label(frame, text="Welcome to McHacker! \n "
                                  "would you like to log in or sign up?", 
                                  font=("Times New Roman", 25))
        self.question1.pack(pady=50)

        self.button1 = tk.Button(bottomframe, text="Sign up",
                                 command=signuppage, font=("Times New Roman", 20))
        self.button1.grid(row=0, column=0, padx=100)

        self.button2 = tk.Button(bottomframe, text="Login",
                                 command=loginpage, font=("Times New Roman", 20))
        self.button2.grid(row=0, column=1, padx=100)


class loginpage:
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

        self.password = tk.Entry(frame, font=("Times New Roman", 20))
        self.password.pack()

        errormessage = tk.StringVar()
        errormessage.set("")

        self.errormessage = tk.Label(frame, font=("Times New Roman", 20),
                                     textvariable=errormessage)
        self.errormessage.pack(pady=55)


        self.signup = tk.Button(bottomframe, text="don't have an account",
                                font=("Times New Roman", 20),
                                command=signuppage)
        self.signup.grid(row=1, column=1, padx=100)

        self.submit = tk.Button(bottomframe, text="submit",
                                font=("Times New Roman", 20),
                                command=self.logintest)
        self.submit.grid(row=1, column=2, padx=100)

    def logintest(self):
        """Search the external accounts file for matching credentials"""
        with open("Accounts.txt") as f:
            lines = f.readlines()
            for line in lines:
                if self.username.get() == line[:line.index("|")]:
                    if self.password.get() == line[line.index("|")+1:-1]:
                        mainpage()

            errormessage.set("Username or password is incorrect,"
                             " please try again")
            return


class signuppage:
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
                               command=loginpage)
        self.login.grid(row=0, column=0, padx=100)

        self.submit = tk.Button(bottomframe, text="submit",
                                font=("Times New Roman", 20),
                                command=self.signuptest)
        self.submit.grid(row=0, column=1, padx=100)

    def signuptest(self):
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
            loginpage()


window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

bottomframe = tk.Frame(window)
bottomframe.pack()

startup = mainpage()

window.minsize(width=840, height=500)
window.resizable(width=False, height=False)

window.mainloop()
