# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk 
import pandas as pd
import numpy as np
import sys

btntext_temp=None
choicee_temp=None

ra2=None


#實作radiobutton鍵
def sel():
   selection = "You selected the option " + str(choice.get())
   print(selection+"\n")
   

def sel2(choicee_output):
   global ra2
   #select = "You selected the optionnn " + str(choicee_output)
   ra2=str(choicee_output)
   print(ra2)
   #print(select+"\n")
   

def choose_name(quickPrint):
        global choicee_temp
        global ra2
        ra2="公司資料"
        win3=tk.Tk() 
        choic = tk.IntVar()
        win3.geometry("1000x800")
        win3.title("project_stockj")
        
        radiotext1=tk.StringVar()
        radiotext1.set("公司資料")
        radioo1 = tk.Radiobutton(win3, text="公司資料", variable=choic,textvariable=radiotext1,value=1,command=lambda: sel2(radiotext1.get()))
        radioo1.grid(row=0,column=0,padx=5,pady=5)
        ra2=str(radiotext1.get())
        

        radiotext2=tk.StringVar()
        radiotext2.set("營收盈餘")
        radioo2 = tk.Radiobutton(win3, text="營收盈餘", variable=choic,textvariable=radiotext2,value=2,command=lambda: sel2(radiotext2.get()))
        radioo2.grid(row=0,column=1,padx=5,pady=5)

        radiotext3=tk.StringVar()
        radiotext3.set("股利政策")
        radioo3 = tk.Radiobutton(win3, text="股利政策", variable=choic,textvariable=radiotext3,value=3,command=lambda: sel2(radiotext3.get()))
        radioo3.grid(row=0,column=2,padx=5,pady=5)

        radiotext4=tk.StringVar()
        radiotext4.set("申報轉讓")
        radioo4 = tk.Radiobutton(win3, text="申報轉讓", variable=choic,textvariable=radiotext4,value=4,command=lambda: sel2(radiotext4.get()))
        radioo4.grid(row=0,column=3,padx=5,pady=5)
        
        radioo1.select()
        sel2(radiotext1.get())
        
        
        
        btntextt=tk.StringVar()
        btntextt.set("測試1!!")
        stockkt=tk.Button(win3,text=btntextt.get(),textvariable=btntextt,command=lambda: choose_name2(btntextt.get())) 
        stockkt.grid(row=1,column=0,padx=5,pady=5)
        
        btntextt2=tk.StringVar()
        btntextt2.set("測試2!!")
        stockkt2=tk.Button(win3,text=btntextt2.get(),textvariable=btntextt2,command=lambda: choose_name2(btntextt2.get())) 
        stockkt2.grid(row=1,column=1,padx=5,pady=5)
        
     
 
        win3.mainloop()



def choose_name2(quickPrint):
    global btntext_temp
    global ra2
    btntext_temp=quickPrint
    outputtt=str(btntext_temp)
    outputtt+=str(ra2)
    btntext_temp=quickPrint
    print(outputtt+"\n")

    df2 = pd.DataFrame()
    df2['F1']= ['aa1','bb1','cc1']                  #np.arange(0,10,1)
    df2['F2']= ['ff2','dd2','ee2']
    
    app2 = QtWidgets.QApplication([])
    table2 = QtWidgets.QTableView()
    mymodel2 = PandasModel(df2)
    table2.setModel(mymodel2)
    table2.show()
    app2.exec_()
    
    
#實作送出鍵
def check_send():
    global btntext_temp
    
    print("test"+ name_text.get()+"  "+stock_class.get())
    if(str(stock_class.get())!="類股"):
        df = pd.DataFrame()
        df['Field1']= ['aa','bb','cc']                  #np.arange(0,10,1)
        df['Field2']= ['ff','dd','ee']
        app = QtWidgets.QApplication([])
        table = QtWidgets.QTableView()
        mymodel = PandasModel(df)
        table.setModel(mymodel)
        table.show()
        app.exec_()
    else:
        win2=tk.Tk() 
        win2.geometry("1000x800")
        win2.title("project_stock")
        btntext=tk.StringVar()
        btntext.set("哭哭!!")
        stockk=tk.Button(win2,text=btntext.get(),textvariable=btntext,command=lambda: choose_name(btntext.get())) 
        stockk.pack()
        
        btntext2=tk.StringVar()
        btntext2.set("yaya!!")
        stockk2=tk.Button(win2,text=btntext2.get(),textvariable=btntext2,command=lambda: choose_name(btntext2.get())) 
        stockk2.pack()
        
        win2.mainloop()
        
        
        
    
        


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                if(index.column() != 0):
                    return str(self._data.values[index.row()][index.column()])
                else:
                    return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[section]
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return str(self._data.index[section])
        return None

    def flags(self, index):
        flags = super(self.__class__,self).flags(index)
        flags |= QtCore.Qt.ItemIsSelectable
        flags |= QtCore.Qt.ItemIsEnabled
        return flags


if __name__=='__main__':

    win=tk.Tk()
    win.geometry("1000x800")
    win.title("project")

    num_text=tk.StringVar()
    btntext=tk.StringVar()
    #輸入的值
    name_text=tk.StringVar()
    choice = tk.IntVar()
   
    
    stock_class_label=tk.Label(win,text="搜尋方式:",width=10)
    stock_class_label.grid(row=0,column=1,padx=5,pady=5)
    stock_class_value=tk.StringVar()
    stock_class=ttk.Combobox(win,width=20,textvariable=stock_class_value)
    stock_class['value']=("股票名稱","股票代碼","類股")
    stock_class.grid(row=0,column=2,padx=10,pady=5)
    stock_class.current(0)
    
    stock_name=tk.Label(win,text="輸入:",width=20)
    stock_name.grid(row=0,column=4,padx=5,pady=5)

    stock_name_text=tk.Entry(win,textvariable=name_text,width=20)
    stock_name_text.grid(row=0,column=5,padx=5,pady=5)

    stock_send=tk.Button(win,text="送出",width=20,command=check_send)
    stock_send.grid(row=0,column=6,padx=5,pady=5)
    


    radio1 = tk.Radiobutton(win, text="公司資料", variable=choice,value=1,command=sel)
    radio1.grid(row=1,column=3,padx=5,pady=5)

    radio2 = tk.Radiobutton(win, text="營收盈餘", variable=choice, value=2,command=sel)
    radio2.grid(row=1,column=4,padx=5,pady=5)

    radio3 = tk.Radiobutton(win, text="股利政策", variable=choice, value=3,command=sel)
    radio3.grid(row=1,column=5,padx=5,pady=5)

    radio4 = tk.Radiobutton(win, text="申報轉讓", variable=choice, value=4,command=sel)
    radio4.grid(row=1,column=6,padx=5,pady=5)
    
    output_area=tk.Label(win,text="輸出:",width=100,height=50, bg = "white")
    output_area.grid(row=2,column=2)
    output_area.grid(columnspan=5)
    
    win.mainloop()
    
    