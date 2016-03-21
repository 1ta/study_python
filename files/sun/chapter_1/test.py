pointsStr = input("Enter the lead in points: ")
points = int(pointsStr)

has_ball = input("Does the lead has ball(yes or no): ")
if has_ball == "yes":
    points = points - 3
else:
    points = points + 3

if points < 0:
    points = 0

points = points ** 2

time_left = input("The seconds of match left:")
seconds = int(time_left)

if points > seconds:
    print("the lead is safe")
else:
    print("the lead is not safe")
