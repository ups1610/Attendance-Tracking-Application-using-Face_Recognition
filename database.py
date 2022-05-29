###--Useful libraries
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import window_height
from typing import ValuesView
from PIL import Image,ImageTk,ImageDraw
from click import command
from cv2 import BORDER_ISOLATED, BORDER_REFLECT, resize
from matplotlib.animation import ImageMagickBase
from pyrsistent import v
from soupsieve import select
from sympy import residue
from tkinter import messagebox as msg
import mysql.connector
from tkinter import filedialog
import os
import cv2

class Student_Management_System:
    def __init__(self,root):
        self.root=root
        self.root.minsize(700,400)
        
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Tracking Attendance System")

        #----------Defining Function variables for data entry such as department, name, etc.----------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_mentor=StringVar()

        #---------------------------------------------------------
        #=================Header==================================

        #------------------Upper Image---------------------
        f=Frame(self.root,bg='green',width=1530,height=790)
        f.pack()
        bg_img=Image.open(r"E:\python\MS_project\Face_Recognition_System\image_reource\database.png")
        bg_img=bg_img.resize((1470,220),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(bg_img)

        bg_img_label=Label(f,image=self.img2)
        bg_img_label.place(x=30,y=6,width=1470,height=220)
        
        #-------heading------
        btn=Label(bg_img_label,text='DATABASE',border=0,borderwidth=0,bg='white',activebackground='white',font=(SUNKEN,20,'italic','underline'),fg='purple')
        btn.place(x=0,y=5,width=210,height=50)

        #------Back Button--------------------
        back_btn=Button(bg_img_label,text='Back',fg='green',bg='white',font=(SUNKEN,13,'bold'),border=0,command=self.root.destroy)
        back_btn.place(x=1350,y=3,height=25,width=90)

        #*******************Frame conataing Student detais and database********************
        main_frame=Frame(self.root,bd=2,bg='black',border=1)
        main_frame.place(x=20,y=230,width=1485,height=560)

        #--------------------left-frame-------------------
        l_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Details",font='SUNKIN')
        l_frame.place(x=10,y=5,width=720,height=540)

        img_lft=Image.open(r"E:\python\MS_project\Face_Recognition_System\image_reource\Untitled design (2).png")
        img_lft=img_lft.resize((450,115),Image.ADAPTIVE)
        self.img_lft=ImageTk.PhotoImage(img_lft)

        self.img_lft_label=Button(l_frame,image=self.img_lft,activebackground='white',activeforeground='white',background='white',command=self.change_img,border=0,borderwidth=0)
        self.img_lft_label.place(x=150,y=0,width=450,height=105)

        #---------current course information frame-----------
        course_frame=LabelFrame(l_frame,bd=2,bg='white',relief=RIDGE,text="Current course",font='SUNKIN',fg='brown')
        course_frame.place(x=4,y=105,width=710,height=110)
        
        #-Department
        dep_label=Label(course_frame,text='Department',font=(SUNKEN,13,'bold'),bg='white') 
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("SUNKEN",13,'normal'),width=20,state='readonly')
        dep_combo['values']=('Choose','Computer','Information Technology','Electronics','Mechanical','Chemical','Civil')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #-Course
        c_label=Label(course_frame,text='Course',font=(SUNKEN,13,'bold'),bg='white') 
        c_label.grid(row=0,column=2,padx=10,sticky=W)

        c_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("SUNKEN",13,'normal'),width=20,state='readonly')
        c_combo['values']=('Choose','B.Tech','M.Tech','BSC','BA','MA')
        c_combo.current(0)
        c_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #-Graduation Year
        y_label=Label(course_frame,text='Graduation Year',font=(SUNKEN,13,'bold'),bg='white') 
        y_label.grid(row=1,column=0,padx=10,sticky=W)

        y_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("SUNKEN",12,'normal'),width=20,state='readonly')
        y_combo['values']=('Choose','2022','2023','2024','2025')
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #-Semester
        sem_label=Label(course_frame,text='Semester',font=(SUNKEN,12,'bold'),bg='white') 
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("SUNKEN",12,'normal'),width=20,state='readonly')
        sem_combo['values']=('Choose','I','II','III','IV','V','VI','VII','VIII')
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #-Student  information
        st_frame=LabelFrame(l_frame,bd=2,bg='white',relief=RIDGE,text="Student Information",font='SUNKIN',fg='brown')
        st_frame.place(x=4,y=220,width=710,height=288)
        
        #-Student ID
        std_id_label=Label(st_frame,text='StudentID:',font=(SUNKEN,13,'bold'),bg='white') 
        std_id_label.grid(row=0,column=0,padx=10,sticky=W)

        std_id_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_id,font=('SUNKEN',13,'normal'))
        std_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #-Student Name
        std_name_label=Label(st_frame,text='Name:',font=(SUNKEN,13,'bold'),bg='white') 
        std_name_label.grid(row=0,column=2,padx=10,sticky=W)

        std_name_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_name,font=('SUNKEN',13,'normal'))
        std_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #S-ection
        std_sec_label=Label(st_frame,text='Section:',font=(SUNKEN,13,'bold'),bg='white') 
        std_sec_label.grid(row=1,column=0,padx=10,sticky=W)

        sec_combo=ttk.Combobox(st_frame,textvariable=self.var_sec,font=("SUNKEN",12,'normal'),width=18,state='readonly')
        sec_combo['values']=('select','A','B','C','D','E','F','G','H','I','J')
        sec_combo.current(0)
        sec_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #--Roll No
        stdid_label=Label(st_frame,text='RollNo:',font=(SUNKEN,13,'bold'),bg='white') 
        stdid_label.grid(row=1,column=2,padx=10,sticky=W)

        stdid_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_roll,font=('SUNKEN',13,'normal'))
        stdid_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #-Gender
        stdid_label=Label(st_frame,text='Gender:',font=(SUNKEN,13,'bold'),bg='white') 
        stdid_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_combo=ttk.Combobox(st_frame,textvariable=self.var_gender,font=("SUNKEN",12,'normal'),width=18,state='readonly')
        gender_combo['values']=('select','Male','Female','Others')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)  

        #-Date of Birth
        stdid_label=Label(st_frame,text='DOB:',font=(SUNKEN,13,'bold'),bg='white') 
        stdid_label.grid(row=2,column=2,padx=10,sticky=W)

        stdid_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_dob,font=('SUNKEN',13,'normal'))
        stdid_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #-Email
        std_mail_label=Label(st_frame,text='Email ID:',font=(SUNKEN,13,'bold'),bg='white') 
        std_mail_label.grid(row=3,column=0,padx=10,sticky=W)

        std_mail_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_email,font=('SUNKEN',13,'normal'),validate='focus')
        std_mail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number
        std_phone_label=Label(st_frame,text='Phone No:',font=(SUNKEN,13,'bold'),bg='white') 
        std_phone_label.grid(row=3,column=2,padx=10,sticky=W)
        
        std_phone_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_phone,font=('SUNKEN',13,'normal'))
        std_phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        std_add_label=Label(st_frame,text='Address:',font=(SUNKEN,13,'bold'),bg='white') 
        std_add_label.grid(row=4,column=0,padx=10,sticky=W)

        std_add_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_address,font=('SUNKEN',13,'normal'))
        std_add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Mentor Name
        std_add_label=Label(st_frame,text='Mentor Name:',font=(SUNKEN,13,'bold'),bg='white') 
        std_add_label.grid(row=4,column=2,padx=10,sticky=W)

        std_mname_entry=ttk.Entry(st_frame,width=20,textvariable=self.var_mentor,font=('SUNKEN',13,'normal'))
        std_mname_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #-----Radio button for making yes or know for photos--------
        self.var_radio1=StringVar()
        radio_button_1=ttk.Radiobutton(st_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes",cursor='hand2')
        radio_button_1.grid(row=6,column=0,sticky=W,padx=10)
        
        radio_button_2=ttk.Radiobutton(st_frame,variable=self.var_radio1,text="No Photo Sample",value="No",cursor='hand2')
        radio_button_2.grid(row=6,column=2,sticky=W,padx=10) 

        #--------------buttons frame with buttons----------------
        btn_frame=Frame(st_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=3,y=220,width=700,height=37)
        
        save_btn=Button(btn_frame,text='SAVE',command=self.add_data,width=14,font=(SUNKEN,11,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        del_btn=Button(btn_frame,text='DELETE',command=self.del_data,width=14,font=(SUNKEN,11,'bold'),bg='blue',fg='white')
        del_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text='UPDATE',command=self.update_data,width=14,font=(SUNKEN,11,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text='RESET',command=self.reset_data,width=14,font=(SUNKEN,11,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(btn_frame,text='TAKE PHOTO',command=self.photos_dataset,width=16,font=(SUNKEN,11,'bold'),bg='blue',fg='white')
        take_photo_btn.grid(row=0,column=4)



        #-----------------------right-frame---------------------------------
        r_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font='SUNKEN')
        r_frame.place(x=740,y=5,width=730,height=540)

        img_rht=Image.open(r"E:\python\MS_project\Face_Recognition_System\image_reource\data.png")
        img_rht=img_rht.resize((650,130),Image.ADAPTIVE)
        self.img_rht=ImageTk.PhotoImage(img_rht)

        self.img_rht_label=Button(r_frame,image=self.img_rht,activebackground='white',activeforeground='white',background='white',command=self.change_img_2,border=0,borderwidth=0)
        self.img_rht_label.place(x=60,y=0,width=650,height=125)

        #-----------search system bar---------------------------------
        srch_frame=LabelFrame(r_frame,bd=2,bg='white',relief=RIDGE,text='Search Bar',font='SUNKEN',fg='brown')
        srch_frame.place(x=5,y=107,width=710,height=70)
        
        srch_label=Label(srch_frame,text='Search By:',font=(SUNKEN,13,'bold'),bg='red',fg='white',border=2)
        srch_label.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        self.var_search=StringVar()
        srch_combo=ttk.Combobox(srch_frame,font=("SUNKEN",12,'normal'),textvariable=self.var_search,width=15,state='readonly',background='black')
        srch_combo['values']=('Select','Student_id','Roll','Phone')
        srch_combo.current(0)
        srch_combo.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        self.var_search_all=StringVar()
        srch_entry=ttk.Entry(srch_frame,font=(SUNKEN,13,"normal"),textvariable=self.var_search_all)
        srch_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        srch_btn=Button(srch_frame,text="Search",width=14,font=("SUNKEN",9,"bold"),bg='blue',fg='white',command=self.search)
        srch_btn.grid(row=0,column=4)

        showall_btn=Button(srch_frame,text="Show All",width=14,font=("SUNKEN",9,"bold"),bg='blue',fg='white',command=self.fetch_data)
        showall_btn.grid(row=0,column=5,padx=5)

        #=========database frame================
        data_frame=Frame(r_frame,bd=2,bg='white',relief=RIDGE)
        data_frame.place(x=5,y=190,width=710,height=320)
        
        #-------Adding Scroll Bar--------------------------
        scroll_x=ttk.Scrollbar(data_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(data_frame,orient=VERTICAL)

        self.std_data_table=ttk.Treeview(data_frame,column=('dep','course','year','sem','id','name','sec','roll','gender','dob','email','phone','address','teacher','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set,)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.std_data_table.xview)
        scroll_y.config(command=self.std_data_table.yview)

        #--------Adding Scroll bar column headings------------------
        self.std_data_table.heading('dep',text='Department')
        self.std_data_table.heading('course',text='Course')
        self.std_data_table.heading('year',text='Graduation Year')
        self.std_data_table.heading('sem',text='Semester')
        self.std_data_table.heading('id',text='StudentID')
        self.std_data_table.heading('name',text='Name')
        self.std_data_table.heading('sec',text='Section')
        self.std_data_table.heading('roll',text='Roll No')
        self.std_data_table.heading('gender',text='Gender')
        self.std_data_table.heading('dob',text='DOB')
        self.std_data_table.heading('email',text='Email ID')
        self.std_data_table.heading('phone',text='Phone No')
        self.std_data_table.heading('address',text='Address')
        self.std_data_table.heading('teacher',text='Mentor Name')
        self.std_data_table.heading('photo',text='Take Photo Sample')
        self.std_data_table['show']='headings'

        self.std_data_table.column('dep',width=100)
        self.std_data_table.column('course',width=100)
        self.std_data_table.column('year',width=100)
        self.std_data_table.column('sem',width=100)
        self.std_data_table.column('id',width=100)
        self.std_data_table.column('name',width=100)
        self.std_data_table.column('sec',width=100)
        self.std_data_table.column('roll',width=100)
        self.std_data_table.column('gender',width=100)
        self.std_data_table.column('dob',width=100)
        self.std_data_table.column('email',width=100)
        self.std_data_table.column('phone',width=100)
        self.std_data_table.column('address',width=100)
        self.std_data_table.column('teacher',width=100)
        self.std_data_table.column('photo',width=110)

        self.std_data_table.pack(fill=BOTH,expand=1)
        self.std_data_table.bind("<ButtonRelease>",self.cursor_get)
        self.fetch_data()
     
    #------------------------------------------------------------------------- 
    #==========================Functions====================================

    #---------------------------Save function-------------------------------
    def add_data(self):
        if self.var_dep.get()=="Choose" or self.var_name.get()=="" or self.var_id.get()=="":
            msg.showerror('error','Required all fields',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_sem.get(),
                                                                                                               self.var_id.get(),
                                                                                                               self.var_name.get(),
                                                                                                               self.var_sec.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_mentor.get(),
                                                                                                               self.var_radio1.get()

                                                                                                          ))   
                conn.commit()
                self.fetch_data()
                conn.close()
                msg.showinfo('Success','Details added successfully',parent=self.root)
            except Exception as es:
                msg.showerror('error',f'due to :{str(es)}',parent=self.root)   
       
    #---------------Data Fetch------------------------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from student')
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.std_data_table.delete(*self.std_data_table.get_children())
            for i in data:
                self.std_data_table.insert('',END,values=i)
            conn.commit()
        conn.close()  

    #--------------------get cursor-----------------------------          
    def cursor_get(self,event=""):
        cursor_focus=self.std_data_table.focus()
        content=self.std_data_table.item(cursor_focus)
        val=content['values']

        self.var_dep.set(val[0]),
        self.var_course.set(val[1]),
        self.var_year.set(val[2]),
        self.var_sem.set(val[3]),
        self.var_id.set(val[4]),
        self.var_name.set(val[5]),
        self.var_sec.set(val[6]),
        self.var_roll.set(val[7]),
        self.var_gender.set(val[8]),
        self.var_dob.set(val[9]),
        self.var_email.set(val[10]),
        self.var_phone.set(val[11]),
        self.var_address.set(val[12]), 
        self.var_mentor.set(val[13]), 
        self.var_radio1.set(val[14]) 

        #------------------Upade function ------------------------
    def update_data(self):
        if self.var_dep.get()=="Choose" or self.var_name.get()=="" or self.var_id.get()=="":
            msg.showerror('error','Required all fields',parent=self.root)
        else:
            try:
                update_val=msg.askyesno("Update","Do you wnat to update this record",parent=self.root)
                if(update_val>0):
                    conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",( 

                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                self.var_sec.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_mentor.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_id.get()
                                                                                                               
                                                                                                                                                                                                           )) 
                else:
                    if not update_val:
                        return 
                msg.showinfo("Success",'Records updated successfullty',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                msg.showerror("Error",f"due to:{str(es)}",parent=self.root) 

    # -----------delete function-----------------
    def del_data(self):
        if self.var_id.get()=="":
            msg.showerror("Error","StudentID must be required",parent=self.root)
        else:
            try:
                del_row=msg.askyesno("Student Delete Page",'Do you want to delete the record',parent=self.root)
                if del_row>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    sql_quiery='delete from student where Student_id=%s'
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql_quiery,val)
                else:
                    if not del_row:
                        return
                msg.showinfo("Success","Record deleted successfully",parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                msg.showerror('Error',f'due to: {str(es)}',parent=self.root)  

    #----------------reset function-------------------------------------
    def reset_data(self):
        self.var_dep.set('Choose')
        self.var_course.set('Choose')
        self.var_year.set('Choose')
        self.var_sem.set('Choose')
        self.var_id.set('')
        self.var_name.set('')
        self.var_sec.set('Select')
        self.var_roll.set('')
        self.var_gender.set('Select')
        self.var_address.set('')
        self.var_phone.set('')
        self.var_mentor.set('')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_radio1.set('')

    #--------------------search function------------------------
    def search(self):
        if self.var_search.get()=="" or self.var_search_all.get()=="":
            msg.showerror('Error','Filled is empty',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from student where '+str(self.var_search.get())+" LIKE '%"+str(self.var_search_all.get())+"%'")
                get_data=my_cursor.fetchall()
                if len(get_data)!=0:
                    self.std_data_table.delete(*self.std_data_table.get_children())
                    for i in get_data:
                        self.std_data_table.insert("",END,values=i)
                    conn.commit()
                conn.close()         
            except Exception as es:
                msg.showerror('Error',f'due to: {str(es)}',parent=self.root)


    #-------------change image function/feature----------------------
    def change_img(self):
        val=msg.askyesno('Change','Want to change image')
        if val>0:
            fbd=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Images',filetypes=(('JPG File','*.jpg'),("All Files","*.*")))
            image=Image.open(fbd)
            img_browse=image.resize((450,105),Image.ANTIALIAS)
            self.photo_img=ImageTk.PhotoImage(img_browse)
            self.img_lft_label.config(image=self.photo_img)
        else:
            return    

    def change_img_2(self):
        val=msg.askyesno('Change','Want to change image')
        if val>0:
            fbd=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open Images',filetypes=(('JPG File','*.jpg'),("All Files","*.*")))
            image=Image.open(fbd)
            img_browse=image.resize((450,105),Image.ANTIALIAS)
            self.photo_img=ImageTk.PhotoImage(img_browse)
            self.img_rht_label.config(image=self.photo_img) 
        else:
            return   






    #-----------------------------DataSet for Photos---------------------------------
    def photos_dataset(self):
        if self.var_dep.get()=="Choose" or self.var_name.get()=="" or self.var_id.get()=="":
            msg.showerror('error','Required all fields',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='root',database='face_dataset',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from student')
                res=my_cursor.fetchall()
                id=0
                for i in res:
                    id=id+1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",( 

                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_mentor.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_id.get()==id+1                                                                                          
                                                                                                                                                                                                           )) 
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                #------------------------Load dataset of face frontals from opencv--------------------------
                face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                #---image croping function---------
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor=1.3,min Neighbour=5

                    for(x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped

                cam = cv2.VideoCapture(0)
                image_id=0
                while True:
                    ret, my_frame=cam.read()
                    if face_cropped(my_frame) is not None:
                        image_id+=1
                        face=cv2.resize(face_cropped(my_frame),(350,350))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        img_path="face_data/user."+str(id)+"."+str(image_id)+".jpg"
                        cv2.imwrite(img_path,face)
                        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Cropped_face',face)

                    if cv2.waitKey(1)==13 or int(image_id)==100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                msg.showinfo('Success','Dataset Generated successfully')
            except Exception as es:
                print({str(es)})
                msg.showerror("Error",f"due to: {str(es)}",parent=self.root)
                

                                                                                                                                                                                      


if __name__ == "__main__":
    root=Tk()
    root.minsize(700,400)
    obj=Student_Management_System(root)
    root.mainloop()      
