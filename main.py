from tkinter import *
import math

# colors and other constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#  timer reset functionality
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0
    start_button.config(state=NORMAL)

# timer mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN)
    start_button.config(state=DISABLED)

# countdown mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        sessions = math.floor(reps / 2)
        for i in range(sessions):
            mark += "✔"
        label_check.config(text=mark)
        start_button.config(state=NORMAL)

# ui setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
canvas.grid(column=2, row=2)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))


# text
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Montserrat", 40, "bold"))
label.grid(column=2, row=1)
label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_check.grid(column=2, row=4)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)

window.mainloop()
