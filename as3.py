"""
Rohan Tadphale
Collaborators - None

This is a CSV analysis program for class 422 UI Design and Programming
"""

import pandas as pd
import datetime
import plotly
import plotly.graph_objs as go
import collections

# graphPlotted = 0
df1 = pd.read_csv('otherData.csv')
df2 = pd.read_csv('myData2.csv')


def numOfUsers(df):
	users = []
	for j in range(1, len(df.index)):
		if df.loc[j, "UID"] not in users:
			users.append(df.loc[j, "UID"])
	return len(users)


def avgTaskTime(df):
	global graphPlotted
	newUserAt = []
	totalEventsCreated = 0
	total_delta_s = 0
	dataset = collections.namedtuple('dataset', ['events', 'delta'])

	users = []
	for j in range(1, len(df.index)):
		if df.loc[j, "UID"] not in users:
			users.append(df.loc[j, "UID"])
			newUserAt.append(j)
	nUsers = numOfUsers(df)

	for k in range(0, len(newUserAt)):
		f_user = newUserAt[k]
		if k < len(newUserAt)-1:
			s_user = newUserAt[k+1]
		else:
			s_user = len(df)

		eventsCreated_data1 = 0
		eventsCreated_data2 = 0
		for row in df.loc[f_user:s_user, "Target"]:
			if row == "button#create-event-button.btn.btn-outline-primary":
				eventsCreated_data2 = eventsCreated_data2+1
			elif row == "button#create-event-button.btn.btn-secondary":
				eventsCreated_data1 = eventsCreated_data1 + 1
		totalEventsCreated = totalEventsCreated + eventsCreated_data1 + eventsCreated_data2

		if nUsers == 23:
			d0 = df.loc[f_user, "Timestamp"]
			d1 = df.loc[s_user - 1, "Timestamp"]

			date0 = datetime.datetime.strptime(d0, "%m/%d/%Y %H:%M:%S")
			date1 = datetime.datetime.strptime(d1, "%m/%d/%Y %H:%M:%S")
			delta = date1 - date0
			delta_d = delta.days
			delta_s = delta.seconds + (delta_d * 86400)
			total_delta_s = delta_s + total_delta_s
			# print(total_delta_s)
			print("Total Time taken by user", k+1, "to complete", eventsCreated_data2, "tasks:", delta)
			if eventsCreated_data2 != 0:
				print("Average time per task:", delta_s / eventsCreated_data2, "s\n")
			else:
				print("")

		elif nUsers == 13:
			d0 = df.loc[f_user, "Timestamp"]
			d1 = df.loc[s_user - 1, "Timestamp"]

			date0 = datetime.datetime.strptime(d0, "%m/%d/%Y %H:%M:%S")
			date1 = datetime.datetime.strptime(d1, "%m/%d/%Y %H:%M:%S")
			delta = date1 - date0
			delta_d = delta.days
			delta_s = delta.seconds + (delta_d * 86400)
			total_delta_s = delta_s + total_delta_s
			# print(total_delta_s)
			print("Total Time taken by user", k + 1, "to complete", eventsCreated_data1, "tasks:", delta)
			if eventsCreated_data1 != 0:
				print("Average time per task:", delta_s / eventsCreated_data1, "s\n")
			else:
				print("")
	print("Total events Created:", totalEventsCreated)
	return dataset(totalEventsCreated, total_delta_s)

		# 	if not graphPlotted and k == len(newUserAt)-1:
		# 		print("Total events Created:", totalEventsCreated)
		# 		plotGraphs(totalEventsCreated, delta_s)
		# 		graphPlotted = True
		# elif nUsers == 13:
		# 	print("Total Time taken by user", k+1, "to complete", eventsCreated_data1, "tasks:", delta)
		# 	if eventsCreated_data1 != 0:
		# 		print("Average time per task:", delta_s / eventsCreated_data1, "s\n")
		# 	else:
		# 		print("")
		# 	if graphPlotted == 2 and k == len(newUserAt)-1:
		# 		print("Total events Created:", totalEventsCreated)
		# 		plotGraphs(totalEventsCreated, delta_s)
		# 		graphPlotted = 2


def plotGraphs(events_A, delta_A, events_B, delta_B):
	n1 = numOfUsers(df1)
	n2 = numOfUsers(df2)
	trace1 = go.Bar(
		x=["Number of Users", "Total Events Created (/10)", "Average events per user", "Events/10m", "Total Time Spent On Design (min) (/10)", "Average Time Spent per User"],
		y=[n1, events_A/10, events_A/n1, (events_A*60*7.5)/delta_A, delta_A/600, delta_A/(60*n1)],
		name='Design A',
		marker=dict(
			color='rgb(55, 83, 109)'
		)
	)

	trace2 = go.Bar(
		x=["Number of Users", "Total Events Created (/10)", "Average events per user", "Events/10m", "Total Time Spent On Design (min) (/10)", "Average Time Spent per User"],
		y=[n2, events_B/10, events_B/n2, (events_B*8640*5)/delta_B, delta_B/60000, delta_B/(6000*n2)],
		name='Design B',
		marker=dict(
			color='rgb(26, 118, 255)'
		)
	)

	data = [trace1, trace2]
	layout = go.Layout(
		title='Calendar design - A/B Testing',
		xaxis=dict(
			tickfont=dict(
				size=14,
				color='rgb(107, 107, 107)'
			)
		),
		yaxis=dict(
			title='',
			titlefont=dict(
				size=16,
				color='rgb(107, 107, 107)'
			),
			tickfont=dict(
				size=14,
				color='rgb(107, 107, 107)'
			)
		),
		legend=dict(
			x=0,
			y=1.0,
			bgcolor='rgba(255, 255, 255, 0)',
			bordercolor='rgba(255, 255, 255, 0)'
		),
		barmode='group',
		bargap=0.15,
		bargroupgap=0.1
	)
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename='style-bar.html')


def main():
	dataset1 = collections.namedtuple('dataset', ['events', 'delta'])
	dataset2 = collections.namedtuple('dataset', ['events', 'delta'])
	print("\n--- Calendar Design A Analysis ---\n")
	n1 = numOfUsers(df1)
	print("Number of Participants:", n1, "\n")
	dataset1 = avgTaskTime(df1)
	print("\n\n\n--- Calendar Design B Analysis ---")
	n2 = numOfUsers(df2)
	print("Number of Participants:", n2, "\n")
	dataset2 = avgTaskTime(df2)
	plotGraphs(dataset1.events, dataset1.delta, dataset2.events, dataset2.delta)


if __name__ == '__main__':
		main()