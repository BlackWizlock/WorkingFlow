usr_int = 47
usr_output = list()
for i in range(1, usr_int + 1):
    cnt = 0
    while i != cnt:
        if len(usr_output) == usr_int:
            break
        else:
            usr_output += [str(i)]
            cnt += 1

    if len(usr_output) == usr_int:
        break
print(*usr_output)
