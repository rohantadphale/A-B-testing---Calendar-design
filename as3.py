'''
Rohan Tadphale
Collaborators - None

This is a CSV analysis program for class 422 UI Design and Programming
'''

import pandas as pd
import datetime

df = pd.read_csv('myData.csv')

i = 0
newUserAt = []
users = []
k = 0
totalEventsCreated = 0

for j in range(1, len(df.index)):
	if df.loc[j, "UID"] not in users:
		users.append(df.loc[j, "UID"])
		newUserAt.append(j)
print("Number of Participants:", len(users), "\n")

for k in range(1, len(newUserAt)):
	f_user = newUserAt[k]
	if k < len(newUserAt)-1:
		s_user = newUserAt[k+1]
	else:
		s_user = len(df)

	eventsCreated = 0
	for row in df.loc[f_user:s_user, "Target"]:
		if row == "button#create-event-button.btn.btn-outline-primary" or \
				row == "button#create-event-button.btn.btn-secondary":
			eventsCreated = eventsCreated+1
	totalEventsCreated = totalEventsCreated + eventsCreated
	print("User", k, "created", eventsCreated, "events.")

	d0 = df.loc[f_user, "Timestamp"]
	d1 = df.loc[s_user-1, "Timestamp"]
	print(d0, d1)

	date0 = datetime.datetime.strptime(d0, "%m/%d/%Y %H:%M:%S")
	date1 = datetime.datetime.strptime(d1, "%m/%d/%Y %H:%M:%S")
	delta = date1 - date0
	delta_s = delta.seconds
	print("Total Time taken by user", k, "to complete", eventsCreated, "tasks:", delta)
	if eventsCreated != 0:
		print("Average time per task:", delta_s / eventsCreated, "s\n")
print("Total events Created:", totalEventsCreated)
