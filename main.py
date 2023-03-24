
import random
print("""
                               ****WELCOME  TO  RANDOM  PASSWORD  GENERATOR****
""")

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_" 
while True:
  
  no_of_password=int(input("Enter the number of passwords you want:"))
  length_of_password=int(input("Enter the length of required passwords:"))

  for i in range(no_of_password):
     password=str()

     for j in range(length_of_password):
        char_pick=random.choice(characters)
        password+=char_pick
     print(f"The Random password generated is {password}")

  if (choice:=input("Do your want to continue generating more passwords(yes/no):").lower()) == "no":
        break
  else:
        continue
  

print("""                                           Thankyou!                                                 """)

