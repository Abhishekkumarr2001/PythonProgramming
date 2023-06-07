import _tkinter
from distutils.command.config import config
from tkinter import Button, Canvas, Label, PhotoImage, Tk
import math

from matplotlib import image
from numpy import pad
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")


def start_timer():
    global reps
    reps += 1

    work_sec = 25*60
    short_break_sec = 5*60
    long_break_sec = 20*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="pink")
    count_down(work_sec)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔️"
        check_mark.config(text=mark)


window = Tk()
window.title("Pamodora")
window.config(padx=50, pady=50, bg="#f7f5dd")

title_label = Label(text="Timer", font=(
    "Courier", 50, "bold"), fg="green", bg="#f7f5dd")
title_label.grid(column=1, row=0)


canvas = Canvas(width=500, height=500, bg="#f7f5dd", highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(250, 250, image=tomato)
timer_text = canvas.create_text(250, 250, text="00:00", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", height=2, width=10, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", height=2, width=10, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(font=("Courier", 20, "bold"), fg="green", bg="#f7f5dd")
check_mark.grid(column=1, row=3)

window.mainloop()
