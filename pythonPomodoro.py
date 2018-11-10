import tkinter
import winsound
import time
import os
'''
Pomodoro timer created to require little user interaction
'''

# -- FUNCTIONS -------
# Define function passed the type of time that sets the time
def set_time(timeType):
    # Loop to return input
    while True:
        try:
            # Get integer input from user for the specific time type
            return int(input('Enter ' + timeType + ' time in seconds as an integer: '))
        # Print error if input isn't an int and return to getting integer input
        except: #ValueError:
            print('Invalid input')
            continue

# Define function passed state and times that returns data
def change_state():
    # If the user is working
    if isWorking == True:
        # Set & return the variables for the break state
        return 'Take a break!', 'BreakSound', breakTime, False
    # Else, the user is not working
    else:
        # Set & return the variables for the work state
        return 'Get back to work!', 'WorkSound', workTime, True

# -- PROGRAM START -------
global isWorking
global workTime
global breakTime
print('Press Ctrl+C to exit during the countdown.')
# Get and set both the work and break times using the set_time() function
workTime = set_time("work")
breakTime = set_time("break")
# Create counter variable to track time and initialize it to be the value of workTime
counter = workTime
# Initialize boolean for state that tells whether the user is working
isWorking = True

# Loop to repeatedly run countdown and inform user
while True:
    # If the countdown is running
    if counter > 0:
        # Wait one second, decrement the counter, and print the remaining time
        print(counter)
        time.sleep(1)
        counter -= 1
    # Else if the counter is done
    elif (counter <= 0):
        # Get data sequence from change_state() function and set the varibles
        notification, sound, passedTime, booleanState = change_state()
        # Using the variables which were set according to the state, print the message,
        # play the sound, set the counter, and set the state
        print(notification)
        # Sound options for different operating systems (Wav files only)
            # os.system("aplay sound.wav&") # Linux
            # os.system("afplay sound.wav&") # Mac
        winsound.PlaySound(sound, winsound.SND_ASYNC) #windows
        counter = passedTime
        isWorking = booleanState