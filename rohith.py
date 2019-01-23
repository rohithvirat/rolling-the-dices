import random
import tkinter as tk
min = 1
max = 6

roll_again = "yes"

while roll_again == 1:
   
    

    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, text="QUIT", fg="red",command=quit)
                 
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text="rolling the dice....",command=write_slogan)
                   
    slogan.pack(side=tk.LEFT)

    root.mainloop()
    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, text="QUIT", fg="red",command=quit)
                 
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text="the values are.....",command=write_slogan)
                   
    slogan.pack(side=tk.LEFT)

    root.mainloop()
    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, text="QUIT", fg="red",command=quit)
                 
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text=random.randint(min, max),command=write_slogan)
                   
    slogan.pack(side=tk.LEFT)

    root.mainloop()
    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, text="QUIT", fg="red",command=quit)
                 
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text=random.randint(min, max),command=write_slogan)
                   
    slogan.pack(side=tk.LEFT)

    root.mainloop()
    if roll_again==2:
        break
    

    roll_again = int(input("Roll the dices again?"))

