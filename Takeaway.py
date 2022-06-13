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
        clear()
        global image1, image2, image3, image4, image5, image6
        image1 = ImageTk.PhotoImage(Image.open("Images\Beef burger.png"))
        image2 = ImageTk.PhotoImage(Image.open("Images\Chicken burger.png"))
        image3 = ImageTk.PhotoImage(Image.open("Images\Ham burger.png"))
        image4 = ImageTk.PhotoImage(Image.open("Images\Bacon egg burger.png"))
        image5 = ImageTk.PhotoImage(Image.open("Images\Fish burger.png"))
        image6 = ImageTk.PhotoImage(Image.open("Images\Vege burger.png"))
        self.panel1 = tk.Label(frame, image=image1)
        self.panel1.pack(side=tk.LEFT)
        self.panel2 = tk.Label(frame, image=image2)
        self.panel2.pack(side=tk.RIGHT)
        self.panel3 = tk.Label(frame, image=image3)
        self.panel3.pack(side=tk.LEFT)
        self.panel4 = tk.Label(bottomframe, image=image4)
        self.panel4.pack(side=tk.RIGHT)
        self.panel5 = tk.Label(bottomframe, image=image5)
        self.panel5.pack(side=tk.LEFT)
        self.panel6 = tk.Label(bottomframe, image=image6)
        self.panel6.pack(side=tk.RIGHT)


class startuppage:
    """The initial page with a signup and login button"""
    def __init__(self):
        """Create signup and login buttons"""
        clear()
        self.question1 = tk.Label(frame, text="Log in or sign up?")
        self.question1.pack()
        self.button1 = tk.Button(bottomframe, text="Sign up",
                                 command=signuppage)
        self.button1.grid(row=2, column=1)
        self.button2 = tk.Button(bottomframe, text="Login",
                                 command=loginpage)
        self.button2.grid(row=2, column=2)


class loginpage:
    """The login page with input boxes, and a register and submit button"""
    def __init__(self):
        """Create username and password input boxes with labels on top,
        create submit button and signup button and an error message label"""
        clear()
        global errormessage
        self.logintext = tk.Label(frame, text="Login to your account")
        self.logintext.pack()
        self.usernametext = tk.Label(frame, text="username")
        self.usernametext.pack()
        self.username = tk.Entry(frame)
        self.username.pack()
        self.passwordtext = tk.Label(frame, text="password")
        self.passwordtext.pack()
        self.password = tk.Entry(frame)
        self.password.pack()
        self.signup = tk.Button(bottomframe, text="don't have an account",
                                command=signuppage)
        self.signup.grid(row=1, column=1)
        self.submit = tk.Button(bottomframe, text="submit",
                                command=self.logintest)
        self.submit.grid(row=1, column=2)
        errormessage = tk.StringVar()
        errormessage.set("")
        self.errormessage = tk.Label(frame, textvariable=errormessage)
        self.errormessage.pack()

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
        self.signuptext = tk.Label(frame, text="Signup for an account")
        self.signuptext.pack()
        self.usernametext = tk.Label(frame, text="username")
        self.usernametext.pack()
        self.username = tk.Entry(frame)
        self.username.pack()
        self.passwordtext = tk.Label(frame, text="password")
        self.passwordtext.pack()
        self.password = tk.Entry(frame)
        self.password.pack()
        self.confirmpasswordtext = tk.Label(frame, text="confirm password")
        self.confirmpasswordtext.pack()
        self.confirmpassword = tk.Entry(frame)
        self.confirmpassword.pack()
        self.login = tk.Button(bottomframe, text="already have an account",
                               command=loginpage)
        self.login.grid(row=1, column=1)
        self.submit = tk.Button(bottomframe, text="submit",
                                command=self.signuptest)
        self.submit.grid(row=1, column=2)
        errormessage = tk.StringVar()
        errormessage.set("")
        self.errormessage = tk.Label(frame, textvariable=errormessage)
        self.errormessage.pack()

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
bottomframe.pack(side=tk.BOTTOM)
startup = startuppage()
window.mainloop()
