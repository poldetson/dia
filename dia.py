#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys
import csv
import tkinter
import datetime

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
train = []  # [name, timetable = [[Num, time], [Num, time], .. [Num, time]]

# Func: station data input
def station_read(stations):
    print('station_read')
    csvfile = open("station.txt", encoding="utf-8")
    for row in csv.reader(csvfile):
        station = [row[0], int(row[1])]
        stations.append(station)

# Func: train data input
def train_read(train):
    print('train_read')
    flag = 0
    origin_time_dt = datetime.datetime.strptime('00:00', '%H:%M')
    print('origin_time_dt')
    print(origin_time_dt)
    minute_in_seconds = datetime.timedelta(minutes=1)
    print('minute_in_seconds')
    print(minute_in_seconds)
    csvfile = open("train.txt", encoding="utf-8") 
    for row in csv.reader(csvfile):
        print(row)
        if flag == 0:
            train.append(row)   # as Train name
            flag = 1
        else:
            train_num = int(row[0])
            print('train_num')
            print(train_num)
            time_at_station = datetime.datetime.strptime(row[1], ' %H:%M')
            td = time_at_station - origin_time_dt
            print('td')
            print(td)
            train_time = int(td / minute_in_seconds)
            print('train_time')
            print(train_time)
            train.append([train_num, train_time])

# display core
def disp_stations():
    print('disp_station')
    line = baseline_top
    for hour in range(5, 24):
        canvas.create_text(baseline_left+(hour-5)*60, line-20, text = format(hour, '02'), font=("Helvetica", 18, "bold"))
    for station in stations:
        station_name = station[0]
        line = station[1]
        canvas.create_text(baseline_left-80, line, text = station_name, font=("Helvetica", 18, "bold"))
        canvas.create_line(baseline_left, line, baseline_right, line, width=3.0, fill='black')

def disp_train(train):
    print('disp_train')
    # draw lines
    flag = 0 
    for tmp in train:
        if flag == 0:
            flag = 1
            train_name = tmp
        elif flag == 1:
            flag = 2
            last_station = stations[int(tmp[0])][1]
            last_time = tmp[1]
        else:
            station = stations[int(tmp[0])][1]
            time = tmp[1]
            canvas.create_line(last_time, last_station, time, station, width=3.0, fill='red')
            last_station = station
            last_time = time
    # draw dots
    flag = 0
    for tmp in train:
        if flag == 0:
            flag = 1
        else:
            canvas.create_oval(tmp[1] - DOT_SIZE/2, stations[int(tmp[0])][1] - DOT_SIZE/2, tmp[1] + DOT_SIZE/2, stations[int(tmp[0])][1] + DOT_SIZE/2 , fill='blue')

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

train_read(train)
print(train)

disp_stations()

disp_train(train)

canvas.pack()
root.mainloop()

