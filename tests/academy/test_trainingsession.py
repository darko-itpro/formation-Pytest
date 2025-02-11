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

class TestAddStudent:
    def test_add_first_student(self):
        session = TrainingSession("formation python", 4, 10)
        student = Student("Harry", "Potter", "Poudlard")

        session.add_student(student)

        assert len(session.students) == 1
        assert session.students[0] == student
        assert session.seats_left == 9

    @pytest.mark.xfail(reason="Need to fix this")
    def test_duplicate_student_must_raise(self):
        session = TrainingSession("formation python", 4, 10)
        student = Student("Harry", "Potter", "Poudlard")
        session.add_student(student)

        with pytest.raises(ValueError):
            session.add_student(student)

