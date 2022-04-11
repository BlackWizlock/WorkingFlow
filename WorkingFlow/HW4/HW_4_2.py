login, password = input("Введите логин : \t"), input("Введите пароль : \t")
if len(login) > 3 and len(password) >= 8 and len(set(map(password.count,"0123456789"))) > 1:
    print("Это хорошие логин и пароль!")
else:    
    if len(login) <= 3:
        print("Логин должен содержать больше 3 символов.")
    if len(password) <= 8:
        print("Пароль должен содержать больше 8 символов.")
    if len(set(map(password.count,"0123456789"))) == 1:
        print("Пароль должен содержать хотя бы одну цифру.")
        