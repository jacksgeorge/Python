salary=float(input("How much do you make a year? " ))
percent=float(input("How much is your raise? "))
percent=percent/100
new=(salary*percent)+salary
month=new/12
home=month-(month*0.23)
print("Your new salary is:",new)
print("your monthly take home is:",home) 