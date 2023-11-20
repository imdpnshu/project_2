from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow, write in terminal pillow will be installed PIL(python imaging library)
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        # Variables
        self.var_dep=StringVar() #creating variable for the entry field
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        # 1st image
        img=Image.open(r"college_image\6.jpg")
        img=img.resize((540,140),Image.ANTIALIAS) #ANTIALIAS converts high level image to low level
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,command=self.open_img,image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=140)

         # 2nd image
        img_2=Image.open(r"college_image\5.jpeg")
        img_2=img_2.resize((540,140),Image.ANTIALIAS) #ANTIALIAS converts high level image to low level
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,command=self.open_img_2,image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=140)

         # 3rd image
        img_3=Image.open(r"college_image\7.jpg")
        img_3=img_3.resize((540,140),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,command=self.open_img_3,image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=1000,y=0,width=540,height=140)

        #bg image

        img_4=Image.open(r"college_image\8.jpeg")
        img_4=img_4.resize((1530,600),Image.ANTIALIAS) 
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lb1=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lb1.place(x=0,y=140,width=1530,height=600)


        lb1_title=Label(bg_lb1,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",30,"bold"),fg="blue",bg="white")
        lb1_title.place(x=0,y=0,width=1530,height=32)
        
        
        # manage frame
        Manage_frame=Frame(bg_lb1, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=2, y=35, width=1360, height=525)

        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=2,y=2,width=660,height=510)

        #img
        img_5=Image.open(r"college_image\3.jpg")
        img_5=img_5.resize((650,120),Image.ANTIALIAS) 
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

        #Current course label frame information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=105)

        # Labels and Combobox
        # Department
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",11,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2, sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",10,"bold"),width=25,state="readonly" )
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=15,pady=5,sticky=W)

        # Course
        course_std=Label(std_lbl_info_frame, font=("arial", 11, "bold"),text="Courses",bg="white")
        course_std.grid(row=0,column=2,sticky=W, padx=2,pady=5)

        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course, state="readonly",font=("arial", 10,"bold"), width=25)
        com_txtcourse_std['value']=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, sticky=W, padx=15,pady=5)


        #year
        currunt_year=Label(std_lbl_info_frame, font=("arial",11,"bold"),text="Year:",bg="white")
        currunt_year.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        com_txt_currunt_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,state="readonly",
                                                        font=("arial",10,"bold"),width=25)
        com_txt_currunt_year['value']=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txt_currunt_year.current(0)
        com_txt_currunt_year.grid(row=1,column=1,sticky=W,padx=15)

        #semster
        label_Semester=Label(std_lbl_info_frame,font=("arial",11,"bold"), text="Semester",bg="white")
        label_Semester.grid(row=1,column=2,sticky=W,padx=2, pady=10)
        comSemester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester, state="readonly",
                                                        font=("arial",10,"bold"),width=25)
        comSemester['value']=("Select Semester","Semester-1","Semester-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=15,pady=10)
        
        # Student class label frame information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class_frame.place(x=0,y=225,width=650,height=150)

        #labels entry
        #ID
        lbl_id=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="StudentID:",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2, pady=1)

        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("arial",9,"bold"),width=28)
        id_entry.grid(row=0,column=1,sticky=W,padx=10, pady=1)

        # Name
        lbl_Name=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Student Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=0, pady=1)

        txt_Name=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name, width=28,font=("arial",9,"bold"))
        txt_Name.grid(row=0,column=3,sticky=W,padx=10, pady=1)
       
        #Division
        lbl_div=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2, pady=1)
       
        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div, state="readonly",
                                                        font=("arial",9,"bold"),width=15)
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1, column=1, sticky=W, padx=10,pady=1)
       
        # Roll
        lbl_roll=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Roll No:",bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2, pady=1)
       
        txt_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,width=28,font=("arial",9,"bold"))
        txt_roll.grid(row=1,column=3,padx=2,pady=1)
       
        # Gender
        lbl_gender=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2, pady=1)
       
        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,state="readonly",
                                                        font=("arial",9,"bold"),width=15)
        com_txt_div['value']=("Select Gender","Male","Female","Other")
        com_txt_div.current(0)
        com_txt_div.grid(row=2, column=1, sticky=W, padx=10,pady=1)
       
        #DOB
        lbl_dob=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2, pady=1)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob, width=28,font=("arial",9,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=1)

        # Email
        lbl_email=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Email:",bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2, pady=1)

        txt_email=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email, width=28,font=("arial",9,"bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=1)
        
        # Phone
        lbl_phone=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Phone:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2, pady=1)

        txt_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone, width=28,font=("arial",9,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=1)
        
        # Address
        lbl_address=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Address:",bg="white")
        lbl_address.grid(row=4,column=0,sticky=W,padx=2, pady=1)

        txt_address=ttk.Entry(std_lbl_class_frame, textvariable=self.var_address,width=28,font=("arial",9,"bold"))
        txt_address.grid(row=4,column=1,padx=2,pady=1)

        # Teacher
        lbl_teacher=Label(std_lbl_class_frame,font=("arial",10,"bold"), text="Teacher:",bg="white")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2, pady=1)

        txt_teacher=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher, width=28,font=("arial",9,"bold"))
        txt_teacher.grid(row=4,column=3,padx=2,pady=1)
        
        # Button Form
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0, y=380, width=650,height=38)
        
        btn_Add=Button(btn_frame, text="Save", command=self.add_data,font=("arial",11,"bold"), width=17, bg="blue", fg="white")
        btn_Add.grid(row=0, column=0, padx=1)
        
        btn_update=Button(btn_frame, text="Update",command=self.update_data, font=("arial",11,"bold"), width=17, bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete=Button(btn_frame,command=self.delete_data, text="Delete", font=("arial",11,"bold"), width=17, bg="blue", fg="white")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset=Button(btn_frame,command=self.reset_data,text="Reset", font=("arial",11,"bold"), width=17, bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=1)


        #Right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Details",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataRightFrame.place(x=670,y=2,width=685,height=510)

        #img1
        img_6=Image.open(r"college_image\6th.jpg")
        img_6=img_6.resize((675,200),Image.ANTIALIAS) 
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img=Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=675,height=200)

        #Right frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",11,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=200,width=675,height=60)

        search_by=Label(Search_Frame,font=("arial",10,"bold"), text="Search By:",fg="white",bg="black")
        search_by.grid(row=0,column=0,sticky=W,padx=2, pady=1)

        # search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,state="readonly",
                                                        font=("arial",9,"bold"),width=15)
        com_txt_search['value']=("Select Option","Roll","Phone","student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search, width=28,font=("arial",9,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(Search_Frame, command=self.search_data, text="Search", font=("arial",11,"bold"), width=11, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=5)

        btn_ShowAll=Button(Search_Frame,command=self.fetch_data, text="Show All", font=("arial",11,"bold"), width=11, bg="blue", fg="white")
        btn_ShowAll.grid(row=0, column=4, padx=5)

        #=================== STUDENT TABLE AND SCROLL BAR ===================
        table_frame=Frame(DataRightFrame, bd=4,relief=RIDGE)
        table_frame.place(x=0, y=260,width=675, height=220)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem", "id","name","div","roll","gender","dob","email","phone","address","teacher"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")

        self.student_table["show"]="headings" # remove the default first blank column, and tables start with department it self

        self.student_table.column("dep", width=100) # manage the width of each column
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="cumberSOME@123", database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get()

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # fetch Function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="cumberSOME@123", database="mydata")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])

    def update_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("Update", "Are you sure to update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="cumberSOME@123", database="mydata")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(

                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_std_id.get()

                                                                                                                                                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student  sucessfully update", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_std_id.get()=="":
             messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to delete this student")
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="cumberSOME@123", database="mydata")
                    my_cursur=conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Your Student data has been Deleted", parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

# reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        

    # search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="cumberSOME@123", database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+ "%'")
                data=my_cursur.fetchall()

                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END,values=i)

                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)



    # open image
    def open_img(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Images", filetypes=(("JPG File","*.jpg"),("JPEG File","*.jpeg"),("PNG File","*.png"),("All Files","*.*")))  # getcwd - current working directory
        img=Image.open(fln)
        img_browse=img.resize((540,140),Image.ANTIALIAS) #ANTIALIAS converts high level image to low level
        self.photoimg_browse=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)


    # open image
    def open_img_2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Images", filetypes=(("JPG File","*.jpg"),("JPEG File","*.jpeg"),("PNG File","*.png"),("All Files","*.*")))  # getcwd - current working directory
        img_1=Image.open(fln)
        img_browse_1=img_1.resize((540,140),Image.ANTIALIAS) #ANTIALIAS converts high level image to low level
        self.photoimg_browse_1=ImageTk.PhotoImage(img_browse_1)
        self.btn_2.config(image=self.photoimg_browse_1)


   # open image
    def open_img_3(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Images", filetypes=(("JPG File","*.jpg"),("JPEG File","*.jpeg"),("PNG File","*.png"),("All Files","*.*")))  # getcwd - current working directory
        img_2=Image.open(fln)
        img_browse_2=img_2.resize((540,140),Image.ANTIALIAS) #ANTIALIAS converts high level image to low level
        self.photoimg_browse_2=ImageTk.PhotoImage(img_browse_2)
        self.btn_3.config(image=self.photoimg_browse_2)












if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()