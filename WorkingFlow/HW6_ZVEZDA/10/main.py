import csv


def read_file(filename: str):
	lst_file_data = list()
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			lst_file_data.append(row)
	return lst_file_data


def logic(lst_file_data: list):
	output_list = list()
	for i in lst_file_data:
		usr_sum = 0
		for j in range(1, 4):
			usr_sum += int(i[j])
		output_list.append(f'{str(i[0])} {str(round(usr_sum / 3, 1))}')
	return output_list


def main():
	lst_file_data = read_file('db.csv')
	print(*logic(lst_file_data), sep='\n')


if __name__ == '__main__':
	main()
