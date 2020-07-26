import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

auditorium = df.loc[df['room assignment'] == 'Auditorium', 'course name']
large = df.loc[df['room assignment']== 'Large room', 'course name']
medium = df.loc[df['room assignment']== 'Medium room', 'course name']
small = df.loc[df['room assignment']== 'Small room', 'course name']

aud_index = sorted(list(auditorium.unique()))
large_index = sorted(list(large.unique()))
medium_index = sorted(list(medium.unique()))
small_index = sorted(list(small.unique()))

for room in auditorium:
    room_num = int(aud_index.index(room)) + int(1)
    df.loc[df['course name']== room, 'room assignment']= 'Auditorium-' + str(room_num)

for room in large:
    room_num = int(large_index.index(room)) + int(1)
    df.loc[df['course name']== room, 'room assignment']= 'Large-' + str(room_num)

for room in medium:
    room_num = int(medium_index.index(room)) + int(1)
    df.loc[df['course name']== room, 'room assignment']= 'Medium-' + str(room_num)

for room in small:
    room_num = int(small_index.index(room)) + int(1)
    df.loc[df['course name']== room, 'room assignment']= 'Small-' + str(room_num)

df.rename(columns={'room assignment': 'room number'}, inplace=True)
df