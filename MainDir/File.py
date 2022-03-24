with open('dataset_3363_2.txt', 'r') as inf:
    usr_str = inf.readline()

usr_output = ""
print(usr_str)
dig = ''
cnt_let = len(usr_str)
i = 0
while i != cnt_let:
    cnt = 1

    dig = ""
    if '0' <= usr_str[i] <= '9':
        while usr_str[i].isdigit():
            dig += usr_str[i]
            i += 1
            if i == len(usr_str):
                break

        for j in range(int(dig), 1, -1):
            usr_output += usr_str[i - 1 - len(dig)]
    else:
        usr_output += usr_str[i]
        i += 1
with open('out.txt', 'w') as file_out:
    file_out.write(usr_output)
