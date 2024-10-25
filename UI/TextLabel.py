from tkinter import *
from UI.Color import *
from UI.Pel import *


class textLabel:
    """
    This class is to create Text Label to show different results on the window.
    """

    def __init__(self, parentMaze, title, value):
        self.title = title
        self._value = value
        self._parentMaze = parentMaze
        self._var = None
        self.drawLabel()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self._var.set(f"{self.title} : {v}")

    # Vẽ lable
    def drawLabel(self):
        self._var = StringVar()
        self.lab = Label(
            self._parentMaze._canvas,
            textvariable=self._var,
            bg="white",
            fg="black",
            relief=RIDGE,
        )
        self._var.set(f"{self.title} : {self.value}")
        self.lab.pack(expand=True, side=RIGHT, anchor=NW)
