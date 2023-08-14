# crate a class to catgrized colors
class bcolors: 
    Red          = "\033[31m"
    Green        = "\033[32m" 
    White        = "\033[97m"
    Blue         = "\033[34m"
 # import modules 
import os
import os.path
import datetime
import time
import sys
# defined folders names to save files
date=datetime.datetime.now()
folder1_name=date.strftime("%Y")
folder2_name=date.strftime("%B")
folder3_name=date.strftime("%d")
# function to print with animetion
def typer(string):
    string = list(string)
    for char in string:
        time.sleep(0.1)
        print(char, end="",flush=True)
#function to print help for user
def helper ():
    hlp=bcolors.Blue+"""
    enter ths command to 
    save! -->> save text as a file
    open! -->> show the file content on screen
    del!  -->> delete a file
    exit! -->> exit the program
    help! -->> show the help 
    """+bcolors.White
    typer(hlp)
#function to make a path if dont finde it
def path_make():
    if os.getcwd() !=folder1_name+"/"+folder2_name+"/"+folder3_name:
        if not os.path.exists(folder1_name+"/"+folder2_name+"/"+folder3_name):
            os.makedirs(folder1_name+"/"+folder2_name+"/"+folder3_name)
#function to save files in selcted path
def save (text):
    try:
        text.append(folder1_name+"/"+folder2_name+"/"+folder3_name)
        if os.getcwd() !=folder1_name+"/"+folder2_name+"/"+folder3_name:
            os.chdir(folder1_name+"/"+folder2_name+"/"+folder3_name)
        name=input('enter file name with extention\t:')
        file=open(name,'w')
        for i in text:
            file.write(i+'\n')
        file.close
        mass=bcolors.Green+'saved...'+bcolors.White
        typer(mass)
        os.chdir('C:\\Users\\DELL\\Desktop\\note')
    except:
        mass=bcolors.Red+'dont save retry please...'+bcolors.White
        typer(mass)
#function to print an old files content
def show_file ():
    try:
        if os.getcwd() !=folder1_name+"/"+folder2_name+"/"+folder3_name:
            os.chdir(folder1_name+"/"+folder2_name+"/"+folder3_name)
        name=input('enter file name with extention\t:')
        file=open(name,'r')
        text=file.read()
        file.close()
        print(text)
        os.chdir('C:\\Users\\DELL\\Desktop\\note')
    except:
        mass=bcolors.Red+'an error retry please...'+bcolors.White
        typer(mass)
# function to delete files
def delete ():
    try:
        if os.getcwd() !=folder1_name+"/"+folder2_name+"/"+folder3_name:
            os.chdir(folder1_name+"/"+folder2_name+"/"+folder3_name)
        name=input('enter file name with extention\t:')
        print('\a')
        ans=input(bcolors.Red+'do yiu relly want to dlet name.txt...............(enter Y for yse)\n'+bcolors.White)
        if ans=='Y':
            os.remove(name)
            mass=bcolors.Green+'deleted...'+bcolors.White
            typer(mass)
        else:
            pass
        os.chdir('C:\\Users\\DELL\\Desktop\\note')
    except:
        mass=bcolors.Red+'an error retry please...'+bcolors.White
        typer(mass)
#maine loop
while True:
    text=[]
    os.chdir('C:\\Users\\DELL\\Desktop\\note')
    path_make()
    print('\nenter text')
    #get multi line input
    while True:
        t=input()
        #detction the command
        if t=='save!':#
            save(text)
            break
        elif t=='del!':
            delete()
            break
        elif t=='open!':
            show_file ()
            break
        elif t=='exit!':
            sys.exit()
            break
        elif t=='help!':
            helper()
            break
        else:
            text.append(t)