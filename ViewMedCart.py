from Order import OrderMed

class MedCart:
    def view_medcart(Medlist,Medprice):
        flag = True
        global check
        global length
        check = 0
        length = len(Medprice)
        
        while flag :
            for i in range(len(Medlist)):
                print ("For",Medlist[i]," : Rs. ",Medprice[i])
            print("*-----*-----*-----*-----*-----*")
            print("")      
            if check <= length:
                print("")
                k=int(input("Do you want to order the medicine??\n1.Yes/press any key to view medicines only numbers:"))     
                check +=1
                if k==1:  
                    i = int(input("Enter your choice:"))
                    i-=1              
                    OrderMed.ordermed(Medprice[i],i)

            else:
                 flag = False


            
            
               
            



                




        
      

 