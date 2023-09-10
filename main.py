#!/usr/bin/python3 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
import customtkinter
THEME = "DARK"
customtkinter.set_appearance_mode(THEME)  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

global PriceList
PriceList = []

class App(tk.Frame):
    global f
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        global TaxPerDollar
        TaxPerDollar = tk.IntVar()
        global Price
        Price = tk.IntVar()
#	LEFT FRAME 1
        leftframe = customtkinter.CTkFrame(
        root
        )
        leftframe.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        

        Label = customtkinter.CTkLabel(leftframe, text="\nSales Tax Per Dollar")
        Label.pack()
        self.TaxPerDollarIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0.000")
        self.TaxPerDollarIPT.pack()
        self.TaxPerDollar = tk.IntVar()
        self.TaxPerDollar.set("0")
        self.TaxPerDollarIPT["textvariable"] = self.TaxPerDollar
        
        Label = customtkinter.CTkLabel(leftframe, text="\nPrice")
        Label.pack()
        self.PriceIPT = customtkinter.CTkEntry(leftframe, placeholder_text="$0")
        self.PriceIPT.pack()
        self.Price = tk.IntVar()
        self.Price.set("0")
        self.PriceIPT["textvariable"] = self.Price  
        Label = customtkinter.CTkLabel(leftframe, text="")
        Label.pack()
        AddItemButton = customtkinter.CTkButton(
        leftframe,
        text = 'Add Item',
        command = self.AddItem
        ).pack() 
        Label = customtkinter.CTkLabel(leftframe, text="")
        Label.pack()       
        CalcButton = customtkinter.CTkButton(
        leftframe,
        text = 'Calculate Total',
        command = self.Calc
        ).pack() 
        Label = customtkinter.CTkLabel(leftframe, text="")
        Label.pack()               
        ClearButton = customtkinter.CTkButton(
        leftframe,
        text = 'Clear List',
        command = self.Clear
        ).pack()
#	LEFT FRAME 2
        leftframe2 = customtkinter.CTkFrame(
        root
        )
        leftframe2.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        Label = customtkinter.CTkLabel(leftframe2, text="Items")
        Label.pack()
        global ItemsBox 
        ItemsBox = customtkinter.CTkTextbox(
        leftframe2,
        state='disabled'
        )
        ItemsBox.pack(fill = BOTH)
        
        Label = customtkinter.CTkLabel(leftframe2, text="Total")
        Label.pack()        
        global Totals 
        Totals = customtkinter.CTkTextbox(
        leftframe2,
        state='disabled'
        )
        Totals.pack(fill = BOTH)
#	MISC SCRIPTS
    def AddItem(self):
        Price = float(self.PriceIPT.get())
        PriceList.append(Price)
        self.Price.set("0")
        ItemsBox.configure(state='normal')
        ItemsBox.insert(END, f'{PriceList[-1]}\n')
        ItemsBox.configure(state='disabled') 
        
    def Clear(self):
        ItemsBox.configure(state='normal')
        ItemsBox.delete(1.0, END)
        ItemsBox.configure(state='disabled')  
        PriceList.clear()
        SubTotal = 0  
        Total = 0   
        Totals.configure(state='normal')
        Totals.delete(1.0, END)
        Totals.configure(state='disabled')    
    def Calc(self):
        TaxPerDollar = float(self.TaxPerDollarIPT.get())
        SubTotal = 0
        SubTotal = sum(PriceList)   
        Total = 0

        TaxPerDollar += 1
        Total = round(float(SubTotal) * float(TaxPerDollar), 2)
            
        Totals.configure(state='normal')
        Totals.delete(1.0, END)
        Totals.insert(END, f'SubTotal: {round(SubTotal, 2)}\n Total: {Total}\n')
        Totals.configure(state='disabled')       
                           
title = "Sales Tax Calculator"
root = customtkinter.CTk(className="STC")
root.geometry("900x500")
root.resizable(True,True)
myapp = App(root)
myapp.master.title(title)
myapp.mainloop()
