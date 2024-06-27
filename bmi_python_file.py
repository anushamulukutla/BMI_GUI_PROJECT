import csv
import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def BMI_cal(weight, height):
    h = height * height
    return weight/h

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 24.9:
        return "Normal weight"
    if bmi < 29.9:
        return "Overweight"
    return "Obesity"

def user_details():
    name = nameentry.get()
    age =  agespinbox.get()
    weight = weightentry.get()
    height = heightentry.get()
    if not name or not age or not weight or not height:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return None
    try:
        age = int(age)
        weight = float(weight)
        height = float(height)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid numerical values for age, weight, and height")
        return None
    bmi = BMI_cal(weight, height)
    category = bmi_category(bmi)
    return name, age, weight, height, bmi, category

def write_csv_file(Bmdata):
    data = user_details()
    with open("bmidata.csv", "a") as bmicsv:
        writer = csv.writer(bmicsv)
        writer.writerow(data)

def save_data():
    user_data = user_details()
    if user_data:
        write_csv_file(user_data)
        messagebox.showinfo("Data Saved", "Your data has been saved successfully!")
        clear_entries()

def clear_entries():
    nameentry.delete(0, tkinter.END)
    agespinbox.delete(0, tkinter.END)
    weightentry.delete(0, tkinter.END)
    heightentry.delete(0, tkinter.END)

def get_list_of_category():
    bmi_cat = []
    with open("bmidata.csv",'r') as rdcsv:
        readlines = rdcsv.readlines()
        for line in readlines:
            newline = line.split(",")
            category_bmi = newline[-1]
            bmi_cat.append(category_bmi.strip())
    return bmi_cat

def show_graph_pie():
    listcount = []
    listcat = []
    bmi_cat_list = get_list_of_category()
    dict_bmi_cat = {"Underweight": 0, "Normal weight": 0, "Overweight": 0, "Obesity": 0}
    for item in bmi_cat_list:
        if item in dict_bmi_cat:
            dict_bmi_cat[item] += 1
    for cat, cnt in dict_bmi_cat.items():
        listcount.append(cnt)
        listcat.append(cat)
#to display the code in the same GUI Window
    figure = Figure(figsize=(6, 6), dpi=100)
    ax = figure.add_subplot(111)
    ax.pie(listcount, labels=listcat, autopct='%1.1f%%')
    ax.set_title("BMI CATEGORY!!!")

    canvas = FigureCanvasTkAgg(figure, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main window
window = tkinter.Tk()
window.title("BMI CALCULATION FORM")
frame = tkinter.Frame(window)

bmicalframe = tkinter.LabelFrame(window, text="USERINFO_TO_CAL_BMI")
bmicalframe.grid(row=0, column=0, padx=10, pady=10)

graph_frame = tkinter.LabelFrame(window, text="BMI CATEGORY GRAPH")
graph_frame.grid(row=0, column=1, padx=10, pady=10)

namelabel = tkinter.Label(bmicalframe, text="Name")
namelabel.grid(row=0, column=0)
nameentry = tkinter.Entry(bmicalframe)
nameentry.grid(row=0, column=1)

heightlabel = tkinter.Label(bmicalframe, text="Height(M)")
heightlabel.grid(row=2, column=0)
heightentry = tkinter.Entry(bmicalframe)
heightentry.grid(row=2, column=1)

weightlabel = tkinter.Label(bmicalframe, text="Weight(KG)")
weightlabel.grid(row=3, column=0, pady=10)
weightentry = tkinter.Entry(bmicalframe)
weightentry.grid(row=3, column=1, pady=10)

agelabel = tkinter.Label(bmicalframe, text="Age")
agespinbox = tkinter.Spinbox(bmicalframe, from_=1, to=100)
agelabel.grid(row=1, column=0)
agespinbox.grid(row=1, column=1)

savebtn = tkinter.Button(bmicalframe, text='Save', command=save_data)
savebtn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

continu_btn = tkinter.Button(bmicalframe, text="Continue", command=clear_entries)
continu_btn.grid(row=4, column=2, columnspan=1, padx=10, pady=10)

show_graph = tkinter.Button(bmicalframe, text='Show Graph', command=show_graph_pie)
show_graph.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
