import time
import plyer
import requests
import webbrowser


api = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom"
room_id1 = '33989'


def live_info(room_id):
    try:
        info = requests.get(api, params={'room_id': room_id}).json()
        live_title = info['data']['room_info']['title']
        live_status = info['data']['room_info']['live_status']
        status = {'live_title': live_title, 'live_status': live_status, 'Error': 0}
        return status
    except TypeError:
        status = {'live_title': 'Err', 'live_status': 'Err', 'Error': 1}
        return status


if __name__ == '__main__':
    plyer.notification.notify(title='', message='程序启动成功')
    time.sleep(10)
    while True:
        Info = live_info(room_id1)
        if Info['live_status'] == 1 and Info['Error'] == 0:
            plyer.notification.notify(title='直播通知', message='泛式正在直播\n\n{}'.format(Info['live_title']))
            webbrowser.open('https://live.bilibili.com/'+room_id1)
            break
        elif Info['Error'] == 1:
            plyer.notification.notify(title='泛式开播了吗？', message='API错误，程序将休眠10分钟')
            time.sleep(600)
            Info = live_info(room_id1)
            if Info['Error'] == 1:
                plyer.notification.notify(title='泛式开播了吗？', message='API第二次错误，程序退出')
                break
        time.sleep(200)
