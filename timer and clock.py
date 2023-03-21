import tkinter as tk
from tkinter import *
import time
import pygame
pygame.mixer.init()
def new_window():
    # create a window
    window = tk.Tk()
    window.title('Electronic Clock')
    window.geometry('1439x900')

    
    selected_var = StringVar(window)  
    # Create a function for updating clock
    def clock_update():
        current_time = time.strftime('%H:%M:%S %p')
        clock_label.config(text=current_time)
        window.after(1000, clock_update)



    w = OptionMenu(window, selected_var, "blip.wav","boing2.wav","dog_barking.wav","alarm_beep.wav","bell_ringing.wav") 
    w.pack() 
   
#creating the submit button

# Function to be called when user selects an option 
   
# Create a label
    clock_label = tk.Label(window, font=('Helvetica', 60, 'bold'), bg='green', fg='white')
    clock_label.pack(fill=BOTH, expand=1)
    

# create a function for setting timer
    def set_timer():
        timer_hours = int(hours_entry.get() or 0)
        timer_minutes = int(minutes_entry.get() or 0)
        timer_seconds = int(seconds_entry.get() or 0)
        total_seconds = timer_hours * 3600 + timer_minutes * 60 + timer_seconds
        count_down(total_seconds)

    def count_down(total_seconds):
     # create a function for seconds):
        
        timer_label.config(text=str(total_seconds))
        total_seconds -= 1
        if total_seconds >= 0:
            window.after(1000, count_down, total_seconds)
        else:
            timer_expired()
        

# create a function for timer expired
    def timer_expired():
        expired_label.config(text="Time is Up!")
        
        
        sound_file = selected_var.get()
        pygame.mixer.music.load(sound_file)
        try: 
            pygame.mixer.music.play()
        except pygame.error:  
            if sound_file == "":
                pygame.mixer.music.load("dog_barking.wav")
                pygame.mixer.music.play()

    # create a label for timer
    timer_label = tk.Label(window, font=('Helvetica', 50, 'bold'), bg='black', fg='white')
    timer_label.pack(fill=BOTH, expand=1)

# create entries
    hours_label = tk.Label(window, text="Hours")

    minutes_label = tk.Label(window, text="Minutes")
    seconds_label = tk.Label(window, text="Seconds")
    hours_label.pack()
    minutes_label.pack()
    seconds_label.pack()
    hours_entry = tk.Entry(window)
    minutes_entry = tk.Entry(window)
    seconds_entry = tk.Entry(window)

    hours_entry.pack()
    minutes_entry.pack()
    seconds_entry.pack()

# call a function
    clock_update()
    
    def play_sound_a():
        
        pygame.mixer.music.load(selected_var.get())
        pygame.mixer.music.play()



# create a button
    set_timer_btn = tk.Button(window, text="Set Timer", command=set_timer)
    set_timer_btn.pack()

# create a dismiss button
    dismiss_btn = tk.Button(window, text="Dismiss", command=lambda: hide_expired_label())
    dismiss_btn.pack()
    play_sound = tk.Button(window, text="Play the sound", command=lambda: play_sound_a())
    play_sound.pack()
    

# create a function to hide the expired label
    def hide_expired_label():
        pygame.mixer.init()
        pygame.mixer.music.stop()
        window.destroy()
        new_window()
    
# create a label for timer expired
    expired_label = tk.Label(window, font=('Helvetica', 30, 'bold'), bg='red', fg='white')
    expired_label.pack(fill=BOTH, expand=1)

    window.mainloop()
new_window()