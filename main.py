from parse_input import parse_input
from project1_starter import find_aval_timeslots, schedule_meeting

with open('output.txt', 'w') as file: # creates a new empty output file
    pass

data = parse_input('input.txt')

for sch in data:
    person1_busy_Schedule = sch[0]
    person1_work_hours = sch[1]
    person2_busy_Schedule = sch[2]
    person2_work_hours = sch[3]
    duration_of_meeting = sch[4]

    person1_aval = find_aval_timeslots(person1_busy_Schedule, person1_work_hours, duration_of_meeting)
    person2_aval = find_aval_timeslots(person2_busy_Schedule, person2_work_hours, duration_of_meeting)

    meeting_time = str( schedule_meeting(person1_aval, person2_aval, duration_of_meeting) )

    with open('output.txt', 'a') as file:
        file.write(meeting_time + '\n')