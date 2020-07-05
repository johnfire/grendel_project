#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:55:26 2020

@author: christopher
"""


# import tkinter
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.startDAI_button = Button(master, text="start DecAI", command=lambda: self.update("add"))
        self.startPhy_button = Button(master, text="Start Phy", command=lambda: self.update("subtract"))
        self.startXX_button = Button(master, text="StartXX", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=40, sticky=W+E)

        self.startDAI_button.grid(row=2, column=0)
        self.startPhy_button.grid(row=3, column=0)
        self.startXX_button.grid(row=4, column=0, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
root.geometry("800x600")
my_gui = Calculator(root)
root.mainloop()
