# # Задание "Исследуем: есть ли связь между продолжительностью курса и количеством преподавателей"

courses_1 = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors_1 = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


def create_courses_list(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    return courses_list


def get_duration_index(courses_list):

    duration_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course["duration"], index])
    duration_index.sort()
    return duration_index


def get_mcount_index(courses_list):
    mcount_index = []
    for index, course in enumerate(courses_list):
        mcount_index.append([len(course["mentors"]), index])  # напишите код по аналогии с duration_index
    mcount_index.sort()
    return mcount_index


def create_indexes_d(duration_index):
    indexes_d = []
    for duration, index in duration_index:
        indexes_d.append(index)
    return indexes_d


def create_indexes_m(mcount_index):
    indexes_m = []
    for duration, index in mcount_index:
        indexes_m.append(index)
    return indexes_m


def get_result(indexes_d, indexes_m):
    res = []
    print("Связь есть" if indexes_d == indexes_m else "Связи нет")
    res.append("Связь есть" if indexes_d == indexes_m else "Связи нет")
    print(f"Порядок курсов по длительности: {indexes_d}")
    res.append(f"Порядок курсов по длительности: {indexes_d}")
    print(f"Порядок курсов по количеству преподавателей: {indexes_m}")
    res.append(f"Порядок курсов по количеству преподавателей: {indexes_m}")
    return res


if __name__ == "__main__":
    create_courses_list(courses_1, mentors_1, durations)
    get_duration_index(create_courses_list(courses_1, mentors_1, durations))
    get_mcount_index(create_courses_list(courses_1, mentors_1, durations))
    create_indexes_d(get_duration_index(create_courses_list(courses_1, mentors_1, durations)))
    create_indexes_m(get_mcount_index(create_courses_list(courses_1, mentors_1, durations)))
    res = get_result(create_indexes_d(get_duration_index(create_courses_list(courses_1, mentors_1, durations))),
               create_indexes_m(get_mcount_index(create_courses_list(courses_1, mentors_1, durations))))
