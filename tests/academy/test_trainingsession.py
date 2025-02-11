import pytest
from project.academy.training import TrainingSession, Student

class TestTrainingSessionInitiation:
    @pytest.mark.constructor
    def test_trainingsession(self):
        session = TrainingSession("formation python", 4, 10)

        assert session.subject == "Formation Python"
        assert session.seats_left == 10
        assert len(session.students) == 0

    duration_exception = [0, -1]

    @pytest.mark.constructor
    @pytest.mark.parametrize("duration", duration_exception)
    def test_must_have_one_day(self, duration):
        with pytest.raises(ValueError):
            TrainingSession("formation python", duration, 10)

@pytest.fixture
def training():
    return TrainingSession("formation python", 4, 10)

@pytest.fixture
def student_potter():
    return Student("Harry", "Potter", "Poudlard")

class TestAddStudent:

    def test_add_first_student(self, training, student_potter):
        training.add_student(student_potter)

        assert len(training.students) == 1
        assert training.students[0] == student_potter
        assert training.seats_left == 9

    @pytest.mark.xfail(reason="Need to fix this")
    def test_duplicate_student_must_raise(self, training, student_potter):
        training.add_student(student_potter)
        assert len(training.students) == 1

        with pytest.raises(ValueError):
            training.add_student(student_potter)

class TestTrainingWithStudents:
    @pytest.fixture(autouse=True)
    def add_one_student_to_training(self, training, student_potter):
        training.add_student(student_potter)


    def test_data_are_ok(self, training, student_potter):
        assert len(training.students) == 1
        assert training.students[0] == student_potter

    def test_add_new_student(self, training, student_granger):
        training.add_student(student_granger)
        assert len(training.students) == 2

def test_our_trainings(trainings):
    assert len(trainings) == 1
