###--Useful libraries
from ntpath import join
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk,ImageDraw
from cv2 import BORDER_ISOLATED, resize
from matplotlib.animation import ImageMagickBase
from sklearn.feature_extraction import img_to_graph
from sqlalchemy import true
from sympy import residue
from database import Student_Management_System
import numpy as np
from tkinter import messagebox as msg
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import time

class Attendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+300+100")
        self.root.minsize(700,400)
        self.root.maxsize(1000,600)
        Grid.rowconfigure(self.root, 0,weight=1)
        Grid.columnconfigure(self.root,0,weight=1)
        self.root.title("Face Recognition Tracking Attendance System")
        
        #-------background-------------
        bg_img=Image.open(r"image_reource\attend.png")
        bg_img=bg_img.resize((1000,600),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(bg_img)

        bg_img_label=Label(self.root,image=self.img)
        bg_img_label.pack(side='top',fill='both',expand=True)

        #-----back button-----------------
        back_btn=Button(bg_img_label,text='Back',fg='green',bg='white',font=(SUNKEN,13,'bold'),cursor='hand2',command=self.root.destroy)
        back_btn.pack(side='top',anchor=E)

        #--------------heading-----------------
        btn=Image.open(r"image_reource\train_btn.png")
        btn=btn.resize((100,100),Image.ANTIALIAS)
        self.btn=ImageTk.PhotoImage(btn)
        b=Button(bg_img_label,text='Attendance',bg='green',fg='white',border=1,cursor='hand2',relief=SUNKEN,font=("SUNKEN",20,'bold'),command=self.recognition)
        b.pack(side='bottom',expand=True,padx=100,pady=150,ipadx=30,ipady=5,anchor=SW)

        # progressbar
        self.progress = ttk.Progressbar(bg_img_label, orient = HORIZONTAL,length = 250, mode = 'determinate')
        # place the progressbar
        self.progress.place_configure(x=100,y=455)
        
    
     #----------------Taking Attendance function--------------------   
    def attendance(self,i,r,n,d):
        with open("admin.csv",'r+',newline='\n') as f:
            list=f.readlines()
            name_list=[]
            for line in list:
                d_entry=line.split((","))
                name_list.append(d_entry[0])
            if((i not in name_list) and (n not in name_list) and (d not in name_list) and (r not in name_list)):
                now=datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f'\n{i},{r},{n},{d},{dtString},{d1},PRESENT')


    #----------------------------------------------------------------------------
    #========================recognition function================================
    def recognition(self):
        start = time.time()
        period=23
        def bar():
            import time
            self.progress['value'] = 20
            self.root.update_idletasks()
            time.sleep(1)
    
            self.progress['value'] = 60
            self.root.update_idletasks()
            time.sleep(1)
  
            self.progress['value'] = 80
            self.root.update_idletasks()
            time.sleep(1)
  
            self.progress['value'] = 100
            self.root.update_idletasks()
            time.sleep(1)
  
            self.progress['value'] = 150
            self.root.update_idletasks()
            time.sleep(1)
            self.progress['value'] = 200
        bar()   
        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scalefactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confindence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()

                my_cursor.execute('select Name from student where Student_id='+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute('select Dep from student where Student_id='+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute('select Roll from student where Student_id='+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute('select Student_id from student where Student_id='+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confindence>78:
                    cv2.putText(img,f'ID: {i}',(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Roll: {r}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Name: {n}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f'Department: {d}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unkown Student",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord  
            print(predict)
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('lbph_classifier.xml')

        cam=cv2.VideoCapture(0)
        while True:
            ret,img=cam.read()
            img=recognize(img,clf,faceCascade) 
            cv2.imshow("Welcome to FACE RECOGNITION",img)

            if cv2.waitKey(1)==13:
                break
            if time.time() > start + period:
                break

        cam.release()
        cv2.destroyAllWindows()



        

if __name__ == "__main__":
    root=Tk()
    root.minsize(700,400)
    root.maxsize(1000,600)
    object=Attendance_System(root)
    root.mainloop() 