'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk

def calculate_BMI(h, w):
    bmi = w / (h / 100)**2
    if bmi > 30:
        return "肥胖", bmi
    elif bmi >= 25:
        return "過重", bmi
    elif bmi >= 18.5:
        return "正常", bmi
    else:
        return "太輕", bmi

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        ttkStyle = ttk.Style()
        ttkStyle.theme_use("default")
        ttkStyle.configure("red.TFrame", background = "red")
        ttkStyle.configure("white.TFrame", background = "white")
        ttkStyle.configure("yellow.TFrame", background = "yellow")
        ttkStyle.configure("white.Tlabel", background = "white")
        ttkStyle.configure("gridLabel.TLabel", font = ("Helvetica", 16), foreground = "#666666")
        ttkStyle.configure("gridEntry.TEntry", font = ("Helvetica", 16))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand = True, fill = tk.BOTH, padx = 30, pady = 30)

        topFrame = ttk.Frame(mainFrame, height = 100)
        topFrame.pack(fill = tk.X)

        ttk.Label(topFrame, text = "BMI試算", font = ("Helvetica", "20")).pack(pady = 20)

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
        nameEntry = ttk.Entry(bottomFrame, style = "gridEntry.TEntry")
        nameEntry.grid(column = 1, row = 0, sticky = tk.W, padx = 10)

        ttk.Label(bottomFrame, text = "出生年月日", style = "gridLabel.TLabel").grid(column = 0, row = 1, sticky = tk.E)
        ttk.Label(bottomFrame, text = "2000/03/01", style = "gridLabel.TLabel").grid(column = 0, row = 2, sticky = tk.E)

        birthEntry = ttk.Entry(bottomFrame, style = "gridEntry.TEntry")
        birthEntry.grid(column = 1, row = 1, sticky = tk.W, rowspan = 2, padx = 10)

        ttk.Label(bottomFrame, text = "身高(cm): ", style = "gridLabel.TLabel").grid(column = 0, row = 3, sticky = tk.E)
        heightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        heightEntry.grid(column=1,row=3,sticky=tk.W, padx = 10)

        ttk.Label(bottomFrame,text="體重(kg): ",style='gridLabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        weightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        weightEntry.grid(column=1,row=4,sticky=tk.W, padx = 10)

        messageText = tk.Text(bottomFrame,height=5,width=35, state=tk.DISABLED, takefocus = 0, bd = 0)
        messageText.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)

        commitBtn = ttk.Button(bottomFrame,text="計算", command = self.calculate_and_show)
        commitBtn.grid(column=1,row=6,sticky=tk.W)

        self.height_entry = heightEntry
        self.weight_entry = weightEntry
        self.message_text = messageText

    def calculate_and_show(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            category, bmi = calculate_BMI(height, weight)
            message = f"您的BMI是: {bmi}\n您的體重: {category}"
        except ValueError:
            message = "請輸入有效的數字"

        self.message_text.config(state = tk.NORMAL)
        self.message_text.delete(1.0, tk.END)
        self.message_text.insert(tk.END, message)
        self.message_text.config(state = tk.DISABLED)

        
            
def main():
    '''
    這是程式的執行點
    '''

    window = Window()
    window.title("BMI計算")
    #window.geometry("400x500")
    window.mainloop()

if __name__ == "__main__":
    main()