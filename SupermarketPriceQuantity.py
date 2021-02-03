p1 = int(input("Enter Price 1: "))
q1= int(input("Enter Quantity 1: "))
p2 = int(input("Enter Price 2: "))
q2=int(input("Enter Quantity 2: "))
p3 = int(input("Enter Price 3: "))
q3=int(input("Enter Quantity 3: "))
p4 = int(input("Enter Price 4: "))
q4=int(input("Enter Quantity 4: "))
p5 = int(input("Enter Price 5: "))
q5=int(input("Enter Quantity 5: "))
a=int(input("Enter Amount: "))
total = p1*q1+p2*q2+p3*q3+p4*q4+p5*q5
print("Total Amount Payable:",total)
b=total-a
print("Balance Amount is:",b)
discount=total/100*10
print("Discount Price:",discount)