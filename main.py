import datetime
import emoji
from application.salary import calculate_salary
from application.db.people import get_employees

def print_script():
    print(f'{datetime.datetime.now()} : {calculate_salary()}')
    print(f'{datetime.datetime.now()} : {get_employees()}')

if __name__ == '__main__':
    print_script()
    print(emoji.emojize('отлично поработали, коллеги :thumbs_up:'))