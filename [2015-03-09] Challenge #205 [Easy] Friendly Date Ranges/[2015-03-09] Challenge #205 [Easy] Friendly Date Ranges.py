 # [2015-03-09] Challenge #205 [Easy] Friendly Date Ranges

ipt = '2018-07-22 2015-07-04 DMY'
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
}


def beautiful_dates(date, month_dict, day_dict):
    first_date, second_date, mode = [w1.split('-') for w1 in date.split()]

    return fix_date(first_date, day_dict, month_dict), fix_date(second_date, day_dict, month_dict)



def fix_date(date, day_dict, month_dict):    
    year = date[0]
    month = date[1]
    # day = date[2][1] if date[2][0] == '0' else date[2]
    day = int(date[2])
    return [month_dict[month], '{}{}'.format(day, day_dict[day] if day <= 4 else day_dict[day%4]), year]

print beautiful_dates(ipt, month_dict, day_dict)