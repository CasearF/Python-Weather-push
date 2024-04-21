# 导入requests库，用于发送HTTP请求
import requests
import json

# POST请求的URL，这里假设你有一个本地服务器在192.168.1.133的3001端口上运行，用于接收POST请求
webhook_url = 'http://192.168.1.133:3001/webhook/msg'

# 定义一个函数，用于发送GET请求获取天气数据
def get_weather_data(city_code):
    # 构建请求URL，其中city_code是城市代码，用于指定要查询的城市
    url = f"http://t.weather.sojson.com/api/weather/city/{city_code}" 
    # 发送GET请求
    response = requests.get(url)

    # 如果响应状态码不是200（即请求成功），则返回错误信息
    if response.status_code != 200:
        return f"请求失败，状态码：{response.status_code}"

    # 尝试解析响应内容为JSON格式
    try:
        weather_data = response.json()
        # 提取城市名称
        city_name = weather_data['cityInfo']['city']
        # 提取当前温度
        wendu = weather_data['data']['wendu']
        # 提取天气状况
        weather_description = weather_data['data']['forecast'][0]['type']
        # 提取空气质量
        quality = weather_data['data']['quality']
        # 提取PM2.5和PM10
        pm25 = weather_data['data']['pm25']
        pm10 = weather_data['data']['pm10']
        # 提取其他信息
        forecast = weather_data['data']['forecast'][0]['notice']
        # 返回格式化的天气信息字符串
        return f"天气推送 城市：{city_name}\n 当前温度：{wendu}℃\n 天气：{weather_description}\n 空气质量：{quality}\n PM2.5：{pm25}\n PM10：{pm10}\n 预报：{forecast}\n 信息来自中国气象网查询"
    except json.JSONDecodeError as e:
        # 如果JSON解析失败，返回错误信息
        return f"解析JSON失败：{e}"

# 定义一个函数，用于发送POST请求
def send_post_request(content, recipient):
    # 设置请求头，指定内容类型为JSON
    headers = {
        'Content-Type': 'application/json'
    }
    # 构建POST请求的数据，包括接收者、消息类型和内容
    payload = {
        "to": recipient,  # 使用传入的recipient参数作为接收者
        "type": "text",
        "content": content
    }
    # 发送POST请求，并将数据以JSON格式发送
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    # 打印响应状态码
    print(f"Response status code: {response.status_code}")

# 主函数，程序的入口点
if __name__ == '__main__':
    city_code = '101080913'  # 北京的城市代码
    weather_info = get_weather_data(city_code)
    # 假设接收者名称为"艾米拉特工"
    recipients = ["demo01", "demo02", "demo03"]
    for recipient in recipients:
        # 发送消息给当前的接收者
        send_post_request(weather_info, recipient)
