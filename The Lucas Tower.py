def move_discs(n, from_peg, to_peg, temp_peg):
    """
    Guide that shows the process of solving the conundrum
    :param n: number of discs
    :param from_peg: initial tower
    :param to_peg: tower to move to
    :param temp_peg: temporary tower
    :return: None
    """
    if n > 0:
        move_discs(n - 1, from_peg, temp_peg, to_peg)
        print('Переложить кольцо с', from_peg, 'башни на', to_peg)
        move_discs(n - 1, temp_peg, to_peg, from_peg)

def lucas_tower():
    "Function call"
    num_discs = int(input('Введите количество дисков: '))
    from_peg = 1
    temp_peg = 2
    to_peg = 3
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('Все кольца перемещены')
    r = (2 ** num_discs) - 1
    print('Количество сделанных перемещений для решения головоломки:', r)

lucas_tower()
