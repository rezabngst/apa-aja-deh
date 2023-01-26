import pyautogui
import tkinter as tk
from tkinter import filedialog

root=tk.Tk()

#membuat tampilan pada tkinter
canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()

#menentukan jenis file ekstensi
def takeScreenshot():
    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

#membuat tombol eksekusi
myButton=tk.Button(text='Take Screenshot',command=takeScreenshot,bg='black',fg='white',font=10)
canvas1.create_window(150,150,window=myButton)

root.mainloop()
