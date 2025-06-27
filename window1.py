def fxn1():

    import tkinter as tk
    from tkinter import PhotoImage
    from tkinter import *
    from tkinter import messagebox
    import requests
    from PIL import ImageTk,Image
    window=Tk()
    window.title("CARDIOVASCULAR   DISEASE  PREDICTION")
    window.geometry("1800x950")
    window.configure(bg="#2ad2db")
  # window.resizable(0,0)

 #ICON 
    path =("icon_image.png")
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    window.iconphoto(False,render)

 #=IMAGE 
    image=Image.open("w2.png").resize((1700,820))
    image = ImageTk.PhotoImage(image)
    image_label=tk.Label(window,image=image)               
    image_label.pack()
    image_label.place(x=-100,y=-245)

 # FRAME
    heading_entry=Frame(window,width=1650,height=400,bg="#2ad2db")
    heading_entry.place(x=0,y=500)

 #ENTRY
    Label(heading_entry,text="Patient_name :-",font=("Bahnschrift",15),fg="black",bg="#2ad2db").place(x=230,y=20)
    Patient_name=StringVar()
    Patient_name=Entry(window,textvariable=Patient_name,width=15,font=("Bahnschrift Light",25),bg="#2ad2db",fg="black",bd=10)
    Patient_name.place(x=400,y=500)
    Label(heading_entry,text="Age :-",font=("Bahnschrift",15),fg="black",bg="#2ad2db").place(x=900,y=20)
    Age=StringVar()
    Age=Entry(window,textvariable=Age,width=15,font=("Bahnschrift Light",25),bg="#2ad2db",fg="black",bd=10)
    Age.place(x=980,y=500)

 #RADIO BUTTON1
    Label(heading_entry,text="Gender",font=("Bahnschrift",15),fg="black",bg="#2ad2db").place(x=270,y=105)
    gender_var = tk.StringVar()
    def show_selected_gender():
    selected_gender = gender_var.get()
    print(f"Selected Gender: {selected_gender}")
    radio_male = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male", command=show_selected_gender)
    radio_female = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female", command=show_selected_gender)
    gender_var.set("Male")
    radio_male.pack(pady=5)
    radio_female.pack(pady=5)
    radio_female.place(x=300,y=640)
    radio_male.place(x=250,y=640)

 #RADIO BUTTON2
    Label(heading_entry,text="Smoke",font=("Bahnschrift",15),fg="black",bg="#2ad2db").place(x=585,y=105)
    smoke_var = tk.StringVar()
    def show_selected_smoke():
    selected_smoke = smoke_var.get()
    print(f"Selected smoke: {selected_smoke}")
    radio_yes = tk.Radiobutton(window, text="yes", variable=smoke_var, value="yes", command=show_selected_smoke)
    radio_no = tk.Radiobutton(window, text="no", variable=smoke_var, value="no", command=show_selected_smoke)
    smoke_var.set("no")
    radio_yes.pack()
    radio_no.pack()
    radio_yes.place(x=580,y=640)
    radio_no.place(x=620,y=640)

 #RADIO BUTTON3
    Label(heading_entry,text="Physical_activity",font=("Bahnschrift",15),fg="black",bg="#2ad2db").place(x=850,y=105)
    physical_activity_var = tk.StringVar()
    def show_selected_physical_activity():
    selected_physical_activity = physical_activity_var.get()
    print(f"Selected Physical_activity: {selected_physical_activity}")
    radio_yes = tk.Radiobutton(window, text="yes", variable=physical_activity_var, value="yes", command=show_selected_physical_activity)
    radio_no = tk.Radiobutton(window, text="no", variable=physical_activity_var, value="no", command=show_selected_physical_activity)
    physical_activity_var.set("yes")
    radio_yes.pack()
    radio_no.pack()
    radio_yes.place(x=880,y=640)
    radio_no.place(x=920,y=640)

 #RADIO BUTTON4
    Label(heading_entry,text="Alcohol_intake",font=("Bahnschrift",15),fg="black",bg="#2ad2db").place(x=1180,y=105)
    alcohol_intake_var = tk.StringVar()
    def show_selected_alcohol_intake():
    selected_alcohol_intake = alcohol_intake_var.get()
    print(f"Selected Alcohol_intake: {selected_alcohol_intake}")
    radio_yes = tk.Radiobutton(window, text="yes", variable=alcohol_intake_var, value="yes", command=show_selected_alcohol_intake)
    radio_no = tk.Radiobutton(window, text="no", variable=alcohol_intake_var, value="no", command=show_selected_alcohol_intake)
    physical_activity_var.set("yes")
    radio_yes.pack()
    radio_no.pack()
    radio_yes.place(x=1200,y=640)
    radio_no.place(x=1240,y=640)

 #PREDICTION BUTTON
    Button(window,width=39,pady=7,text="PREDICT",bg="#28a4c9",fg="white",border=10).place(x=650,y=700)

 #LOGOUT 
    new_win = tk.Button(window,text="LOGOUT",font=("Cooper",12,"bold"),fg="black",bg="#2ad2db",border=10,width=10,relief="groove")
    new_win.place(x=1400,y=30)
    window.mainloop()

#57a1f8
#28a4c9