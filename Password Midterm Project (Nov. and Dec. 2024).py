# Import string and random module
import random

# Instantiate starting variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
evenLength = True
letterSum = 0
randomNum = 0
password = ""
allowSpecialChar = True
yesOrNo = ""

# Prompt user for minimum length of the password
length = int(input("What is the minimum length of the password?: "))

# Asks user if the password can include special characters
yesOrNo = input("Can the password include special characters? (Y or N):")
if yesOrNo == "N":
  allowSpecialChar = False

# Determines if given length is even or odd
if length % 2 == 1:
  evenLength = False
 
# Generates random letters
for i in range(length):
  randomNum = random.randint(0, 25)
  savedLetter = alphabet[randomNum : randomNum + 1]
 
  if evenLength == False: # Length is odd
   
    if randomNum % 2 == 0:
      password += savedLetter
    else:
      password += savedLetter.upper()
  else: # Length is even
   
    if randomNum % 2 == 0:
      password += savedLetter.upper()
    else:
      password += savedLetter
  letterSum += randomNum
 
# Generates random symbol based on letterSum (if allowSpecialNum is true)
letterSum = letterSum % 10

if allowSpecialChar:
  if letterSum >= 8:
    password += "_"
  elif letterSum >= 5:
    password += "@"
  elif letterSum >= 2:
    password += "-"
  else:
    password += "!"

# Generate random numbers
for i in range(length//2):
    password += str(random.randint(0, 9))

# Print final password
print("\Generated password: " + password)

# NOTICE: I updated the program to where the special character is optional, and I made it to where the random special character is based on the one’s place value of letterSum

# Strengths of Program: Customizable minimal length, cannot be determined by the website's name, includes both uppercase and lowercase letters

# Weaknesses of Program: Couldn't work for passwords that can only use specific special characters
