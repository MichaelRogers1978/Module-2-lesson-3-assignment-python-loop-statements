# task 1

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesaday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range (len(days)):
    mood = random.choice(moods)
    print(f"day {days [day]} you were feeling {mood}")

    



# task 2


# Simulate a mood tracker that records your mood at three different times of the day
# (morning, afternoon, evening) for each day of the week.
#  Use nested loops to implement this: the outer loop should iterate over 
#  the days, and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. Use the 
# random module again to randomly select the mood.

time_of_day = ["morning", "afternoon", "evening"]
moods = ["Happy", "Mad", "Sad"]
for day in days:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"My mood is {mood}: in the {day} {time}")