from application import salary as s
from application.DB import people as p
from datetime import datetime


if __name__ == '__main__':
    today = datetime.today()
    print(today.date())
    p.get_employees()
    s.calculate_salary()