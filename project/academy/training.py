from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    first_name: str
    last_name: str
    company_name: str


class TrainingSession:
    def __init__(self, subject: str, duration: int, max_seats: int):
        self.subject = subject
        self._duration = duration
        self._students: [Student] = []
        self._max_seats = None
        self.update_seats(max_seats)

        if self._duration < 1:
            raise ValueError(f"Training duration must be greater than or equal to 1, got {self.duration}")


    def add_student(self, student: Student):
        self._students.append(student)

    def update_seats(self, new_max_seats: int):

        if new_max_seats < 1:
            raise ValueError(f"Training seats must be greater than or equal to 1, got {new_max_seats}")

        self._max_seats = new_max_seats


    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, new_subject: str):
        self._subject = new_subject.title()

    @property
    def duration(self):
        return self._duration

    @property
    def max_seats(self):
        return self._max_seats

    @property
    def students(self):
        return self._students.copy()

    @property
    def seats_left(self):
        return self._max_seats - len(self._students)
