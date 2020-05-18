from tkinter import *

window = Tk()

def convert_kg_to_gm(value):
    if type(value) == float:
        return value * 1000.0
    else:
        return float(value) * 1000.0

def convert_kg_to_lb(value):
    if type(value) == float:
        return value * 2.20462
    else:
        return float(value) * 2.20462

def convert_kg_to_oz(value):
    if type(value) == float:
        return value * 35.2739199982575
    else:
        return float(value) * 35.2739199982575


def convert_units():
    input_value = float(ent_field_value.get())

    txt_grams.delete("1.0", END)
    txt_grams.insert(END, str(convert_kg_to_gm(input_value)))
    txt_pounds.delete("1.0", END)
    txt_pounds.insert(END, str(convert_kg_to_lb(input_value)))
    txt_ounces.delete("1.0", END)
    txt_ounces.insert(END, str(convert_kg_to_oz(input_value)))


ent_field_value = StringVar()
ent_field = Entry(window, textvariable = ent_field_value)
ent_field.grid(row = 0, column = 0)

lbl_unit = Label(window, text = "Kg")
lbl_unit.grid(row = 0, column = 1)

btn_convert = Button(window, text="Convert", command = convert_units)
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