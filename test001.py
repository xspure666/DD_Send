import time
from flask import Flask
from flask import request
import datetime
from sendDD import send as send_message

# Press the green button in the gutter to run the script.


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def prometheus_alarm():
    print("=====#########进入程序########========")
    message = ""
    if request.method == "POST":
        print("Post Menthod")
        get_data = request.get_json()
        # 解析json参数
        alert = get_data["alerts"]

        # print('长度为', len(alert))
        print("############################")
        for i in alert:
            status = i["status"]
            labels = i["labels"]
            alertname = labels["alertname"]
            instance = labels["instance"]
            # job = labels["job"]
            serverity = labels["serverity"]
            annotations = i["annotations"]
            summary = annotations["summary"]
            startsAt = i["startsAt"]
            # startsAt_1 = datetime.datetime.strptime(startsAt, "%Y-%m-%d %H:%M:%S")
            endsAt = i["endsAt"]
            generatorURL = i["generatorURL"]
            now_time = datetime.datetime.now()
            startsAt = datetime.datetime.strptime(startsAt, "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(hours=8)

            alarm_long = str(round((now_time - startsAt).seconds / 60 / 60, 3))
            #
            # startsAt = datetime.datetime.strptime(startsAt, "%Y-%m-%d %H:%M:%S")
            # endsAt = datetime.datetime.strptime(endsAt, "%Y-%m-%d %H:%M:%S")

            # alarm_long = '100'
            if status == "firing":
                info_message = "通知类型：告警推送" + "\n服务地址：" + instance + "\n告警类型：" + alertname + "\n告警级别：" + serverity + "\n当前时间：" + str(
                    now_time).split(".")[0] + "\n开始时间：" + str(startsAt).split(".")[0] + "\n告警时长：" + alarm_long + " 小时\n告警详情：" + summary + "\n\n"
                message += info_message
            else:
                info_message = "通知类型：解除告警" + "\n服务地址：" + instance + "\n告警类型：" + alertname + "\n告警级别：" + serverity + "\n当前时间：" + str(
                    now_time).split(".")[0] + "\n开始时间：" + str(startsAt).split(".")[0] + \
                               "\n结束时间：" + str(endsAt).split(".")[0] + "\n告警时长：" + alarm_long + " 小时\n告警详情：" + summary + "\n\n"
                message += info_message
            print("############################")
            print(message)
            print("############################\n\n\n")

    else:
        print("Get Menthod")
    send_message(message)
    return get_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
