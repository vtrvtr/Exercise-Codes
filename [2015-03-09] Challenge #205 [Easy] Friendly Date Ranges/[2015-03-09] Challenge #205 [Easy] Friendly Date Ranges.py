 # [2015-03-09] Challenge #205 [Easy] Friendly Date Ranges

ipt = '2018-07-02 2015-07-04 DMY'
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
    '1': 'st',
    '2': 'nd',
    '3': 'rd',
}


def beautiful_dates(date, month_dict, day_dict):
    first_date, second_date, mode = [w1.split('-') for w1 in date.split()]
    return '{} {} {}, {} {} {}'.format(day_dict[first_date[2]] if first_date[2] in day_dict.keys() else first_date[2],
                                       month_dict[first_date[1]], first_date[
                                           0] if first_date[0] != second_date[0] else '',
                                       day_dict[second_date[2]] if second_date[
                                           2] in day_dict.keys() else second_date[2],
                                       month_dict[second_date[1]], second_date[0] if second_date[0] != first_date[0] else '')
print beautiful_dates(ipt, month_dict, day_dict)
