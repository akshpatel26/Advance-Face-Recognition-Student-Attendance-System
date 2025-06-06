from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #=================Variables=====================#
        self.var_dep=StringVar()
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
        
        #first img
        img=Image.open("D:/Advance-Face-Recognition-Student-Attendance-System-Project/images/a1.webp")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open("D:/Advance-Face-Recognition-Student-Attendance-System-Project/images/a2.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img2=Image.open("D:/Advance-Face-Recognition-Student-Attendance-System-Project/images/a1.webp")
        img2 = img2.resize((600, 130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)  
        
        # bg images
        img3=Image.open("C:/Users/Fenil Patel/OneDrive/Desktop/Multiple-Disease-Prediction-Webapp-main/Frontend/h.png")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        # Close button function
        def close_and_return():
            self.root.destroy()  # Close current window
            main_frame.deiconify()  # Show main window (unhide it)
        
        # Close button
        close_btn = Button(title_lbl, text="Close", font=("times new roman", 15, "bold"), bg="white", fg="Red", cursor="hand2", command=close_and_return)
        close_btn.place(x=1300, y=0, width=200, height=45) 
        
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left=Image.open("D:/Advance-Face-Recognition-Student-Attendance-System-Project/images/a1.webp")
        img_left = img_left.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=0,width=720,height=130)
        
        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=15,y=135,width=720,height=115)
        
        #Department
        dep_label=Label(current_course_frame,text='Department',font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="read only",width=17)
        dep_combo['value']=("Select Department","Computer","It","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(current_course_frame,text='Course',font=("time new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",12,"bold"),state="read only",width=17)
        course_combo['value']=("Select Course","SE","BE","TE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_course_frame,text='Year',font=("time new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",12,"bold"),state="read only",width=17)
        year_combo['value']=("Select year","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        semester_label=Label(current_course_frame,text='Sem',font=("time new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",12,"bold"),state="read only",width=17)
        semester_combo['value']=("Select Course","sem-1","sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
         # clas Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" Student Information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=15,y=260,width=720,height=400)
        
        #student id
        studentid_label=Label(class_student_frame,text='Student ID:',font=("time new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("time new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
         #student Name
        studentName_label=Label(class_student_frame,text='Student Name:',font=("time new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("time new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #class division
        class_div_label=Label(class_student_frame,text='Class Division:',font=("time new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("time new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("time new roman",12,"bold"),state="read only",width=18)
        div_combo['value']=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #roll no
        roll_no_label=Label(class_student_frame,text='Roll NO:',font=("time new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("time new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text='Gender:',font=("time new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("time new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("time new roman",12,"bold"),state="read only",width=18)
        gender_combo['value']=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(class_student_frame,text='DOB:',font=("time new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("time new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)
        
        #Email
        email_label=Label(class_student_frame,text='Email:',font=("time new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("time new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)
        
        #Phone No
        phone_label=Label(class_student_frame,text='Phone NO:',font=("time new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("time new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text='Address:',font=("time new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("time new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)
        
        #teacher Name
        teacher_label=Label(class_student_frame,text='Teacher Name:',font=("time new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("time new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0) 
                
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

        
        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=700,height=40)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("time new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("time new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("time new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("time new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=700,height=40)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=34,font=("time new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=34,font=("time new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)
        
        img_right=Image.open("D:/Advance-Face-Recognition-Student-Attendance-System-Project/images/a2.jpg")
        img_right= img_right.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=680,height=130)
        
        # ======================== Search System ====================== #
        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        Search_frame.place(x=10,y=135,width=680,height=70)
        
        search_label=Label(Search_frame,text='Search By:',font=("time new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        search_combo=ttk.Combobox(Search_frame,font=("time new roman",13,"bold"),state="read only",width=17)
        search_combo['value']=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        search_entry=ttk.Entry(Search_frame,width=12,font=("time new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)
        
        search_btn=Button(Search_frame,text="Save",width=11,font=("time new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        
        showAll_btn=Button(Search_frame,text="Show All",width=11,font=("time new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)
        
        # ============ table frame ============= #
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=680,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    #=========================Function decration ==========================#
        
         
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="AP_18!P",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
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
                                                                                                               self.var_teacher.get(), 
                                                                                                               self.var_radio1.get()   
                                                                                                            
                                                                                                             ))   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)                                                                                               
                                                                                                  
   #=================fetch data===========================#     
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AP_18!P",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                
            conn.commit()
        conn.close()    
                                                                                                     
    #======================get cursor=======================#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),    
        self.var_course.set(data[1]),                                                                                            
        self.var_year.set(data[2]),                                                                                                      
        self.var_semester.set(data[3]),                                                                                                           
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),             
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]), 
        self.var_radio1.set(data[14]) 
    
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root) 
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="AP_18!P",database="face_recognizer")
                    my_cursor=conn.cursor()
                
                # Fixed SQL query with correct column names matching your database.
                    my_cursor.execute("""Update student set 
                       Dep=%s,
                       course=%s,
                       Year=%s,
                       Semester=%s,
                       Name=%s,
                       Division=%s,
                       Roll=%s,
                       Gender=%s,
                       Dob=%s,
                       Email=%s,
                       Phone=%s,
                       Address=%s,
                       Teacher=%s,
                       PhotoSample=%s 
                       where `Student id`=%s""",(
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
                           self.var_radio1.get(),
                           self.var_std_id.get()
                       ))
                
                    conn.commit()
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    self.fetch_data()
                    conn.close()
                else:
                    return      
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    def delete_data(self):         
        if self.var_std_id.get()=="":             
            messagebox.showerror("Error", "Student ID is required", parent=self.root)         
        else:             
            try:                 
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?", parent=self.root)                 
                if delete>0:                     
                    conn=mysql.connector.connect(host="localhost",username="root",password="AP_18!P",database="face_recognizer")                     
                    my_cursor=conn.cursor()                     
                    sql="delete from student where `Student id`=%s" 
                    val=(self.var_std_id.get(),)                     
                    my_cursor.execute(sql,val)
                    
                    conn.commit()
                    messagebox.showinfo("Delete","Successfully deleted student")
                    self.fetch_data()
                    conn.close()
                else:
                    return                       
                                
            except Exception as es:                
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    # def search_data(self):
    #     if self.serchTxt_var.get()=="" or self.search_var.get()=="Select Option":
    #         messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
    #     else:
    #         try:
                
    #             conn=mysql.connector.connect(host="localhost",username="root",password="AP_18!P",database="face_recognizer")                     
    #             my_cursor=conn.cursor()
    #             my_cursor.execute('''select * from student where self.search_var.get() LIKE "%" + self.serchTxt_var.get())+ %''')
    #             rows=my_cursor.fetchall()         
    #             if len(rows)!=0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for i in rows:
    #                     self.student_table.insert("",END,values=i)
    #                 if rows==None:
    #                     messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                     conn.commit()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="AP_18!P",database="face_recognizer")                     
                my_cursor=conn.cursor()
                my_cursor.execute('''SELECT * FROM student''')
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                
                # Fixed SQL query with correct column names matching your database
                my_cursor.execute("""Update student set 
                    Dep=%s,
                    course=%s,
                    Year=%s,
                    Semester=%s,
                    Name=%s,
                    Division=%s,
                    Roll=%s,
                    Gender=%s,
                    Dob=%s,
                    Email=%s,
                    Phone=%s,
                    Address=%s,
                    Teacher=%s,
                    PhotoSample=%s 
                    where `Student id`=%s""",(
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
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
    
                # Face capture code
                face_classifier =cv2.CascadeClassifier( "haarcascade_frontalface_default.xml")

    
                def face_cropped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)
    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)
                       
    
             
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()       