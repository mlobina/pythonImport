from application.salary import calculate_salary
from application.people import get_employees
from application.query_date import query_date

def main():
    query_date()
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()
