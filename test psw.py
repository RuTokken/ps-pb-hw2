psw = input('Введите пароль') 
a = 0
result = 0
try:
    result = a/len(psw)
    result = int(psw) 
    print('пароль только из цифр')
except ZeroDivisionError:
    print('пустой пароль')
except:
    print('требования к паролю соблюдены') 