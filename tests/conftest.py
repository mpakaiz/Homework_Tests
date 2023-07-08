import pytest
from task_2 import mentors, courses, create_mentors_list, compair_pairs
from task_3 import courses_1, mentors_1, durations, create_courses_list, get_duration_index, get_mcount_index, \
    create_indexes_d, create_indexes_m, get_result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture()
def get_data_from_task_2():
    create_mentors_list(mentors)
    res = compair_pairs(create_mentors_list(mentors))
    return res


@pytest.fixture()
def get_data_from_task_3():
    create_courses_list(courses_1, mentors_1, durations)
    get_duration_index(create_courses_list(courses_1, mentors_1, durations))
    get_mcount_index(create_courses_list(courses_1, mentors_1, durations))
    create_indexes_d(get_duration_index(create_courses_list(courses_1, mentors_1, durations)))
    create_indexes_m(get_mcount_index(create_courses_list(courses_1, mentors_1, durations)))
    res = get_result(create_indexes_d(get_duration_index(create_courses_list(courses_1, mentors_1, durations))),
               create_indexes_m(get_mcount_index(create_courses_list(courses_1, mentors_1, durations))))
    return res


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    driver = webdriver.Chrome(service=driver_service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()
