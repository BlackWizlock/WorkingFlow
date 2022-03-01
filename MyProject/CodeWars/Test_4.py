def assemble(arr):
    if len(arr) > 0:
        res = "*" * len(arr[0])
        res = list(res)
        for i in range(len(arr)):
            for y in range(len(arr[i])):
                if arr[i][y] != "*":
                    res[y] = arr[i][y]
        for i in range(0, len(res)):
            if "*" == res[i]:
                res.pop(i)
                res.insert(i, "#")
    else:
        return ""
    return "".join(res)



input_test = ['******', '******', '******', '******']
print(assemble(input_test))


"""
result = "abcde"


input = [
  "a*c**",
  "**cd*",
  "a*cd*"
]
result = "a#cd#"
"""