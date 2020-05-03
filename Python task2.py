#Welcome
    
import string
import random
container= []
    
#def user_details ():
first_name=input ('Enter your first name: ')
container.append("First Name: " + first_name)
      
last_name=input ('Enter your last name: '  )
container.append("Last Name: " + last_name)
      
email=input ('Enter your email: ')
container.append("Email: " + email)
     
#random password generator 
user_string = (first_name [0:2] + last_name[-2:])
        
lettersAndDigits = string.ascii_letters + string.digits
random_string = ''.join((random.choice(lettersAndDigits)
      for i in range(5)))
      
userpassword = user_string + random_string
      
# A validation function
def validation():
  print("""
        
Kindly respond with a 'yes' or 'no':
         """)
  print("Is this password '" +userpassword + "' fine by you? ")
      
  while True:
    response = input().lower()
      
    if response == "yes":
      container.append("Password: " + userpassword)
      print("These are your details:")
      for item in container:
        print(item)
          
    elif response == "no":
      def password_chooser():
        while True:
          print("Input a password of your choice: ")
          password= input()
          if len(password)<7:
            print("Your password must be 7 characters or longer.")
            password_chooser()
          else:
              container.append("Password: " + password)
              print("These are your details:")
              for item in container:
                print(item)
          break
      password_chooser()
        
    else:
      validation()
      break
      print("Can you kindly enter a yes or no?")
    break
        
validation()