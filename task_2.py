
# # Задание "Суперимена: преподаватели с какими именами учат сразу на двух курсах?"

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

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
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            name = name.split(' ')[0]
            course_names.append(name)
        mentors_names.append(course_names)
    return mentors_names


def compair_pairs(mentors_names):
    pairs = []
    res = []
# # попарное сравнение "наборов" преподавателей на курсах. каждую новую пару запоминаем для исключения повторов.
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
            if pair not in pairs:
                pairs.append(pair)
                all_names_sorted = sorted(intersection_set)
                all_names_sorted = ', '.join(all_names_sorted)

                print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {all_names_sorted}")
                # yield (f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {all_names_sorted}")
                res.append(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {all_names_sorted}")
    return res


if __name__ == "__main__":
    create_mentors_list(mentors)
    compair_pairs(create_mentors_list(mentors))
