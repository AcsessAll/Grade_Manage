import tkinter as tk
from tkinter import * 
from LoginPage import *  
from LoginPage_admin import *

class login(object):
    def __init__(self,master=None):
        self.root=master
        self.root.title('python大数阶乘计算器')  
        self.root.geometry("300x200")
        self.createPage()

    def createPage(self):
        self.page =tk.Frame(self.root) #创建Frame  
        self.page.pack() 
        Button(self.page,text='点击进入服务器1：文哥无敌',command = self.user).grid(row=5, column=0, pady=5)
        #Button(self.page,text='教师及管理员登录',command = self.admin).grid(row=5, column=2, pady=5)

    def user(self):
        self.root.destroy()  #函数销毁
        root = tk.Tk()
        LoginPage(root)
        root.mainloop()
    #def admin(self):
       # self.root.destroy()
        #root = tk.Tk()
       # LoginPage_admin(root)
        #root.mainloop()
