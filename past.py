import pygame
import random
import tkinter as tk
from tkinter import *
from subprocess import call
import os, sys, inspect
from os import path
import pygame

font_name = pygame.font.match_font('Georgia')

window = Tk() #Создаём окно приложения.
window.title("Игра")
window.geometry('400x300')
frame = Frame(window)
frame.pack(pady=20,padx=20)




def calculate_bmi():
 call(["python", "main.py"])


weight_lb = Label(
        frame,
        text="The Game Of Serega",
    )
weight_lb.grid(row=3, column=1)


weight_lb = Label(
        frame,
        text="Начать игру?",
    )
weight_lb.grid(row=4, column=1)

cal_btn = Button(
   frame, #Заготовка с настроенными отступами.
   text='Начать', #Надпись на кнопке.
    command=calculate_bmi
    # command=calculate_bmi
)
cal_btn.grid(row=5, column=1)




window.mainloop()









