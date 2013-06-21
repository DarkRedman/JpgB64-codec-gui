import base64
import tkinter as tk
from tkinter import *

def encodeJpeg(imgpath):
    f=open(imgpath,'rb')
    data=f.read()
    f.close()
    base64data=base64.b64encode(data)
    return base64data.decode()

def decodeJpeg(imgpath,data):
    jpgdata=base64.b64decode(data)
    f=open(imgpath,'wb')
    f.write(jpgdata)
    f.close()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        self.title="img base64 codec"

    def createWidgets(self):
        #define a new frame and put a text area in it
        textfr=Frame(self)
        self.text=Text(textfr,height=10,width=50,background='white')
        
        # put a scroll bar in the frame
        scroll=Scrollbar(textfr)
        self.text.configure(yscrollcommand=scroll.set)
        
        #pack everything
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textfr.pack(side=TOP)

        self.btnEncode = tk.Button(self)
        self.btnEncode["text"] = "Encode a picture"
        self.btnEncode["command"] = self.encode
        self.btnEncode.pack()

        self.btnDecode = tk.Button(self)
        self.btnDecode["text"] = "Decode a picture"
        self.btnDecode["command"] = self.decode
        self.btnDecode.pack()

        self.btnCopy = tk.Button(self)
        self.btnCopy["text"] = "Copy text"
        self.btnCopy["command"] = self.copy
        self.btnCopy.pack()

        self.QUIT = Button(self, text="Quitter", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def encode(self):
        import os
        filename=tk.filedialog.askopenfilename(title="Open an image",parent=self.master,defaultextension="*.jpg",filetypes=[("Jpeg pictures","*.jpg")],initialdir=r'C:\Users\DarkRedman\Pictures')#os.path.expanduser("~user\\Pictures"))
        if not filename is None or filename !='':
            self.text.delete(0.0, END)
            self.text.insert(END, encodeJpeg(filename), 'color')

    def decode(self):
        import os
        
        filename=tk.filedialog.asksaveasfilename(title="Save an image",parent=self.master,defaultextension="*.jpg",filetypes=[("Jpeg pictures","*.jpg")],initialdir=r'C:\Users\DarkRedman\Pictures')#os.path.expanduser("~user\\Pictures"))
        if not filename is None or filename !='':
            decodeJpeg(filename,self.text.get(0.0,END))
    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.text.get(0.0,END))
            
root = tk.Tk()
app = Application(master=root)
app.mainloop()
