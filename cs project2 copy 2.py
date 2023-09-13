# %%
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="3876",database="bank")
c=mydb.cursor()
tup=('A/c no. : ','Name : ','DOB : ','Ph no : ','Opening balance : ')
tup1=('Name : ','DOB : ','Ph no : ','Opening balance : ')
print('=============================WELCOME TO BANK MANAGEMENT SYSTEM============================='.center(90))

def open_ac():
    try:
        c.execute('select max(ac_no)  from details2')
        max_ac_tup=c.fetchone()
        if max_ac_tup==(None,):
            ac=1
        else:
            for i in max_ac_tup:
                ac=i+1
        name=input('Name : ')
        dob=input('DOB (DD/MM/YYYY) : ')
        contact=input('Phone No. : ')
        ob=int(input('Opening Balance : '))
        data1=(ac,name,dob,contact,ob)
        data2=(ac,name,ob)
        sql1='insert into details2 values (%s,%s,%s,%s,%s)'
        sql2='insert into balance2 values (%s,%s,%s)'
        c.execute(sql1,data1)
        c.execute(sql2,data2)
        mydb.commit()
        print('Data Entered Successfully')
        print('Your New Account no. : ',ac)
    except:
        print("Something went wrong. Try again")

def close_ac():
    try:
        ac=int(input('A/c no. : '))
        c.execute('DELETE FROM details2 WHERE ac_no='+str(ac))
        c.execute('DELETE FROM balance2 WHERE ac_no='+str(ac))
        print('Account closed Successfully')
        mydb.commit()
    except:
        print("Something went wrong. Try again")

def balance():
    try:
        ac=int(input('A/c no. : '))
        c.execute('select balance from balance2 where ac_no='+str(ac))
        bal=c.fetchone()
        for i in bal:
            print('Account no. : ',ac)
            print('Balance     : ',i)
    except:
        print("Something went wrong. Try again")


def parti_disp_ac():
    try:
        ac=int(input('A/c no. : '))
        print('')
        c.execute('select name,dob,contact_no,opening_balance from details2 where ac_no='+str(ac))
        disc=c.fetchall()
        for i in disc:
            for j,k in zip(tup1,i):
                print(j,k,'\n')
    except:
        print("Something went wrong. Try again")

def mod_ac():
    try:
        ac=int(input('A/c no. : '))
        choice=input('''1. contact_no
2. dob
Press 1 for contact_no
Press 2 for dob
Enter choice no. : ''')
        if choice=='1':
            new_contact_no=input('New Contact No. : ')
            cont_tup=(new_contact_no,)
            sql3=('update details2 set contact_no=%s where ac_no='+str(ac))
            c.execute(sql3,cont_tup)
            mydb.commit()
        elif choice=='2':
            new_dob=input('New DOB (DD/MM/YYYY) : ')
            dob_tup=(new_dob,)
            sql4=('update details2 set dob=%s where ac_no='+str(ac))
            c.execute(sql4,dob_tup)
            mydb.commit()
        else:
            print('Wrong choice')
    except:
        print("Something went wrong. Try again")

def depo_amt():
    try:
        ac=int(input('A/c no. : '))
        c.execute('select balance from balance2 where ac_no='+str(ac))
        bal=c.fetchone()
        for i in bal:
            print('Account no. : ',ac)
            print('Balance     : ',i)
        d_amt=int(input('Amount to be deposited : '))
        new_d_amt=i+d_amt
        c.execute('update balance2 set balance='+str(new_d_amt)+' where ac_no='+str(ac))
        mydb.commit()
        print('Amount deposited successfully')
        print('New balance : ',new_d_amt)
    except:
        print("Something went wrong. Try again")

def with_amt():
    try:
        ac=int(input('A/c no. : '))
        c.execute('select balance from balance2 where ac_no='+str(ac))
        bal=c.fetchone()
        for i in bal:
            print('Account no. : ',ac)
            print('Balance     : ',i)
        w_amt=int(input('Amount to be withdrawl : '))
        if w_amt<=i:
            new_w_amt=i-w_amt
            c.execute('update balance2 set balance='+str(new_w_amt)+' where ac_no='+str(ac))
            mydb.commit()
            print('Amount withdrawl successfully')
            print('New balance : ',new_w_amt)
        else:
            print('Amount exceeded the A/c balance')
    except:
        print("Something went wrong. Try again")

def all_desc_ac():
    try:
        c.execute('select * from details2')
        all_desc=c.fetchall()
        for i in all_desc:
            for j,k in zip(tup,i):
                print(j,k,'\n')
    except:
        print("Something went wrong. Try again")

def menu():
    print('''
                            1. OPEN A SAVINGS ACCOUNT
                            2. DEPOSITE MONEY
                            3. WITHDRAWL MONEY
                            4. BALANCE ENQUIRY
                            5. DISPLAY A PARTICULAR CUSTOMER'S DETAILS
                            6. DISPALY ALL CUSTOMER DETAILS
                            7. MODIFY CUSTOMER DETAIL
                            8. CLOSE A SAVINGS ACCOINT
                            9. QUIT''')
    
    choice=input('Enter Task No : ')
    print('')
    if (choice=='1'):
        open_ac()
    elif (choice=='2'):
        depo_amt()
    elif (choice=='3'): 
        with_amt()   
    elif (choice=='4'):   
        balance() 
    elif (choice=='5'):
        parti_disp_ac()    
    elif (choice=='6'):
        all_desc_ac()    
    elif (choice=='7'):
        mod_ac()    
    elif (choice=='8'):
        close_ac()
    elif (choice=='9'):
        print("-------------End of job-------------".center(90))
        quit()
    else:
        print('Wrong choice.......')
    menu()
menu()