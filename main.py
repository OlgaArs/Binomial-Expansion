def parse(expr):
    expr = expr.replace('(', '')
    expr = expr.replace(')^', ' ')
    expr = expr.replace('+', ' +')
    expr = expr.replace('-', ' -')
    expr = expr.replace('*', ' *')
    expr = expr.replace('/', ' /')

    expr = expr.split(' ')
    expr = [elem for elem in expr if elem != '']
    expr.insert(1, expr[0][-1])
    expr[0] = (1 if expr[0][:-1] == '' else (-1 if expr[0][:-1] == '-' else expr[0][:-1]))

    return expr


def expand(expr):
    from math import factorial
    a, x, b, n = parse(expr)
    if n == '0':
        return '1'
    elif n == '1':
        return (a if a != 1 else '') + x + b

    a = int(a)
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