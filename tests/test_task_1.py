from task_1 import mentors, create_mentors_list, create_all_names_list, sorting, count_popular_names, get_result


def test_result_1():
    res = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    create_mentors_list(mentors)
    create_all_names_list(create_mentors_list(mentors))
    sorting(create_all_names_list(create_mentors_list(mentors)))
    count_popular_names(sorting(create_all_names_list(create_mentors_list(mentors))),
                        create_all_names_list(create_mentors_list(mentors)))
    obj = get_result(count_popular_names(sorting(create_all_names_list(create_mentors_list(mentors))),
                                   create_all_names_list(create_mentors_list(mentors))))

    assert res == obj
