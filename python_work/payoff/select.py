import money


def select():
    if money.money == 1000:
        print('没发工资，现有存款:', money.money)
    elif money.money == 2000:
        print('发工资啦，现有存款:', money.money)
    else:
        print('出现错误')
