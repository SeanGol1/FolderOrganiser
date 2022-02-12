from cgitb import text
from distutils.command.config import config
import os
from tkinter import *
from tkinter import ttk

    # Configs

_directory = 'C:\\Users\\seang\\OneDrive\\Desktop\\Test'
_useCurrentDir = False
_renameFile = False
_testMode = False
log = []


 
def GUI():

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    var = StringVar()

    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Label(frm, text="Rename files:").grid(column=0, row=1)
    ttk.Radiobutton(frm, text="Yes",variable=var,value='Y').grid(column=0,row=2)
    ttk.Radiobutton(frm, text="No",variable=var,value='N').grid(column=1,row=2)
    ttk.Button(frm,text="Execute", command=readFiles).grid(column=0,row=3)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=3)
    root.mainloop()
    




def readFiles():
    dir = _directory
    fileNames = []
    inp = '_'

    # Get all files in Directory with {inp} in name

    if(_useCurrentDir):
        dir = os.getcwd()
    
    print('current:'+ os.getcwd())

    for r, d, f in os.walk(dir):
        for file in f:
            filepath = os.path.join(r, file)
            if inp in file:                                
                fileNames.append(os.path.join(r, file))               
    print(f" {len(fileNames)} files found.")

    # Send each item to create a new folder
    for f in fileNames:
        newFolder(f)
        

def newFolder(fileName):   

    # Remove the file name
    fn = fileName.split('_')     
    fn = fn[:-1]
    fn = '\\'.join(fn)

    # Check if path exists and create
    #print('Changing ' + fn + ' to ' + pathname + '...')
    if not os.path.exists(fn)  and _testMode == False:
        os.makedirs(fn)
        
    moveFiles(fileName,fn)

def moveFiles(file,folder):

    if(_renameFile):
        # Get file name
        fn = file.split('_')     
        name = fn[(len(fn) - 1)]
    else:
        fn = file.split('\\')
        name = fn[(len(fn) - 1)]

    print('Moving file: '+ name)
    print('From: ' + file)
    print('To: ' + folder)
    if(_testMode == False):
        os.replace(file, folder + '\\' + name)


GUI()