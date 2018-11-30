import winsound
import time
import os

'''
Pomodoro timer created to require little user interaction without the need for a browser
'''

# -- FUNCTIONS -------
# Define function passed the type of time that sets that time
def set_time(timeType):
    while True:
        try:
            # Get integer input from user for the specific time type
            inputData = input('Enter ' + timeType + ' hours, minutes, and seconds separated by a space: ')
            h, m, s = inputData.split(' ')
            timeData = [h, m, s]
            for i, data in enumerate(timeData):
                timeData[i] = int(timeData[i])
                if(timeData[i] > 60):
                    print("Input " + str(timeData[i]) + " > 60; flooring.")
                    timeData[i] = 60
            h, m, s = timeData
            return h, m, s
        # Print error and return to getting integer input
        except Exception as e: #ValueError:
            print(e)
            continue

# Define function passed state and times that returns data
def change_state():
    # If the user is working
    if isWorking:
        # Set & return the variables for the break state
        return 'Take a break!', 'BreakSound', breakHours, breakMinutes, breakSeconds
    # Else, the user is not working
    else:
        # Set & return the variables for the work state
        return 'Get back to work!', 'WorkSound', workHours, workMinutes, workSeconds

# -- PROGRAM START -------

print('Press Ctrl+C to exit during the countdown.')
# Get and set both the work and break times using the set_time() function
workHours, workMinutes, workSeconds = set_time("work")
breakHours, breakMinutes, breakSeconds = set_time("break")
# Create counter variables to track time and initialize them to be the value for working state
counterHours, counterMinutes, counterSeconds = workHours, workMinutes, workSeconds
isWorking = True

# Loop to repeatedly run countdown logic and inform user
while True:
    # If the countdown is running
    if (counterHours >= 0 and counterMinutes >= 0 and counterSeconds >= 0):
        # Wait one second, decrement the counter, and print the remaining time
        print(counterHours, counterMinutes, counterSeconds)
        if(counterSeconds > 0):
            counterSeconds -= 1
        elif(counterMinutes > 0):
            counterMinutes -= 1
            counterSeconds = 59
        elif(counterHours > 0):
            counterHours -= 1
            counterMinutes = 59
            counterSeconds = 59
        time.sleep(1)
    # Else if the counter is done
        if(counterHours == 0 and counterMinutes == 0 and counterSeconds == 0):
            # Get data sequence from change_state() function and set the varibles
            notification, sound, passedHours, passedMinutes, passedSeconds = change_state()
            # Using the variables which were set according to the state, print the message,
            # play the sound, and set the counter
            print(notification)
            try:
                winsound.PlaySound(sound, winsound.SND_ASYNC)
            except Exception:
                # If error, try method for playing sound on linux
                try:
                    os.system("aplay " + sound + ".wav&")
                except Exception:
                    # If error, try method for playing sound on a Mac
                    try:
                        os.system("afplay " + sound + ".wav&")
                    except Exception as e:
                        print(e)
            counterHours, counterMinutes, counterSeconds = passedHours, passedMinutes, passedSeconds
            isWorking = not isWorking
            time.sleep(1)