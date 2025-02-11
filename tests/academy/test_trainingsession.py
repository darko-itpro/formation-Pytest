import pytest
from project.academy.training import TrainingSession, Student

class TestTrainingSessionInitiation:
    def test_trainingsession(self):
        session = TrainingSession("formation python", 4, 10)

        assert session.subject == "Formation Python"
        assert session.seats_left == 10
        assert len(session.students) == 0

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

