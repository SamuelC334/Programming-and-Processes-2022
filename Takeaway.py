import tkinter as tk

def clear():
    for widgets in frame.winfo_children():
      widgets.destroy()
    for widgets in bottomframe.winfo_children():
        widgets.destroy()

class startuppage:
    def __init__(self):
        clear()
        self.question1 = tk.Label(frame, text="Log in or sign up?")
        self.question1.pack()
        self.button1 = tk.Button(bottomframe, text="Sign up", command=signuppage)
        self.button1.grid(row=2,column=1)
        self.button2 = tk.Button(bottomframe, text="Login", command=loginpage)
        self.button2.grid(row=2,column=2)

class loginpage:
    def __init__(self):
        clear()
        self.usernametext = tk.Label(frame, text="username")
        self.usernametext.pack()
        self.username = tk.Entry(frame)
        self.username.pack()
        self.passwordtext = tk.Label(frame, text="password")
        self.passwordtext.pack()
        self.password = tk.Entry(frame)
        self.password.pack()
        self.submit = tk.Button(frame, text="submit", command=self.logintest)
        self.submit.pack()

    def logintest(self):
        print(self.username.get(), self.password.get())

class signuppage:
    def __init__(self):
        clear()
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
        self.submit = tk.Button(frame, text="submit", command=self.signuptest)
        self.submit.pack()

    def signuptest(self):
        print(self.username.get(), self.password.get(), self.confirmpassword.get())

window = tk.Tk()
frame = tk.Frame(window)
frame.pack()
bottomframe = tk.Frame(window)
bottomframe.pack(side=tk.BOTTOM)
startup = startuppage()
window.mainloop()