import requests, random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.decode('utf-8').splitlines()

for word in WORDS:
	if 1 <= len(word) <= 2:
		WORDS.remove(word)

print(WORDS)

for i in range(6):
	print(random.choice(WORDS))
