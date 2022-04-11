import string

user_str = "Если «если» перед «после», значит «после» после «если»."
symbols_alphabet = string.punctuation + "«»"
for i in symbols_alphabet:
    user_str = user_str.replace(i, "")
user_lst = user_str.split()
for i in range(0, len(user_lst)):
    user_lst[i] = user_lst[i].lower()
user_dict = {k : user_lst.count(k) for k in user_lst}        
print(f'Всего слов: {sum(user_dict.values())}')
for k, v in user_dict.items():
    print(f'{k:10} - {v:2}')
    