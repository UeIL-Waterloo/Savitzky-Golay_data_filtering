"""
Created on Sun Oct  9 16:58:03 2022

@author: tyler

A short script for Savitzky-Golay filtering 

MIT License

Copyright (c) 2023 Tyler Lott

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
