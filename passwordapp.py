def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception('Şifre en az 9 karakterde olmalidir!')
    elif not re.search("[a-z]",psw):
        raise Exception('parola küçük harf içermelidir! ')
    elif not re.search("[A-Z]",psw):
        raise Exception('parola büyük harf içermelidir! ')
    elif not re.search("[0-9]",psw):
        raise Exception('parola rakam içermelidir! ')
    
    else: 
        print("Geçerli parola")
    
password = '123w45'

try:
    check_password(password)
except Exception as ex:
    print(ex)
finally:
    print("Validration tamamlandi! ")