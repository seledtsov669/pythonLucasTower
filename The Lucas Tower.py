def move_rings(n, init_tow, end_tow, temp_tow):
    """
    Guide that shows the process of solving the conundrum
    :param n: number of discs
    :param init_tow: initial tower
    :param end_tow: tower to move to
    :param temp_tow: temporary tower
    :return: None
    """
    if n > 0:
        move_rings(n - 1, init_tow, temp_tow, end_tow)
        print('Перенести кольцо с', init_tow, 'башни на', end_tow)
        move_rings(n - 1, temp_tow, end_tow, init_tow)

def lucas_tower():
    """Function call"""
    num = int(input('Введите количество дисков: '))
    init_tow = 1
    temp_tow = 2
    end_tow = 3
    r = (2 ** num) - 1
    move_rings(num, init_tow, end_tow, temp_tow)
    print('Головоломка решена')
    print('Количество сделанных перемещений для решения головоломки:', r)

lucas_tower()
