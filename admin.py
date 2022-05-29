###--Useful libraries
import string
from time import strftime, time
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk,ImageDraw
from cv2 import BORDER_ISOLATED, resize
from matplotlib.animation import ImageMagickBase
from numpy import std
from sklearn.feature_extraction import img_to_graph
from sklearn.linear_model import Ridge
from sqlalchemy import func, true
from sympy import residue
from database import Student_Management_System
from train_data import Training_system
from face_recognition import Attendance_System
from attendance_db import Attendance_Database_System
from student_window import student
from tkinter import messagebox
from datetime import datetime
from time import strftime
from pytz import timezone
import os
import chatfun
import webbrowser

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.title("Face Recognition Tracking Attendance System")

        #------background image
        bg_img=Image.open(r"image_reource\admin_home.png")
        bg_img=bg_img.resize((1530,790),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(bg_img)
        bg_img_label=Label(self.root,image=self.img2)
        bg_img_label.place(x=0,y=0)
        
        #----------Time bar-----------------
        def current_time():
           now_utc = datetime.now(timezone('UTC'))
           now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
           string=now_asia.strftime('%H:%M:%S %p')
           lbl.config(text=string)
           lbl.after(1000,current_time)

        lbl=Label(bg_img_label,font=(SUNKEN,15,'bold'),fg='black',bg='gray93',border=0,borderwidth=0)
        lbl.place_configure(height=50,width=115)
        current_time()
        
        #------------------------------------------------------------------------
        #==============================header buttons=============================
        # Creating Menubar
        menubar = Menu(self.root)
  
        # Adding File Menu and commands
        file = Menu(menubar, tearoff = 0,bg='white')
        menubar.add_cascade(label='Menu', menu = file,state='active')
        file.add_command(label ='Register', command = self.student_register)
        file.add_separator()
        file.add_command(label ='Photos_Data', command = self.open_img)
        file.add_separator()
        file.add_command(label ='Train_Model', command = self.train_function)
        file.add_separator()
        file.add_command(label ='Mark Attendance', command = self.mark_attendance)
        file.add_separator()
        file.add_command(label ='Attendance Report', command = self.attendance_report)
        file.add_separator()
        file.add_command(label ='Chatbot', command = chatfun.Widget)
        file.add_separator()
        file.add_command(label ='Exit', command = self.root.destroy)
        std = Menu(menubar, tearoff = 0,bg='white')
        menubar.add_cascade(label='Student_Window', menu = std,state='active')
        std.add_command(label ='Open', command =self.std_window )
        std.add_separator()
        std.add_command(label ='Exit', command = self.root.destroy)
        self.root.config(menu = menubar)
        #-------home button-------------
        home_btn=Button(bg_img_label,text='Home',bg='gray93',font=('Arial',13,'bold'),fg='black',activebackground='gray93',activeforeground='white',border=0,borderwidth=0)
        home_btn.place(x=560,y=10,width=100,height=25)

        #--------About button------------
        about_btn=Button(bg_img_label,text='About',bg='gray93',font=('Arial',13,'bold'),fg='black',activebackground='gray93',activeforeground='white',border=0,borderwidth=0,command=self.about_func,cursor='hand2')
        about_btn.place(x=670,y=10,width=100,height=25)

        #--------Developer Button---------------
        dev_btn=Button(bg_img_label,text='Developer',bg='gray93',font=('Arial',13,'bold'),fg='black',activebackground='gray93',activeforeground='white',border=0,borderwidth=0,command=self.developer_func,cursor='hand2')
        dev_btn.place(x=790,y=10,width=100,height=25)
        
        #--------Exit Button---------------
        exit_btn=Button(bg_img_label,text='Exit',bg='red',font=('Arial',13,'bold'),fg='white',activebackground='red',activeforeground='white',border=0,borderwidth=3,command=self.iExit,cursor='hand2',relief=RIDGE)
        exit_btn.place(x=1400,y=10,width=100,height=25)
         
        #--------------------------------------------------------------------------------
        #==============================Middle Frame=====================================
        
        #----Student Register box--------------------------
        img2=Image.open(r"image_reource\bt_1.png")
        img2=img2.resize((250,250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img2)

        b1=Button(bg_img_label,image=self.photoimg,command=self.student_register,cursor="hand2",activeforeground='white',activebackground='grey93',border=0,borderwidth=0,bg='gray93',relief=RIDGE,anchor=N)
        b1.place(x=195,y=150,width=170,height=183,bordermode='inside')

        reg_btn=Button(bg_img_label,text='Register Here',command=self.student_register,cursor="hand2",activeforeground='white',activebackground='grey93',borderwidth=0,bg='gray93',relief=RIDGE,font=(SUNKEN,15,'italic','underline'),fg='black')
        reg_btn.place(x=210,y=130,width=150,height=25,bordermode='outside')

        #-----Train data Box--------------------------------
        img1=Image.open(r"image_reource\bt_2.png")
        img1=img1.resize((250,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img_label,image=self.photoimg1,command=self.train_function,cursor="hand2",activeforeground='white',activebackground='gray93',border=0,borderwidth=0,bg='gray93',relief=RIDGE)
        b1.place(x=655,y=257,width=165,height=165,bordermode='inside')

        reg_btn=Button(bg_img_label,text='Train_Model Here',command=self.train_function,cursor="hand2",activeforeground='white',activebackground='grey93',borderwidth=0,bg='gray93',relief=RIDGE,font=(SUNKEN,15,'italic','underline'),fg='black')
        reg_btn.place(x=670,y=225,width=162,height=25,bordermode='outside')

        #------Attendance box------------
        img3=Image.open(r"image_reource\bt_3.png")
        img3=img3.resize((250,250),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img3)

        b2=Button(bg_img_label,image=self.photoimg_2,command=self.mark_attendance,cursor="hand2",activeforeground='white',activebackground='grey93',border=0,borderwidth=0,bg='gray93',relief=RIDGE)
        b2.place(x=1090,y=172,width=170,height=175,bordermode='inside')

        attend_btn=Button(bg_img_label,text='Mark Attendance',command=self.mark_attendance,cursor="hand2",activeforeground='white',activebackground='grey93',borderwidth=0,bg='gray93',relief=RIDGE,font=(SUNKEN,15,'italic','underline'),fg='black')
        attend_btn.place(x=1121,y=140,width=150,height=25,bordermode='outside')

        #---------Heading Label------------------
        txt=Label(bg_img_label,text='Attendance Tracking',bg='gray93',fg='gray12',font=(SUNKEN,30,'bold','italic'))
        txt.place(x=150,y=550,height=50,width=400)
        txt=Label(bg_img_label,text='Software',bg='gray93',fg='gray12',font=(SUNKEN,30,'bold','italic'))
        txt.place(x=160,y=600,height=50,width=400)



    #----------------------------------------------------------------------
    #============================Functions===============================
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

    #---Back_button-------------
    def back_button(self):
        root.destroy() 
    #------Exit Function-------------
    def iExit(self):
        self.iExit=messagebox.askyesno("Exit","Do you want to exit")
        if self.iExit >0:
            self.root.destroy()
        else:
            return

    #-----Mark Attendance-----------
    def attendance_report(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Database_System(self.new_window)
        print(self.app)
        print(self.new_window)
    
    #----chatbot function---------
    def mark_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_System(self.new_window)
        print(self.app)
        print(self.new_window)
    
    #----Student Register function------------
    def student_register(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Management_System(self.new_window)
        print(self.app)
    
    #------train dataset function-----------
    def train_function(self):
        self.new_window=Toplevel(self.root)
        self.app=Training_system(self.new_window)  

    #-----Student Window-----------
    def std_window(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)    

    #-----photo dataset function---------
    def open_img(self):
        os.startfile("face_data")                     


   




if __name__ == "__main__":
    root=Tk()
    root.minsize(1000,650)
    #root.resizable(True, True)
    #root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0, weight=1)
    obj=Face_recognition_system(root)
    root.mainloop() 