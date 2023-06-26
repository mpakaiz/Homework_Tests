from pprint import pprint

# # Задание "Исследуем: есть ли связь между продолжительностью курса и количеством преподавателей"

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
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

# с этого момента начинается выполнение задания 3.
# на входе у вас есть только список курсов courses_list. про исходные данные, на базе которых он был сделан, вы ничего не знаете

# Подсказка: если связь между продолжительностью курсов и количеством преподавателей есть,
# то после сортировки курсов по длительности и по количеству преподавателей курсы должны идти в одном и том же порядке
# Проверьте себя: в этом задании курсы будут идти в таком порядке:
# ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"] - по продолжительности,
# ["Python-разработчик с нуля", "Frontend-разработчик с нуля", "Fullstack-разработчик на Python", "Java-разработчик с нуля"] - по количеству преподавателей
# То есть ваш скрипт должен вывести "Связи нет", т.к. порядок оказался разный

# Подсказка 1: для сравнения используйте не названия курсов, а их порядковые номера в списке courses_list
# Подсказка 2: для сравнения сделайте пары [duration, index] и [mentors_count, index]
# Допишите код ниже, который добавляет эти пары в список duration_index и mcount_index соответственно:
# pprint(courses_list)




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

# pprint(duration_index)
# pprint(mcount_index)
# Отсортируйте список duration_index и список mcount_index
# Подсказка: функция sort() будет сортировать по первому элементу (то есть по duration и по количеству преподавателей),
# поэтому вы сразу получите правильный результат.
# Самостоятельно напишите код сортировки ниже:


# pprint(duration_index)
# pprint(mcount_index)
# # Теперь вам необходимо отделить отсортированные индексы. Перенесите их в отдельные списки:
# # indexes_d (индексы для сортировки курсов по длительности) и
# # indexes_m (индексы для сортировки курсов по количеству преподавателей)



# # Допишите код ниже:
def create_indexes_d(duration_index):
    indexes_d = []

    for duration, index in duration_index:
        indexes_d.append(index)
    return indexes_d

# для indexes_m напишите аналогичный код самостоятельно:

def create_indexes_m(mcount_index):
    indexes_m = []
    for duration, index in mcount_index:
        indexes_m.append(index)
    return indexes_m
# print(indexes_d)
# print(indexes_m)
# # Сравните два получившихся списка индексов. Если они равны, то есть индексы идут в одинаковом порядке,
# # выведите "Связь есть", если не равны - выведите "Связи нет" и ниже - номера курсов по длительности, а потом - по количеству преподавателей
# # Допишите код ниже:

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
    create_courses_list(courses, mentors, durations)
    get_duration_index(create_courses_list(courses, mentors, durations))
    get_mcount_index(create_courses_list(courses, mentors, durations))
    create_indexes_d(get_duration_index(create_courses_list(courses, mentors, durations)))
    create_indexes_m(get_mcount_index(create_courses_list(courses, mentors, durations)))
    get_result(create_indexes_d(get_duration_index(create_courses_list(courses, mentors, durations))),
               create_indexes_m(get_mcount_index(create_courses_list(courses, mentors, durations))))