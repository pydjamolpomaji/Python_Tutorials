import sys
from tkinter import *
import time


def times():
    current_time = time.strftime('%H:%M:%S')
    clock.config(text=current_time)
    clock.after(200, times)


root = Tk()
root.geometry('500x250')
clock = Label(root, font=('times', 50, 'bold'), bg='white')
clock.grid(row=2, column=2, pady=25, padx=100)
times()

digital = Label(root, text='Digital Clock', font='times 24 bold')
digital.grid(row=0, column=2)

H_M_S = Label(root, text=' Hours      Minutes      Seconds   ', font='times 15 bold')
H_M_S.grid(row=3, column=2)

root.mainloop()
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
