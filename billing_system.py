from tkinter import *
import sqlite3
import math,random,os
from tkinter import messagebox

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="Maroon")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="KD Billing Login",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='silver',fg='white',textvariable = user_name)
    uname.config(width=40)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='silver',fg='white',textvariable = password)
    pas.config(width=40)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c in logdata:
            if b == uname.get() and c == pas.get():
                login.destroy()
                root=Tk();
                obj=Bill_App(root);
                root.mainloop();
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "aqua", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="green")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="KD Billing SignUp",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='silver',fg='black',textvariable = fname)
    fname.config(width=40)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='silver',fg='black',textvariable = uname)
    user.config(width=40)
    user.place(relx=0.31,rely=0.5)    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='silver',fg='black',textvariable = passW)
    pas.config(width=40)
    pas.place(relx=0.31,rely=0.6)
    
    
    def addUserToDataBase():
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        
        conn = sqlite3.connect('user.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?)",(fullname,username,password)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
        #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('user.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
        
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase)
    sp.configure(width = 15,height=1, activebackground = "aqua", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white")
    log.configure(width = 16,height=1, activebackground = "aqua", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()
def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="kdp12.png")
    canvas.create_image(40,10,image=img,anchor=NW)
    
    button = Button(root, text='Start',command = signUpPage) 
    button.configure(width = 102,height=2, activebackground = "aqua", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()


        
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color="Black";
        fg_color="red"
        fg_c1="Light Green"
        title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

        #//////========== Cosmetics Variables================////////
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

        #//////========== Grocery Variables================//////// 
         
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #//////========== Cold Drinks Variables================////////
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.pepsi=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #//////========== Total Product Price and Tax Variables================////////
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        

        #//////==========Customer variables===============================/////////////
        
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        

        #//////////===============================Customer Details Frame==================================///////////

        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("Times New Roman",18,"bold"),bg=bg_color,fg="gold")
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg=fg_color,font=("Times New Roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_lbl=Label(F1,text="Phone No.",bg=bg_color,fg=fg_color,font=("Times New Roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg=fg_color,font=("Times New Roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=20,textvariable=self.bill_no,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font=("Arial 12 bold")).grid(row=0,column=6,padx=10,pady=10)

        #/////////////=============================Cosmetics  Frame========================================////////////

        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("Times New Roman",18,"bold"),bg=bg_color,fg="gold")
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="Face Wash",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl=Label(F2,text="Hair spray",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F2,text="Hair Gel",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        body_lbl=Label(F2,text="Body Lotion",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #/////////////=============================Grocery  Frame========================================////////////

        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("Times New Roman",18,"bold"),bg=bg_color,fg="gold")
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        g6_lbl=Label(F3,text="Tea",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #/////////////=============================Cold Drink Frame========================================////////////

        F4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,font=("Times New Roman",18,"bold"),bg=bg_color,fg="gold")
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Maza",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Cock",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Pepsi",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="Limca",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        c6_lbl=Label(F4,text="Sprite",font=("Times New Roman",16,"bold"),bg=bg_color,fg=fg_c1).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("Times New Roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #/////////////=============================Bill Area Frame========================================////////////

        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=330,height=380)

        bill_title=Label(F5,text="Bill Area",font=("Arial",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        
        #/////////////=============================Bill Menu Frame========================================////////////
        fg_6="aqua"

        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("Times New Roman",18,"bold"),bg=bg_color,fg="gold")
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Cosmetic Price",font=("Times New Roman",14,"bold"),bg=bg_color,fg=fg_6).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",font=("Times New Roman",14,"bold"),bg=bg_color,fg=fg_6).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks Price",font=("Times New Roman",14,"bold"),bg=bg_color,fg=fg_6).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",font=("Times New Roman",14,"bold"),bg=bg_color,fg=fg_6).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",font=("Times New Roman",14,"bold"),bg=bg_color,fg=fg_6).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold Drinks Tax",font=("Times New Roman",14,"bold"),bg=bg_color,fg=fg_6).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="black",fg="white",pady=15,bd=2,width=10,font=("arial",15,"bold")).grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="black",fg="white",pady=15,bd=2,width=10,font=("arial",15,"bold")).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="black",fg="white",pady=15,bd=2,width=10,font=("arial",15,"bold")).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="black",fg="white",pady=15,bd=2,width=10,font=("arial",15,"bold")).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
    def total(self):
        
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+    
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p=self.rice.get()*80
        self.g_f_p=self.food_oil.get()*180   
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*20

        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p 
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_m_p=self.maza.get()*40
        self.d_c_p=self.cock.get()*30  
        self.d_f_p=self.frooti.get()*60
        self.d_p_p=self.pepsi.get()*70
        self.d_l_p=self.limca.get()*50
        self.d_s_p=self.sprite.get()*50

        self.total_cold_drink_price=float(
                                    self.d_m_p+
                                    self.d_c_p+  
                                    self.d_f_p+
                                    self.d_p_p+
                                    self.d_l_p+
                                    self.d_s_p
                                  )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.total_bill=float( self.total_cosmetic_price+
                               self.total_grocery_price+
                               self.total_cold_drink_price+
                               self.c_tax+
                               self.g_tax+
                               self.d_tax
                             )  
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t welcome to store \n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,"\n====================================")
        self.txtarea.insert(END,"\nProduct\t\tQty\t   Price")
        self.txtarea.insert(END,"\n====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details must be Entered ")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product purchased")
        else:
            self.welcome_bill()

            #========cosmetics============//
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t   {self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t   {self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t   {self.c_fw_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\nHair Spary\t\t{self.spray.get()}\t   {self.c_hs_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\nHair Gel\t\t{self.gell.get()}\t   {self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\nBody Lotion\t\t{self.loshan.get()}\t   {self.c_bl_p}")

            #========grocery============//
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t   {self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\nFood Oil\t\t{self.food_oil.get()}\t   {self.g_f_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\nDaal\t\t{self.daal.get()}\t   {self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t   {self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSugar\t\t{self.sugar.get()}\t   {self.g_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea\t\t{self.tea.get()}\t   {self.g_t_p}")

            #========cold drinks============//
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\nMaza\t\t{self.maza.get()}\t   {self.d_m_p}")
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\nCocacola\t\t{self.cock.get()}\t   {self.d_c_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t   {self.d_f_p}")
            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\nPepsi\t\t{self.pepsi.get()}\t   {self.d_p_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\nLimca\t\t{self.limca.get()}\t   {self.d_l_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t   {self.d_s_p}")

            #============tax==============//
            self.txtarea.insert(END,"\n------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nCold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            self.txtarea.insert(END,"\n------------------------------------")
            self.txtarea.insert(END,f"\nTotal Bill : \t\t\tRs. {str(self.total_bill)}")
            self.txtarea.insert(END,"\n------------------------------------")
            self.save_bill()

            
    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill Number")
                
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear data")
        if op>0:
                #//////========== Cosmetics Variables================////////
                self.soap.set(0)
                self.face_cream.set(0)
                self.face_wash.set(0)
                self.spray.set(0)
                self.gell.set(0)
                self.loshan.set(0)

                #//////========== Grocery Variables================//////// 
                 
                self.rice.set(0)
                self.food_oil.set(0)
                self.daal.set(0)
                self.wheat.set(0)
                self.sugar.set(0)
                self.tea.set(0)

                #//////========== Cold Drinks Variables================////////
                self.maza.set(0)
                self.cock.set(0)
                self.frooti.set(0)
                self.pepsi.set(0)
                self.limca.set(0)
                self.sprite.set(0)

                #//////========== Total Praoduct Price and Tax Variables================////////
                self.cosmetic_price.set("")
                self.grocery_price.set("")
                self.cold_drink_price.set("")

                self.cosmetic_tax.set("")
                self.grocery_tax.set("")
                self.cold_drink_tax.set("")
                

                #//////==========Customer variables===============================/////////////
                
                self.c_name.set("")
                self.c_phone.set("")
                self.bill_no.set("")
                x=random.randint(1000,9999)
                self.bill_no.set(str(x))
                self.search_bill.set("")

                self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()
        
                
    
if __name__=='__main__':
    start()


