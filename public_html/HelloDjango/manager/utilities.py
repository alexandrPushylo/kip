from datetime import date, timedelta
import locale
from random import choice
#---------------------------------------------------

ONE_DAY = timedelta(days=1)
STATUS_APPLICATION = {"Подтвержден", "Не подтвержден", "Отменен"}
WEEKDAY = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
TODAY = date.today()
TOMORROW = TODAY + ONE_DAY
choice_day = {'today': TODAY, 'next_day': TOMORROW}
dict_Staff = {'admin': 'Администратор', 'foreman': 'Прораб', 'master': 'Мастер', 'driver': 'Водитель', 'mechanic': 'Механик', 'employee_supply': 'Снабжение'}
status_application = {'absent': 'Отсутствует', 'saved': 'Сохранена', 'submitted': 'Подана', 'approved': 'Одобрена'}
status_constr_site = {'closed': 'Закрыт', 'opened': 'Открыт'}

#--FUNCTIONS-------------------------------------------------
def set_locale(): locale.setlocale(locale.LC_ALL, 'ru-RU')

def get_day_in_days(day: date, count_days: int):
    return day + timedelta(count_days)

def get_difference(a: set, b: set):
    return list(a.difference(b))

def get_week(c_date, week=None):
    if week == 'l':
        curr_date = c_date - timedelta(7)
    elif week == 'n':
        curr_date = c_date + timedelta(7)
    else:
        curr_date = c_date
    day_idx = (curr_date.weekday()) % 7
    sunday = curr_date - timedelta(days=day_idx)
    curr_date = sunday
    for n in range(7):
        yield curr_date
        curr_date += ONE_DAY

