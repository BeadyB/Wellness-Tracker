import tkinter
from tkinter import * 
from tkinter.ttk import *


def student_add():
    window = tkinter.Tk()
    window.title("ADD")
    window.minsize(width=800, height=500)

    Students = []
    done = False
    while done != True:
        stu = input("Enter a student's name and number. Type DONE when you are finished: ")
    if stu == "DONE":
        done = True 
    else:
        Students.append(stu)


def student_remove():
    window = tkinter.Tk()
    window.title("REMOVE")
    window.minsize(width=800, height=500)
    
    Students = []
    done = False
    while done != True:
        rem = input("Enter the name and number of the student to be removed: ")
    if rem == "done":
        done = True 
    else:
        Students.remove(rem)



window = tkinter.Tk()
window.title("Wellness Tracker")
window.minsize(width=800, height=500)

output_label = tkinter.Label(text="", justify=tkinter.RIGHT, width=8)
ADD_button = tkinter.Button(text='ADD', command=student_add)
REM_button = tkinter.Button(text='REMOVE', command=student_remove)
Label(text="Wellness Tracker", font=('Helvetica 17 bold')).pack(pady=30)

output_label.pack(padx=20, pady=20, side=tkinter.RIGHT)
ADD_button.pack(padx=20, pady=20)
REM_button.pack(padx=20, pady=30)

window.mainloop()





#This is how a student is removed from the database
def student_remove():

    Student = Student
    done = False
    while done != True:
         rem = input("Enter the name and number of the student to be removed: ")
    if rem == "done":
      done = True 
    else:
      Student.remove(rem)
    print(Student)
student_remove()

#You should be able to see all the student names


