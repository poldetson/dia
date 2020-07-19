#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys
import csv
import tkinter

# graphical value
DOT_SIZE = 10
CANVAS_SIZE_HEIGHT = 1500
CANVAS_SIZE_WIDTH = 1500
# draw base lines
baseline_top = 100
baseline_left = 200
baseline_right = baseline_left + 60 * (23-5)

# Data
#stations = [['A', 100], ['B', 200], ['C', 0]]
stations = []
train = []

# Func: station data input
def station_read(stations):
    csvfile = open("station.txt", encoding="utf-8")
    for row in csv.reader(csvfile):
        station = [row[0], int(row[1])]
        stations.append(station)


# Func: train data input
def train_read():
    csvfile = open("train.txt", encoding="utf-8")
    for row in csv.reader(csvfile):
        time = []
        for column in row:
            time.append(int(column))
        train.append(time)

# display core
def disp_stations():
    line = baseline_top
    for hour in range(5, 24):
        canvas.create_text(baseline_left+(hour-5)*60, line-20, text = format(hour, '02'), font=("Helvetica", 18, "bold"))
    for station in stations:
        station_name = station[0]
        line = station[1]
        canvas.create_text(baseline_left-80, line, text = station_name, font=("Helvetica", 18, "bold"))
        canvas.create_line(baseline_left, line, baseline_right, line, width=3.0, fill='black')

def disp_train():
    # draw lines
    flag = 0
    i = 0
    for time in train:
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
    for time in train:
        canvas.create_oval(time[0] - DOT_SIZE/2, stations[i][1] - DOT_SIZE/2, time[0] + DOT_SIZE/2, stations[i][1] + DOT_SIZE/2 , fill='blue')
        i = i + 1

# canvas commands
# create_rectangle(x0, y0, x1, y1, **options)

## main 

root = tkinter.Tk()
root.title(u"dia")
#root.geometry("400x300")
canvas = tkinter.Canvas(root, height=CANVAS_SIZE_HEIGHT, width=CANVAS_SIZE_WIDTH)

station_read(stations)
#print("stations")
#print(stations)

train_read()
#print(train)

disp_stations()

disp_train()

canvas.pack()
root.mainloop()

