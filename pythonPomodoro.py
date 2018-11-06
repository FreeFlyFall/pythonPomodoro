## Pomodoro Timer ##
import tkinter
import winsound
import time
import os

##Pomodoro timer created to require little user interaction

# To-do:
# Create GUI with tkinter

# Define function passed the type of time to be set
def set_time(timeType):
    # Loop trying to return input
    while True:
        try:
            # Get integer input from user for the specific time type
            return int(input('Enter ' + timeType + ' time in seconds as an integer: '))
        # Print error if input isn't an int and return to getting integer input
        except: #ValueError:
            print('Invalid input')
            continue

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

# Tell the user how to exit the program during operation
print('Press Ctrl+C if you want to exit during the countdown.')

# Set work and break times using the set_time() function
workTime = set_time("work")
breakTime = set_time("break")
# Create counter variable to track time and initialize it to be the value of workTime
counter = workTime
# Initialize boolean for state
isWorking = True

# Loop to run countdown and inform user
while True:
    # If the countdown is running
    if counter > 0:
        # Wait one second, decrement the counter, and print the remaining time
        print(counter)
        time.sleep(1)
        counter -= 1

    # Else if the counter is done
    elif (counter <= 0):
        # Get data tuple from time_up() function
        data = time_up(isWorking, breakTime, workTime)
        # Using the data indices which were set according to the state, print the message,
        # play the sound, set the counter, and set the state
        print(data[0])
        # Sound options for different operating systems (Wav files only)
        # os.system("aplay sound.wav&") # Linux
        # os.system("afplay sound.wav&") # Mac
        winsound.PlaySound(data[1], winsound.SND_ASYNC) #windows
        counter = data[2]
        isWorking = data[3]
