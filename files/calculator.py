while True:
    expr = input('enter the expression:')
    if expr == 'exit':
        break
    s = eval(expr)
    print(s)
