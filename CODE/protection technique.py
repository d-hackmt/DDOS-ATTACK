# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:32:17 2023

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 11:51:56 2023

@author: admin
"""

import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()



#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))






Height = tk.IntVar()
Weight = tk.IntVar()

def main():
    h = Height.get()
    w = Weight.get()
    

image2 = Image.open('IMG.jpg')
image2 = image2.resize((1500, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



lbl = tk.Label(root, text="Protection Techniques of DDOS ATTACK", font=('Lucida Sans Unicode', 40,' bold ',), height=1, width=45,bg="#8B0A50",fg="white")
lbl.place(x=0, y=3)


image2 = Image.open('IMG.jpg')
image2 = image2.resize((90, 60), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=7, y=8)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=450, y=300)


# logolbl=tk.Label(LabelFrame,bd=0).grid(row=0,columnspan=2,pady=20)
        
# lbluser=tk.Label(LabelFrame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
# txtuser=tk.Entry(LabelFrame,bd=5,textvariable=username,font=("",15),bg="white")
# txtuser.grid(row=1,column=1,padx=20)



        
Login_frame=tk.Frame(root)
Login_frame.place(x=180,y=200)
        

        
lbluser=tk.Label(Login_frame,text="Network Security: \n Firewalls: Implement firewalls to filter out malicious traffic and allow only legitimate requests.",compound=LEFT,font=("Times new roman", 20, "bold"),bg="darkseagreen2").grid(row=1,column=0,padx=20,pady=10)


Login_frame=tk.Frame(root)
Login_frame.place(x=180,y=300)
            
lbluser=tk.Label(Login_frame,text="Web Application Firewalls (WAF):\n Deploy a WAF to protect against application-layer DDoS attacks.",compound=LEFT,font=("Times new roman", 20, "bold"),bg="darkseagreen2").grid(row=1,column=0,padx=20,pady=10)


Login_frame=tk.Frame(root)
Login_frame.place(x=180,y=400)
            
lbluser=tk.Label(Login_frame,text="Traffic Monitoring and Analysis:\n Regularly monitor network traffic for unusual patterns.\n  Analyze traffic data to identify potential DDoS attacks early on.",compound=LEFT,font=("Times new roman", 20, "bold"),bg="darkseagreen2").grid(row=1,column=0,padx=20,pady=10)


Login_frame=tk.Frame(root)
Login_frame.place(x=180,y=550)
            
lbluser=tk.Label(Login_frame,text="Rate Limiting and Traffic Shaping:\n Implement rate limiting and traffic shaping to control the amount of incoming traffic. ",compound=LEFT,font=("Times new roman", 20, "bold"),bg="darkseagreen2").grid(row=1,column=0,padx=20,pady=10)




#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image



         


root.mainloop()