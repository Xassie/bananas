"""
Написать программу реализующую хранение информации об ВУЗах.
Структура: наименование, год открытия, количество факультетов,
количество студентов.
Программа должна позволять:
а) загружать информацию из файла;
б) выполнять поиск товара по наименованию;
в) фильтровать товары по количеству студентов;
г) добавлять записи;
д) удалять записи;
е) сохранять данные в файле.
Для выполнения задания используйте стандартный модуль csv
"""


import csv


def start_function():
	with open('py.csv', 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=";")
		next(csv_reader)
		for line in csv_reader:
			print(line)


def find_function():
	with open('py.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=";")
		a = input('name/year/n_fac/n_stud: ')
		b = input('value: ')
		for line in csv_reader:
			if line[a] == b:
				print(line)
			"""
			a может принимать следующие значения:
				a = [name,year,n_far,n_stud]
			"""
			# print(line[a])


def filter_function():
	with open('py.csv', 'r') as csv_file:
		a = []
		csv_reader = csv.DictReader(csv_file, delimiter=";")
		for line in csv_reader:
			a.append(dict(line))
		for i in range(len(a)):
			a[i]['n_stud'] = int(a[i]['n_stud'])
		for r in sorted(a, key=lambda x: -x['n_stud']):
			print(r)


def append_function():
	with open('py.csv', 'a+', newline='') as file:
		writer = csv.writer(file, delimiter=";")
		inp = input("Данные о вузе через пробел: ").split(" ")
		"""
		inp должна принмать 4 значения.
		"""
		writer.writerow(inp)


def deleted_function():
	with open('py.csv', 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file, delimiter=";")
		with open('new_names.csv', 'w', newline="") as new_file:
			fieldnames = ['name','n_fac','year','n_stud']
			csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter=";") 
			csv_writer.writeheader()
			a = input('name/year/n_fac/n_stud: ')
			b = input('value: ')
			for line in csv_reader:
				if line[a] == b:
					del line
				else:
					csv_writer.writerow(line)


if __name__ == "__main__":
	choise = input("Выберите команду: start_function,find_function\n"
		"filter_function, append_function, deleted_function\n").lower()
	if choise == "start_function":
		start_function()
	elif choise == "find_function":
		find_function()
	elif choise == "filter_function":
		filter_function()
	elif choise == "append_function":
		append_function()
	elif choise == "deleted_function":
		deleted_function()
