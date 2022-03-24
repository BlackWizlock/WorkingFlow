# "Программа принимает на вход две строки одинаковой длины,
# на первой строке записаны символы исходного алфавита,
# на второй строке — символы конечного алфавита,
# после чего идёт строка, которую нужно зашифровать переданным ключом,
# и ещё одна строка, которую нужно расшифровать."

n = 4
usr_input = [str(input()) for x in range(n)]
dct_translate, dct_untranslate, usr_out_1, usr_out_2 = dict(), dict(), str(), str()

for i in range(0, len(usr_input[0])):
    dct_translate.update({usr_input[0][i]: usr_input[1][i]})
    dct_untranslate.update({usr_input[1][i]: usr_input[0][i]})

for i in range(0, len(usr_input[2])):
    usr_out_1 += dct_translate.get(usr_input[2][i])
print(usr_out_1)

for i in range(0, len(usr_input[3])):
    usr_out_2 += dct_untranslate.get(usr_input[3][i])
print(usr_out_2)