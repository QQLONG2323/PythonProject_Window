'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import re

#BMI計算式
def calculate_BMI(h, w):
    bmi = w / (h / 100)**2
    if bmi > 30:
        return "肥胖, 少吃點多運動", bmi
    elif bmi >= 25:
        return "過重, 少吃點", bmi
    elif bmi >= 18.5:
        return "正常, 請保持", bmi
    else:
        return "太輕, 多吃點", bmi

#互動介面
class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        ttkStyle = ttk.Style()
        ttkStyle.theme_use("default")
        ttkStyle.configure("red.TFrame", background = "red")
        ttkStyle.configure("white.TFrame", background = "white")
        ttkStyle.configure("yellow.TFrame", background = "yellow")
        ttkStyle.configure("white.TLabel", background = "white")
        ttkStyle.configure("gridLabel.TLabel", font = ("Helvetica", 16), foreground = "#666666")
        ttkStyle.configure("gridEntry.TEntry", font = ("Helvetica", 16))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height = 100)
        topFrame.pack(fill = tk.X)

        ttk.Label(topFrame, text = "BMI試算", font = ("Helvetica", "20")).pack(pady = (80, 20))

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand = True, fill = tk.BOTH)
        bottomFrame.columnconfigure(0, weight = 3, pad = 20)
        bottomFrame.columnconfigure(1, weight = 5, pad = 20)
        bottomFrame.rowconfigure(0, weight=1,pad=20)
        bottomFrame.rowconfigure(3, weight=1,pad=20)
        bottomFrame.rowconfigure(4, weight=1,pad=20)
        bottomFrame.rowconfigure(5, weight=1,pad=20)
        bottomFrame.rowconfigure(6, weight=1,pad=20)    

        ttk.Label(bottomFrame, text = "姓名", style = "gridLabel.TLabel").grid(column = 0, row = 0, sticky = tk.E)
        self.nameEntry = ttk.Entry(bottomFrame, style = "gridEntry.TEntry")
        self.nameEntry.grid(column = 1, row = 0, sticky = tk.W, padx = 10)

        ttk.Label(bottomFrame, text = "出生年月日", style = "gridLabel.TLabel").grid(column = 0, row = 1, sticky = tk.E)
        ttk.Label(bottomFrame, text = "2000/03/01", style = "gridLabel.TLabel").grid(column = 0, row = 2, sticky = tk.E)
        self.birthEntry = ttk.Entry(bottomFrame, style = "gridEntry.TEntry")
        self.birthEntry.grid(column = 1, row = 1, sticky = tk.W, rowspan = 2, padx = 10)

        ttk.Label(bottomFrame, text = "身高(cm): ", style = "gridLabel.TLabel").grid(column = 0, row = 3, sticky = tk.E)
        self.heightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        self.heightEntry.grid(column=1,row=3,sticky=tk.W, padx = 10)

        ttk.Label(bottomFrame,text="體重(kg): ",style='gridLabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        self.weightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        self.weightEntry.grid(column=1,row=4,sticky=tk.W, padx = 10)

        self.messageText = tk.Text(bottomFrame,height=5,width=35, state=tk.DISABLED, takefocus = 0, bd = 0)
        self.messageText.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)
  
        #---------------commitFrame_start---------------
        #有左右兩個鍵
        commitFrame = ttk.Frame(bottomFrame)
        commitFrame.grid(column=0,row=6,columnspan=2)
        commitFrame.columnconfigure(0,pad=10)       

        commitBtn = ttk.Button(commitFrame,text="計算", command = self.calculate_and_show)
        commitBtn.grid(column=0,row=0)
        
        clearBtn = ttk.Button(commitFrame, text="清除", command = self.press_clear)
        clearBtn.grid(column=1, row=0)
        #---------------commitFrame_end---------------

        #---------------logoImage_create---------------
        logoImage = Image.open("./logo.png")
        resizeImage = logoImage.resize((180,45), Image.LANCZOS)
        self.logoPhoto = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(self, image=self.logoPhoto, width=180)
        logoLabel.place(x=40,y=45)
        #---------------logoImage_end---------------  
       
    #清除按鈕的功能
    def press_clear(self):        
        self.nameEntry.delete(0, tk.END)
        self.birthEntry.delete(0, tk.END)
        self.heightEntry.delete(0, tk.END)
        self.weightEntry.delete(0, tk.END)
        self.messageText.config(state = tk.NORMAL)
        self.messageText.delete('1.0', tk.END)
        self.messageText.config(state = tk.DISABLED)
        print('清除')

    def calculate_and_show(self):

        name = self.nameEntry.get()

        birth = self.birthEntry.get()
        dateRegex = re.compile(r"^\d\d\d\d/\d\d/\d\d$")
        birthMatch = re.match(dateRegex,birth)
        if birthMatch is None:
            birth = ""

        if name=="" or birth=="":
            message = "有姓名/生日沒填或生日格式不正確"
            self.messageText.config(state = tk.NORMAL)
            self.messageText.delete(0.0, tk.END)
            self.messageText.insert(tk.END, message)
            self.messageText.config(state = tk.DISABLED)
            return
              
        try:   
            height = float(self.heightEntry.get())            
            weight = float(self.weightEntry.get())
            if height !=0 and weight != 0:
                category, bmi = calculate_BMI(height, weight)
                message = f"{name}\n您的生日是: {birth}\n您的BMI是: {bmi}\n您的體重: {category}"
            else:
                message = "身高體重皆不可為0"       
        except ValueError:
            message = "請輸入有效的數字"
            
        self.messageText.config(state = tk.NORMAL)
        self.messageText.delete(0.0, tk.END)
        self.messageText.insert(tk.END, message)
        self.messageText.config(state = tk.DISABLED)
        

    

def close_window():
    print("視窗關閉")
    w.destroy()
        
            
def main():
    '''
    這是程式的執行點
    '''

    window = Window()
    window.title("BMI計算")
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", lambda:close_window(window))
    window.mainloop()

if __name__ == "__main__":
    main()