import time
from flask import Flask
from flask import request

# Press the green button in the gutter to run the script.


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def prometheus_alarm():
    print("===begin====")
    recive_json = []
    recive_count = 0
    s_time = int(time.time())
    while True:
        n_time = time.time()
        time_late = n_time - s_time
        recive_count += 1
        print("request.method:", request.method)
        if request.method == "POST":
            print("====正在获取数据===========")
            post_data = request.get_json()
            recive_json.append(post_data)
            print("000000======00000000000")
            print(recive_json)
            print("0000000=====0000000000")
            if time_late > 1 or recive_count >= 4:
                print("此次循环了%s次" % recive_count)
                print("此次接收耗时%s秒" % time_late)
                print("此次接收了%s个数据" % len(recive_json))
                print("11111111======1111111111")
                print(request.get_json())
                print("11111111======1111111111")
                break
            else:
                print("正在循环")
                continue

        print("====********第%s次接收数据&&&&&&&&&&&" % recive_count)

        print("====********第%s秒钟&&&&&&&&&&&" % time_late)

    if len(recive_json) > 0:
        print("输出的数据为：================\n有%s个数据" % len(recive_json))
        print(recive_json)
    else:
        print("***********无数据**************")
    print("————————————————结束了哈哈++++++++++++++++++")
    return "Post Test"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
