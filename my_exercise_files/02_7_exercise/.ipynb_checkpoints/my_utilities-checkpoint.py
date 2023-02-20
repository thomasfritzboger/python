"""
- the function must take 4 arguments (period_as_timedelta, time_of_day, number_of_meetings, start_date=now())
- the function should then return a list of datetimes for a series of meetings that should take place from start_date and evenly distributed throughout the period.
- create another list of number of attendents, that was actually there at each meeting.
- create a bar plot of attendance through the series of meetings.
"""
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import random

def get_meeting_dates(period_as_time_delta,time_of_day,number_of_meetings,start_date=datetime.datetime.now()):
    # dates evenly distributed throughout the period_as_timedelta
     meeting_dates = [start_date + i * (period_as_time_delta / number_of_meetings) for i in range(number_of_meetings)]
     print(len(meeting_dates))
     for m in meeting_dates:
        print(m.strftime("%A, %d. %b %I:%M%p"))
     print('\n\n')

     # Add the time_of_day to each date in the meeting_dates list
     meeting_dates = [datetime.datetime.combine(d.date(), time_of_day) for d in meeting_dates]
     for m in meeting_dates:
        print(m.strftime("%A, %d. %b %I:%M%p"))
     attendee_counts = [random.randint(0, 100) for _ in range(number_of_meetings)]
     return meeting_dates, attendee_counts

dates, attendance = get_meeting_dates(timedelta(days=30), datetime.time(10, 0), 12)

plt.bar(dates, attendance)
plt.xlabel('Meeting Date')
plt.ylabel('Attendance')
#plt.title('Attendance at Meetings')
#plt.xticks(rotation=45)
#plt.tight_layout()
plt.show()

