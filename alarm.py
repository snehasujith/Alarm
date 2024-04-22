import tkinter as tk
import tkinter.messagebox as messagebox
import time

def set_alarm():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        messagebox.showerror("Invalid Input", "Please enter valid hour (0-23) and minute (0-59)")
        return

    alarm_time = f"{hour:02d}:{minute:02d}"

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Wake up!")
            break
        time.sleep(1)

# Create the main window
root = tk.Tk()
root.title("Simple Alarm")

# Hour Entry
hour_label = tk.Label(root, text="Hour:")
hour_label.grid(row=0, column=0, padx=5, pady=5)
hour_entry = tk.Entry(root, width=5)
hour_entry.grid(row=0, column=1, padx=5, pady=5)

# Minute Entry
minute_label = tk.Label(root, text="Minute:")
minute_label.grid(row=1, column=0, padx=5, pady=5)
minute_entry = tk.Entry(root, width=5)
minute_entry.grid(row=1, column=1, padx=5, pady=5)

# Set Alarm Button
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
