#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
class Application(Frame):
	def __init__(self, master=None):
		self.pack()
		self.createWidgets()

	def createWidgets():
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()