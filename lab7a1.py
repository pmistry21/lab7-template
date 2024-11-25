#!/usr/bin/env python3

# Name: Prasad Mistry
# Student Number: 111964193
# Student Email: pmistry21@myseneca.ca
# Course: OPS445
# Section: ZAA
# Semester: Fall 2024

from lab7a import *
t1 = Time(8,0,0)
t2 = Time(8,55,0)
t3 = Time(9,50,0)

td = Time(0,50,0)

tsum1 = sum_times(t1,td)
tsum2 = sum_times(t2,td)
tsum3 = sum_times(t3,td)   

ft = format_time
print(ft(t1),'+',ft(td),'-->',ft(tsum1))
print(ft(t2),'+',ft(td),'-->',ft(tsum2))
print(ft(t3),'+',ft(td),'-->',ft(tsum3))
