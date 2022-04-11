with open ('dataset_3363_3.txt', 'r') as inf:
    s2=inf.read().strip().lower()
s=[str(i) for i in s2.split()]
count=0
c=0
for i in s:
    if s.count(i)>=count:
        count=s.count(i)
        c=i
with open ('output.txt', 'w') as out:
    out.write(c)
    out.write(" ")
    out.write(str(count))