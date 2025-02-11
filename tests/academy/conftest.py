import pytest
from project.academy.training import Student

@pytest.fixture
def student_granger() -> Student:
    return Student("Hermione", "Granger", "Poudlard")


@pytest.fixture
def trainings(training):
    return [training]

@pytest.fixture(scope='module')
def connect_database(request):
    pass
