n = int(input())
words = set()
words.update({str(input().lower()) for i in range(n)})
m = int(input())
strings = set()
stri = []
for i in range(m):
    stri += input().lower().split()
print(*(set(stri) - words), sep="\n")