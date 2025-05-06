def create_password():
    user_pin =int(input("Enter a password: "))
    with open ("login.txt","w") as file:
        file.write(user_pin)
        print("password saved")


def Saved_password():
    try:
        with open ("login.txt","r") as file:
            return file.read()
    except FileNotFoundError:
        return None


def check_password():
    password=Saved_password()
    if password is None:
        print("password is none")
        create_password()
    else:
        user_pass=input("create your password")
        if user_pass==password:
            print("login successfully!")
        else:
            print("incorrect password")
            


def Admin():
    while True:
        check_password()
        print("1.create account")
        print("2.Deposit Money")
        print("3.Withdrew Money")
        print("4.Check Balance")
        print("5.Transaction History")
        print("6.Exit")
        try:
            Check=int(input("Enter a number(1-6): "))
            if Check==1:
                create_account()
            elif Check==2:
                Deposit_money()
            elif Check==3:
                Withdrew_money()
            elif Check==4:
                check_balance()
            elif Check==5:
                transaction_history()
            elif Check==6:
                print("Exit")
                break
            else:
                print("Number is incorrect.Please try again")
        except ValueError:
            print("Invalid input.Please try again")

def customer():
    while True:
        check_password()
        print("1.Deposit Money")
        print("2.Withdrew Money")
        print("3.Check Balance")
        print("4.Transaction History")
        print("5.Exit")
        try:
            Check=int(input("Enter a number(1-6): "))
            if Check==1:
                Deposit_money()
            elif Check==2:
                Withdrew_money()
            elif Check==3:
                check_balance()
            elif Check==4:
                transaction_history()
            elif Check==5:
                print("Exit")
                break
            else:
                print("Number is incorrect.Please try again")
        except ValueError:
            print("Invalid input.Please try again")


def manu():
    print("----Welcome to mini bank----")
    print("1.Admin service")
    print("2.Customer service")
    print("3.Exit")
    while True:
        try:
            check=int(input("Enter a number(1-3): "))
            if check==1:
                Admin()
            elif check==2:
                customer()
            elif  check==3:
                print("Exiting.Thank you")
            else:
                print("incorrect number. Please try again")
        except ValueError:
            print("Invalid input. Please try again")
            

