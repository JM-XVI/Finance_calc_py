Userinput = input("Enter your name: ")
Out_total = 0
while True:
    Outgoings = int(input("Enter outgoing value:  "))
    Out_total = Out_total + Outgoings
    a = input("Do you want to enter another outgoing value? (Enter 'y' for yes or 'n' for no)   ")
    if a == "y":  
        continue
    elif a == "n":
        print("total outgoings are:  ", Out_total)
        break
    else:
        print("the input is invalid, please try again (y for yes, n for no)    ")
        a = input("Do you want to enter another outgoing value    ")

income = float(input("Enter your income "))

final_total = (income - Out_total)
final = (final_total, Userinput)

print ("you are left with", final)

with open ("finance.txt", "w") as f:
    f.write (str(final))
    f.close()
