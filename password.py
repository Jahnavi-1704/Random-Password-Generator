import random
import string

#A function to shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#The Main program starts here

length=int(input("Enter the password length: "))
password=""
j=1

if(input("Do you want a mixed password?")=='Y'):
  for x in range(length):
    if(j==1):
      uppercaseLetter1=chr(random.randint(65,90)) 
      password=password + uppercaseLetter1
      j=j+1
      
    elif(j==2):
      lowercaseLetter1=chr(random.randint(97,122))
      password=password + lowercaseLetter1
      j=j+1
      
    elif(j==3):
      digit1=chr(random.randint(48,57))
      password=password + digit1
      j=j+1
      
    elif(j==4):
      punctuationSign1=chr(random.randint(33,126))
      password=password + punctuationSign1
      j=1
    
elif(input("Do you want only an uppercase password?")=='Y'):
  for x in range(length):
    uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    password=password + uppercaseLetter1

elif(input("Do you want only a lowercase password?")=='Y'):
  for x in range(length):
    lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
    password=password + lowercaseLetter1
    
elif(input("Do you want only a digit password?")=='Y'):
  for x in range(length):
    digit1=chr(random.randint(48,57))
    password=password + digit1
    
elif(input("Do you want only a symbolic password?")=='Y'):
  for x in range(length):
    punctuationSign1=chr(random.randint(33,126)) #Generate a random punctuation sign (based on ASCII code)
    password=password + punctuationSign1
    
    
#Generate password using all the characters, in random order
#password = uppercaseLetter1 + lowercaseLetter1 + digit1 + punctuationSign1

password = shuffle(password)

#Output
print(password)
