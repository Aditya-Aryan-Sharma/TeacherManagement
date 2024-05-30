# Teacher Management Application
This is a teacher management console-based application designed to store, retrieve and search through teacher data.
It implements file-based system to store teacher records in a csv file.

Task 1: Show All Teachers
In this task data from the teachers.csv file is read and all the stored entries are displayed.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/442ccc76-9d61-45b1-8ae4-d4956accee8d)

Task 2: Add a teacher
In this task a new record is created by taking input from the user for teacher's full name, age, Date of Birth, and number of classes in which he/she teaches. The new record is appended to the existing file and if the file is not created then it creates the file and then stores the new entry into it.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/7e033914-c6e0-4c3b-9a70-0c500d9aded2)

Task 3: Filter teachers based on criteria
In this task, the existing records are filtered on the age and number of classes parameter. The user is required to input two space separated integers denoting the starting and ending point of a range in which the age and the number of classes lie in.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/8668e29e-748a-416d-b70d-f5fac1cf5056)

Task 4: Search for a teacher
In this task, the system searches the data for a particular name fed as an input from the user. If multiple records exists for a particular name, then those records are filtered on the Date of Birth parameter.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/8d8abbb9-86a5-4ddf-a439-c682771c5cdd)

Task 5: Update a teacher's record
In this task, the application updates a particular feild of a teacher's record based on the user input. Here, it is assumed that Date of Birth won't be changed by the user as is the case with age. So, only name and number of classes can be changed for a given teacher.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/61a3c607-3489-4bef-a01e-6de29caef2fa)

Task 6: Delete a teacher
In this task, a teacher's record is deleted from the files if the user enters the name and DOB of the teacher.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/d2343f76-977f-4fc3-87fe-77a2ce58bb60)

Task 7: (Bonus)
In this task, we search through all the entries and count the number of classes each teacher teaches, and then use it to compute the average number of classes teacher takes.
![image](https://github.com/Aditya-Aryan-Sharma/TeacherManagement/assets/83038560/4e32656b-3a61-4619-a27f-f7ba7dbb7c8d)

Steps to run the application:
1) cd Simpplr
2) python -u “main.py”
