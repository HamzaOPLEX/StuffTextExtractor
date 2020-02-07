import re
import pyperclip

# Created By HamzaOPLEX 

''' 
    1 - Just Copy The Text you want to search in
    2 - Run The Python Script
'''     

text_past = pyperclip.paste()
# search for PhoneNumbers
phone_ReEx = re.compile(r"\d{3}[._+-]?\d{3}[._+-]?\d{4}",re.DOTALL)
phoneSearch = phone_ReEx.findall(text_past)
for i in phoneSearch :
        print(i)

# search for Emails
email_RegEx = re.compile(r"[a-z0-9-]*@[a-z0-9]*.[a-z]*",re.DOTALL|re.I)
emailSearch = email_RegEx.findall(text_past)
for i in emailSearch :
        print(i)
# search for URL 
Compile = re.compile(r"http[s]?://w{3}.[a-z]*.[a-z]*",re.DOTALL|re.I)
URLsearch = Compile.findall(text_past)
for i in URLsearch :
    print(i)
