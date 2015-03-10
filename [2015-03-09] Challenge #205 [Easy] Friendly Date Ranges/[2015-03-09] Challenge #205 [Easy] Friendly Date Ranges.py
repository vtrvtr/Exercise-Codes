 # [2015-03-09] Challenge #205 [Easy] Friendly Date Ranges

ipt = '2015-04-01 2020-09-10 DMY'
month_dict = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}
day_dict = {
    1: 'st',
    2: 'nd',
    3: 'rd',
    4: 'th',
    5: 'th',
    6: 'th',
    7: 'th',
    8: 'th',
    9: 'th',
}


def beautiful_dates(date, month_dict, day_dict):
    first_date, second_date, mode = [w1.split('-') for w1 in date.split()]
    month1, day1, year1 = fix_date(first_date, day_dict, month_dict)
    month2, day2, year2 = fix_date(second_date, day_dict, month_dict)
    return '{} {}{} - {} {}{}'.format(month1, day1, ', '+year1 if year1 != year2 else '',
        month2 if month2 != month1 else '', day2, ', '+year2 if year2 == year1 else '')



def fix_date(date, day_dict, month_dict):    
    year = date[0]
    month = date[1]
    day = int(date[2])
    return [month_dict[month], '{}{}'.format(day, day_dict[day] if day <= 4 else day_dict[day%9]), year]

print beautiful_dates(ipt, month_dict, day_dict)