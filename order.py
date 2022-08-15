food=["Burger","Drink","Fries","Apple Pie"]
prices=[5,2,8,5]

myOrderFood=[]
myOrderCost=[]
total=0

print("Welcome to JmFoods")

order=input("Can I take your order?")
if order=="No":
    exit()
else:
    print("Thankyou")

nextOrder=True
counter=0
while nextOrder==True:
    foodOrder=input("Please enter item")
    if foodOrder=="Burger":
        myOrderFood.append(food[0])
        myOrderCost.append(prices[0])
        counter=counter+1
        total=total+(prices[0])

    elif foodOrder=="Drink":
        myOrderFood.append(food[1])
        myOrderCost.append(prices[1])
        counter=counter+1
        total=total+(prices[1])

    elif foodOrder=="Fries":
        myOrderFood.append(food[2])
        myOrderCost.append(prices[2])
        counter=counter+1
        total=total+(prices[2])

    elif foodOrder=="Apple Pie":
        myOrderFood.append(food[3])
        myOrderCost.append(prices[3])
        counter=counter+1
        total=total+1(prices[3])

    else:
        print("Not in the menu")
    finished=input("Have you finished ordering Y/N")
    if finished=="N":
        nextOrder=True
    else:
        nextOrder=False
y=0
print("Here is your order")
print("   ")
print("***")
while y <counter:
    print("Item: "+(myOrderFood[y]))
    print("Cost: $"+str(myOrderCost[y]))
    y=y+1

print("The final cost is $"+str(total))