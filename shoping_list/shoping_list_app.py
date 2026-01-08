menu=("1.add","2.remove","3.show","4.exit")
user_additem=[]
while True:
   print("\nmenu")
   for item in menu:
      print(item)

   user_input=int(input("Enter Your choices : "))

   if user_input==1: 
     user_add=input("item name: ")
     user_additem.append(user_add)
     
   elif user_input==2:
     print(user_additem)
     user_remove=input(" remove item name: ")
     if user_remove  in user_additem:
       up=user_additem.remove(user_remove)
       up=user_additem
     else:
       print("enter valid item from the list")
       user_remove=input(" remove item name: ")

   elif user_input == 3:
        print("Your items:", user_additem)

   elif user_input == 4:
        print("Exit")
        break

   else:
        print("Invalid choice. Please select from the menu.")










