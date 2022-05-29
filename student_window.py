###--Useful libraries
import string
from time import strftime, time
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk,ImageDraw
from cv2 import BORDER_ISOLATED, resize
from matplotlib.animation import ImageMagickBase
from sklearn.feature_extraction import img_to_graph
from sqlalchemy import true
from sympy import residue
from face_recognition import Attendance_System
from exp import Attendance_Database
from tkinter import messagebox
from datetime import datetime
from time import strftime
from pytz import timezone
import os
import chatfun
import webbrowser

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition Tracking Attendance System")

        #=======================background===========================
        bg_img=Image.open(r"image_reource\std_screen.png")
        bg_img=bg_img.resize((1550,800),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(bg_img)

        bg_img_label=Label(self.root,image=self.img2)
        bg_img_label.pack()
        
        #==================header===================================
        #-------home button-------------
        home_btn=Button(bg_img_label,text='Home',bg='black',font=('Arial',13,'bold'),fg='white',activebackground='black',activeforeground='white',border=0,borderwidth=0)
        home_btn.place(x=560,y=10,width=100,height=25)

        #--------About button------------
        about_btn=Button(bg_img_label,text='About',bg='black',font=('Arial',13,'bold'),fg='white',activebackground='black',activeforeground='white',border=0,borderwidth=0,command=self.about_func,cursor='hand2')
        about_btn.place(x=670,y=10,width=100,height=25)

        #--------Developer Button---------------
        dev_btn=Button(bg_img_label,text='Developer',bg='black',font=('Arial',13,'bold'),fg='white',activebackground='black',activeforeground='white',border=0,borderwidth=0,command=self.developer_func,cursor='hand2')
        dev_btn.place(x=790,y=10,width=100,height=25)

        #--------Exit Button---------------
        exit_btn=Button(bg_img_label,text='Exit',bg='red',font=('Arial',13,'bold'),fg='white',activebackground='red',activeforeground='white',border=0,borderwidth=2,command=self.iExit,cursor='hand2',relief=RIDGE)
        exit_btn.place(x=1400,y=10,width=100,height=25)

        #========================Middle===============================

        #---------mark_attendance button-------------
        img=Image.open(r"image_reource\std_img1.png")
        img=img.resize((460,430),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(img)
        
        img_btn=Button(bg_img_label,image=self.img,bg='black',border=0,borderwidth=0,activebackground='black',activeforeground='blue',cursor='hand2',command=self.mark_attendance)
        img_btn.place(x=180,y=330,width=270,height=390)
        
        topic_label=Button(bg_img_label,text='Mark Attendance',bg='white',border=0,borderwidth=0,fg='black',font=(SUNKEN,15,'underline'),activebackground='white',activeforeground='black',cursor='hand2',command=self.mark_attendance)
        topic_label.place(x=247,y=555,width=150,height=25)
        topic=Label(bg_img_label,text='Practice Presence\nembrance the place\nwhere life happen.',bg='white',fg='black',border=0,borderwidth=0,font=(SUNKEN,13,'italic'))
        topic.place(x=240,y=580,width=160,height=90)
        start=Button(bg_img_label,text='Start Here',bg='white',fg='black',border=0,borderwidth=0,font=(SUNKEN,13,'underline'),cursor='hand2',command=self.mark_attendance)
        start.place(x=275,y=670,width=90,height=20)
        
        #------------Attendance Report button------------------
        img1=Image.open(r"image_reource\std_img2.png")
        img1=img1.resize((460,430),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)

        img1_btn=Button(bg_img_label,image=self.img1,bg='black',border=0,borderwidth=0,activebackground='black',activeforeground='blue',cursor='hand2',anchor=S,command=self.attendance_rep)
        img1_btn.place(x=520,y=282,width=320,height=440)

        topic_2_label=Button(bg_img_label,text='Attendance Report',bg='white',border=0,borderwidth=0,fg='black',font=(SUNKEN,15,'underline'),activebackground='white',activeforeground='black',command=self.attendance_rep)
        topic_2_label.place(x=600,y=467,width=180,height=25)
        topic_2=Label(bg_img_label,text='When students improve\ntheir attendance rates,\nthey improve their\nacademic prospects and\nchances for graduating.',bg='white',fg='black',border=0,borderwidth=0,font=(SUNKEN,13,'italic'))
        topic_2.place(x=605,y=490,width=190,height=180)
        start_2=Button(bg_img_label,text='Start Here',bg='white',fg='black',border=0,borderwidth=0,font=(SUNKEN,13,'underline'),cursor='hand2',command=self.attendance_rep)
        start_2.place(x=655,y=650,width=90,height=20)

        
        #----------Chatbot button----------------------------
        frame=Button(bg_img_label,bg='white',border=0,borderwidth=0,activebackground='white',activeforeground='white',cursor='hand2',command=chatfun.Widget)
        frame.place(x=953,y=530,height=190,width=300)

        frame2=Button(bg_img_label,bg='white',border=0,borderwidth=0,activebackground='white',activeforeground='white',cursor='hand2',command=chatfun.Widget)
        frame2.place(x=953,y=452,height=80,width=80)

        frame3=Button(bg_img_label,bg='white',border=0,borderwidth=0,activebackground='white',activeforeground='white',cursor='hand2',command=chatfun.Widget)
        frame3.place(x=1153,y=457,height=80,width=88)

        topic_3_label=Button(bg_img_label,text='Chat With Me',bg='white',border=0,borderwidth=0,fg='black',font=(SUNKEN,15,'underline'),activebackground='white',activeforeground='black',cursor='hand2',command=chatfun.Widget)
        topic_3_label.place(x=1015,y=537,width=180,height=25)
        topic_3=Label(bg_img_label,text='Any sufficiently advanced\n technology is \n indistingishable \nacademic prospects and\n from magic.',bg='white',fg='black',border=0,borderwidth=0,font=(SUNKEN,13,'italic'))
        topic_3.place(x=1010,y=565,width=200,height=100)
        start_3=Button(bg_img_label,text='Start Here',bg='white',fg='black',border=0,borderwidth=0,font=(SUNKEN,13,'underline'),cursor='hand2',command=chatfun.Widget)
        start_3.place(x=1065,y=675,width=90,height=20)

        #=====================Footer=============================

        #--------footer image---------------------------
        img4=Image.open(r"image_reource\std_img4.png")
        img4=img4.resize((350,300),Image.ANTIALIAS)
        self.img4=ImageTk.PhotoImage(img4)

        img4_btn=Button(bg_img_label,image=self.img4,bg='black',border=0,borderwidth=0,activebackground='black',activeforeground='blue',cursor='hand2',command=self.about_func)
        img4_btn.place(x=1400,y=650,width=140,height=150)

    #=========================Functions=========================================
    #---Mark Attendance----------
    def attendance_rep(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Database(self.new_window)
    
    #----chatbot function--------
    def mark_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_System(self.new_window)

    #-----About function---------
    def about_func(self):
        self.new_root=Toplevel(bg='black')
        self.new_root.title('About')    
        self.new_root.geometry('1000x250+250+320')
        self.new_root.maxsize(1000,250)
        self.new_root.minsize(1000,250)

        #------Frame-------------
        f=Frame(self.new_root,bg='gray85',border=2,borderwidth=2,highlightcolor='black',highlightthickness='2',relief=RIDGE,)
        f.place(x=10,y=6,width=980,height=235)

        #------Exit button-------
        close_btn=Button(f,text='Close',bg='green',fg='white',activebackground='gray85',activeforeground='green',font=(SUNKEN,13,'bold'),command=self.close_func)
        close_btn.place(x=870,y=200,width=100,height=25)

        #-----------About Content-----------------------------
        img5=Image.open(r"image_reource\text_img.png")
        img5=img5.resize((850,230),Image.ANTIALIAS)
        self.img5=ImageTk.PhotoImage(img5)
        content=Label(f,image=self.img5,fg='black',bg='gray85',border=0,borderwidth=0)
        content.place(x=0,y=1,width=850,height=235)

    #-----developer function---------
    def developer_func(self):
        self.new_root_2=Toplevel(bg='black')
        self.new_root_2.title('About')    
        self.new_root_2.geometry('1000x250+250+320')
        self.new_root_2.maxsize(1000,250)
        self.new_root_2.minsize(1000,250)

        #------Frame-------------
        f=Frame(self.new_root_2,bg='gray85',border=2,borderwidth=2,highlightcolor='black',highlightthickness='2',relief=RIDGE,)
        f.place(x=10,y=6,width=980,height=235)

        img5=Image.open(r"image_reource\my_text.png")
        img5=img5.resize((600,70),Image.ANTIALIAS)
        self.img5=ImageTk.PhotoImage(img5)
        content=Label(f,image=self.img5,fg='black',bg='gray85',border=0,borderwidth=0)
        content.place(x=200,y=10,width=600,height=70)
        
        #Define a callback function
        def callback(url):
            webbrowser.open_new_tab(url)

        #Create a Label to display the link
        link = Label(f, text="LinkedIn",font=('Helveticabold', 15,'underline'), fg="blue", cursor="hand2",bg='gray85')
        link.place(x=350,y=100,width=250,height=25)
        link.bind("<Button-1>", lambda e:
        callback("https://www.linkedin.com/in/upendrapratapsingh-1610/"))

        def call(url):
            webbrowser.open_new_tab(url)

        #Create a Label to display the link
        link = Label(f, text="Microsoft.com",font=('Helveticabold', 15,'underline'), fg="black", cursor="hand2",bg='gray85')
        link.place(x=350,y=200,width=250,height=25)
        link.bind("<Button-1>", lambda e:
        call("https://www.microsoft.com/en-in"))

        #------Exit button-------
        close_btn=Button(f,text='Close',bg='green',fg='white',activebackground='gray85',activeforeground='green',font=(SUNKEN,13,'bold'),command=self.close_root2_func)
        close_btn.place(x=870,y=200,width=100,height=25)      
    
    #--About closing function 
    def close_func(self):
        self.new_root.destroy()
    def close_root2_func(self):
        self.new_root_2.destroy()                          

    #---Back_function-------------
    def back_button(self):
        root.destroy()
    #---Exit function----------     
    def iExit(self):
        self.iExit=messagebox.askyesno("Exit","Do you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return     
           
   
        

        


if __name__=='__main__':
    root=Tk()
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    obj=student(root)
    root.mainloop()        