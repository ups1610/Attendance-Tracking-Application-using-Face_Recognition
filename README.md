# Under Microsoft Intern Engage <img align="center" width="150px" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyVdPTK0R8Xl32-L04RApWEIkv_FAzISrHDOFNqrHQ65axV2JhhGWcppvPx9xM-YRlNLQ&usqp=CAU" />
## Attendance_tracking_application 
### Application Objective
The manual Attendance System is ineffective in today's hectic time with a huge population. Tracking down one's attendance on a one-on-one basis as adapted by the majority of universities and educational institutions is quite a time consuming and not accurate. The pen-paper method of tracking attendance is outdated and we need an upgrade. Advantages of an automatic face-recognition attendance system:

* ***No paperwork.***
* ***It will save time and effort.***
* ***No risk of human error/proxy/fake attendance.***
* ***Improve efficiency and productivity.***
* ***Attendance data is available to both teachers and students.***
* ***Accuracy and Reliability.***
### About && Features 
This is a desktop application which works on __Face Recognition Technology.__ The Application is based on University Attendance Monitoring System. It's aim is to take the attendance of the students present in a particular class in an University. It consist of the following components:

***Admin Window***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/admin_window.png?alt=media&token=ffd2b638-48ef-41c9-8d42-c6fcf785b181)
***Student Window***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/student_window.png?alt=media&token=3e62fbc2-37bd-494f-b479-9486f856adc3)
***Student Registration Window***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/register.png?alt=media&token=e71aebfe-ed80-4718-b0f7-4c9be2f1fcb9)
***Training the Dataset Window***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/train_window.png?alt=media&token=17f60ffb-e1f6-410b-9567-c5dea5ec3ec8)
***Attendance Window***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/mark_attendance%20(2).png?alt=media&token=a52ce49d-1c55-4793-b75d-0eff1f83394f)
***Attendance Report***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/attendance_report.png?alt=media&token=9a039d20-7b15-4b4d-b968-0eb85eb6b685)
***Interactive ChatBot***
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/chat.png?alt=media&token=dee9837a-a67a-4d3c-9746-24d6779e68a3)
## Work Flow of Apllication
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/app_frame.png?alt=media&token=7fd0a0af-75a8-4813-8f57-eea38b67cb9c)
**Admin** used to register the data of students present in universities and after that data needs to be trained and students are ready to mark the attendance.
The attendance have been marked in two ways :
* Admin have the access to mark the attendance
* Students can mark their attendance through student portal 
* If any false attendance marked by the student Admin have the access to change the attendance report
Here is the attendance sample :
![Add Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/sample.png?alt=media&token=57e19b6e-27ad-4bd2-a7a4-349f316f3059)
## Technologies,FrameWork & Algorithm Used
* Python <img align="center" width="50px" src="https://www.python.org/static/opengraph-icon-200x200.png"/>
* MySQL Database <img align="center" width="50px" src="https://d1.awsstatic.com/asset-repository/products/amazon-rds/1024px-MySQL.ff87215b43fd7292af172e2a5d9b844217262571.png"/>
* opencv <img align ="center" width="100px" src="https://s3.kdbeer.dev/download/IMG_5fbab1507284d4be4733a21c-354953604.png" />
* Tkinter (GUI) 
* Harcassade classifier model 
* LBPH Algorithm  
## Challenges Faced
The 3 week journey is amazing to tackle out the problem and building a prototype. Some of the challenges that I faced during the period are:
* Setting up the enviornment variable is a great challenge that give me exposure to play with path accessibility
* Tkinter GUI is goot to design a desktop application but tooks a time to link one page to another
* Database connectivity is a great challenge for me it took over 1 day to connect my application to MySQL connector
* Installing a package creates lots of efforts such as voice packages some sklearn sub packages
* The most challenging thing is to deal with dependency of python packages
## Learnings
I have learnt:
* tkinter GUI for making application interactive sucha as button ,box images and its connection to the function
* first time the connection of database to the application
* first time linking of a page to another page in python
* fetching of data usibg SQL quiries
* the concept of harcassade classifier and implementaion of LBPH algorithm
* features of some useful libraries like PIL,freeze,cv2,Pyaudio,speech recognition etc.
* to create the virtual environment setup.
## How to Run
* Download latest version of Python say Python3.10.4
* Install All the required libraries in **requirements.txt**
use
```
     pip install -r requirements.txt
```
* Install tkinter library 
```
     pip install tk
     pip install mysql_connector
     pip install opencv-contrib-python
     pip install Pillow
```
* If left any libraray it's present in every **.py** file
* If using conda environment make sure of path variable and face any error like *ImportError: DLL load failed while importing _arpack: The specified procedure could not be found*
use:
```
     $> conda remove --force numpy, scipy
     $> pip install numpy
     $> pip install scipy
```
***MySQL Setup***
* Download Mysql workbwnch 8.0 CE https://dev.mysql.com/downloads/windows/installer/8.0.html
* set password = root and username=root(default)
* Create schema name as **face_dataset**
* Import the **sql_data->student** file to schema
* Follow the video



https://user-images.githubusercontent.com/75423160/170851210-154852d9-7629-42b7-ad6d-788ce8476f77.mp4



***Running Flow of application***
* **For Admin**
Start with **admin.py** file and all the options are given that window
then register the students data in database, train the model, mark the attendance and see the report in **admin.csv** file
* **For Student**
Start with **student_window.py** 
where he/she can mark the attendance use the chatbot and see the attendance report

## Other Files Information
* **train.py** file conatins the training model function of dataset
* **face recognition.py** conatins the face algorithm to recognise the face
* **chatfun.py** contains the chatbot properties
* **databse.py** contains student database
* **attendance_db.py** contains the attendance report database
## Future Scope
Due to 3 weeks of time I am able to implement only major features of my application
some more features such as:
* Face recognition Login authentication
* Personal Dashboard
* short attendance mail
* voice controlled system etc..
here is the flow diagram:
![App Screenshot](https://firebasestorage.googleapis.com/v0/b/face-recognition-system-d0666.appspot.com/o/application_frame.png?alt=media&token=638b5abc-d6a1-40de-92d6-fdcb908881d8)

