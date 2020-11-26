saved_money = 1000


def send():
    print('发工资啦')
    send_money = int(input('请输入发放工资数额：'))
    global select_money
    select_money = saved_money + send_money


def select():
    print('现有存款:', select_money)


if __name__ == '__main__':
    send()
    select()
