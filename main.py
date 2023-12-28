import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK ='✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset ():
    window.after_cancel(timer)
    title.config(text='TIMER',fg=GREEN)
    checkmark.config(text='')
    # text.config(text='00:00')
    canvas.itemconfig(text_timer,text='00:00')

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    l_break_sec = LONG_BREAK_MIN *60
    # work_sec = 3
    # s_break_sec = 2
    # l_break_sec = 1
    if reps == 7:
        count_down(l_break_sec)
        title.config(text='RELAX', fg=GREEN)
        checkmark.config(text=CHECKMARK*math.floor(reps/2))
    elif reps % 2 == 0 or reps == 0:
        count_down(s_break_sec)
        title.config(text='RELAX', fg=GREEN)
        checkmark.config(text=CHECKMARK*math.floor(reps/2))
    else:
        count_down(work_sec)
        title.config(text='WORK', fg=RED)
        checkmark.config(text=CHECKMARK*math.floor(reps/2))




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
title = tkinter.Label(text='Timer',font=(FONT_NAME,30,"bold"),bg=YELLOW,fg=GREEN)
start_button=tkinter.Button(text='Start',command=start_timer)
reset_button=tkinter.Button(text='Reset', command=reset)
checkmark = tkinter.Label(text='✔')
window.title('pomodoro')
window.config(padx=100, pady=50,bg=YELLOW)
canvas =tkinter.Canvas(width=200, height=223,bg=YELLOW,highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=image)
text_timer = canvas.create_text(100, 135, text='00:00', fill='White', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)
checkmark.grid(column=1,row=400)
title.grid(column=1,row=0)








window.mainloop()