import string
digs = string.digits + string.ascii_letters


def int2base():
    x=int(input("Enter number to be converted >>"))
    base=int(input("Enter base >>"))
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()
    print("Answer is",''.join(digits))
    return ''.join(digits)

# int2base()