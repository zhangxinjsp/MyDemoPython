#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.master.title("My Do-Nothing Application")
        self.master.maxsize(1000, 400)
        self.master.minsize(1000, 400)

        self.var = tk.StringVar(self)
        self.create_widgets()

    def create_widgets(self):
        self.l = tk.Label(self, textvariable=self.var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
        # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
        self.l.pack()

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        self.var.set("qwerty")


root = tk.Tk()
app = Application(master=root)

app.mainloop()
