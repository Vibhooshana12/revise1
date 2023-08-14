from ViewMedPro import MedProducts
import time
import re
Echeck=r'^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]+\w+[.]\w{2,3}$'
Pcheck=r'^[A-Z]?[a-z0-9]+[!@#$%^&*()_+]?\w{0,3}$'
UEmail=["Vibhoo@gmail.com"]
Upassword=["Vi@12"]
Uphonenumber=["6374897300"]
Uusername=["Vibhoo"]

class Signup():  
    @classmethod
    def signupch(self):
        v=True
        while v:
            User_name = input("Enter UserName:  ")
            Uusername.append(User_name)
            Email =input("Enter Email Id:  ")
            print("Enter Password that should :\n1.Starts with Capital Letter\n2.If you need Use Special Character(1)\n3.Note after Special Character 0 or 3 alphanumeric is accepted")
            Password = input("Enter Password:  ")
            if (re.search(Echeck,Email)):
                UEmail.append(Email)
                if (re.search(Pcheck,Password)):
                    Upassword.append(Password)
                    print("@Strong Password@")
                    v=False
                else:
                    print("\t\t\t<<<<<<<Not Valid a password>>>>>>>\t\t\t")
            else:
                print("\t\t\t<<<<<<<Not Valid Email Id>>>>>>>\t\t\t")
        flag = True
        while flag:
            try:
                PhoneNumber= int(input("Enter your Mobile number: "))
                if PhoneNumber > 6000000000 and PhoneNumber < 10000000000:
                    pass
                else:
                    print("\t\t\t<<<<<<<Enter the valid one>>>>>>>\t\t\t")

            except:
                print("\t\t\tYour Mobile Number entered is '<<<<Not Valid>>>>' try with a valid number\t\t\t")
            else:
                if PhoneNumber > 6000000000 and PhoneNumber < 10000000000:
                    Uphonenumber.append(PhoneNumber)
                    print("\t\t\t\t!*!*!*!*!...Your Registration is Successful...!*!*!*!*!\t\t\t\t")
                    flag = False


class Login():
    def __init__(self):
       self.UserName =" "
       self.UserPassword = " "

    @classmethod
    def signinch(self):
        self.UserName =input("Enter UserName:  ")
        self.UserPassword = input("Enter UserPassword:  ")
        for i in range(len(Uusername)):
            if Uusername[i] == self.UserName:
                if Upassword[i] ==  self.UserPassword:
                            print("\t\t\tHai",Uusername[i],"you have Logged in Sucessfully:)\t\t\t")
                            time.sleep(2)
                            print("\t\t\t",Uusername[i],"Welcome to Sasi Pharmacy:)\t\t\t")
                            print("")
                            print("View Medicine Products")
                            MedProducts.medProducts()
                            break
        else:
            print("\t\t\t<<<<<<<Invalid User>>>>>>\t\t\t")
            print("\t\t\t<<<<<<<Enter a Valid User Name and Password>>>>>>>\t\t\t")
