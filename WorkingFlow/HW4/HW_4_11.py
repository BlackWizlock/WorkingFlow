user_input = [
    "офицер",
    "персей",
    "плюсна",
    "подруб",
    "подряд",
    "полиол",
    "популо",
    "свекла",
    "сизетт",
    "синьор",
    "усилие",
    "утенок",
]

print(
    {key: [x[0] for x in user_input].count(key) for key in [x[0] for x in user_input]}
)
