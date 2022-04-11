free_mail_domain = ["yandex.ru", "mail.ru", "gmail.com" , "yahoo.com", "rambler.ru"]
user_mail = input("Enter e-mail address : \t")
user_mail = user_mail.partition("@")
if len(user_mail) != 3:
    print("Это вообще не почта")
else:
    if user_mail[2] in free_mail_domain:
        print("Это почта, она на бесплатном домене")
    else:
        print("Это почта, она на корпоративном домене")

