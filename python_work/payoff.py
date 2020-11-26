money = 1000


def send():
    global money
    money += 1000


def select():
    if money == 1000:
        print('没发工资，现有存款:', money)
    elif money == 2000:
        print('发工资啦，现有存款:', money)
    else:
        print('出现错误')


if __name__ == '__main__':
    send()
    select()
