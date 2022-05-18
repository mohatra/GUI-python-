from cProfile import label
from distutils import command
from re import M
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class system():
    def __init__(self,robot):
        self.robot=robot 
        #add a title 
        self.robot.title("Ecorp ")
    
        #the size of the window 
        self.robot.geometry("600x900")
        self.robot.resizable(False, False)
        
        #the icon of the window 
        self.robot.iconbitmap("C:/Users/Gamer PC/Downloads/letter-e.ico")
        
        #image background
        self.bg=PhotoImage(file="C:/Users/Gamer PC/Desktop/full1.png")
        self.bg_image=Label(self.robot, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #subtitles
        sub=Label(text="E CORP MEMBERS AREA", font=("cairo", "20" , "bold"),fg="white", bg="#212121").place(x=149,y=320)
        sub=Label(text="Sing in to your account", font=("Raleway", "17"), fg="black", bg="#868685").place(x=170,y=430)
        usern=Label(text="Username", font=("Raleway", "12"), fg="black", bg="#868685").place(x=155,y=480)
        sub=Label(text="Password", font=("Raleway", "12"), fg="black", bg="#868685").place(x=155,y=560)
        sub=Label(text="Member id", font=("Raleway", "12"), fg="black", bg="#868685").place(x=155,y=640)
        
        #email entry
        self.username=Entry(font=("Verdana", "10"),fg="black",bg="white",bd=0)
        self.username.place(x=190,y=520,width=250,height=25)
        
        #password entry
        self.password=Entry(font=("Verdana", "10"),fg="black",bg="white",bd=0,show="•")
        self.password.place(x=190,y=600,width=250,height=25)
        
        #ID entry 
        self.id=Entry(font=("Verdana", "10"),fg="black",bg="white",bd=0,show="•")
        self.id.place(x=190,y=677,width=100,height=25)
        #buttons 
        forgot=Button(text="Forgot password?" , font=("Raleway" , "8" ),fg="black",bg="#868685", bd=0 , activebackground="#868685")
        forgot.place(x=350, y=630)

        #sing in button 
        self.enter=PhotoImage(file="C:/Users/Gamer PC/Desktop/button.png")     
        benter=Button(self.robot , image=self.enter , bd=0 ,bg="#868685" , activebackground="#868685" ,command= self.logs)   
        benter.place(x=300,y=700)
    
    def logs(self):
        if self.username.get()=="" or self.password.get()=="" or self.id.get()=="" :
            messagebox.showerror("Error", " Empty columns " , parent=self.robot)
                
        elif self.username.get()!="trabelcimohamed17@gmail.com" or self.password.get()!="123456789" or self.id.get()!="17052003":
            messagebox.showerror("Error", "invalid username or password or check you ID" , parent=self.robot)
            
        else: 
            messagebox.showinfo("welcom",f"welcom {self.username.get()}")

                
    
    
robot=Tk()
obj= system(robot)
robot.mainloop()