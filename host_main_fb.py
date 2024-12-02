from tkinter import *

#вибір варіанта додатку

root1 = Tk()
root1.title("Feedback")
root1.geometry("300x400")
root1.resizable(width=False,height=False)
root1['bg']="#3C3C3C"

Lab1=Label(text="Оберіть свій варіант",font="Vernada 15",bg="#3C3C3C",fg="white")
Lab1.place(x=50,y=30)

Butt2=Button(width=20,text="я клієнт",font="Vernada 15",bg="#282828",fg="white",relief=FLAT,overrelief=GROOVE)
Butt2.place(x=35,y=200)

Butt1=Button(width=20,text="я надаю послуги",font="Vernada 15",bg="#282828",fg="white",relief=FLAT,overrelief=GROOVE)
Butt1.place(x=35,y=250)

Butt3=Button(width=20,text="я робітник",font="Vernada 15",bg="#282828",fg="white",relief=FLAT,overrelief=GROOVE)
Butt3.place(x=35,y=300)

#Регістрація "я надаю послуги"

def reg1():
    root2 = Tk()
    root2.title("Registration feedback")
    root2.geometry("500x500") 
    root2.resizable(width=False,height=False)
    root2['bg'] = "#3C3C3C"

    l1=Label(root2,text="Вітаємо в додатку!", font="Vernada 17" , fg="white")
    l1.place(x=145,y=7)
    l1['bg']="#3C3C3C"

    l2=Label(root2,text="Для того щоб продовжити необхідно зареєструватись.", font="Vernada 13" , fg="white")
    l2.place(x=35,y=40)
    l2['bg']="#3C3C3C"

    l3=Label(root2,text="Ключ доступу" , font="Vernada 15" , fg="white")
    l3.place(x=175,y=70)
    l3['bg']="#3C3C3C"
    
    
    e1=Entry(root2,width=53,font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
    e1.place(x=8,y=105)
    e1.insert(0,"")
    e1['bg']= "white"
    e1.get()

    l4=Label(root2,text="Ваш email" , font="Vernada 15" , fg="white")
    l4.place(x=190,y=135)
    l4['bg']="#3C3C3C"

    e2=Entry(root2,width=53 , font="Vernada 13",justify=RIGHT,foreground="#3C3C3C")
    e2.place(x=8,y=170)
    e2.insert(0,"@gmail  ")
    e2['bg']= "white"
    e2.get()

    l4=Label(root2,text="Ваше П.І.Б." , font="Vernada 15" , fg="white")
    l4.place(x=187,y=200)
    l4['bg']="#3C3C3C"

    e3=Entry(root2,width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
    e3.place(x=8,y=235)
    e3.insert(0,"")
    e3['bg']= "white"
    e3.get()
    
    l5=Label(root2,text="Назва компанії" , font="Vernada 15" , fg="white")
    l5.place(x=173,y=270)
    l5['bg']="#3C3C3C"

    e4=Entry(root2,width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
    e4.place(x=8,y=305)
    e4.insert(0,"")
    e4['bg']= "white"
    e4.get()

    b1 =Button(root2,text="готово", font="Vernada 15" ,foreground="white",relief=FLAT,overrelief=GROOVE)
    b1['bg']="#282828"
    b1.place(x=205,y=355)

    clsb2=Button(text="X",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
    
    #головне меню "я надаю послуги"
   
    def host():
        root3 = Tk()
        root3.title("feedback host")
        root3.geometry("940x550")
        root3.resizable(width=False , height=False)
        root3['bg'] = "#3C3C3C"

        hd1=Button(root3,text="Кабінет",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd1.place(x=0,y=0)

        hd2=Button(root3,text="Наряди",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd2.place(x=111,y=0)

        hd3=Button(root3,text="Рахунки",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd3.place(x=223,y=0)

        hd4=Button(root3,text="Клієнти",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd4.place(x=339,y=0)

        hd5=Button(root3,text="Робітники",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd5.place(x=450,y=0)

        hd6=Button(root3,text="Історія СТО",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd6.place(x=588,y=0)

        hd7=Button(root3,text="Налаштування",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
        hd7.place(x=747,y=0)

        #Віджет "Кабінет" 
        
        def cabinet():
            
            hd1['state']=DISABLED
            hd2['state']=DISABLED
            hd3['state']=DISABLED
            hd4['state']=DISABLED
            hd5['state']=DISABLED
            hd6['state']=DISABLED
            hd7['state']=DISABLED

            c1=Label(root3,text=" Ім'я користувача :",font="Vernada 19",bg="#3C3C3C",fg="white")
            c1.place(x=0,y=80)
            c2=Label(root3,text="1",font="Vernada 19",bg="#3C3C3C",fg="white")
            c2.place(x=215,y=80)
            c3=Label(root3,text=" Назва Компанії :",font="Vernada 19",bg="#3C3C3C",fg="white")
            c3.place(x=0,y=120)
            c4=Label(root3,text="1",font="Vernada 19",bg="#3C3C3C",fg="white")
            c4.place(x=200,y=120)
            c5=Label(root3,text=" Робітників компанії :",font="Vernada 19",bg="#3C3C3C",fg="white")
            c5.place(x=0,y=160)
            c6=Label(root3,text="1",font="Vernada 19",bg="#3C3C3C",fg="white")
            c6.place(x=249,y=160)
            
            bt1=Button(width=30,text="Назначити робітника",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt1.place(x=8,y=240)
            
            bt2=Button(width=30,text="Відкрити наряд",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt2.place(x=8,y=305)
            
            bt3=Button(width=30,text="Відкрити рахунок",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt3.place(x=8,y=370)

            bt4=Button(width=30,text="Додати клієнта",font="Vernada 19",bg="#282828",fg="white", relief=FLAT,overrelief=GROOVE)
            bt4.place(x=8,y=435)
            
            cl1=Label(text="Посада робітника",font="Vernada 19",bg="#3C3C3C",fg="white")
            
            cl2=Label(text="П.І.Б. робітника",font="Vernada 19",bg="#3C3C3C",fg="white")
            
            cl3=Label(text="доступ до віджетів",font="Vernada 19",bg="#3C3C3C",fg="white")
            
            en1=Entry(width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
            en1.insert(0,"")
            
            en2=Entry( width=53, font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
            en2.insert(0,"")

            chl1=Checkbutton(root3,text="Наряди",font="Vernada 20",bg="#3C3C3C",fg="white")

            chl2=Checkbutton(root3,text="Рахунки",font="Vernada 20",bg="#3C3C3C",fg="white")

            chl3=Checkbutton(root3,text="Клієнти",font="Vernada 20",bg="#3C3C3C",fg="white")
            
            chl4=Checkbutton(root3,text="Історія СТО",font="Vernada 20",bg="#3C3C3C",fg="white")
            
            clb1=Button(root3,text="Зареєструвати",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            
            clb2=Button(root3,text="X",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            clb2.place(x=910,y=49)

            clsb2=Button(root3,text="X",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            
            root3.geometry("940x550")
           
            def close2():
                    
                c1.destroy()
                c2.destroy()
                c3.destroy()
                c4.destroy()
                c5.destroy()
                c6.destroy()
                bt1.destroy()
                bt2.destroy()
                bt3.destroy()
                bt4.destroy()
                clb2.destroy()
                    
                hd1['state']=NORMAL
                hd2['state']=NORMAL
                hd3['state']=NORMAL
                hd4['state']=NORMAL
                hd5['state']=NORMAL
                hd6['state']=NORMAL
                hd7['state']=NORMAL
                

                root3.geometry("940x550")
                                                                                     
            clb2.config(command=close2)
            
            #Кнопка "назначити робітника"
          
            def new_worker():
                
                c1.destroy()
                c2.destroy()
                c3.destroy()
                c4.destroy()
                c5.destroy()
                c6.destroy()
                bt1.destroy()
                bt2.destroy()
                bt3.destroy()
                bt4.destroy()
                clb2.destroy()
                
                hd1['state']=DISABLED
                hd2['state']=DISABLED
                hd3['state']=DISABLED
                hd4['state']=DISABLED
                hd5['state']=DISABLED
                hd6['state']=DISABLED
                hd7['state']=DISABLED
                
                cl1.place(x=10,y=80)
                
                cl2.place(x=10,y=160)
                               
                en1.place(x=8,y=120)

                en2.place(x=8,y=200)
                
                cl3.place(x=10,y=240)

                chl1.place(x=10,y=280)

                chl2.place(x=10,y=320)
                
                chl3.place(x=10,y=360)
                
                chl4.place(x=10,y=400)
                
                clb1.place(x=147,y=460)
                
                clsb2.place(x=910,y=49)

                root3.geometry("940x520")
                
                def close2():
                    
                    cl1.destroy()
                    cl2.destroy()
                    cl3.destroy()
                    en1.destroy()
                    en2.destroy()
                    chl1.destroy()
                    chl2.destroy()
                    chl3.destroy()
                    chl4.destroy()
                    clb1.destroy()
                    clb2.destroy()
                    clsb2.destroy()

                    hd1['state']=NORMAL
                    hd2['state']=NORMAL
                    hd3['state']=NORMAL
                    hd4['state']=NORMAL
                    hd5['state']=NORMAL
                    hd6['state']=NORMAL
                    hd7['state']=NORMAL
                    
                    root3.geometry("940x550")
                    
                clsb2.config(command=close2)  
            
            bt1.config(command=new_worker)

            #Кнопка "Відкрити наряд"
            
            def new_order():   
                
                c1.destroy()
                c2.destroy()
                c3.destroy()
                c4.destroy()
                c5.destroy()
                c6.destroy()
                bt1.destroy()
                bt2.destroy()
                bt3.destroy()
                bt4.destroy()
                clb2.destroy()
                
                hd1['state']=DISABLED
                hd2['state']=DISABLED
                hd3['state']=DISABLED
                hd4['state']=DISABLED
                hd5['state']=DISABLED
                hd6['state']=DISABLED
                hd7['state']=DISABLED
                
                #
                csl1=Label(text="Номер наряду",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl1.place(x=390,y=60)                           
                
                ##
                csl2=Label(text="Держ.Номер авто",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl2.place(x=373,y=125)               
                
                ###
                csl3=Label(text="Телефон власника авто",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl3.place(x=340,y=185)
                
                csl4=Label(text="Перелік задач",font="Vernada 21",bg="#3C3C3C",fg="white")
                csl4.place(x=380,y=250)
                
                ####
                csl5=Label(text="Двигун:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl5.place(x=230,y=280)
                
                #####
                csl6=Label(text="Ходова частина:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl6.place(x=230,y=370)
                
                ######
                csl7=Label(text="Трансмісія:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl7.place(x=230,y=470)

                #######
                csl8=Label(text="Електрообладнання/салон:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl8.place(x=230,y=570)

                #
                ent1=Entry(width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
                ent1.insert(0,"")
                ent1.place(x=230,y=100)
                
                ##
                ent2=Entry( width=53, font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
                ent2.insert(0,"")
                ent2.place(x=230,y=162)
                
                ###
                ent3=Entry(width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
                ent3.insert(0,"")
                ent3.place(x=230,y=225)
                
                ####
                ent4=Entry( width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent4.insert(0,"")
                ent4.place(x=230,y=315)
                
                #####
                ent5=Entry(width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent5.place(x=230,y=400)
                
                ######
                ent6=Entry(width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent6.place(x=230,y=500)
                
                #######
                ent7=Entry(width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent7.place(x=230,y=600)

                clsb2=Button(root3,text="X",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
                clsb2.place(x=910,y=49)
                
                ####
                clsb3=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)
                clsb3.place(x=712,y=307) 
                
                #####
                clsb4=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)           
                clsb4.place(x=712,y=392)
                
                ######
                clsb5=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)
                clsb5.place(x=712,y=492)

                clsb6=Button(text="Створити наряд",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT)
                clsb6.place(x=395,y=700)
                
                #######
                clsb7=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)
                clsb7.place(x=712,y=592)

                ent44=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")

                ent55=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")

                ent66=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")

                ent77=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")
        
                root3.geometry("940x750")
                                                                
                def plus1():

                    ent44.place(x=230,y=345)
                    clsb3.destroy()

                clsb3.config(command=plus1)     
                

                def plus2():
                    
                    ent55.place(x=230,y=430)
                    clsb4.destroy()
                
                clsb4.config(command=plus2)

                def plus3():
                    
                    ent66.place(x=230,y=530)
                    clsb5.destroy()

                clsb5.config(command=plus3)

                def plus4():
                    
                    ent77.place(x=230,y=630)    
                    clsb7.destroy()

                clsb7.config(command=plus4)

                def close2():
                    
                    csl1.destroy()
                    csl2.destroy()
                    csl3.destroy()
                    csl4.destroy()
                    csl5.destroy()
                    csl6.destroy()
                    csl7.destroy()
                    csl8.destroy()
                    ent1.destroy()
                    ent2.destroy()
                    ent3.destroy()
                    ent4.destroy()
                    ent44.destroy()
                    ent5.destroy()
                    ent55.destroy()
                    ent6.destroy()
                    ent66.destroy()
                    ent7.destroy()
                    ent77.destroy()
                    clsb2.destroy()
                    clsb3.destroy()
                    clsb4.destroy()
                    clsb5.destroy()
                    clsb6.destroy()
                    clsb7.destroy()
                    
                    hd1['state']=NORMAL
                    hd2['state']=NORMAL
                    hd3['state']=NORMAL
                    hd4['state']=NORMAL
                    hd5['state']=NORMAL
                    hd6['state']=NORMAL
                    hd7['state']=NORMAL
                    
                    root3.geometry("940x550")
                                                                                     
                clsb2.config(command=close2)        
           
                
            
            bt2.config(command=new_order)
           
            #Кнопка "новий рахунок"
            
            def new_check():
                
                c1.destroy()
                c2.destroy()
                c3.destroy()
                c4.destroy()
                c5.destroy()
                c6.destroy()
                bt1.destroy()
                bt2.destroy()
                bt3.destroy()
                bt4.destroy()
                clb2.destroy()

                hd1['state']=DISABLED
                hd2['state']=DISABLED
                hd3['state']=DISABLED
                hd4['state']=DISABLED
                hd5['state']=DISABLED
                hd6['state']=DISABLED
                hd7['state']=DISABLED
                           
                #
                csl1=Label(text="Номер рахунку",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl1.place(x=390,y=60)                           
                
                ##
                csl2=Label(text="Номер наряду",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl2.place(x=373,y=125)               
                
                ###
                csl3=Label(text="Телефон власника авто",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl3.place(x=340,y=185)
                
                csl4=Label(text="Перелік запчастин",font="Vernada 21",bg="#3C3C3C",fg="white")
                csl4.place(x=358,y=250)
                
                ####
                csl5=Label(text="Двигун:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl5.place(x=230,y=280)
                
                #####
                csl6=Label(text="Ходова частина:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl6.place(x=230,y=370)
                
                ######
                csl7=Label(text="Трансмісія:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl7.place(x=230,y=470)

                #######
                csl8=Label(text="Електрообладнання/салон:",font="Vernada 19",bg="#3C3C3C",fg="white")
                csl8.place(x=230,y=570)

                #
                ent1=Entry(width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
                ent1.insert(0,"")
                ent1.place(x=230,y=100)
                
                ##
                ent2=Entry( width=53, font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
                ent2.insert(0,"")
                ent2.place(x=230,y=162)
                
                ###
                ent3=Entry(width=53 , font="Vernada 13",justify=CENTER,foreground="#3C3C3C")
                ent3.insert(0,"")
                ent3.place(x=230,y=225)
                
                ####
                ent4=Entry( width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent4.insert(0,"")
                ent4.place(x=230,y=315)
                
                #####
                ent5=Entry(width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent5.place(x=230,y=400)
                
                ######
                ent6=Entry(width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent6.place(x=230,y=500)
                
                #######
                ent7=Entry(width=53, font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ent7.place(x=230,y=600)

                clsb2=Button(root3,text="X",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
                clsb2.place(x=910,y=49)
                
                ####
                clsb3=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)
                clsb3.place(x=712,y=307) 
                
                #####
                clsb4=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)           
                clsb4.place(x=712,y=392)
                
                ######
                clsb5=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)
                clsb5.place(x=712,y=492)

                clsb6=Button(text="Створити рахунок",font="Vernada 15",bg="#282828",foreground="white",relief=FLAT)
                clsb6.place(x=395,y=660)
                
                #######
                clsb7=Button(text="+",font="Vernada 15",bg="#3C3C3C",foreground="white",relief=FLAT)
                clsb7.place(x=712,y=592)

                ent44=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")

                ent55=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")

                ent66=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")

                ent77=Entry( width=68, font="Vernada 10",justify=LEFT,foreground="#3C3C3C")
        
                root3.geometry("940x750")
                                                                
                def plus1():

                    ent44.place(x=230,y=345)
                    clsb3.destroy()

                clsb3.config(command=plus1)     
                

                def plus2():
                    
                    ent55.place(x=230,y=430)
                    clsb4.destroy()
                
                clsb4.config(command=plus2)

                def plus3():
                    
                    ent66.place(x=230,y=530)
                    clsb5.destroy()

                clsb5.config(command=plus3)

                def plus4():
                    
                    ent77.place(x=230,y=630)    
                    clsb7.destroy()

                clsb7.config(command=plus4)

                def close2():
                    
                    csl1.destroy()
                    csl2.destroy()
                    csl3.destroy()
                    csl4.destroy()
                    csl5.destroy()
                    csl6.destroy()
                    csl7.destroy()
                    csl8.destroy()
                    ent1.destroy()
                    ent2.destroy()
                    ent3.destroy()
                    ent4.destroy()
                    ent44.destroy()
                    ent5.destroy()
                    ent55.destroy()
                    ent6.destroy()
                    ent66.destroy()
                    ent7.destroy()
                    ent77.destroy()
                    clsb2.destroy()
                    clsb3.destroy()
                    clsb4.destroy()
                    clsb5.destroy()
                    clsb6.destroy()
                    clsb7.destroy()
                    
                    hd1['state']=NORMAL
                    hd2['state']=NORMAL
                    hd3['state']=NORMAL
                    hd4['state']=NORMAL
                    hd5['state']=NORMAL
                    hd6['state']=NORMAL
                    hd7['state']=NORMAL
                    
                    root3.geometry("940x550")
                                                                                     
                clsb2.config(command=close2)

            bt3.config(command=new_check)
                   
            #Кнопка "новий клієнт"
            
            def new_client():

                c1.destroy()
                c2.destroy()
                c3.destroy()
                c4.destroy()
                c5.destroy()
                c6.destroy()
                bt1.destroy()
                bt2.destroy()
                bt3.destroy()
                bt4.destroy()
                clb2.destroy()
                
                hd1['state']=DISABLED
                hd2['state']=DISABLED
                hd3['state']=DISABLED
                hd4['state']=DISABLED
                hd5['state']=DISABLED
                hd6['state']=DISABLED
                hd7['state']=DISABLED
                
                lc1=Label(text="Ім'я Користувача",font="Vernada 19",bg="#3C3C3C",fg="white")
                lc1.place(x=10,y=80)
                
                lc2=Label(text="Особистий код для входу",font="Vernada 19",bg="#3C3C3C",fg="white")
                lc2.place(x=10,y=160)
                               
                lc3=Label(text="Доступ до інформації",font="Vernada 19",bg="#3C3C3C",fg="white")
                lc3.place(x=10,y=240)
                
                ens1=Entry(width=53 , font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ens1.place(x=8,y=120)

                ens2=Entry(width=53 , font="Vernada 13",justify=LEFT,foreground="#3C3C3C")
                ens2.place(x=8,y=200)

                hcl1=Checkbutton(root3,text="Наряди на авто",font="Vernada 20",bg="#3C3C3C",fg="white")

                hcl2=Checkbutton(root3,text="Рахунки на авто",font="Vernada 20",bg="#3C3C3C",fg="white")

                hcl3=Checkbutton(root3,text="Історія авто",font="Vernada 20",bg="#3C3C3C",fg="white")
                
                hcl1.place(x=10,y=280)

                hcl2.place(x=10,y=320)
                
                hcl3.place(x=10,y=360)
                               
                clb1.place(x=147,y=460)
                
                clsb2.place(x=910,y=49)

                root3.geometry("940x520")
                
                def close2():
                    
                    lc1.destroy()
                    lc2.destroy()
                    lc3.destroy()
                    ens1.destroy()
                    ens2.destroy()
                    hcl1.destroy()
                    hcl2.destroy()
                    hcl3.destroy()
                    clb1.destroy()
                    clb2.destroy()
                    clsb2.destroy()
                    
                    hd1['state']=NORMAL
                    hd2['state']=NORMAL
                    hd3['state']=NORMAL
                    hd4['state']=NORMAL
                    hd5['state']=NORMAL
                    hd6['state']=NORMAL
                    hd7['state']=NORMAL
                    
                    root3.geometry("940x550")
                    
                clsb2.config(command=close2)  
            
            bt4.config(command=new_client)
        
        hd1.config(command=cabinet)  
        
        #Віджет "Наряди"

        def orders():

            hd1['state']=DISABLED
            hd2['state']=DISABLED
            hd3['state']=DISABLED
            hd4['state']=DISABLED
            hd5['state']=DISABLED
            hd6['state']=DISABLED
            hd7['state']=DISABLED
           
            can1=Canvas(root3,width=445,height=430,bg="#282828")
            can1.place(x=460,y=89)
            
            can2=Canvas(root3,width=400,height=430,bg="#282828")
            can2.place(x=30,y=89)
            
            clsb2=Button(root3,text="X",font="Vernada 13",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            clsb2.place(x=915,y=48)

            btn1=Button(root3,text="Закрити наряд",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btn1.place(x=720,y=460)

            lbl1=Label(text="Відкритий наряд №",font="Vernada 19",bg="#3C3C3C",fg="white")
            lbl1.place(x=540,y=50)
            lbl11=Label(text="",font="Vernada 19",bg="#3C3C3C",fg="white")
            lbl11.place(x=770,y=50)

            lbl2=Label(text="Перелік відкритих нарядів",font="Vernada 19",bg="#3C3C3C",fg="white")
            lbl2.place(x=70,y=50)

            lbl3=Label(text="Держ. номер авто:",font="Vernada 15",bg="#282828",fg="white")
            lbl3.place(x=465,y=95)
            lbl33=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lbl33.place(x=640,y=95)

            lbl4=Label(text="Тел. власника авто:",font="Vernada 15",bg="#282828",fg="white")
            lbl4.place(x=465,y=130)
            lbl44=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lbl44.place(x=655,y=130)

            lbl5=Label(text="Перелік задач:",font="Vernada 15",bg="#282828",fg="white")
            lbl5.place(x=465,y=165)
            
            lbl6=Label(text="Двигун - ",font="Vernada 15",bg="#282828",fg="white")
            lbl6.place(x=465,y=200)
            lbl66=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbl66.place(x=550,y=204)
            
            lbl7=Label(text="Ходова частина - ",font="Vernada 15",bg="#282828",fg="white")
            lbl7.place(x=465,y=255)
            lbl77=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbl77.place(x=630,y=259)

            lbl8=Label(text="Трансмісія - ",font="Vernada 15",bg="#282828",fg="white")
            lbl8.place(x=465,y=310)
            lbl88=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbl88.place(x=580,y=314)
            
            lbl9=Label(text="Електрообладнання/салон - ",font="Vernada 15",bg="#282828",fg="white")
            lbl9.place(x=465,y=365)
            lbl99=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbl99.place(x=725,y=369)

            def close2():
                    
                lbl1.destroy()
                lbl11.destroy()
                lbl2.destroy()
                lbl3.destroy()
                lbl33.destroy()
                lbl4.destroy()
                lbl44.destroy()
                lbl5.destroy()
                lbl6.destroy()
                lbl66.destroy()
                lbl7.destroy()
                lbl77.destroy()
                lbl8.destroy()
                lbl88.destroy()
                lbl9.destroy()
                lbl99.destroy()
                can1.destroy()
                can2.destroy()
                btn1.destroy()
                clsb2.destroy()
                
                hd1['state']=NORMAL
                hd2['state']=NORMAL
                hd3['state']=NORMAL
                hd4['state']=NORMAL
                hd5['state']=NORMAL
                hd6['state']=NORMAL
                hd7['state']=NORMAL
                    
                root3.geometry("940x550")
                    
            clsb2.config(command=close2)

        hd2.config(command=orders)
        
        #Віджет "рахунки"

        def checks():
            
            hd1['state']=DISABLED
            hd2['state']=DISABLED
            hd3['state']=DISABLED
            hd4['state']=DISABLED
            hd5['state']=DISABLED
            hd6['state']=DISABLED
            hd7['state']=DISABLED
           
            can1=Canvas(root3,width=445,height=430,bg="#282828")
            can1.place(x=460,y=89)
            
            can2=Canvas(root3,width=400,height=430,bg="#282828")
            can2.place(x=30,y=89)

            clsb2=Button(root3,text="X",font="Vernada 13",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            clsb2.place(x=915,y=48)

            btns1=Button(root3,text="Закрити рахунок",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btns1.place(x=700,y=460)

            lbls1=Label(text="Відкритий рахунок №",font="Vernada 19",bg="#3C3C3C",fg="white")
            lbls1.place(x=540,y=50)
            lbls11=Label(text="2",font="Vernada 19",bg="#3C3C3C",fg="white")
            lbls11.place(x=790,y=50)

            lbls2=Label(text="Перелік відкритих рахунків",font="Vernada 19",bg="#3C3C3C",fg="white")
            lbls2.place(x=70,y=50)

            lbls3=Label(text="Держ. номер авто:",font="Vernada 15",bg="#282828",fg="white")
            lbls3.place(x=465,y=95)
            lbls33=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lbls33.place(x=640,y=95)

            lbls4=Label(text="Тел. власника авто:",font="Vernada 15",bg="#282828",fg="white")
            lbls4.place(x=465,y=130)
            lbls44=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lbls44.place(x=655,y=130)

            lbls5=Label(text="Перелік деталей:",font="Vernada 15",bg="#282828",fg="white")
            lbls5.place(x=465,y=165)
            
            lbls6=Label(text="Двигун - ",font="Vernada 15",bg="#282828",fg="white")
            lbls6.place(x=465,y=200)
            lbls66=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbls66.place(x=550,y=204)
            
            lbls7=Label(text="Ходова частина - ",font="Vernada 15",bg="#282828",fg="white")
            lbls7.place(x=465,y=255)
            lbls77=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbls77.place(x=630,y=259)

            lbls8=Label(text="Трансмісія - ",font="Vernada 15",bg="#282828",fg="white")
            lbls8.place(x=465,y=310)
            lbls88=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbls88.place(x=580,y=314)
            
            lbls9=Label(text="Електрообладнання/салон - ",font="Vernada 15",bg="#282828",fg="white")
            lbls9.place(x=465,y=365)
            lbls99=Label(text="",font="Vernada 13",bg="#282828",fg="white")
            lbls99.place(x=725,y=369)

            def close2():
                    
                lbls1.destroy()
                lbls11.destroy()
                lbls2.destroy()
                lbls3.destroy()
                lbls33.destroy()
                lbls4.destroy()
                lbls44.destroy()
                lbls5.destroy()
                lbls6.destroy()
                lbls66.destroy()
                lbls7.destroy()
                lbls77.destroy()
                lbls8.destroy()
                lbls88.destroy()
                lbls9.destroy()
                lbls99.destroy()
                can1.destroy()
                can2.destroy()
                btns1.destroy()
                clsb2.destroy()
                
                hd1['state']=NORMAL
                hd2['state']=NORMAL
                hd3['state']=NORMAL
                hd4['state']=NORMAL
                hd5['state']=NORMAL
                hd6['state']=NORMAL
                hd7['state']=NORMAL
                    
                root3.geometry("940x550")
                    
            clsb2.config(command=close2)

        hd3.config(command=checks)    
        
        def clients():
            
            hd1['state']=DISABLED
            hd2['state']=DISABLED
            hd3['state']=DISABLED
            hd4['state']=DISABLED
            hd5['state']=DISABLED
            hd6['state']=DISABLED
            hd7['state']=DISABLED
           
            can1=Canvas(root3,width=445,height=430,bg="#282828")
            can1.place(x=460,y=89)
            
            can2=Canvas(root3,width=400,height=430,bg="#282828")
            can2.place(x=30,y=89)

            clsb2=Button(root3,text="X",font="Vernada 13",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            clsb2.place(x=915,y=48)

            btnb1=Button(root3,text="Видалити клієнта",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnb1.place(x=690,y=460)

            btnb2=Button(root3,text="Змінити права",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnb2.place(x=507,y=460)
            
            lblb1=Label(text="Активний акаунт клієнта",font="Vernada 19",bg="#3C3C3C",fg="white")
            lblb1.place(x=540,y=50)

            lblb2=Label(text="Перелік активних акаунтів",font="Vernada 19",bg="#3C3C3C",fg="white")
            lblb2.place(x=70,y=50)

            lblb3=Label(text="Ім'я користувача:",font="Vernada 15",bg="#282828",fg="white")
            lblb3.place(x=465,y=95)
            lblb33=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblb33.place(x=640,y=95)

            lblb4=Label(text="Телефон користувача:",font="Vernada 15",bg="#282828",fg="white")
            lblb4.place(x=465,y=150)
            lblb44=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblb44.place(x=675,y=150)

            lblb5=Label(text="Наряди на авто:",font="Vernada 15",bg="#282828",fg="white")
            lblb5.place(x=465,y=185)
            lblb55=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblb55.place(x=675,y=185)
            
            lblb6=Label(text="Рахунки на авто:",font="Vernada 15",bg="#282828",fg="white")
            lblb6.place(x=465,y=220)
            lblb66=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblb66.place(x=630,y=220)
            
            lblb7=Label(text="Авто користувача:",font="Vernada 15",bg="#282828",fg="white")
            lblb7.place(x=465,y=255)
            lblb77=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblb77.place(x=640,y=255)
                      
            def close2():
                    
                lblb1.destroy()
                lblb2.destroy()
                lblb3.destroy()
                lblb33.destroy()
                lblb4.destroy()
                lblb44.destroy()
                lblb5.destroy()
                lblb55.destroy()
                lblb6.destroy()
                lblb66.destroy()
                lblb7.destroy()
                lblb77.destroy()
                can1.destroy()
                can2.destroy()
                btnb1.destroy()
                btnb2.destroy()
                clsb2.destroy()
                
                hd1['state']=NORMAL
                hd2['state']=NORMAL
                hd3['state']=NORMAL
                hd4['state']=NORMAL
                hd5['state']=NORMAL
                hd6['state']=NORMAL
                hd7['state']=NORMAL
                    
                root3.geometry("940x550")
                    
            clsb2.config(command=close2)
        
        hd4.config(command=clients)    
        
        def workers():

            hd1['state']=DISABLED
            hd2['state']=DISABLED
            hd3['state']=DISABLED
            hd4['state']=DISABLED
            hd5['state']=DISABLED
            hd6['state']=DISABLED
            hd7['state']=DISABLED
           
            can1=Canvas(root3,width=445,height=430,bg="#282828")
            can1.place(x=460,y=89)
            
            can2=Canvas(root3,width=400,height=430,bg="#282828")
            can2.place(x=30,y=89)

            clsb2=Button(root3,text="X",font="Vernada 13",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            clsb2.place(x=915,y=48)

            btnc1=Button(root3,text="Видалити робітника",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnc1.place(x=660,y=460)

            btnc2=Button(root3,text="Змінити права",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnc2.place(x=477,y=460)

            lblc1=Label(text="Активний акаунт робітника",font="Vernada 19",bg="#3C3C3C",fg="white")
            lblc1.place(x=540,y=50)

            lblc2=Label(text="Перелік активних акаунтів",font="Vernada 19",bg="#3C3C3C",fg="white")
            lblc2.place(x=70,y=50)

            lblc3=Label(text="Ім'я користувача:",font="Vernada 15",bg="#282828",fg="white")
            lblc3.place(x=465,y=95)
            lblc33=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblc33.place(x=640,y=95)

            lblc4=Label(text="Посада користувача:",font="Vernada 15",bg="#282828",fg="white")
            lblc4.place(x=465,y=150)
            lblc44=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblc44.place(x=675,y=150)

            lblc5=Label(text="Наряди у виконанні:",font="Vernada 15",bg="#282828",fg="white")
            lblc5.place(x=465,y=185)
            lblc55=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblc55.place(x=675,y=185)

            lblc6=Label(text="Створені рахунки:",font="Vernada 15",bg="#282828",fg="white")
            lblc6.place(x=465,y=220)
            lblc66=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            lblc66.place(x=675,y=220)
            
            
            def close2():
                    
                lblc1.destroy()
                lblc2.destroy()
                lblc3.destroy()
                lblc33.destroy()
                lblc4.destroy()
                lblc44.destroy()
                lblc5.destroy()
                lblc55.destroy()
                lblc6.destroy()
                lblc66.destroy()
                can1.destroy()
                can2.destroy()
                btnc1.destroy()
                btnc2.destroy()
                clsb2.destroy()
                
                hd1['state']=NORMAL
                hd2['state']=NORMAL
                hd3['state']=NORMAL
                hd4['state']=NORMAL
                hd5['state']=NORMAL
                hd6['state']=NORMAL
                hd7['state']=NORMAL
                    
                root3.geometry("940x550")
                    
            clsb2.config(command=close2)

        hd5.config(command=workers) 
        
        def story():
        
            hd1['state']=DISABLED
            hd2['state']=DISABLED
            hd3['state']=DISABLED
            hd4['state']=DISABLED
            hd5['state']=DISABLED
            hd6['state']=DISABLED
            hd7['state']=DISABLED
           
            can1=Canvas(root3,width=445,height=430,bg="#282828")
            can1.place(x=460,y=89)
            
            can2=Canvas(root3,width=400,height=430,bg="#282828")
            can2.place(x=30,y=89)

            clsb2=Button(root3,text="X",font="Vernada 13",bg="#282828",foreground="white",relief=FLAT,overrelief=GROOVE)
            clsb2.place(x=915,y=48)

            btnc1=Button(root3,text="Видалити",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnc1.place(x=660,y=460)

            btnc2=Button(can2,text="Рахунки",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnc2.place(x=120,y=93)

            btnc3=Button(can2,text="Наряди",font="Vernada 17",bg="#3C3C3C",foreground="white",relief=FLAT,overrelief=GROOVE)
            btnc3.place(x=230,y=93)

            lblc1=Label(text="Закритий документ",font="Vernada 19",bg="#3C3C3C",fg="white")
            lblc1.place(x=540,y=50)

            lblc2=Label(text="Перелік документів",font="Vernada 19",bg="#3C3C3C",fg="white")
            lblc2.place(x=70,y=50)
            
            #змінні для кнопок "наряди/рахунки"
           
            ##наряди
            
            lblc3=Label(text="Номер наряду:",font="Vernada 15",bg="#282828",fg="white")

            lblc33=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            
            lblc4=Label(text="Номер авто:",font="Vernada 15",bg="#282828",fg="white")
            
            lblc44=Label(text="",font="Vernada 15",bg="#282828",fg="white")

            lblc5=Label(text="Коментар механіка:",font="Vernada 15",bg="#282828",fg="white")

            lblc55=Label(text="",font="Vernada 15",bg="#282828",fg="white")

            lblc6=Label(text="Номер власника авто:",font="Vernada 15",bg="#282828",fg="white")
            
            lblc66=Label(text="",font="Vernada 15",bg="#282828",fg="white")
           
            ##рахунки

            lblcc3=Label(text="Ім'я користувача:",font="Vernada 15",bg="#282828",fg="white")

            lblcc33=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            
            lblcc4=Label(text="Посада користувача:",font="Vernada 15",bg="#282828",fg="white")
            
            lblcc44=Label(text="",font="Vernada 15",bg="#282828",fg="white")

            lblcc5=Label(text="Наряди у виконанні:",font="Vernada 15",bg="#282828",fg="white")

            lblcc55=Label(text="",font="Vernada 15",bg="#282828",fg="white")

            lblcc6=Label(text="Створені рахунки:",font="Vernada 15",bg="#282828",fg="white")
            
            lblcc66=Label(text="",font="Vernada 15",bg="#282828",fg="white")
            
            #рахунки
            
            def check1():
                
                lblcc3.destroy()              
                lblcc33.destroy()
                lblcc4.destroy()               
                lblcc44.destroy()              
                lblcc5.destroy()              
                lblcc55.destroy()
                lblcc6.destroy()              
                lblcc66.destroy()
                
                lblc3.place(x=465,y=95)
                
                lblc33.place(x=640,y=95)

                lblc4.place(x=465,y=150)
                
                lblc44.place(x=675,y=150)
               
                lblc5.place(x=465,y=185)
                
                lblc55.place(x=675,y=185)

                lblc6.place(x=465,y=220)
                
                lblc66.place(x=675,y=220)
           
            btnc3.config(command=check1)
            
            #наряди
            
            def ord1():

                lblc3.destroy()              
                lblc33.destroy()
                lblc4.destroy()               
                lblc44.destroy()              
                lblc5.destroy()              
                lblc55.destroy()
                lblc6.destroy()              
                lblc66.destroy()
                
                lblcc3.place(x=465,y=95)
                
                lblcc33.place(x=640,y=95)

                lblcc4.place(x=465,y=150)
                
                lblcc44.place(x=675,y=150)
               
                lblcc5.place(x=465,y=185)
                
                lblcc55.place(x=675,y=185)

                lblcc6.place(x=465,y=220)
                
                lblcc66.place(x=675,y=220)

            btnc2.config(command=ord1)
            
            def close2():
                    
                lblc1.destroy()
                lblc2.destroy()
                lblc3.destroy()
                lblc33.destroy()                
                can1.destroy()
                can2.destroy()
                btnc1.destroy()
                btnc3.destroy()
                btnc2.destroy()
                clsb2.destroy()
                
                hd1['state']=NORMAL
                hd2['state']=NORMAL
                hd3['state']=NORMAL
                hd4['state']=NORMAL
                hd5['state']=NORMAL
                hd6['state']=NORMAL
                hd7['state']=NORMAL
                    
                root3.geometry("940x550")
                    
            clsb2.config(command=close2)

        hd6.config(command=story)
        root2.destroy()
                         
        root3.mainloop()  

    b1.config(command=host)     
   
    root1.destroy()
    
    root2.mainloop()

Butt1.config(command=reg1)

root1.mainloop()