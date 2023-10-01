#Calculate alarm time based on current time and timer setting in hours, using 24-hour time format.

curr_time = int(input('\nEnter the current hour (0 to 23): '))
timer_hrs = int(input('Set the timer (in hours) to : '))
print('\nThe alarm will sound at {:02d}'.format((curr_time + timer_hrs)
                                                % 24), ':00', sep = '')
