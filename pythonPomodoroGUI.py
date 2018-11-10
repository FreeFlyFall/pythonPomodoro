## Pomodoro Timer ##
import tkinter as tk
import winsound
import time
import os

'''
Pomodoro timer created to require little user interaction
and remove the need to have a browser open
'''

# Class for the display counter label
class displayCounter():
    # Initialize data for the class
    def __init__(self, window):
        self.window=window
        self.notifLabel = tk.Label(text="")
        self.notifLabel.grid(column=0, row=4)
        self.counter = workTime
        self.isWorking = True
        # Tuple for the initial display, [1] empty for compatibility
        # with concatenation when reconfiguring notifLabel(text). I'm being lazy, I know.
        self.data = ('Get to work!', '')
        self.tick()

    #function called every second
    def tick(self):
        try:
            # If the countdown is running
            if self.counter > 0:
                # Set and display the counter string and decrement the counter
                counterDisplayString = self.data[0] + " " + str(self.counter)
                self.notifLabel.config(text=counterDisplayString)
                self.counter -= 1
            # Else if the counter is done
            elif (self.counter <= 0):
                # Get data tuple from time_up() function
                self.data = self.time_up()
                # Using the data indices which were set in time_up(),
                # print the message, play the sound, set the counter, and set the isWorking boolean
                #(Use SND_FILENAME to pause counter while playing the sound)
                # # Sound options for different operating systems (only wav files are compatible with winsound)
                    # os.system("aplay sound.wav&") # Linux
                    # os.system("afplay sound.wav&") # Mac
                winsound.PlaySound(self.data[1], winsound.SND_ASYNC) #windows
                self.counter = self.data[2]
                self.isWorking = self.data[3]
        # Print exception if it occurs
        except Exception as e: #ValueError:
            print(e)
        # Use tkinter's after() function to call tick every second
        self.id=self.window.after(1000, self.tick)

    # Set the state according to the isWorking boolean
    def time_up(self):
        # If the user is working
        if self.isWorking == True:
            # Set tuple values for the break state
            msg = 'Take a break!'
            soundName = 'BreakSound'
            counter = breakTime
        # Else, the user is not working
        else:
            # Set tuples values for the work state
            msg = 'Get back to work!'
            soundName = 'WorkSound'
            counter = workTime
        # Invert the isWorking boolean to be sent back in the tuple
        isWorking = not self.isWorking
        # Create tuple containing the data to be returned and return it
        returnData = (msg, soundName, counter, isWorking)
        return returnData

# number of instances
instances = 0
# Function to instantiate the counter and allow the times to be set while limiting counter to 1 instance
def instantiate_displayCounter():
    global workTime
    global breakTime
    global instances
    # Set the work and break times according to input in the entry fields
    workTime = int(workEntry.get())
    breakTime = int(breakEntry.get())
    # Only allow one instance of the counter
    if(instances == 0):
        d = displayCounter(window)
        instances += 1
    else:
        pass

# TKINTER ---------------------
# SETUP WINDOW
window = tk.Tk()
window.title("Python Pomodoro")
window.geometry("250x150")
# LABEL
label1 = tk.Label(text="Pomodoro", font=("Times New Roman", 20))
label1.grid(column=0, row=0)
workLabel = tk.Label(text="Work length")
workLabel.grid(column=0, row=1)
breakLabel = tk.Label(text="Break length")
breakLabel.grid(column=0, row=2)
# ENTRY
workEntry = tk.Entry()
workEntry.grid(column=1, row=1)
breakEntry = tk.Entry()
breakEntry.grid(column=1, row=2)
# BUTTON
button1 = tk.Button(text="Start", font=("Times New Roman", 12), command=instantiate_displayCounter)
button1.grid(column=0, row=3)
# MAINLOOP
#d = displayCounter(window)
window.mainloop()


