import pytest
from task_2 import mentors, courses, create_mentors_list, compair_pairs

def pytest_make_parametrize_id(val):
    return repr(val)

@pytest.fixture
def get_data_from_task_2():
    create_mentors_list(mentors)
    res = compair_pairs(create_mentors_list(mentors))
    return res