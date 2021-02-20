import sys
import random
import pandas as pd
import datetime

"""
Creates a weight training programme and outputs the schedule as a webpage.
Uses some start weights for the key movements and a random selection of supplementary exercises week to week.
Applies an incremental weight increase week to week for key exercises.
"""
output_path = ""
if len(sys.argv) < 2:
    sys.exit("Provide an output path for the programme.")
else:
    output_path = sys.argv[-1]

push_exercises = ['dumbbell bench press', 'dumbbell military press', 'incline dumbbell bench',
                  'elevated push-up',  'arnold shoulder press', 'tricep throwbacks', 'dips', 'skull crushers']
pull_exercises = ['deadlift', 'dumbbell row', 'trap shrugs',
                  'lat pulldown', 'dumbbell curl', 'pull ups']
legs_exercises = ['squat', 'bulgarian one leg', 'dumbbell lunges',
                  'romanian deadlift', 'leg press', 'calf raise', 'quad curl', 'ham curl', ]

WEEKS = 6
TODAY = datetime.date.today()

bench = 10
military = 12
deadlift = 60
dumbrow = 16
squat = 30
bulgarian = 10

bench_increment = 2
military_increment = 2
deadlift_increment = 10
dumbrow_increment = 2
squat_increment = 10
bulgarian_increment = 2

columns = ['WEEK', 'Legs', 'Push', 'Pull']
weeks = list(range(WEEKS))
rows = []
for week in weeks:
    legs = legs_exercises[:2] + random.sample(legs_exercises[2:], 3)
    legs = "- " + "\n- ".join(legs) + "\n"
    legs += "Squat: {}, Bulgarian: {}".format(
        squat + (squat_increment * week), bulgarian + (bulgarian_increment * week))
    push = push_exercises[:2] + random.sample(push_exercises[2:], 3)
    push = "- " + "\n- ".join(push) + "\n"
    push += "Bench {}, Military: {}".format(
        bench + (bench_increment * week), military + (military_increment * week))
    pull = pull_exercises[:2] + random.sample(pull_exercises[2:], 3)
    pull = "- " + "\n- ".join(pull) + "\n"
    pull += "Dead: {}, Dumbrow: {}".format(deadlift + (
        deadlift_increment * week), dumbrow + (dumbrow_increment * week))
    rows.append([str(week+1) + "\n{}".format((TODAY + datetime.timedelta(days=(7*week))).strftime("%d/%m/%Y")), legs, push, pull])

df = pd.DataFrame(data=rows, columns=columns)
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programme</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
</head>
<body>
    {0}
</body>
</html>
""".format(df.to_html(index=False, classes='table').replace("\\n", "<br>"))

try:
    with open(output_path, 'w+') as file:
        file.write(html)
    print("New program created")
except Exception as e:
    print(e)

