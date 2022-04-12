cities = [{
		"pk":     1,
		"fields": {
				"name":       "Рим",
				"timezone":   "GMT+1",
				"country":    3,
				"country_ru": "Италия"
		}
},
		{
				"pk":     2,
				"fields": {
						"name":       "Милан",
						"timezone":   "GMT+1",
						"country":    3,
						"country_ru": "Италия"
				}
		},
		{
				"pk":     3,
				"fields": {
						"name":       "Венеция",
						"timezone":   "GMT+1",
						"country":    3,
						"country_ru": "Италия"
				}
		},
		{
				"pk":     4,
				"fields": {
						"name":       "Стамбул",
						"timezone":   "GMT+3",
						"country":    4,
						"country_ru": "Турция"
				}
		},
		{
				"pk":     5,
				"fields": {
						"name":       "Кемер",
						"timezone":   "GMT+3",
						"country":    4,
						"country_ru": "Турция"
				}
		},
		{
				"pk":     6,
				"fields": {
						"name":       "Сиде",
						"timezone":   "GMT+3",
						"country":    4,
						"country_ru": "Турция"
				}
		},
		{
				"pk":     7,
				"fields": {
						"name":       "Тбилиси",
						"timezone":   "GMT+4",
						"country":    2,
						"country_ru": "Грузия"
				}
		},
		{
				"pk":     8,
				"fields": {
						"name":       "Казбеги",
						"timezone":   "GMT+4",
						"country":    2,
						"country_ru": "Грузия"
				}
		},
		{
				"pk":     9,
				"fields": {
						"name":       "Хельсинки",
						"timezone":   "GMT+2",
						"country":    5,
						"country_ru": "Финляндия"
				}
		},
		{
				"pk":     10,
				"fields": {
						"name":       "Санкт-Петербург",
						"timezone":   "GMT+3",
						"country":    1,
						"country_ru": "Россия"
				}
		},
		{
				"pk":     11,
				"fields": {
						"name":       "Москва",
						"timezone":   "GMT+3",
						"country":    1,
						"country_ru": "Россия"
				}
		},
		{
				"pk":     12,
				"fields": {
						"name":       "Казань",
						"timezone":   "GMT+3",
						"country":    1,
						"country_ru": "Россия"
				}
		},
		{
				"pk":     13,
				"fields": {
						"name":       "Сочи",
						"timezone":   "GMT+3",
						"country":    1,
						"country_ru": "Россия"
				}
		},
		{
				"pk":     14,
				"fields": {
						"name":       "Псков",
						"timezone":   "GMT+3",
						"country":    1,
						"country_ru": "Россия"
				}
		},
		{
				"pk":     15,
				"fields": {
						"name":       "Нижний Новгород",
						"timezone":   "GMT+3",
						"country":    1,
						"country_ru": "Россия"
				},
		},
]

new_cities = {}


def main():
	for city in cities:
		if city["fields"]["country_ru"] not in new_cities.keys():
			new_cities[city["fields"]["country_ru"]] = [city["fields"]["name"]]
			print(city["fields"]["country_ru"])
			print(f'- {city["fields"]["name"]}')
		else:
			new_cities[city["fields"]["country_ru"]].append(city["fields"]["name"])
	for key, values in new_cities.items():
		print(key)
		for value in values:
			print(f'- {value}')


if __name__ == '__main__':
	main()
