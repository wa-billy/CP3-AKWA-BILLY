print("      WAASHoP")
print("===================")
username = input("Enter Your userame: ")
password = input("Enter Your password: ")
if username == "akwa2567" and password == "Smart139":
    print("correct")
    print("Welcome To WAASHoP")
    print("-------------------")
    print("Select your product")
    print("1.>> Muay Shirt")
    print("2.>> Mauy Pant")
    product = int(input("Select product: "))
    if product == 1:
        print("<Mauy Shirt>")
        print("_____________")
        print("1.>> Muay Mad Shirt: 849THB")
        mauyMad = 849
        print("2.>> Muay Sok Shirt: 956THB")
        mauySok = 956
        print("3.>> Muay Feemue Shirt: 899THB")
        mauyFee = 899
        mauyShirt = int(input("Select mauyShirt: "))
        amount = int(input("Enter amount: "))
        print("_____________")
        if mauyShirt == 1:
            print("price :",849*amount,"THB")
            print("vat 7%")
            print("Total :",849*amount+(849*7/100),"THB")
            print("_____________")
        if mauyShirt == 2:
            print("price :", 956 * amount, "THB")
            print("vat 7%")
            print("Total :", 956 * amount + (956 * 7 / 100), "THB")
            print("_____________")
        if mauyShirt == 3:
            print("price :", 899 * amount, "THB")
            print("vat 7%")
            print("Total :", 899 * amount + (899 * 7 / 100), "THB")
            print("_____________")
    if product == 2:
        print("<Mauy Pant>")
        print("_____________")
        print("1.>> Muay Mad Pant: 759THB")
        mauyMad = 759
        print("2.>> Muay Sok Pant: 799THB")
        mauySok = 799
        print("3.>> Muay Feemue Pant: 829THB")
        mauyFee = 829
        mauyPant = int(input("Select mauyShirt: "))
        amount = int(input("Enter amount: "))
        print("_____________")
        if mauyPant == 1:
            print("price :", 759 * amount, "THB")
            print("vat 7%")
            print("Total :", 759 * amount + (759 * 7 / 100), "THB")
            print("_____________")
        if mauyPant == 2:
            print("price :", 799 * amount, "THB")
            print("vat 7%")
            print("Total :", 799 * amount + (799 * 7 / 100), "THB")
            print("_____________")
        if mauyPant == 3:
            print("price :", 829 * amount, "THB")
            print("vat 7%")
            print("Total :", 829 * amount + (829 * 7 / 100), "THB")
            print("_____________")











