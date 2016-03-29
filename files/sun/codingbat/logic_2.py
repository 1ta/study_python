def make_bricks(small, big, goal):
    if goal > small + 5*big:
        return False
    if  goal%5 <= small:
            return True
    else:
        return False

def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  return sum

def lucky_sum(a, b, c):
    sum = 0
    if a != 13:
        sum += a
        if b != 13:
            sum += b
            if c != 13:
                 sum += c
    return sum

def make_chocolate(small, big, goal):
    if goal > small + 5*big:
        return -1
    if goal%5 > small:
        return -1
    if goal/5 > big:
        return goal-big*5
    else:
        return goal%5
