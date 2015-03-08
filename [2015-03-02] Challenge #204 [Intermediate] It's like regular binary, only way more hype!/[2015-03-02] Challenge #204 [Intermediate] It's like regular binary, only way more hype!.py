 #[2015-03-02] Challenge #204 [Intermediate] It's like regular binary, only way more hype!



import sys

class ANPlusB(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def Sub(self, n_plus):
    return ANPlusB(self.a, self.b + self.a * n_plus)

  def Eval(self, n):
    return self.a * n + self.b

  def __str__(self):
    if self.b < 0:
      s = "-"
      b = - self.b
    else:
      s = "+"
      b = self.b
    return "% 4sn %s % 4s" % (self.a, s, b)

  def __add__(self, other):
    return ANPlusB(self.a + other.a, self.b + other.b)

  def __sub__(self, other):
    return ANPlusB(self.a - other.a, self.b - other.b)


TABLE = {-2: ANPlusB(1, -1),
         -1: ANPlusB(0, 1),
          0: ANPlusB(1, 1),
          1: ANPlusB(1, 0),
        }
biggest = 1
smallest = -1


def F(n_plus, k):
  """Find the a*n +b for 2^(n + n_plus) + k ."""
  # Note something is broken for negaitve n_plus, going below -10
  # causes infinite recursion.
  global smallest, biggest
  if k not in TABLE:
    if k < smallest:
      val = _FSmaller(k)
      smallest = k
    else:
      val = _FBigger(k)
      biggest = k
    TABLE[k] = val
  val = TABLE[k]
  return val.Sub(n_plus)


def _FBigger(k):
  if k % 2:
    return F(0, k - 1) - F(0, k - 2)
  else:
    return F(-1, k / 2) + F(-1, (k / 2) - 1)


def _FSmaller(k):
  if k % 2:
    return F(0, k + 2) - F(0, k + 1)
  else:
    return F(-1, k / 2) + F(-1, (k / 2) - 1)


def main():
  min, max = [int(x) for x in sys.argv[1:]]

  for i in range(min, max+1, 2):
    print "h(2^n + % 4d) = %s" % (i, F(0, i))

if __name__ == "__main__":
  main()
