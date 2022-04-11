line = input()
line_spaceless = ""
for i in line:
  if i not in "_ ":
    line_spaceless =line_spaceless + i
print (line_spaceless)

