from ViewMedCart import MedCart
MedNameList=[]
Price_List=[]
class MedProducts():
    @classmethod
    def medProducts(self):
        global flag
        flag = True
        while flag:
                print("")
                print("1.OTC Medicine")
                print("2.Skin Care")
                Pro_choice=int(input("Enter Product Choice: "))
                print("*-----*-----*-----*-----*-----*")
                ###OTC MEDCINE###
                if(Pro_choice == 1):
                    print("OTC MEDICINES")
                    print("-------------")
                    Otcmed=["aspirin","Gaviscon","Cepacol","Cetirizine","Paracetamol"]
                    OTC_Price=[11,86.5,63.5,17.5,12]
                    for i in range(len(Otcmed)):
                        print(Otcmed[i]," : Rs.",OTC_Price[i])
                    print("*-----*-----*-----*-----*-----*")
                    print("")
                    print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")    
                    Eo_choice = int(input("Enter Otc-Medicine no: "))
                    for i in range (len(Otcmed)):
                        if (i == (Eo_choice-1)):
                            print("Medicine: ",Otcmed[i]," - Rs",OTC_Price[i])
                            MedNameList.append(Otcmed[i])
                            Price_List.append(OTC_Price[i])
                            print("Selected Medicine is added to the Cart")
                            print("*------*-----*-----*-----*-----*------*")
                            print("")
                            print("1.View Cart \n2.Add Medicine \n3.Skip")
                            k=int(input("Enter Your Choice: "))
                            if k==1:
                                MedCart.view_medcart(MedNameList,Price_List)
                                flag = False
                            elif k==2:
                                self.medProducts()
                            else:
                                print("***Skipped Here***")
                                print("*-----*-----*-----*-----*-----*")                               
                ###SKIN_CARE####
                elif (Pro_choice == 2):
                    print("SKIN CARE MEDICINES")
                    print("--------------------")
                    Skin_Care=["Calamine Lotion","cetaphil gentle","Eucerin Cream","Differin 0.1 gel","Isotretinoin"]
                    Sc_Price=[125,184.5,167.6,263.5,778]
                    for i in range(len(Skin_Care)):
                        print(Skin_Care[i],": Rs. ", Sc_Price[i])
                    print("*-----*-----*-----*-----*-----*")
                    print("")
                    print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")    
                    ES_choice = int(input("Enter Skin care - Medicine no: "))
                    for i in range (len(Skin_Care)):
                            if (i == (ES_choice-1)):
                                print("Skin Care Product: ",Skin_Care[i]," - Rs",Sc_Price[i])
                                MedNameList.append(Skin_Care[i])
                                Price_List.append(Sc_Price[i])
                                print("Selected Medicine is added to the Cart")
                                print("*------*-----*-----*-----*-----*------*")
                                print("")
                                print("1.View Cart \n2.Add Medicine \n3.Skip")
                                k=int(input("Enter Your Choice: "))
                                if(k==1):
                                    MedCart.view_medcart(MedNameList,Price_List)
                                    flag = False
                                elif k==2:
                                    self.medProducts()
                                else:
                                    print("***Skipped Here***")
                                    print("*-----*-----*-----*-----*-----*")
                
                else:
                    print("You Have Selected a Invalid Choice...!!")


        

    

                        









