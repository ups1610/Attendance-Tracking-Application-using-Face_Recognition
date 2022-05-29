###--Useful libraries
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk,ImageDraw
from click import command
from cv2 import BORDER_ISOLATED, resize
from matplotlib.animation import ImageMagickBase
from sklearn.feature_extraction import img_to_graph
from sqlalchemy import true
from sympy import residue
from database import Student_Management_System
import numpy as np
from tkinter import messagebox as msg
import cv2
import os

class Training_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+400+150")
        self.root.minsize(700,400)
        self.root.maxsize(1000,600)
        Grid.rowconfigure(self.root, 0,weight=1)
        Grid.columnconfigure(self.root,0,weight=1)
        self.root.title("Face Recognition Tracking Attendance System")
        
        #---------------------------------------------------------
        #===================Header==============================
        
        #-------background-------------
        bg_img=Image.open(r"image_reource\train_window.png")
        bg_img=bg_img.resize((1000,600),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(bg_img)

        bg_img_label=Label(self.root,image=self.img)
        bg_img_label.pack(side='top',fill='both',expand=True)

        #---------train button-------------------------------
        b=Button(bg_img_label,text='TRAIN',bg='DarkOrange',fg='white',border=3,cursor='hand2',relief=RIDGE,command=self.train_func,font=(SUNKEN,13,'bold','underline'),width=0,height=0)
        b.pack(side='bottom',expand=True,padx=100,pady=150,ipadx=30,ipady=5,anchor=SW)
        
        # progressbar
        self.progress = ttk.Progressbar(bg_img_label, orient = HORIZONTAL,length = 200, mode = 'determinate')
        # place the progressbar
        self.progress.place_configure(x=70,y=360)
    
        #--------------------------------------------------------
        #================train function=====================    
    def train_func(self):
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
        data_path=("face_data")
        paths=[os.path.join(data_path,file) for file in os.listdir(data_path)]

        faces=[]
        ids=[]
        for path in paths:
            image = Image.open(path).convert('L')#gray code scale
            image_np = np.array(image,'uint8')
            id = int(os.path.split(path)[1].split(".")[1])

            ids.append(id)
            faces.append(image_np)
            cv2.imshow("Training...",image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #----------------train model----------------------
        lbph_classifier = cv2.face.LBPHFaceRecognizer_create()
        lbph_classifier.train(faces,ids)

        #Below line will store the histograms for each one of the iamges
        lbph_classifier.write('lbph_classifier.xml')
        cv2.destroyAllWindows()
        msg.showinfo("Success",'Dataset training completed successfuly',parent=self.root)

    
        

        



        

if __name__ == "__main__":
    root=Tk()
    root.minsize(700,400)
    root.maxsize(1000,600)
    object=Training_system(root)
    root.mainloop() 

