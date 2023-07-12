import pytest
from task_2 import mentors, create_mentors_list, compair_pairs
from task_3 import mentors_1, courses_1, durations, get_result
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
    res = get_result(mentors_1, courses_1, durations)
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
