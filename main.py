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