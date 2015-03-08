 # [2015-02-18] Challenge #202 [Intermediate] Easter Challenge
from datetime import datetime
import sys

def easter(date):
    _, a = divmod(date, 19)
    b, c = divmod(date, 100)
    d, e = divmod(b, 4)
    g, _ = divmod(8 * b + 13, 25)
    _, h = divmod(19 * a + b - d - g + 15, 30)
    m, _ = divmod(a + 11 * h, 319)
    j, k = divmod(c, 4)
    _, l = divmod(2 * e + 2 * j - k - h + m + 32, 7l)
    n, _ = divmod(h - m + l + 90, 25)
    _, p = divmod(h - m + l + n + 19, 32)
    month = 'April' if n == 4 else 'March'
    return "{} {} {}".format(p, month, date)

print easter(2900)

