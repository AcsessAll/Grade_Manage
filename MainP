from tkinter import *  
from view import *  #菜单栏对应的各个子页面  
  
class MainP(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root 
        self.root.title('成绩管理系统')  
        self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小  
        self.createPage()  
  
    def createPage(self):  
        self.queryPage = QueryFrame(self.root) 
        self.queryPage.pack() #默认显示数据录入界面  
        menubar = Menu(self.root)  
        menubar.add_command(label='查询学生信息', command = self.queryData)  
        self.root['menu'] = menubar  # 设置菜单栏   
    def queryData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()  
  
  
  
   
