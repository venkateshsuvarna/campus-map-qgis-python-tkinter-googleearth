# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:01:16 2018

@author: partF
"""

from Tkinter import *
import sqlite3

conn = sqlite3.connect('M:\\Spring18\\AdvDB\\Project\\2.0\\FullMap.sqlite')
c=conn.cursor()
options=['Source']
categories=['Category']
for row in c.execute("select Name from 'UTA_Full_Map Polygon'"):
    for member in row:
        options.append(member)

for row in c.execute("SELECT DISTINCT(description) FROM 'UTA_Full_Map Polygon'"):
    #print row
    for member in row:
        #print member
        categories.append(member)  
        
#print categories      
c.close()

def calculate():
    building = var.get()
    radius = e.get()
    if radius=='':
        radius='0'
    category = var1.get()
    #print(building+radius)
    file = open('M:\\Spring18\\AdvDB\\Project\\2.0\\input.txt','w')
    
    file.write(building+"\n"+radius+"\n"+category)
    file.close()
    return

def display():
    frame = Frame(window)
    scrollbar = Scrollbar(window, orient=VERTICAL)
    lb = Listbox(window, yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)
    lb.insert(END,"Query Output")
    index=2
    with open("M:\\Spring18\\AdvDB\\Project\\2.0\\output.txt", "r") as output:
        for polygon in output:
            lb.insert(index,polygon)
            index=index+1
    
    scrollbar.pack(side=RIGHT, fill=Y)
    lb.pack(side=LEFT, fill=BOTH, expand=1)      
    return


window=Tk()
window.geometry("400x400")

m=Label(window, text="Find Neighbors")
m.pack()

s=Label(window,text="Source:")
s.pack()

var=StringVar(window)
var.set(options[0])

w=apply(OptionMenu,(window,var)+tuple(options))
w.pack()

d=Label(window,text="Distance (in meters) ")
d.pack()

e = Entry(window)
e.pack()
e.focus_set()

var1=StringVar(window)
var1.set(categories[0])

c=apply(OptionMenu,(window,var1)+tuple(categories))
c.pack()

b = Button(window,text='Process',command=calculate)
b.pack()

dr = Button(window,text='Display Results',command=display)
dr.pack()

window.title("Testing")


window.mainloop()




