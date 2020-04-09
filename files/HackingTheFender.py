'''
Created on May 18, 2019

@author: Winterberger
'''
import csv
import json

compromised_users = []

# Collect Compromised users from passwords.csv which we mysteriously obtained from The Fender
with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)
  
    for password_row in password_csv:
        #print(password_row['Username'])
        compromised_users.append(password_row['Username'])

# Save list of compromised users to a new text file
with open("compromised_users.txt","w") as compromised_user_file:
  
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)
    
# Create JSON to send to our Boss
with open("boss_message.json","w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)
    #print(json.dumps(boss_message_dict, boss_message))
  
# Delete 'passwords.csv' file
with open("new_passwords.csv","w") as new_passwords_obj:
    slash_null_sig = (""" _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/""")
    #print(slash_null_sig)
    writer = csv.writer(new_passwords_obj)
    writer.writerows(slash_null_sig)
  
# Replace original passwords file with hacked one!
with open("passwords.csv", "w") as overwrite_original_file:
    for line in new_passwords_obj:
        overwrite_original_file.writeline(line)