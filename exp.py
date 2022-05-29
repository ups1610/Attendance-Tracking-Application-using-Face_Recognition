###--Useful libraries
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import window_height
from typing import ValuesView
from PIL import Image,ImageTk,ImageDraw,ImageFont
from cv2 import BORDER_ISOLATED, BORDER_REFLECT, resize
from matplotlib.animation import ImageMagickBase
from pyrsistent import v
from soupsieve import select
from sympy import residue
from tkinter import messagebox as msg
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance_Database:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x600+250+0")
        self.root.minsize(700,400)
        self.root.maxsize(1000,600)
        self.root.title("Face Recognition Tracking Attendance System")
        
        self.var_attendance_id=StringVar()
        self.var_attendance_name=StringVar()
        self.var_attendance_roll=StringVar()
        self.var_attendance_dep=StringVar()
        self.var_attendance_date=StringVar()
        self.var_attendance_time=StringVar()
        self.var_attendance_status=StringVar()


        #---banner
        frame = Frame(self.root,bd=2,relief=RIDGE,bg='black',width=1000,height=200)
        frame.pack()
    

        bg_img=Image.open(r"E:\python\MS_project\Face_Recognition_System\image_reource\att_db.png")
        bg_img=bg_img.resize((1000,225),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(bg_img)

        bg_img_label=Label(frame,image=self.img2)
        bg_img_label.pack(side='left',expand=True,fill=X)

        #-------------------------Topic-------------------------
        img=Image.open(r"E:\python\MS_project\Face_Recognition_System\image_reource\txt.png")
        img=img.resize((250,100),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(img)

        label=Label(bg_img_label,image=self.img,border=0,bitmap='error')
        label.place(x=5,y=127,width=245,height=90)

        #--------------Main frame---------------------------------
        main_frame=Frame(self.root,bd=2,bg='black',border=0,width=1000,height=540)
        main_frame.pack(pady=10,expand=True)

        #--------------------------------------left frame-----------------------------------
        head_txt=Label(main_frame,text="Attendance Information",font=(SUNKEN,'15','bold'),bg='black',fg='white')
        head_txt.place(x=200,y=5)

        inner_left_frame=Frame(main_frame,bd=2,bg='lavender',relief=RIDGE)
        inner_left_frame.place(x=16,y=10,width=500,height=325)

        #------------left Label Entry------------
        #--Attendance Id:
        atd_label=Label(inner_left_frame,text='Attendance ID:',font=(SUNKEN,11,'bold'),bg='lavender') 
        atd_label.grid(row=0,column=0,padx=10,sticky=W)

        atd_entry=ttk.Entry(inner_left_frame,width=12,font=('SUNKEN',11,'normal'),background='black',textvariable=self.var_attendance_id)
        atd_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #--Name:
        name_label=Label(inner_left_frame,text='Name:',font=(SUNKEN,11,'bold'),bg='lavender') 
        name_label.grid(row=0,column=2,padx=10,sticky=W)

        name_entry=ttk.Entry(inner_left_frame,width=12,font=('SUNKEN',11,'normal'),background='black',textvariable=self.var_attendance_name)
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #--Roll:
        roll_label=Label(inner_left_frame,text='Roll No:',font=(SUNKEN,11,'bold'),bg='lavender') 
        roll_label.grid(row=1,column=0,padx=10,sticky=W)

        roll_entry=ttk.Entry(inner_left_frame,width=12,font=('SUNKEN',11,'normal'),background='black',textvariable=self.var_attendance_roll)
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #--department:
        dep_label=Label(inner_left_frame,text='Department:',font=(SUNKEN,11,'bold'),bg='lavender') 
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_entry=ttk.Entry(inner_left_frame,width=12,font=('SUNKEN',11,'normal'),background='black',textvariable=self.var_attendance_dep)
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #--Date:
        date_label=Label(inner_left_frame,text='Time:',font=(SUNKEN,11,'bold'),bg='lavender') 
        date_label.grid(row=2,column=0,padx=10,sticky=W)

        date_entry=ttk.Entry(inner_left_frame,width=12,font=('SUNKEN',11,'normal'),background='black',textvariable=self.var_attendance_date)
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
 

        #--Time:
        time_label=Label(inner_left_frame,text='Time:',font=(SUNKEN,11,'bold'),bg='lavender') 
        time_label.grid(row=2,column=2,padx=10,sticky=W)

        time_entry=ttk.Entry(inner_left_frame,width=12,font=('SUNKEN',11,'normal'),background='black',textvariable=self.var_attendance_time)
        time_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #----Attendance status
        status_label=Label(inner_left_frame,text='Status:',font=(SUNKEN,11,'bold'),bg='lavender') 
        status_label.grid(row=3,column=0,padx=10,sticky=W)

        status_combo=ttk.Combobox(inner_left_frame,font=("SUNKEN",11,'normal'),width=12,state='readonly',textvariable=self.var_attendance_status)
        status_combo['values']=('Status','Present','Absent')
        status_combo.current(0)
        status_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #---butoon frame---
        btn_frame=Frame(inner_left_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=50,y=200,width=380,height=30)
        
        save_btn=Button(btn_frame,text='CSVin',width=18,font=(SUNKEN,13,'bold'),bg='green',fg='white',command=self.import_csv)
        save_btn.grid(row=0,column=0)

        del_btn=Button(btn_frame,text='CSVout',width=18,font=(SUNKEN,13,'bold'),bg='green',fg='white',command=self.export_csv)
        del_btn.grid(row=0,column=1)
		

        #---------right-frame------------------
        r_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font='SUNKEN',fg='dark red')
        r_frame.place(x=525,y=10,width=460,height=325)

        #------table frame-----------------
        data_frame=Frame(r_frame,bd=2,bg='white',relief=RIDGE)
        data_frame.place(x=8,y=10,width=440,height=280)

        scroll_x=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(data_frame,column=('id','name','roll','dep','date','time','status'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading('id',text='Attendance ID')
        self.attendance_table.heading('name',text='Name')
        self.attendance_table.heading('roll',text='Roll No')
        self.attendance_table.heading('dep',text='Department')
        self.attendance_table.heading('date',text='Date')
        self.attendance_table.heading('time',text='Time')
        self.attendance_table.heading('status',text='Status')
        self.attendance_table['show']='headings'

        self.attendance_table.column('id',width=105)
        self.attendance_table.column('name',width=105)
        self.attendance_table.column('roll',width=105)
        self.attendance_table.column('dep',width=105)
        self.attendance_table.column('date',width=105)
        self.attendance_table.column('time',width=105)
        self.attendance_table.column('status',width=105)

        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.cursor_get)

    #=======================data fetch function========================
    def data_fetch(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert('',END,values=i)

    def import_csv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.CSV'),('All File','*.*')),parent=self.root)
        with open(fin) as file:
            csv_read=csv.reader(file,delimiter=',')
            for i in csv_read:
                mydata.append(i)
            self.data_fetch(mydata)    


    #----------Export CSV function-------------------
    def export_csv(self):
        try:
            if len(mydata)<1:
                msg.showerror("Error",'No Data Found',parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='Open CSV',filetypes=(('CSV File','*.CSV'),('All File','*.*')),parent=self.root) 
            with open(fln,mode='w',newline="") as file:
                csv_write=csv.writer(file,delimiter=',')
                for i in mydata:
                    csv_write.writerow(i)
                msg.showinfo("Success",'Data exported '+os.path.basename(fln)+" successfully")
        except Exception as es:
            msg.showerror("Error",f'due to :{str(es)}',parent=self.root)                  

    #-----------reset function--------------
    def cursor_get(self,event=""):
        row=self.attendance_table.focus()
        val=self.attendance_table.item(row)
        rows=val['values']
        self.var_attendance_id.set(rows[0])
        self.var_attendance_name.set(rows[1])
        self.var_attendance_roll.set(rows[2])
        self.var_attendance_dep.set(rows[3])
        self.var_attendance_date.set(rows[4])
        self.var_attendance_time.set(rows[5])
        self.var_attendance_status.set(rows[6])

    #----------reset function-----------------
    def reset(self):
        self.var_attendance_id.set("")
        self.var_attendance_name.set("")
        self.var_attendance_roll.set("")
        self.var_attendance_dep.set("")
        self.var_attendance_date.set("")
        self.var_attendance_time.set("")
        self.var_attendance_status.set("")






        
        
        
        

if __name__ == "__main__":
    root=Tk()
    root.minsize(700,400)
    root.maxsize(1000,600)
    object=Attendance_Database(root)
    root.mainloop()           