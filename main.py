import re


def no_special_characters(usr_middle, pwd_middle, pat=re.compile('[@_!#$%^&*()<>?/\|}{~:]')):
    if pat.search(usr_middle) or pat.search(pwd_middle):
        print("Please don't use special characters")
        login()
    else:
        print("Welcome!")


def getting_middle(usr, pwd):
    # Calculate lenght and finding only 4 characters
    
    d_usr=len(usr)-4
    usr_middle=usr[(d_usr+1)//2:len(usr)-(d_usr//2)]

    d_pwd=len(pwd)-4
    pwd_middle=pwd[(d_pwd+1)//2:len(pwd)-(d_pwd//2)]

    print(usr_middle, pwd_middle)
    no_special_characters(usr_middle, pwd_middle)


def login():
    print("Login")
    print("Username:")
    usr = input().replace(" ", "")
    print("Password:")
    pwd = input()
    if re.findall("\d+", usr) or re.findall("\d+", pwd) or usr.isupper() or pwd.isupper():
        print(re.findall("\d+", usr))
        print(re.findall("\d+", pwd))
        print("Please don't use numbers or uppercase words")
        login()
    else:
        getting_middle(usr, pwd)


login()
