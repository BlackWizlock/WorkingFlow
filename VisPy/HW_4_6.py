user_input = "Архангельск - Краков - Восква"
user_input = user_input.split(" - ")
if len(user_input) != len(set(user_input)):
    print("Правила нарушены")
else:    
    counter = set()
    for i in range(0, len(user_input)-1):
        if user_input[i][-1:] in ("ьы"):
            user_input[i] = user_input[i][0:-1]
        counter.add(user_input[i].lower()[-1:] == user_input[i+1].lower()[0])
    
    if all(counter):    
        print("Правила не нарушены")
    else:
        print("Правила нарушены")