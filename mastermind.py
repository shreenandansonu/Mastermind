import tkinter as tk
import color_guess_main

root=tk.Tk()
root.title("Mastermind")
root.iconbitmap("wheel.ico")
root.geometry('640x380')
root.maxsize(width=640,height=380)
root.minsize(width=640,height=380)
root.columnconfigure(0,weight=1)
root.config(background="#283618")

# ----------------------------------------------------------------------------------------------------------------

sequence=color_guess_main.generate_color()
times=0
print(sequence)
def colorguess(event=None):
    global times #using a variable which is out of the function scope
    times +=1
    guess=code_entry.get()
    c=color_guess_main.check_sequence(sequence,guess)[0]
    i=color_guess_main.check_sequence(sequence,guess)[1]
    code_entry.delete(0,tk.END)
    if(c==4):
        correct_cnt.config(text=c)
        incorrect_cnt.config(text=i)
        total_time.config(text=times)
        instruction.config(text=f"✅🎉 You Won in {times} Rounds 🎉✅")
        root.after(2000,reset)
    else:
        correct_cnt.config(text=c)
        incorrect_cnt.config(text=i)   
        if(times<10):
            total_time.config(text=times)
        else:
            total_time.config(text=times,foreground="#ffd60a")  


def reset():
    global sequence, times
    sequence = color_guess_main.generate_color()  
    times = 0                                       
    print(sequence)                                
    correct_cnt.config(text="0")
    incorrect_cnt.config(text="0")
    total_time.config(text="0")
    instruction.config(text="Choose 4 Color Sequence from the list R,G,B,V,Y,O,W")
    total_time.config(text=times,foreground="#fefae0") 
    code_entry.delete(0, tk.END)  
# ----------------------------------------------------------------------------------------------------------------

head_frame=tk.Frame(root,background="#606c38")
head_frame.grid(row=0,column=0,sticky="nsew")
head_frame.rowconfigure(0,weight=1)
head_frame.columnconfigure(0,weight=1)
heading=tk.Label(head_frame,text="MASTERMIND",font=("Oswald",40),foreground="#fefae0",background="#606c38")
heading.grid(row=0,column=0)

# ----------------------------------------------------------------------------------------------------------------

info_frame=tk.Frame(root,background="#bc6c25")
info_frame.grid(row=1,column=0,sticky="nsew")
info_frame.rowconfigure(0,weight=1)
info_frame.columnconfigure(0,weight=1)

for col in range(6):
    info_frame.columnconfigure(col,weight=1)

correctcnt=tk.Label(info_frame,text="Correct",font=("Oswald",15),foreground="#dda15e",background="#bc6c25")
correctcnt.grid(row=0,column=0,sticky="ew",padx=10)

correct_cnt=tk.Label(info_frame,text="0",font=("Oswald",25),foreground="#fefae0",background="#bc6c25")
correct_cnt.grid(row=0,column=1)

incorrectcnt=tk.Label(info_frame,text="Incorrect",font=("Oswald",15),foreground="#dda15e",background="#bc6c25")
incorrectcnt.grid(row=0,column=2,sticky="ew",padx=10)

incorrect_cnt=tk.Label(info_frame,text="0",font=("Oswald",25),foreground="#fefae0",background="#bc6c25")
incorrect_cnt.grid(row=0,column=3)

totaltime=tk.Label(info_frame,text="Rounds",font=("Oswald",15),foreground="#dda15e",background="#bc6c25")
totaltime.grid(row=0,column=4,sticky="ew",padx=10)

total_time=tk.Label(info_frame,text="0",font=("Oswald",25),foreground="#fefae0",background="#bc6c25")
total_time.grid(row=0,column=5)

# ----------------------------------------------------------------------------------------------------------------
entry_frame=tk.Frame(root,background="#283618")
entry_frame.grid(row=2,column=0,sticky="news",padx=5,pady=5)
entry_frame.rowconfigure(0,weight=1)
entry_frame.columnconfigure(0,weight=1)

for row in range(3):
    entry_frame.rowconfigure(row,weight=1)


instruction=tk.Label(entry_frame,text=f"Choose 4 Color Sequence from the list R,G,B,V,Y,O,W ",font=("Oswald",20),background="#283618",foreground="#fefae0")
instruction.grid(row=0,column=0,sticky="news",pady=10)

code_entry=tk.Entry(entry_frame,background="#fefac5",borderwidth=0,font=("Oswald",25),justify="center")
code_entry.grid(row=1,column=0,sticky="ew")
code_entry.bind("<Return>", colorguess)
# ----------------------------------------------------------------------------------------------------------------
buttons_frame=tk.Frame(root,background="#283618")
buttons_frame.grid(row=3,column=0,sticky="news")
buttons_frame.rowconfigure(0,weight=1)
buttons_frame.columnconfigure(0,weight=1)

for col in range(7):
    buttons_frame.columnconfigure(col,weight=1)

# enter=tk.Button(buttons_frame,text="ENTER",font=("Oswald",15),foreground="#283618",background="#dda15e")
# enter.grid(row=0,column=5,sticky="nsew",padx=10)
reset_btn=tk.Button(buttons_frame,text="RESET",font=("Oswald",15),foreground="#fefae0",background="#bc6c25",activebackground="#dda15e",activeforeground="#fefae0",command=reset)
reset_btn.grid(row=0,column=6,sticky="nsew",padx=7,pady=12)


root.mainloop()

# pyinstaller --onefile --noconsole --icon=wheel.ico mastermind.py

