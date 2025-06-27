import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import csv

# Main Prediction Window
def main_window():
    window2 = tk.Tk()
    window2.title("CARDIOVASCULAR DISEASE PREDICTION")
    window2.geometry("1800x950")

    # ICON
    path = ("icon_image.png")
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    window2.iconphoto(False, render)

    # IMAGE
    image = Image.open("w2.png").resize((1700, 820))
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(window2, image=image)
    image_label.pack()
    image_label.place(x=-100, y=-245)

    # FRAME
    heading_entry = tk.Frame(window2, width=1650, height=400, bg="#2ad2db")
    heading_entry.place(x=0, y=500)

    # ENTRY
    tk.Label(heading_entry, text="Patient_name :-", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=230, y=20)
    Patient_name = tk.StringVar()
    tk.Entry(window2, textvariable=Patient_name, width=15, font=("Bahnschrift Light", 25), bg="#2ad2db", fg="black", bd=10).place(x=400, y=500)

    tk.Label(heading_entry, text="Age :-", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=900, y=20)
    Age = tk.StringVar()
    tk.Entry(window2, textvariable=Age, width=15, font=("Bahnschrift Light", 25), bg="#2ad2db", fg="black", bd=10).place(x=980, y=500)

    # RADIO BUTTONS
    gender_var = tk.StringVar(value="Male")
    tk.Label(heading_entry, text="Gender", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=270, y=105)
    tk.Radiobutton(window2, text="Male", variable=gender_var, value="Male").place(x=250, y=640)
    tk.Radiobutton(window2, text="Female", variable=gender_var, value="Female").place(x=300, y=640)

    smoke_var = tk.StringVar(value="no")
    tk.Label(heading_entry, text="Smoke", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=585, y=105)
    tk.Radiobutton(window2, text="yes", variable=smoke_var, value="yes").place(x=580, y=640)
    tk.Radiobutton(window2, text="no", variable=smoke_var, value="no").place(x=620, y=640)

    physical_activity_var = tk.StringVar(value="yes")
    tk.Label(heading_entry, text="Physical_activity", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=850, y=105)
    tk.Radiobutton(window2, text="yes", variable=physical_activity_var, value="yes").place(x=880, y=640)
    tk.Radiobutton(window2, text="no", variable=physical_activity_var, value="no").place(x=920, y=640)

    alcohol_intake_var = tk.StringVar(value="no")
    tk.Label(heading_entry, text="Alcohol_intake", font=("Bahnschrift", 15), fg="black", bg="#2ad2db").place(x=1180, y=105)
    tk.Radiobutton(window2, text="yes", variable=alcohol_intake_var, value="yes").place(x=1200, y=640)
    tk.Radiobutton(window2, text="no", variable=alcohol_intake_var, value="no").place(x=1240, y=640)

    # PREDICTION BUTTON
    def predict():
        age = int(Age.get())
        patient_name = Patient_name.get()
        if age > 50:
            result = "High risk of cardiovascular disease"
        else:
            result = "Low risk of cardiovascular disease"
        messagebox.showinfo("Prediction Result", f"Patient: {patient_name}\nPrediction: {result}")

    tk.Button(window2, width=39, pady=7, text="PREDICT", bg="#28a4c9", fg="white", border=10, command=predict).place(x=650, y=700)

    # LOGOUT
    tk.Button(window2, text="LOGOUT", font=("Cooper", 12, "bold"), fg="black", bg="#2ad2db", border=10, width=10, relief="groove", command=window2.destroy).place(x=1400, y=30)

    window2.mainloop()
