def expand(expr):
    from math import factorial
    from re import compile

    P = compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')
    a, x, b, n = P.findall(expr)[0]

    if n == '0':
        return '1'
    elif n == '1':
        return a + x + ('+' if b[0] != '-' else '') + b
    a = -1 if a == '-' else (1 if a == '' else int(a))
    b = int(b)
    n = int(n)

    res = []
    for k in range(0, n + 1):
        koef = int(factorial(n) / (factorial(n - k) * factorial(k))) * b ** k * a ** (n - k)
        mult = (x if (n - k) > 0 else '') + (('^' + str(n - k)) if (n - k) > 1 else '')
        result = (('' if koef == 1 else ('-' if koef == -1 else str(koef))) + mult) if mult != '' else str(koef)
        res.append('1' if result == '' else result)
    res = [elem if (elem[0] == '-' or i == 0) else ('+' + elem) for i, elem in enumerate(res)]
    return ''.join(res)

if __name__ == '__main__':
    assert expand("(x+1)^0") == "1"
    assert expand("(x+1)^1") == "x+1"
    assert expand("(x+1)^2") == "x^2+2x+1"

    assert expand("(x-1)^0") == "1"
    assert expand("(x-1)^1") == "x-1"
    assert expand("(x-1)^2") == "x^2-2x+1"

    assert expand("(5m+3)^4") == "625m^4+1500m^3+1350m^2+540m+81"
    assert expand("(2x-3)^3") == "8x^3-36x^2+54x-27"
    assert expand("(7x-7)^0") == "1"

    assert expand("(-5m+3)^4") == "625m^4-1500m^3+1350m^2-540m+81"
    assert expand("(-2k-3)^3") == "-8k^3-36k^2-54k-27"
    assert expand("(-7x-7)^0") == "1"