ip=input("Enter IPV4:")

ipv4=ip.split('.')
if len(ipv4)==4 and all(i.isdigit() for i in ipv4):
    ipv4=list(map(int,ipv4))

    if all(0<=i<=255 for i in ipv4):
        if ip.startswith("192.168") or ip.startswith("10.") or ip.startswith("172.16"):
            print("This is a private IP")
        else:
            print("This is Public IPv4 address.")
    else:
        print("Not a IPv4 address.")


mail = input("Enter mail:")

checkmail = "~! $%^&*_=+}{'?-"
checkmail = list(checkmail)           

if mail.endswith("@gmail.com"):
    if len(mail)>8:
        for i in range(len(checkmail)):
            if checkmail[i] in mail:
                print("invalid mail")
                print(f"Invalid character found: {checkmail[i]}")
                break
        else:
            if mail.split('@')[0].isdigit():  
                print("invalid mail")
            else:
                print("Valid Gmail address.")
                
    else:
        print("Not a Gmail address.")

else:
    print("Not a Gmail address.")
