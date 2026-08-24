years = (int(input("Enter employee's years of service:")))
rating = (input("Enter employee's terms of service; Excellent, Good or Other"))

if years >= 5:
    if rating == "Excellent":
         bonus = 0.20
    elif rating == "Good":
         bonus = 0.10
    else:
        bonus = 0.00
else:
     if rating == "Excellent":
          bonus = 0.10
     else:
          bonus = 0.00

print(f'Employee bonus percentage is {bonus} %.')     

#Simple ATM system
balance = 50000
print("Welcome to ATM")
print("1: Withdraw money")
print("2: Check balance")
print("3: Exit")

option = int(input("What option would you prefer to selcet?"))

if option == 1:
     amount = int(input("Enter amount:"))
     if amount <= balance:
          print(' Withdrawal successful')
     else:
          print('Withdrawal amount bigger than balnce')

elif option == 2:
     print(f'Account balance is {balance}')  
     
elif option == 3:     
     print('Operation terminated. You may exit.')

else:
     print('Choice Invalid!')


#language input program
lang = input('Select a language from English, Hausa and Yoruba.')
if lang == English:
     print('Hello')

elif lang == Hausa:
     print('Barka da Zuwa')

elif lang == Yoruba:
     print('Kaabo')          

else:
     print('Language selected is invalid')