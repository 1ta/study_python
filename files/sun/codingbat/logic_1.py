def cigar_party(cigars, is_weekend):
    return (40<=cigars<=60 or (is_weekend and 40<=cigars))
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
         return 2
    else:
         return 1
def squirrel_play(temp, is_summer):
    if 60<=temp<=90:
        return True
    if 60<=temp<=100 and is_summer:
        return True
    else:
        return False

def alarm_clock(day, vacation):
    is_weekend = day == 0 or day == 6
    if vacation:
        if is_weekend:
            return "off"
        else:
            return "10:00"
    else:
        if is_weekend:
            return "10:00"
        else:
            return "7:00"

def love6(a, b):
    if a == 6 or b == 6:
        return True
    if abs(a-b)==6:
        return True
    if sum(a+b)==6:
        return True
    else:
        return False

def in1to10(n, outside_mode):
    if not outside_mode:
        if 1<= n <= 10:
            return True
        else:
            return False
    if outside_mode and (n <= 1 or n>= 10):
            return True
    else:
        return False

def near_ten(num):
    if 0 <= (num+2)%10 <= 4:
        return True
    else:
        return False
