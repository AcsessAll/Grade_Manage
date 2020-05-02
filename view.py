from tkinter import *  
from tkinter.messagebox import *  
  
class InputFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.E6 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1


    def write(self,name,num,course,score):
        f = open('成绩.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<4:
                break
            if info[1] ==num and info[2] ==course:
                 messagebox.showinfo(title='结果', message ="已存在该学生科目信息！")
                 f.close()
                 return

        f.close()
        f = open('成绩.csv','a',encoding='utf-8')
        f.write('{},{},{},{}\n'.format(name,num,course,score))
        f.close()
        messagebox.showinfo(title='提示', message ="写入成功")
        return
    
    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.write(name,num,course,score)
            
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '姓名: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '学号: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = '科目: ').grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = '成绩: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)       
        
        Button(self, text='录入',command=self.click).grid(row=6, column=1, stick=E, pady=10)  
  
  
class DeleteFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()
        
    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def delete(self,num,course):
        temp = 0
        with open("成绩.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
   
        with open("成绩.csv","w",encoding="utf-8") as f_w:
            for line in lines:
                info = line[:-1].split(",")
                if info[1] ==num and info[2] ==course:
                    temp = 1
                    continue
                f_w.write(line)
        if temp==0:
            messagebox.showinfo(title='提示', message ="没有该信息")
        else:
            messagebox.showinfo(title='提示', message ="删除成功")
        
    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.delete(num,course)
            
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '学号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '科目: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Button(self, text='删除',command=self.click).grid(row=6, column=1, stick=E, pady=10)  
  
  
class ModifyFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

        
    def modify(self,name,num,course,score):
        temp = 0
        with open("成绩.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
   
        with open("成绩.csv","w",encoding="utf-8") as f_w:
            for line in lines:
                info = line[:-1].split(",")
                if info[1] ==num and info[2] ==course:
                    temp = 1
                    f_w.write('{},{},{},{}\n'.format(name,num,course,score))
                    continue
                f_w.write(line)
        if temp==0:
            messagebox.showinfo(title='提示', message ="没有该信息")
        else:
            messagebox.showinfo(title='提示', message ="修改成功")
        
    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.modify(name,num,course,score)
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '姓名: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '学号: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = '科目: ').grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = '成绩: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)       
        
        Button(self, text='修改',command=self.click).grid(row=6, column=1, stick=E, pady=10)  

class QueryFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def query(self,num,course):
        f = open('成绩.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[1] ==num and info[2] ==course:
                 messagebox.showinfo(title='结果', message ="姓名："+info[0] +"\n学号:"+info[1] +"\n科目:"+info[2] +"\n成绩:"+info[3] )
                 f.close()
                 return

        messagebox.showinfo(title='提示', message ="没有该信息")
        f.close()
        return        
        
        
    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.query(num,course)
            
            
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '学号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '科目: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Button(self, text='查找',command=self.click).grid(row=6, column=1, stick=E, pady=10)  
  
