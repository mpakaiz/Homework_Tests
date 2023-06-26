import pytest

from task_2 import mentors, courses, create_mentors_list, compair_pairs

@pytest.mark.parametrize(
    'expected', [
        ("На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим"),
        ("На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр,"
         " Евгений, Елена, Кирилл, Максим, Олег, Роман"),
        ("На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений"),
        ("На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим"),
        ("На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений"),
        ("На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр,"
         " Алена, Владимир, Денис, Евгений, Эдгар")
    ])



def test_result_2(get_data_from_task_2, expected):
    # create_mentors_list(mentors)
    # res = compair_pairs(create_mentors_list(mentors))
    for i in get_data_from_task_2:
        assert i == expected
