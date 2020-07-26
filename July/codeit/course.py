import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

for course in df['course name'].unique():
    course_counts = len(df.loc[df['course name'] == course])
    if 5 < course_counts < 15:
        df.loc[df['course name']== course, 'room assignment'] = "Small room"
    elif 15 <= course_counts < 40:
        df.loc[df['course name']== course, 'room assignment'] = "Medium room"
    elif 40 <= course_counts < 80:
        df.loc[df['course name']== course, 'room assignment'] = "Large room"
    elif 80 <= course_counts:
        df.loc[df['course name']==course, 'room assignment'] = "Auditorium"
df.loc[df['status']=="not allowed", "room assignment"] = "not assigned"

df





