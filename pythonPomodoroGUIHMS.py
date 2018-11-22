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
        self.notifLabel.grid(column=2, row=3)
        self.workHours, self.workMinutes, self.workSeconds, self.breakHours, self.breakMinutes, self.breakSeconds = hmsdata
        self.isWorking = True
        # Tuple for the initial display, [1] empty for compatibility
        # with concatenation when reconfiguring notifLabel(text). I'm being lazy, I know.
        self.data = ('Get to work!', '')
        self.tick()

    #function called every second
    def tick(self):
        try:
            if(self.isWorking == True):
                self.displayData = str(self.workHours) + ":" + str(self.workMinutes) + ":" + str(self.workSeconds)
                print(self.workHours, self.workMinutes, self.workSeconds)
                if (self.workHours >= 0 and self.workMinutes >= 0 and self.workSeconds >= 0):
                    # Set and display the counter string and decrement the counter
                    counterDisplayString = self.data[0] + " " + str(self.displayData)
                    self.notifLabel.config(text=counterDisplayString)
                    # If the counter is done
                    if (self.workHours == 0 and self.workMinutes == 0 and self.workSeconds == 1):
                        # Get data tuple from time_up() function
                        self.data = self.time_up()
                        # Using the data indices which were set in time_up(),
                        # print the message, play the sound, set the counter, and set the isWorking boolean
                        #(Use SND_FILENAME to pause counter while playing the sound)
                        # # Sound options for different operating systems (only wav files are compatible with winsound)
                            # os.system("aplay sound.wav&") # Linux
                            # os.system("afplay sound.wav&") # Mac
                        winsound.PlaySound(self.data[1], winsound.SND_ASYNC) #windows
                        self.isWorking = self.data[2]
                    else:
                        if(self.workSeconds > 0):
                            self.workSeconds -= 1
                        elif(self.workMinutes > 0):
                            self.workMinutes -= 1
                            self.workSeconds = 59
                        elif(self.workHours > 0):
                            self.workHours -= 1
                            self.workMinutes = 59
            else:
                self.displayData = str(self.breakHours) + ":" + str(self.breakMinutes) + ":" + str(self.breakSeconds)
                print(self.breakHours, self.breakMinutes, self.breakSeconds)
                if (self.breakHours >= 0 and self.breakMinutes >= 0 and self.breakSeconds >= 0):
                    # Set and display the counter string and decrement the counter
                    counterDisplayString = self.data[0] + " " + str(self.displayData)
                    self.notifLabel.config(text=counterDisplayString)
                    # If the counter is done
                    if (self.breakHours == 0 and self.breakMinutes == 0 and self.breakSeconds == 1):
                        # Get data tuple from time_up() function
                        self.data = self.time_up()
                        # Using the data indices which were set in time_up(),
                        # print the message, play the sound, set the counter, and set the isWorking boolean
                        #(Use SND_FILENAME to pause counter while playing the sound)
                        # # Sound options for different operating systems (only wav files are compatible with winsound)
                            # os.system("aplay sound.wav&") # Linux
                            # os.system("afplay sound.wav&") # Mac
                        winsound.PlaySound(self.data[1], winsound.SND_ASYNC) #windows
                        self.isWorking = self.data[2]
                    else:
                        if(self.breakSeconds > 0):
                            self.breakSeconds -= 1
                        elif(self.breakMinutes > 0):
                            self.breakMinutes -= 1
                            self.breakSeconds = 59
                        elif(self.breakHours > 0):
                            self.breakHours -= 1
                            self.breakMinutes = 59

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

# number of displayCounter instances
instances = 0
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


