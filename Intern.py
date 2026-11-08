from Employee import*
class Intern(Employee):
    def __init__(self, name, salary,months_must_be):
        super().__init__(name, salary)
        self.months_must_be=months_must_be
        if self.months_must_be<1 or self.months_must_be>12:
            raise ValueError("months must be 1-12")

    def title(self):
        return "Intern"


