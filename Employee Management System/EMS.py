class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.annual_salary = 0

    def calculate_annual_salary(self):
        self.annual_salary = self.salary*12
        return self.annual_salary

    def bonus(self, score):
        if score >= 90:
            self.salary += 100

    def promotion(self, score, years):
        return 'Better luck next time'
       
    def __str__(self):
        return f'{self.name},{self.age},{self.salary}'


class Manager(Employee):
    PROMOTION_SCORE = 90
    PROMOTION_YEARS = 5

    def promotion(self, score, years):
        if score >= self.PROMOTION_SCORE and years >= self.PROMOTION_YEARS:
            return 'Promoted to CTO'
        return super().promotion(score, years)


class Engineer(Employee):
    PROMOTION_SCORE = 90
    PROMOTION_YEARS = 2

    def promotion(self, score, years):
        if score >= self.PROMOTION_SCORE and years >= self.PROMOTION_YEARS:
            return 'Promoted to manager'
        return super().promotion(score, years)


class Intern(Employee):
    PROMOTION_SCORE = 90
    PROMOTION_YEARS = 1

    def promotion(self, score, years):
        if score >= self.PROMOTION_SCORE and years >= self.PROMOTION_YEARS:
            return 'Promoted to engineer'
        return super().promotion(score, years)

intern = Intern('David', 25, 1000)
print(intern.promotion(12, 1.5))
