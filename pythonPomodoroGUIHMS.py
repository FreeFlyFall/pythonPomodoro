## Pomodoro Timer ##
import tkinter as tk
import winsound
import time
import os

'''
Pomodoro timer created to require little user interaction
and remove the need to have a browser open
'''

#Initial HMS variables
timeHours, timeMinutes, timeSeconds = 0, 0, 0
# Initial number of displayCounter instances
instances = 0

# displayCounter Object
class displayCounter():
    def __init__(self, window):
        self.window=window
        self.notifLabel = tk.Label(text="")
        self.notifLabel.grid(column=2, row=3)
        self.workHours, self.workMinutes, self.workSeconds, self.breakHours, self.breakMinutes, self.breakSeconds = hmsdata
        self.isWorking = True
        self.textNotifData = ('Get to work!', '')
        global timeHours, timeMinutes, timeSeconds
        timeHours, timeMinutes, timeSeconds = self.workHours, self.workMinutes, self.workSeconds
        self.tick()

    # Called once per second
    def tick(self):
        global timeHours, timeMinutes, timeSeconds
        try:
            # if the countdown is running
            if (timeHours >= 0 and timeMinutes >= 0 and timeSeconds >= 0):
                # Set the HMS data to be displayed
                self.timeDisplayData = str(timeHours) + ":" + str(timeMinutes) + ":" + str(timeSeconds)
                # Set and display the  and decrement the counter
                notifString = self.textNotifData[0] + " " + str(self.timeDisplayData)
                self.notifLabel.config(text=notifString)
                # If the counter is done
                if (timeHours == 0 and timeMinutes == 0 and timeSeconds == 0):
                    # Get data tuple from time_up() function
                    self.textNotifData = self.time_up()
                    # Using the data indices which were set in time_up(),
                    # print the message, play the sound, set the counter, and set the isWorking boolean
                    #(Use SND_FILENAME to pause counter while playing the sound)
                    # # Sound options for different operating systems (only wav files are compatible with winsound)
                        # os.system("aplay sound.wav&") # Linux
                        # os.system("afplay sound.wav&") # Mac
                    winsound.PlaySound(self.textNotifData[1], winsound.SND_ASYNC) #windows
                    self.isWorking = self.textNotifData[2]
                    if(self.isWorking):
                        timeHours, timeMinutes, timeSeconds = self.workHours, self.workMinutes, self.workSeconds
                    else:
                        timeHours, timeMinutes, timeSeconds = self.breakHours, self.breakMinutes, self.breakSeconds
                else:
                    if(timeSeconds > 0):
                        timeSeconds -= 1
                    elif(timeMinutes > 0):
                        timeMinutes -= 1
                        timeSeconds = 59
                    elif(timeHours > 0):
                        timeHours -= 1
                        timeMinutes = 59
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
        # Else, the user is not working
        else:
            # Set tuples values for the work state
            msg = 'Get to work!'
            soundName = 'WorkSound'
        # Invert the isWorking boolean to be sent back in the tuple
        isWorking = not self.isWorking
        # Create tuple containing the data to be returned and return it
        returnData = (msg, soundName, isWorking)
        self.workHours, self.workMinutes, self.workSeconds, self.breakHours, self.breakMinutes, self.breakSeconds = hmsdata
        return returnData

# Function to instantiate the counter and allow the times to be set while limiting counter to 1 instance
def instantiate_displayCounter():
    global instances
    global hmsdata
    hmsdata = [int(workHoursEntry.get()), int(workMinutesEntry.get()), int(workSecondsEntry.get()), int(breakHoursEntry.get()), int(breakMinutesEntry.get()), int(breakSecondsEntry.get())]
    for i, data in enumerate(hmsdata):
        if hmsdata[i] > 60:
            print("Input " + str(hmsdata[i]) + " > 60; flooring.")
            hmsdata[i] = 60
    print("Input = " + str(hmsdata))
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
window.geometry("550x150")
# LABEL
headLabel = tk.Label(text="Pomodoro", font=("Times New Roman", 20))
headLabel.grid(column=0, row=0)
workTextLabel = tk.Label(text="Work length")
workTextLabel.grid(column=0, row=1)
breakTextLabel = tk.Label(text="Break length")
breakTextLabel.grid(column=0, row=2)
workHoursLabel = tk.Label(text="H")
workHoursLabel.grid(column=1, row=1)
breakHoursLabel = tk.Label(text="H")
breakHoursLabel.grid(column=1, row=2)
workMinutesLabel = tk.Label(text="M")
workMinutesLabel.grid(column=3, row=1)
breakMinutesLabel = tk.Label(text="M")
breakMinutesLabel.grid(column=3, row=2)
workSecondsLabel = tk.Label(text="S")
workSecondsLabel.grid(column=5, row=1)
breakSecondsLabel = tk.Label(text="S")
breakSecondsLabel.grid(column=5, row=2)
# ENTRY
workHoursEntry = tk.Entry()
workHoursEntry.grid(column=2, row=1)
breakHoursEntry = tk.Entry()
breakHoursEntry.grid(column=2, row=2)
workMinutesEntry = tk.Entry()
workMinutesEntry.grid(column=4, row=1)
breakMinutesEntry = tk.Entry()
breakMinutesEntry.grid(column=4, row=2)
workSecondsEntry = tk.Entry()
workSecondsEntry.grid(column=6, row=1)
breakSecondsEntry = tk.Entry()
breakSecondsEntry.grid(column=6, row=2)
# BUTTON
button1 = tk.Button(text="Start", font=("Times New Roman", 12), command=instantiate_displayCounter)
button1.grid(column=0, row=3)
# MAINLOOP
window.mainloop()