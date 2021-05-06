import winsound, time, os, re

'''
Pomodoro timer created to require little user interaction and remove the need to have a browser open.
Enter times for work, break, and long break in minutes, and the number of iterations before the long break time activates,
separated by spaces.

e.g. "1h45 15 30 3" to work for 1 hour 45 minutes with a 15 min break for 3 cycles, followed by a cycle with a 30 minute break.

Times can be input as #h#, #h#m, #h, #m, or #. Number with no label are taken as minutes.
    For 1 hour and 45 minutes, acceptable inputs are 1h45, and 1h45m.
    For 1 hour, acceptable input is 1h.
    For 30 minutes, acceptable inputs are 30m, and 30.
'''

# -- FUNCTIONS -------
# Returns time strings
def set_times():
    while True:
        retry = False
        try:
            try:
                w, b, l, i = input('> ').strip().split(' ')
            except KeyboardInterrupt:
                exit()
            except:    
                print('Enter 4 times')
                continue
            # Validate times
            for string in [w, b, l]:
                # Parse hours and minutes from each input
                hours = search_hours(string)
                if hours:
                    hours = hours.group().replace('h','')
                minutes = search_minutes(string)
                if minutes:
                    minutes = minutes.group().replace('m','')
                # Ensure that a time was parsed from the input
                if not hours and not minutes:
                    print(f'Invalid input: {string}')
                    retry = True
                    continue
                # Time is too short
                for string in minutes, hours:
                    if string and int(string) < 1:
                        print(f'{string} is less than 1')
                        retry = True
                # Time is too long
                if hours and int(hours) > 24:
                    print(f'{hours}h is too long')                        
                if minutes and int(minutes)/60 > 24: 
                    print(f'{minutes}m is too long')
            if retry:
                continue
            # Validate iterations
            iterations = re.search('\d+$',i)
            if not iterations or int(iterations.group()) < 1:
                print(f'{i} is not a valid iteration count')
                continue
            # Confirm that the user wants to continue with the input   
            print(f'Work: {w}, Break: {b}, Long Break: {l}, Iterations: {i}')
            try:
                confirm = input('Continue? (Y/n): ').upper()
                if confirm != 'Y' and confirm != '':
                    continue
            except KeyboardInterrupt:
                exit()
            # Return times and number of iterations
            return cycle_time(w), cycle_time(b), cycle_time(l), i
        # Print error and return to getting input
        except Exception as e:
            print(e)

# Search for times
def search_minutes(string):
    return re.search('h/d+$|\d+m|\d+$', string) # Match 1+ digits after h followed by end of line, 1+ digits followed by m, or 1+ digits followed by end of line
def search_hours(string):
    return re.search('(\d+)h',string)

# Return time in minutes
def cycle_time(string):
    # Parse hours and minutes
    hours = search_hours(string)
    if hours:
        hours = hours.group().replace('h','')
    minutes = search_minutes(string)
    if minutes:
        minutes = minutes.group().replace('m','') 
    # Return total minutes
    if hours and minutes:
        return int(hours)*60 + int(minutes)
    elif hours and not minutes:
        return int(hours)*60
    else:
        return int(minutes)

def start_timer(mins, iteration_type):
    seconds = int(mins) * 60
    timer = Timer(seconds)
    # Print time every second until the timer is finished
    print(' '.join([timer.value(),iteration_type])) # Print initial time
    while not timer.is_done():
        if timer.is_next_second(): # When the second has changed since the last poll
            print(f'{timer.value()} {iteration_type}')
        time.sleep(0.1) # Polling rate to update countdown
    # Play a sound when the timer finishes 
    if iteration_type == 'work':
        play_sound('BreakSound')
    else:
        play_sound('WorkSound')

class Timer():
    def __init__(self, seconds):
        self.start_time = time.time()
        self.total_seconds = int(seconds) # How many seconds to wait for
        self.current_second = 0 # Store a second value to compare against time
    def elapsed(self):
        return int(time.time()-self.start_time)
    def is_next_second(self):
        value = self.elapsed() > self.current_second
        self.current_second += self.elapsed() - self.current_second # Update internal time value
        return value
    def value(self):
        display_seconds = int((self.total_seconds - self.elapsed()) % 60)
        display_minutes = int((self.total_seconds/60 - self.elapsed()/60) % 60)
        display_hours = int(self.total_seconds/60/60 - self.elapsed()/60/60)
        if display_seconds == 0 and display_minutes == 0:
            display_hours += 1
        return f'{zero_pad_int(display_hours)}:{zero_pad_int(display_minutes)}:{zero_pad_int(display_seconds)}'
    def is_done(self):
        return self.elapsed() >= self.total_seconds

def play_sound(sound):
    try:
        winsound.PlaySound(sound, winsound.SND_ASYNC)
    except Exception:
        # If error, try method for playing sound on linux
        try:
            os.system(f'aplay {sound}.wav&')
        except Exception:
            # If error, try method for playing sound on a Mac
            try:
                os.system(f'afplay {sound}.wav&')
            except Exception as e:
                print(e)
            
def zero_pad_int(integer):
    if integer < 10:
        return f"0{str(integer)}"
    else:
        return str(integer)

# -- PROGRAM START -------
print('Press Ctrl+C to exit during the countdown.')
string = ('Enter times for work, break, and long break in minutes, and the number of iterations before the long break time activates,'
    ' separated by spaces.\n\ne.g. \"1h45 15 30 3\" to work for 1 hour 45 minutes with a 15 min break for 3 cycles, followed by a cycle with a 30 minute break:')
print(string)
work_time, break_time, long_time, iterations = set_times()
# Loop through cycles
while True:
    for loop in range(int(iterations)+1):
        start_timer(work_time, 'work')
        if loop < int(iterations):
            start_timer(break_time, 'break')
        else:
            start_timer(long_time, 'long break')