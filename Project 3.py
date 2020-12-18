import pytube
from pytube import YouTube
import os
from tkinter import *

root = Tk()

root.geometry("500x400")
root.title("YouTube video download")

def youtube():
    a = var.get()#a is a link :"https://www.youtube.com/watch?v=cJOXu8CwDgM"
    ytvideo = YouTube(a).streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
    ytvideo.download(r"C:/Users/admin/Desktop/python video download")
    

l1 = Label(root,text="YouTube video link", fg="red",font=("bold",20))
l1.place(x=70,y=20)

l2 = Label(root,text="Paste your link here", fg="black",font=("italics",15))
l2.place(x=100,y=60)

var = StringVar()

e1 = Entry(root, textvariable=var, width=60)
e1.place(x=80,y=100)

b1 = Button(root, text="Download", command=youtube, bg="green", width=20, fg="white")
b1.place(x=120,y=130)



root.mainloop()

