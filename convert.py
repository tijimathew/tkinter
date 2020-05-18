from tkinter import *

window = Tk()

ent_value = Entry(window)
ent_value.grid(row = 0, column = 0)

lbl_unit = Label(window, text = "Kg")
lbl_unit.grid(row = 0, column = 1)

btn_convert = Button(window, text="Convert")
btn_convert.grid(row = 0, column = 2)

txt_grams = Text(window, height = 1, width = 20)
txt_grams.grid(row = 1, column = 0)

txt_pounds = Text(window, height = 1, width = 20)
txt_pounds.grid(row = 1, column = 1)

txt_ounces = Text(window, height = 1, width = 20)
txt_ounces.grid(row = 1, column = 2)

lbl_grams = Label(window, text = "gm")
lbl_grams.grid(row = 2, column = 0)

lbl_pounds = Label(window, text = "lb")
lbl_pounds.grid(row = 2, column = 1)

lbl_ounces = Label(window, text = "oz")
lbl_ounces.grid(row = 2, column = 2)

window.mainloop() 