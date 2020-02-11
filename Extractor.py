import re
import pyperclip

''' 
        1- add all copy in a variable 
        2- search in the variable (use re.DOTALL cause we have "\n")
        2-1- first = search for numbers
        2-2- second = search fo emails
'''     

text_past = pyperclip.paste()
# search for PhoneNumbers
phone_ReEx = re.compile(r"\d{3}[._+-]\d{3}[._+-]\d{4}",re.DOTALL)
phoneSearch = phone_ReEx.findall(text_past)
for i in phoneSearch :
        print(i)

# search for Emails
email_RegEx = re.compile(r"[a-z0-9-]*@[a-z0-9]+.\w+",re.DOTALL|re.I)
emailSearch = email_RegEx.findall(text_past)
for i in emailSearch :
        print(i)
#Search For URL that srart with HTTPS / HTTP
Compile = re.compile(r"http[s]?://(www\.)?[a-z]*.[a-z]*",DOTALL|re.I) #Or 'https?://(www\.)?\w+\.\w+'
URLsearch = Compile.finditer(text_past)
for i in URLsearch :
	a = str(i)
	print(re.search("http[s]?://(www\.)?[a-z]*.[a-z]*",a).group())
