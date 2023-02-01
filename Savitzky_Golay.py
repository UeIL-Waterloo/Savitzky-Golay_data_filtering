#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:58:03 2022

@author: tyler

A short script for Savitzky-Golay filtering 

"""
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np 
from scipy.signal import savgol_filter

root = tk.Tk()
root.withdraw()

print("Please select the data with which to perform the Savitzky-Golay filtering method.")

file_path = filedialog.askopenfilename()
file_path = open(os.path.expanduser(file_path))
thickness_array = []
for i in file_path:
    thickness_array.append(i)

thickness_array_stripped = []
data = []
### Cleaning up the text files
for i in thickness_array:
    i_stripped = i.strip('\n')
    thickness_array_stripped.append(i_stripped)

for i in thickness_array_stripped:
    i_stripped2 = float(i.strip("'"))
    data.append(i_stripped2)
x = np.linspace(0,len(data)-1,num=len(data))
w = savgol_filter(data, 101, 2)
plt.plot(x, w, 'b')
plt.plot(x,data,linestyle="-", c="r")
