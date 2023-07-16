from task_1 import mentors, get_result


def test_result_1():
    res = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    obj = get_result(mentors)

    assert res == obj
