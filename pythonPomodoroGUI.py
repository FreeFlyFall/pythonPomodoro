## Pomodoro Timer ##
import tkinter as tk
import winsound
import time
import os

## Pomodoro timer created to require little user interaction
## window.update causes lag. Optimize using after().
## GUI version should probably use OOP

# FUNCTIONS
# Define function to start the app
def set_time():
    try:
        # Get integer input from tkinter entry fields for the 2 time types
        workTime = int(workEntry.get())
        breakTime = int(breakEntry.get())
        counter = workTime
        isWorking = True
        # Tuple for the initial display, [1] empty for compatibility
        # with concatenation when calling set_notifLabel()
        data = ('Get to work!', '')

        # Loop to run countdown and inform user
        while True:
            # If the countdown is running
            if counter > 0:
                # Wait one second, decrement the counter, and print the remaining time
                counterString = str(counter)
                set_notifLabel(data[0] + " " + counterString)
                # Update window, could be more efficient with a coroutine and
                # control variable while using after()
                window.update()
                counter -= 1
                time.sleep(1)
            # Else if the counter is done
            elif (counter <= 0):
                # Get data tuple from time_up() function
                data = time_up(isWorking, breakTime, workTime)
                # Using the data indices which were set according to the state, show the message,
                # play the sound, set the counter, and set the state
                # Sound options for different operating systems (Wav files only)
                    # os.system("aplay sound.wav&") # Linux
                    # os.system("afplay sound.wav&") # Mac
                winsound.PlaySound(data[1], winsound.SND_ASYNC) #windows
                counter = data[2]
                isWorking = data[3]
    # Print error if exception occurs
    except Exception as e: #ValueError:
        #print('Invalid input')
        print(e)


# Define function passed state and times
def time_up(isWorking, breakTime, workTime):
    # If the user is working
    if isWorking == True:
        # Set variables for the break state
        msg = 'Take a break!'
        soundName = 'BreakSound'
        counter = breakTime
    # Else, the user is not working
    else:
        # Set the variables for the work state
        msg = 'Get back to work!'
        soundName = 'WorkSound'
        counter = workTime
    # Invert the state
    isWorking = not isWorking
    # Create a data tuple and return it
    returnData = (msg, soundName, counter, isWorking)
    return returnData

# TKINTER
# Window setup
window = tk.Tk()
window.title("Python Pomodoro")
window.geometry("250x150")
# Label
label1 = tk.Label(text="Pomodoro", font=("Times New Roman", 20))
label1.grid(column=0, row=0)
workLabel = tk.Label(text="Work length")
workLabel.grid(column=0, row=1)
breakLabel = tk.Label(text="Break length")
breakLabel.grid(column=0, row=2)
notifLabel = tk.Label(text="")
notifLabel.grid(column=0, row=4)
def set_notifLabel(update):
    notifLabel['text'] = update
# Entry
workEntry = tk.Entry()
workEntry.grid(column=1, row=1)
breakEntry = tk.Entry()
breakEntry.grid(column=1, row=2)
# Button
button1 = tk.Button(text="Start", font=("Times New Roman", 12), command=set_time)
button1.grid(column=0, row=3)
# mainloop
window.mainloop()