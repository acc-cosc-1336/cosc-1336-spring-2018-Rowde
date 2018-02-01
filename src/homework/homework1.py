#constant variables
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

#variables needed for time
adjusted_hours = 0
adjusted_minutes = 0
adjusted_seconds = 0


def get_hours_since_midnight(seconds):
    '''
    Type the code to calculate total hours given n(number) of seconds
    For example, given 3800 seconds the total hours is 1
    '''
    adjusted_hours = (seconds // SECONDS_IN_HOUR)
    return adjusted_hours

'''
IF YOU ARE OK WITH A GRADE OF 70 FOR THIS ASSIGNMENT STOP HERE.
'''

def get_minutes(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 3
    '''
    adjusted_minutes = ((seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    return adjusted_minutes

def get_seconds(seconds):
    '''
    Type the code to calculate total minutes less whole hour given n(number) of seconds
    For example, given 3800 seconds the total minutes is 20
    '''
    adjusted_seconds = ((seconds % SECONDS_IN_HOUR) % SECONDS_IN_MINUTE)
    return adjusted_seconds
