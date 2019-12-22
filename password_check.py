import re
def password_check(password):
    if len(password) < 6 or len(password) > 16:
        return "Your password must be between 6 and 16 characters"
    else:
        if not re.search('[a-z]',password):
            return "Your password must contain at least one lowercase letter"
        elif not re.search('[A-Z]',password):
            return "Your password must contain at least one uppercase letter"
        elif not re.search('[0-9]',password):
            return "Your password must contain at least one number"
        elif not re.search('[$|#|@]',password):
            return "Your password must contain at least one symbol from #, @ or $"
        else:
            return "Your password meets all requirements"

print(password_check("123456")) #Fails - no lowercase letters
print(password_check("123456abcABC@")) #Succeeds
print(password_check("123456g@")) #Fails - no uppercase letters
print(password_check("123456aA")) #Fails - no symbols
print(password_check("Aa1@")) #Fails - too short
