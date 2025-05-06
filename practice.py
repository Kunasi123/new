'''def create_customer_details():
    name=input("enter your name: ")
    address=input("enter your address: ")
    user_name=input("enter your user name: ")
    intial_balance=float(input("enter amount: "))
    return [name, address, user_name, intial_balance]


def create_customer():
    customer=create_customer_details()
    with open ("customer.txt","a") as file:
        file.write ([customer[0]],[customer[1]])
def create_user():
    customer=create_customer_details()
    with open("user.txt", "a")as file:
        file.write([customer[2]], [customer[3]])

def create_account_no():
    with open("user.txt","r") as file:
        return f"u(int(file.readlines.()[-1].spilt(",")[0][1:])+1: 00)"


def create_account():
    create_customer()
    create_user()
    print("account created succeffully")
    create_account_no()
create_account()'''



'''def create_account():
        
    name=input("enter your name: ")
    address=input("enter your address: ")
    user_name=input("enter your user name: ")
    intial_balance=float(input("enter amount: "))
    return{"Name":name, "Address":address,"User_Id":user_name,"balance":intial_balance}

def create_customer():
    customers=create_account()
    with open ("customer.txt","a") as file:
        file.write ([customers[0][0]],[customers[0][1]])
    with open("user.txt", "a")as file:
        file.write([customers[0][2]], [customers[0][3]])
    with open("user.txt","r") as file:
        return (f"u(int(user_file.readlines()[-1].spilt(" , ")[0][1:])+1:00)")
create_customer()'''

def next_id():
    with open ("users.txt",'r')as file:
        return f"U{int(file.readlines()[-1].spilt(" , ")[0][1:])+1:000}"



def create_account():
    name=input("enter your name: ")
    address=input("enter your address: ")
    user_name=input("enter your user name: ")
    intial_balance=float(input("enter amount: "))
    next_acc= next_id()
    with open("accounts.txt",'a')as file:
        file.write(f"{name}\t")
        file.write(f"{address}\t")
        file.write(f"{user_name}\t")
        file.write(f"{intial_balance}\n")    
    with open("customers.txt",'a')as file:
        file.write(f"{name}\t")
        file.write(f"{address}\n")
    with open("users.txt",'a')as file:
        file.write(f"{user_name}\t")
        file.write(f"{intial_balance}\t")
        file.write(f"{next_acc}\n")
        
create_account()


    
   
  