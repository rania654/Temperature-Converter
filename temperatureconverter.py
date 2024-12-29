from tkinter import *
import tkinter as tk
from tkinter.ttk import *
root = Tk()

root.geometry("500x500")
root.title("Temperature Converter")

def conversion():
    celsius = celsiusbox.get()
    farenheit =(float(celsius)*9/5)+32
    answerlabel.config(text = "Temperature in Farenheit : "+str(farenheit))

head = Label(root, text = "Temperature Converter From Celsius To Farenhrit")
head.pack()

frame = Frame(root)
frame.pack()
label1= Label(frame, text = "Enter the temperature in celsius :")
label1.grid(row = 1, column = 0)

celsiusbox = Entry(frame, width = 10)
celsiusbox.grid(row = 1, column = 1, pady = 10)

answerlabel = Label(frame)
answerlabel.grid(row = 3, column = 0, columnspan = 2, pady = 10)

convert = Button(frame, text = "Convert", width = 30, command = conversion)
convert.grid(row = 4, column = 1, columnspan = 2, pady = 10)





root.mainloop()