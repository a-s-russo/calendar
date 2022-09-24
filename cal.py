import calendar
import datetime


def get_calendar_numbers(month, year, weekday_start=0):
    current_date = datetime.date(year, month, 1)
    next_date_month = (current_date.month + 1) % 12
    next_date_year = current_date.year + ((current_date.month + 1) // 12)
    next_date = datetime.date(next_date_year, next_date_month, 1)
    while current_date.weekday() != weekday_start:
        current_date -= datetime.timedelta(days=1)
    days = []
    while not (current_date.month == next_date.month and len(days) % 7 == 0):
        days.append(current_date.day)
        current_date += datetime.timedelta(days=1)
    return days


def generate_month_row(month, year):
    header = calendar.month_name[month] + ' ' + str(year)
    return header.center(78)


def generate_weekdays_row(weekday_start):
    weekdays = [
        'Monday'.center(10, '.'),
        'Tuesday'.center(10, '.'),
        'Wednesday'.center(10, '.'),
        'Thursday'.center(10, '.'),
        'Friday'.center(10, '.'),
        'Saturday'.center(10, '.'),
        'Sunday'.center(10, '.'),
    ]
    weekdays_row = [
        weekdays[(weekday_start + 0) % 7],
        weekdays[(weekday_start + 1) % 7],
        weekdays[(weekday_start + 2) % 7],
        weekdays[(weekday_start + 3) % 7],
        weekdays[(weekday_start + 4) % 7],
        weekdays[(weekday_start + 5) % 7],
        weekdays[(weekday_start + 6) % 7]
    ]
    return '.' + '.'.join(weekdays_row) + '.'


def generate_line_row():
    return '----------'.join(['+'] * 8)


def generate_number_row(days):
    row = ''
    for day in days:
        row += '|' + str(day).ljust(10)
    return row + '|'


def generate_blank_row():
    return '          '.join(['|'] * 8)


def generate_calendar(month, year, days, weekday_start):
    lines = [generate_month_row(month, year), generate_weekdays_row(weekday_start)]
    num_rows = int(len(days) / 7)
    index = 0
    for row in range(num_rows):
        lines.append(generate_line_row())
        lines.append(generate_number_row(days[index:index + 7]))
        lines.append(generate_blank_row())
        lines.append(generate_blank_row())
        lines.append(generate_blank_row())
        index += 7
    lines.append(generate_line_row())
    calendar = '\n'.join(lines)
    return calendar


if __name__ == '__main__':
    year = int(input('Enter the year for the calendar:\n'))
    month = int(input('Enter the month for the calendar (1-12):\n'))
    weekday = int(input('Enter the weekday start for the calendar (Mon=0, ..., Sun=6):\n'))
    cal = generate_calendar(month, year, get_calendar_numbers(month, year, weekday_start=weekday),
                            weekday_start=weekday)
    print(cal)
    cal_filename = 'calendar_{}_{}.txt'.format(year, month)
    with open(cal_filename, 'w') as file:
        file.write(cal)
    print('Saved to: ' + cal_filename)
