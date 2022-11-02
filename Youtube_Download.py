from tkinter import *
from pytube import *

root = Tk()
root.geometry('700x350')
root.resizable(0,0)
root.title("Youtube Video Downloader")


Label(root,text = 'Youtube Video Downloader', font ='Courier 20 bold').pack()


link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Courier 15').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams
    video.filter(res='720p').first().download()
    Label(root, text = 'DOWNLOADED', font = 'Courier 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD', font = 'Courier 15' ,bg = 'green', padx = 2, command = Downloader).place(x=100 ,y = 180)



root.mainloop()
