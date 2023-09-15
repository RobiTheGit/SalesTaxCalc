#!/usr/bin/python3 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
import customtkinter
#	Set the theme for the window
THEME = "DARK"
customtkinter.set_appearance_mode(THEME)  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
#Create a Global List, PriceList
global PriceList
PriceList = []
'''
Main Tkinter Window Code
'''
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

#	Create TaxPerDollar Variable
        global TaxPerDollar
        TaxPerDollar = tk.IntVar()

#	Create Price Variable
        global Price
        Price = tk.IntVar()

#	LEFT FRAME 1
        leftframe = customtkinter.CTkFrame(root)
        leftframe.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)

#	Sales Tax Input
        Label = customtkinter.CTkLabel(leftframe, text="\nSales Tax Per Dollar")
        Label.pack()
        self.TaxPerDollarIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0.000")
        self.TaxPerDollarIPT.pack()
        self.TaxPerDollar = tk.IntVar()
        self.TaxPerDollar.set("0")
        self.TaxPerDollarIPT["textvariable"] = self.TaxPerDollar

#	Item Price Input         
        Label = customtkinter.CTkLabel(leftframe, text="\nPrice")
        Label.pack()
        self.PriceIPT = customtkinter.CTkEntry(leftframe, placeholder_text="$0")
        self.PriceIPT.pack()
        self.Price = tk.IntVar()
        self.Price.set("0")
        self.PriceIPT["textvariable"] = self.Price  

#	Buttons

#	Filler
        Label = customtkinter.CTkLabel(leftframe, text="")
        Label.pack()
#	Add Item To Total
        AddItemButton = customtkinter.CTkButton(
        leftframe,
        text = 'Add Item',
        command = self.AddItem
        ).pack() 

#	Filler
        Label = customtkinter.CTkLabel(leftframe, text="")
        Label.pack()       

#	Calculate Full Total With Tax
        CalcButton = customtkinter.CTkButton(
        leftframe,
        text = 'Calculate Total',
        command = self.Calc
        ).pack() 

#	Filler
        Label = customtkinter.CTkLabel(leftframe, text="")
        Label.pack()               

#	Clear All Items In The List
        ClearButton = customtkinter.CTkButton(
        leftframe,
        text = 'Clear List',
        command = self.Clear
        ).pack()

#	LEFT FRAME 2
        leftframe2 = customtkinter.CTkFrame(root)
        leftframe2.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)

#	Items List That Shows The Prices
        Label = customtkinter.CTkLabel(leftframe2, text="Items")
        Label.pack()
        global ItemsBox 
        ItemsBox = customtkinter.CTkTextbox(
        leftframe2,
        state='disabled'
        )
        ItemsBox.pack(fill = BOTH)

#	Output Box For The Total Price and the Subtotal        
        Label = customtkinter.CTkLabel(leftframe2, text="Total")
        Label.pack()        
        global Totals 
        Totals = customtkinter.CTkTextbox(
        leftframe2,
        state='disabled'
        )
        Totals.pack(fill = BOTH)

#	MISC SCRIPTS

#	Add Items Code
    def AddItem(self):
#	Get the price of the item from the input
        Price = float(self.PriceIPT.get())
#	Append this value to PriceList 
        PriceList.append(Price)
#	Enable writing to the items list 
        ItemsBox.configure(state='normal')
#	Put the price in at the end of it
        ItemsBox.insert(END, f'{PriceList[-1]}\n')
#	Disable writing to the items list
        ItemsBox.configure(state='disabled') 

#	Clear PriceList and On-Screen List Code      
    def Clear(self):
#	Enable writing to the items list 
        ItemsBox.configure(state='normal')
#	Clear the items list
        ItemsBox.delete(1.0, END)
#	Disable writing to the items list
        ItemsBox.configure(state='disabled')  
#	Clear PriceList
        PriceList.clear()
#	Clear the SubTotal Variable
        SubTotal = 0  
#	Clear the Total Variable
        Total = 0   
#	Enable writing into the totals box
        Totals.configure(state='normal')
#	Clear the totals box
        Totals.delete(1.0, END)
#	Disable writing into the totals box
        Totals.configure(state='disabled')    

#	Total Price Calculation Code
    def Calc(self):
#	Get the tax percentage from the input
        TaxPerDollar = float(self.TaxPerDollarIPT.get())
#	Clear SubTotal 
        SubTotal = 0
#	Set the Subtotal to the sum of all of the items in the price list
        SubTotal = sum(PriceList)   
#	Clear Total
        Total = 0
#	Add 1 to the Tax per dollar to make the math easier
        TaxPerDollar += 1
#	Multiply the Subtotal by the sales tax
        Total = round(float(SubTotal) * float(TaxPerDollar), 2)
#	Enable writing into the output
        Totals.configure(state='normal')
#	Clear the output
        Totals.delete(1.0, END)
#	Write the Subtotal and Total price into the output
        Totals.insert(END, f'Items: {len(PriceList)}\n Subtotal: {round(SubTotal, 2)}\n Total: {Total}\n')
#	Disable writing into the output  
        Totals.configure(state='disabled')       
'''
Tkinter Setup Code
'''
title = "Sales Tax Calculator"
root = customtkinter.CTk(className="STC")
root.geometry("900x500")
root.resizable(True,True)
myapp = App(root)
myapp.master.title(title)
myapp.mainloop()
