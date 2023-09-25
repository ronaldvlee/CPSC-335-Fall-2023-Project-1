from parse_input import parse_input
from typing import List

def convert_to_mins(time_str: str) -> int: # O(1)
    """Takes in time in 'hh:mm' format and converts it to minutes of the day."""
    hr, mins = map(int, time_str.split(':'))
    return hr * 60 + mins

def convert_to_timestr(time_in_mins: int) -> str: # O(1)
    """Takes in time in minutes of the day and converts it to a hh:mm format."""
    hr = time_in_mins // 60
    mins = time_in_mins % 60

    return f'{hr:02d}:{mins:02d}'

def find_aval_timeslots(busy_sch: List[List[str]], work_hrs: List[str], duration: int) -> List[List[int]]: # O(n)
    """Finds all available timeslots that the person has given their busy schedule and workhours."""
    aval_sch = [] # initalize empty list to push the available times into

    busy_sch_mins = [ [convert_to_mins(start), convert_to_mins(end)] for start, end in busy_sch ] # converting the time str to time in mins
    
    work_start = convert_to_mins(work_hrs[0]) # convert work hour's start time to mins
    work_end = convert_to_mins(work_hrs[1])   # convert work hour's end time to mins

    # Visualizing our problem:
    #   {work_start-----[busytime1]---[busytime2]--..--[busytimeX]---work_end}
    #   Encased in the brackets is our imaginary schedule
    #
    # All we have to do is grab the dotted lines in between the busytimes, work_start, work_end

    # Start with the first initial dotted line first, so from work_start to the first "busytime"
    if busy_sch_mins[0][0] > work_start:
        aval_sch.append([work_start, busy_sch_mins[0][0]])

    # ..now for all the busy times in between each other so lets say [busytime1] and [busytime2] and [busytimex] and so on
    # Start from 1 on the range since we already did the first elem
    for i in range(1, len(busy_sch_mins)):
        aval_sch.append([busy_sch_mins[i-1][1], busy_sch_mins[i][0]])

    # Keep in mind that the above isn't doing the last busytime to work_end yet so doing that on the below.
    if busy_sch_mins[-1][1] < work_end:
        aval_sch.append([busy_sch_mins[-1][1], work_end])

    # Now since we do not care for the availability that cannot fit the meeting. We can just filter through those
    # and make a new list for the times that actually fit.
    return [time for time in aval_sch if time[1] - time[0] >= duration]

def schedule_meeting(person1_aval: List[List[int]], person2_aval: List[List[int]], duration: int) -> List[List[str]]: # O(n^2)
    """Given two availabile timeslots (in minute units) and duration of the meeting, returns the available timeslots."""
    aval_times = []

    for start1, end1 in person1_aval:           # these two for loops will go through both availabilities
        for start2, end2 in person2_aval:

            common_start = max(start1, start2)
            common_end = min(end1, end2)

            if common_end - common_start >= duration:
                aval_times.append([convert_to_timestr(common_start), convert_to_timestr(common_end)])

    return aval_times

data = parse_input('input.txt')

for sch in data:
    person1_busy_Schedule = sch[0]
    person1_work_hours = sch[1]
    person2_busy_Schedule = sch[2]
    person2_work_hours = sch[3]
    duration_of_meeting = sch[4]

    person1_aval = find_aval_timeslots(person1_busy_Schedule, person1_work_hours, duration_of_meeting)
    person2_aval = find_aval_timeslots(person2_busy_Schedule, person2_work_hours, duration_of_meeting)

    print(schedule_meeting(person1_aval, person2_aval, duration_of_meeting))