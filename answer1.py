import re

def validate_ip(ip):
    parts = ip.split('.')
    if len(parts) == 4 and all(p.isdigit() for p in parts):
        nums = list(map(int, parts))
        if all(0 <= num <= 255 for num in nums):
            if ip.startswith("192.168") or ip.startswith("10.") or ip.startswith("172.16"):
                return "Invalid: This is a private IP, not a public IP."
            return "Valid public IPv4 address."
    return "Invalid: Not a valid IPv4 address."

def validate_gmail(email):
    if re.match(r'^[a-z0-9._%+-]+@gmail\.com$', email):
        return "Valid Gmail address."
    return "Invalid: Not a valid Gmail address."


ip_address_input = "192.168.1.1"  
email_input = "example@gmail.com"  

print("IP Validation:", validate_ip(ip_address_input))
print("Email Validation:", validate_gmail(email_input))
