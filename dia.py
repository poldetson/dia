#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys
import csv
import tkinter as tk

DOT_SIZE = 10

stations = []
csvfile = open("station.txt", encoding="utf-8")
for row in csv.reader(csvfile):
#    print(row)
    station = [row[0], int(row[1])]
    stations.append(station)
print('stations:')
print(stations)


times = []
csvfile = open("dots.txt", encoding="utf-8")
for row in csv.reader(csvfile):
#    print(row)
    time = []
    for column in row:
#        print(column)
        time.append(int(column))
    times.append(time)
print('times:')
print(times)

root = tk.Tk()
root.title(u"Software Title")
#root.geometry("400x300")

canvas = tk.Canvas(root, height=600, width=1000)

# canvas commands
# create_rectangle(x0, y0, x1, y1, **options)

# draw base lines
baseline_top = 100
baseline_left = 100
baseline_right = 400
#stations = [['A', 100], ['B', 200], ['C', 0]]

line = baseline_top
for station in stations:
    station_name = station[0]
    line = station[1]
    canvas.create_text(baseline_left-15, line, text = station_name, font=("Helvetica", 18, "bold"))
    canvas.create_line(baseline_left, line, baseline_right, line, width=3.0, fill='black')

# draw lines
flag = 0
i = 0
for time in times:
#    print('time:' + str(time))
    if flag == 0:
        flag = 1
        last_station = stations[i][1]
        last_time = time
        i = i + 1
        continue
    station = stations[i][1]
    print('%' + str(i) + ': ' + str(last_time) + ', ' + str(last_station) + ', ' + str(time) + ', ' + str(station))
    canvas.create_line(last_time, last_station, time, station, width=3.0, fill='red')
    last_station = station
    last_time = time
    i = i + 1

# draw dots
i = 0
for time in times:
#    print('time:' + str(time[0]))
#    print('station[i][1]:' + str(stations[i][1]))
    canvas.create_oval(time[0] - DOT_SIZE/2, stations[i][1] - DOT_SIZE/2, time[0] + DOT_SIZE/2, stations[i][1] + DOT_SIZE/2 , fill='blue')
    i = i + 1

canvas.pack()

root.mainloop()

