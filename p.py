print("="*30,"HELLO WELCOME TO PIZZA HUT","="*30)
print("WOULD YOU LIKE TO SEE THE MENU")
ch = input("")
if ch == "yes":
    print("Available Pizza's Today in the menu are:")
    prices = {"pizza":150.0,"chicken pizza":200.0,"onion pizza":180.0,"double cheese pizza":190.0}
    print("\t1. pizza:",prices.get("pizza"))
    print("\t2. chicken pizza:",prices.get("chicken pizza"))
    print("\t3. onion pizza:",prices.get("onion pizza"))
    print("\t4. double cheese pizza:",prices.get("double cheese pizza"))
    

    choice = int(input("what would you like to order enter the number(1,2,3,4):"))
    comform =  input("would you like to order:")
    if comform == "yes":
        match(choice):
            case 1:
                print("hi i am pizza")
    else:
        pass
      
else:
    print("THANK YOU VISIT US AGAIN")
