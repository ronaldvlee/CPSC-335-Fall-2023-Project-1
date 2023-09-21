
# CPSC-335-Fall-2023-Project-1
This project is an algorithm that takes in your schedule, your daily availability (earliest time, latest time) and that of your group member, and the duration of the meeting you want to schedule.  

Time is given and should be returned in military format. For example: 9:30, 22:21. The given times:
- Output should be sorted in ascending order.  
- Inputs are also in sorted order.
## The Problem

### First:
We cannot process a time like "12:30" as a string. We must convert it into a integer.
To do that we first separate the two strings then apply the formula `hours * 60 + minutes`.

Now, we can process the time.
###  Second:
We can break down the problem into two separate problems:
- Find the availability of both people.
- Using the availability of the two, find the available time.

### Third:
To find the availability of the person, we can visualize it like so:

`{work_start-----[busytime1]---[busytime2]--..--[busytimeX]---work_end}`

Above, encased in the brackets is our imaginary schedule. All we have to do is grab the dotted lines in between the busytimes, work_start, work_end.

### Lastly:
We can then find the availability of the two by finding the max of the start and the minimum of the end of the two availabilities. We also need to check if the duration of the availability can fit the duration of the meeting.

## Authors
- Ronald Lee (ronaldvlee@csu.fullerton.edu)
- Israel Faulmino ()