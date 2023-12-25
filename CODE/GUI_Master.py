# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video
#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
# root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("ddos attack")

image2 = Image.open('img1.png')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=70)  # , relwidth=1, relheight=1)


label_l1 = tk.Label(root, text="DDOS Attack",font=("Times New Roman", 25, 'bold'),
                    background="#152238", fg="white", width=70, height=1)
label_l1.place(x=0, y=0)



# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# video_label =tk.Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("videoplayback (2).mp4", video_label,loop = 1, size = (w, h))
# player.play()  # , relwidth=1, relheight=1)
#

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

   
    
def Homepage():
       from subprocess import call
       call(["python","home.py"])
    
def id():
    from subprocess import call
    call(["python","IDS_5.py"])

def id1():
      from subprocess import call
      call(["python","protection technique.py"])  


def window():
  root.destroy()


button1 = tk.Button(root, text="HOME PAGE", command=Homepage, width=25, height=2,font=('times', 15, ' bold '), bg="black", fg="white",bd=4)
button1.place(x=300, y=160)


button2 = tk.Button(root, text="Protection Techniques",command=id1, width=25, height=2,font=('times', 15, ' bold '),bd=4, bg="black", fg="white")
button2.place(x=300, y=260)

button2 = tk.Button(root, text="DDOS ATTACK FILE",command=id,width=25, height=2,font=('times', 15, ' bold '),bd=4, bg="black", fg="white")
button2.place(x=300, y=360)


button3 = tk.Button(root, text="Exit",command=window,width=25, height=2,font=('times', 15, ' bold '),bd=4, bg="black", fg="white")
button3.place(x=300, y=460)

root.mainloop()