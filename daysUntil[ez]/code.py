from datetime import date
import pywinusb.hid as hid
import random

def untilDay(next_date):
    year, month, day = [int(part) for part in next_date.split()]
    return '{} until {}'.format(abs(date.today() -
                                    date(year, month, day)),
                                '{}/{}/{}'.format(year, month, day))


#print untilDay('2015 2 14')


