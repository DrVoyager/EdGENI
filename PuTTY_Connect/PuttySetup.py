import subprocess
import os
import tkinter as tk
import configparser
import re
import ctypes
from tkinter import ttk, messagebox, filedialog
from tkinter import *

root = tk.Tk()

root.title("PuTTY Connect")
win_width = 450
win_height = 616

root.resizable(False,False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
start_x = int((screen_width/2)-(win_width/2))
start_y = int((screen_height/2)-(win_height/2))
root.geometry('{}x{}+{}+{}'.format(win_width,win_height,start_x,start_y))

def puttyBrowsefunc():
    puttyFileLocation = filedialog.askopenfilename()
    puttyFileLocationEntry.insert("12",puttyFileLocation)
def puttyKeyBrowsefunc():
    puttyKeyLocation = filedialog.askopenfilename()
    puttyKeyLocationEntry.insert("12",puttyKeyLocation)

def isValidLinkAddress(linkAddress):
    pattern = '(^ssh:\/\/)+[a-zA-Z0-9]+@[a-zA-Z0-9\.]+:(\d{5})'
    return(bool(re.match(pattern,linkAddress)))

def isValidTunnelInfo(tunnelInfo):
    pattern ='^[0-99]$'
    return(bool(re.match(pattern,tunnelInfo)))
    
def linkGetfunc():
    global hostName, port
    linkAddress = linkAddressEntry.get()
    if isValidLinkAddress(linkAddress):
        linkAddress = linkAddress[6:]
        hostName = linkAddress[:(linkAddress.find(":"))]
        port = linkAddress[(linkAddress.find(":")+1):]
        hostLabel = tk.Label(root, text="Host Name: " + hostName, width=40, anchor='w',fg="red",
                      font=("Sylfaen", 9)).grid(row=6,sticky=W,padx=7)
        portLabel = tk.Label(root, text="Port: " + port , width=40, anchor='w',fg="red",
                      font=("Sylfaen", 9)).grid(row=7,sticky=W,padx=7)
    else:
        ctypes.windll.user32.MessageBoxW(0,"Please Re-Enter Link Address looking Example","Warning",1)
def setTunnelInfo(tunnel):
    global vncServerTxt, sourcePort

    filename = 'Tunnel_' + tunnel +'.txt'
    filedetails = 'vncserver :' + tunnel + ' ;\n' + 'echo \"********************************************************\n'+'Welcome You are Connected to Your VM.\nPlease Go to VNC Viewer and connect to localhost:590'+tunnel+'\n********************************************************"'+ ' ;\n' + '/bin/bash'
    f = open(filename,"w+")
    f.write(filedetails)
    f.close()
    vncServerTxt = os.path.abspath(filename)
    sourcePort = '590' + tunnel + ':127.0.0.1:590' + tunnel

def saveList():
    global userList, savedList
    config = configparser.ConfigParser()
    config.read('puttySetup.ini')
    userList = config.sections()
    
    savedList = Listbox(root, width = 54)
    savedList.grid(row=17, sticky=W,padx=9 ,pady=5,rowspan=3)

    scroll = tk.Scrollbar(root, command=savedList.yview).grid(row=17, sticky=W, padx=350, rowspan=3)

    savedList.configure(yscrollcommand=scroll)

    for user in userList:
        savedList.insert(END, user)

class User:
    puttyFileLocation = ""
    linkAddress = ""
    puttyKeyLocation = ""
    puttyPassphrase= ""
    tunnelInfo= ""
    vncServerTxt= ""
    hostName= ""
    port = ""
    sourcePort = ""
    
puttyFileLocationLabel = tk.Label(root, text="PuTTY Application Location",justify='left',anchor='w',
                     font=("Sylfaen", 11)).grid(row=0, sticky=W, padx=7)
puttyBrowseButton = tk.Button(root, text="Browse", command=lambda :puttyBrowsefunc(),height=1,width=7)
puttyBrowseButton.grid(row=1, sticky=W, padx=375)
linkAddressLabel = tk.Label(root, text="Link Address", anchor='w',
                      font=("Sylfaen", 11)).grid(row=2, sticky=W, padx=7)
instructionLabel1 = tk.Label(root, text="Paste VM Link From GENI into the following box and Click Get", anchor='w',
                      font=("Sylfaen", 9)).grid(row=3, sticky=W, padx=7)
instructionLabel2 = tk.Label(root, text="Example: ssh://geni157@pc1.instageni.idre.ucla.edu:27610", anchor='w',
                      font=("Sylfaen", 9)).grid(row=4, sticky=W, padx=7)
hostLabel = tk.Label(root, text="Host Name: ", width=40, anchor='w',fg="red",
                      font=("Sylfaen", 9)).grid(row=6,sticky=W,padx=7)
portLabel = tk.Label(root, text="Port: " , width=40, anchor='w',fg="red",
                      font=("Sylfaen", 9)).grid(row=7,sticky=W,padx=7)
linkGetButton = tk.Button(root, text="Get", command=lambda :linkGetfunc(),height=1,width=7)
linkGetButton.grid(row=5, sticky=W, padx=375)
puttyKeyLocationLabel = tk.Label(root, text="PuTTY Key Location", width=40, anchor='w',
                        font=("Sylfaen", 11)).grid(row=8, sticky=W, padx=7)
puttyKeyBrowseButton = tk.Button(root, text="Browse", command=lambda :puttyKeyBrowsefunc(),height=1,width=7)
puttyKeyBrowseButton.grid(row=9, sticky=W, padx=375)
puttyPassphraseLabel = tk.Label(root, text="PuTTY Key Passphrase", width=40, anchor='w',
                        font=("Sylfaen", 11)).grid(row=10, sticky=W, padx=7)
tunnelInfoLabel = tk.Label(root, text="Tunnel Info", width=40, anchor='w',
                        font=("Sylfaen", 11)).grid(row=12, sticky=W, padx=7)
instructionLabel3 = tk.Label(root, text="Enter 1 for Client VM & 2 for Server VM", width=40, anchor='w',
                        font=("Sylfaen", 9)).grid(row=13, sticky=W, padx=7)
puttyFileLocationEntry = tk.Entry(root,font=("Sylfaen",11), width = 40)
linkAddressEntry = tk.Entry(root,font=("Sylfaen",11), width = 40)
puttyKeyLocationEntry = tk.Entry(root,font=("Sylfaen",11), width = 40)
puttyPassphraseEntry = tk.Entry(root,font=("Sylfaen",11), width = 40)
puttyPassphraseEntry.config(show="*")
tunnelInfoEntry = tk.Entry(root,font=("Sylfaen",11), width = 40)
vncServerTxtEntry = tk.Entry(root,font=("Sylfaen",11), width = 40)

puttyFileLocationEntry.grid(row=1, sticky=W, padx=(9,10))
linkAddressEntry.grid(row=5, sticky=W, padx=(9,10))
puttyKeyLocationEntry.grid(row=9, sticky=W, padx=(9,10))
puttyPassphraseEntry.grid(row=11, sticky=W, padx=(9,10))
tunnelInfoEntry.grid(row=14, sticky=W, padx=(9,10))
saveLabel = tk.Label(root, text="Saved Sessions",anchor='w',
                        font=("Sylfaen", 11)).grid(row=15, sticky=W, padx=7)
saveNameEntry  = tk.Entry(root,font=("Sylfaen",11), width=40)
saveNameEntry.grid(row=16, sticky=W, padx=(9,10))

saveButton = tk.Button(root, text="Save", command=lambda :savefunc(),height=1,width=7)
saveButton.grid(row=17, sticky=W, padx=375)
loadButton = tk.Button(root, text="Load", command=lambda :loadfunc(),height=1,width=7)
loadButton.grid(row=18, sticky=W, padx=375)
deleteButton = tk.Button(root, text="Delete", command=lambda :deletefunc(),height=1,width=7)
deleteButton.grid(row=19, sticky=W, padx=375)
openButton = tk.Button(root, text="Open PuTTY", command=lambda :openPutty(),height=1,width=11)
openButton.grid(row=20,sticky=W, padx = 175)

saveList()
    
def savefunc():
    config = configparser.ConfigParser()
    config.read('puttySetup.ini')
    user = saveNameEntry.get()
    if(config.has_section(user)):
        config.remove_section(user)
    config.add_section(user)
    config.set(user, 'puttyFileLocation', puttyFileLocationEntry.get()) 
    config.set(user, 'linkAddress' , linkAddressEntry.get())
    config.set(user, 'puttyKeyLocation', puttyKeyLocationEntry.get()) 
    config.set(user, 'puttyPassphrase', puttyPassphraseEntry.get()) 
    config.set(user,'tunnelInfo', tunnelInfoEntry.get())
    with open('puttySetup.ini', 'w') as configfile:
        config.write(configfile)
    saveList()
        
def loadfunc():
    global userList, savedList

    puttyFileLocationEntry.delete(0,'end')
    linkAddressEntry.delete(0,'end')
    puttyKeyLocationEntry.delete(0,'end')
    puttyPassphraseEntry.delete(0,'end')
    tunnelInfoEntry.delete(0,'end')
    saveNameEntry.delete(0,'end')
    
    config = configparser.ConfigParser()
    config.read('puttySetup.ini')
    user = savedList.get(ACTIVE)
    puttyFileLocationEntry.insert("12",config.get(user,'puttyFileLocation'))
    linkAddressEntry.insert("12",config.get(user,'linkAddress'))
    puttyKeyLocationEntry.insert("12",config.get(user,'puttyKeyLocation'))
    puttyPassphraseEntry.insert("12",config.get(user,'puttyPassphrase'))
    tunnelInfoEntry.insert("12",config.get(user,'tunnelInfo'))
    saveNameEntry.insert("12", user)
    linkGetfunc()
    
def deletefunc():
    global userList, savedList

    config = configparser.ConfigParser()
    config.read('puttySetup.ini')
    deleteUser = savedList.get(ACTIVE)
    config.remove_section(deleteUser)
    with open('puttySetup.ini', 'w') as configfile:
        config.write(configfile)
    saveList()
    
def listfunc():
    global userList
    
    config = configparser.ConfigParser()
    config.read('puttySetup.ini')
    userList = config.sections()
    print(userList)

def openPutty():
    global puttyFileLocation, linkAddress, puttyKeyLocation, puttyPassphrase, tunnelInfo, vncServerTxt, hostName, port, sourcePort, savedName

    puttyFileLocation = puttyFileLocationEntry.get()
    puttyKeyLocation = puttyKeyLocationEntry.get()
    puttyPassphrase = puttyPassphraseEntry.get()
    tunnelInfo = tunnelInfoEntry.get()

    setTunnelInfo(tunnelInfo)

    if isValidTunnelInfo(tunnelInfo):
        userCommand = ('\"'+ puttyFileLocation +'\"' + ' -ssh '+ hostName + ' ' + port + ' -i ' +'\"'+
                   puttyKeyLocation + '\"'+ ' -X -L ' + sourcePort +' -pw '+ puttyPassphrase + ' -m ' + '\"' + vncServerTxt + '\"'+ ' -t')
        try:
            subprocess.Popen(userCommand)
        except:
            ctypes.windll.user32.MessageBoxW(0,"Invalid PuTTY Application Location","Warning",0x10)
            
    else:
        ctypes.windll.user32.MessageBoxW(0,"Invalid Tunnel Info. \nPlease Enter 1 for Client and 2 for Server","Warning",0x10)

root.mainloop()
