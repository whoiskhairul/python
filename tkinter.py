import tkinter.messagebox

import tkinter


def hello():
    tkinter.messagebox.showinfo("say hello", "hello Khairul")


top = tkinter.Tk()
top.title("Khairul")
lbl = tkinter.Label(top, bg="green", text="Khairul Islam")
m = tkinter.Canvas(top, bg="red", height=250, width=300)
c = tkinter.Checkbutton(top, text="Techtunes")
b = tkinter.Checkbutton(top, text="Python")
d = tkinter.Button(top, bg="black", fg="white", text="Techtunes")
s = tkinter.Spinbox(top, bg="yellow", from_=1, to=10)
h = tkinter.Button(top, text="Python Tutorial", command=hello)
e = tkinter.Entry(top)
r = tkinter.Radiobutton(top, text="Python Tutorial", value=1)
lbl.pack()
m.pack()
c.pack()
b.pack()
d.pack()
s.pack()
h.pack()
e.pack()
r.pack()
top.mainloop()
