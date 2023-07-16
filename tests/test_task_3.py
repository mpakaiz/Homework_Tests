
obj = [
        'Связи нет', 'Порядок курсов по длительности: [2, 0, 1, 3]',
       'Порядок курсов по количеству преподавателей: [2, 3, 1, 0]'
    ]


def test_result_3(get_data_from_task_3):
    assert get_data_from_task_3 == obj

def test_result_5(get_data_from_task_3):
    assert len(get_data_from_task_3) == len(obj)

