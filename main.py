import subprocess
import requests
import os
from bilibili_api import live, sync
from playsound import playsound
import datetime

#全部变量

# ChatGPT API的URL和密钥
bot_api_url = "https://openaiapi.elecho.top/v1/chat/completions" # openai的api链接
bot_api_key = "your_api_key" # 填写你的api-key

#Edgetts音色
bot_voice = "zh-CN-XiaoyiNeural"

# ChatGPT参数
chatgpt_params = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "现在你正在哔哩哔哩直播，你的名字叫XX，你是由XXX制造的AI模型，后面的聊天将会是b站用户和你的互动，且每一条消息与上一条都没有联系，你的回答要尽量简短。"}],# 设置ai预设
    "max_tokens": 1000,# 设置单次回复量（最大）
    "temperature": 0.7,
    "n": 1,
    "stop": "\n"
}

# 创建以当前日期和时间为名称的目录
now = datetime.datetime.now()
dir_name = now.strftime('%Y%m%d_%H%M%S')
os.makedirs(dir_name, exist_ok=True)

# 连接Bilibili直播弹幕服务器
room_id = int(input("请输入直播间编号: "))# 请勿修改，在CMD界面填写
room = live.LiveDanmaku(room_id)


@room.on("DANMU_MSG")
async def on_danmaku(event):
    content = event["data"]["info"][1]  # 获取弹幕内容
    user_name = event["data"]["info"][2][1]  # 获取用户昵称
    print(f"[{user_name}]: {content}")  # 打印弹幕信息

    question = content  # 设置观众提问

    # 使用ChatGPT与观众进行对话
    chatgpt_params["messages"].append({"role": "user", "content": question})
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bot_api_key}"
    }
    response = requests.post(bot_api_url, headers=headers, json=chatgpt_params)
    response_data = response.json()
    answer = response_data["choices"][0]["message"]["content"]
    print(f"[AI回复{user_name}]: {answer}")  # 打印AI回复信息

    # 使用Edge TTS生成回答的音频文件
    tts_text = answer.replace('"', '\\"')  # 转义引号
    file_name = f'{dir_name}/response_{len(chatgpt_params["messages"])//2}.mp3'  # 文件名按照回复的顺序数字编号
    command = f'edge-tts --voice {bot_voice} --text "{tts_text}" --write-media {file_name}'
    subprocess.run(command, shell=True)  # 执行命令行指令

    # 播放音频文件
    playsound(file_name)

sync(room.connect())  # 开始监听弹幕流
