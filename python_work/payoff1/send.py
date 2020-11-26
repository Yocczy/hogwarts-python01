import money


def send():
    print('发工资啦')
    send_money = int(input('请输入发放工资数额：'))
    global select_money
    select_money = money.saved_money + send_money
