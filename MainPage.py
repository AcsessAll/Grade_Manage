from tkinter import *  
from view import *  #菜单栏对应的各个子页面  
  
class MainPage(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root  
        self.root.title('成绩管理系统')  
        self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小  
        self.createPage()  
  
    def createPage(self):  
        self.inputPage = InputFrame(self.root) # 创建不同Frame  
        self.deletePage = DeleteFrame(self.root)
        self.modifyPage = ModifyFrame(self.root)
        self.queryPage = QueryFrame(self.root) 
        self.inputPage.pack() #默认显示数据录入界面  
        menubar = Menu(self.root)  
        menubar.add_command(label='添加学生信息', command = self.inputData)  
        menubar.add_command(label='删除学生信息', command = self.deleteData)  
        menubar.add_command(label='修改学生信息', command = self.modifyData)  
        menubar.add_command(label='查询学生信息', command = self.queryData)  
        self.root['menu'] = menubar  # 设置菜单栏  
  
    def inputData(self):  
        self.inputPage.pack()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget() 

    def deleteData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack()  
        self.modifyPage.pack_forget()

    def modifyData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack()         
        
    def queryData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()  
  
  
  
   
