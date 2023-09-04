import datetime


def get_birthdays_per_week(users):
    today = datetime.date.today()

    current_weekday = today.weekday()

    start_of_week = today - datetime.timedelta(days=current_weekday)
    end_of_week = start_of_week + datetime.timedelta(days=6)

    birthdays_by_day = {i: [] for i in range(7)}



    for user in users:
        birthday = user['birthday'].replace(year=today.year)
        if start_of_week <= birthday <= end_of_week:
            birthday_weekday = birthday.weekday()
            if birthday_weekday in (5, 6):
                birthday += datetime.timedelta(days=(7-birthday_weekday))
            birthdays_by_day[birthday.weekday()].append(user['name'])
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for i in range(7):
        day = weekdays[i]
        if birthdays_by_day[i]:
            print(f"{day}: {', '.join(birthdays_by_day[i])}")



users = [
    {'name': 'Bill', 'birthday': datetime.date(2000, 9, 4)},
    {'name': 'Jill', 'birthday': datetime.date(2001, 9, 5)},
    {'name': 'Kim', 'birthday': datetime.date(2002, 9, 9)},
    {'name': 'Jan', 'birthday': datetime.date(2003, 9, 10)},
]

get_birthdays_per_week(users)
