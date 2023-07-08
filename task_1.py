# # Задание "Узнайте топ-3 популярных имен"

courses = [
	"Python-разработчик с нуля", "Java-разработчик с нуля",
		   "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"
	]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
	 "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
	 "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
	 "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
	 "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
	 "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
	 "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
	 "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
	 "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def create_mentors_list(mentors):
	all_list = []
	for m in mentors:
		all_list.extend(m)
	return all_list


def create_all_names_list(all_list):
	all_names_list = []
	index = 0
	for mentor in all_list:
		name = all_list[index].split(' ')
		index += 1
		all_names_list.append(name[0])
	return all_names_list


def sorting(all_names_list):
	unique_names = set(all_names_list)
	all_names_sorted = sorted(unique_names)
	all_names_sorted = ', '.join(all_names_sorted)
	return unique_names


def count_popular_names(unique_names, all_names_list):
	popular = []
	for name in unique_names:
		popular.append([name, all_names_list.count(name)])
	popular.sort(key=lambda x: x[1], reverse=True)
	return popular


def get_result(popular):
	top_3 = popular[0:3]
	result = f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а),' \
			 f' {top_3[2][0]}: {top_3[2][1]} раз(а)'
	print(f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а),'
		  f' {top_3[2][0]}: {top_3[2][1]} раз(а)')
	return result


if __name__ == "__main__":

	create_mentors_list(mentors)
	create_all_names_list(create_mentors_list(mentors))
	sorting(create_all_names_list(create_mentors_list(mentors)))
	count_popular_names(sorting(create_all_names_list(create_mentors_list(mentors))),
						create_all_names_list(create_mentors_list(mentors)))
	get_result(count_popular_names(sorting(create_all_names_list(create_mentors_list(mentors))),
								create_all_names_list(create_mentors_list(mentors))))
