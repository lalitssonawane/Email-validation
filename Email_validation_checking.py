
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('Enter user email ID : ')
if re.search(email_condition,user_email) : 
    print('Valid Email')
else : 
    print('Invalid Email')