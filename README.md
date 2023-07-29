# GPTForBiliBiliLive

哔哩哔哩AI直播（使用ChatGPT）

交流群：[303104111](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=CtyH-iI1JBO-jpRUFDrMgx9SZoM0ClTX&authKey=asxcHbxRLNCvJg%2FNo%2FOPsf%2FS7J6XycRaCfSot4bODF1XA7EdEptnCSy61cuabUCt&noverify=0&group_code=303104111)

GPTForBiliBiliLive是一个由ChatGPT驱动的虚拟主播，可以在Bilibili直播中与观众实时互动。它使用自然语言处理和文本转语音技术生成对观众问题的回答。

### 运行环境

- Python 3.6+
- Windows操作系统

### 安装依赖

在命令行中使用以下命令安装所需库：

```bash
pip install  bilibili-api-python edge-tts
```

此外，还需要[下载并安装mpv](https://mpv.io/installation/)。在Windows操作系统上，也需要将 `mpv.exe` 添加到环境变量中。对于其他操作系统，请将其路径添加到系统 `PATH` 环境变量中。

### 使用

1. 用文本编辑工具打开main.py文件。
2. 在# ChatGPT API的URL和密钥中设置api链接（这个可以不改）和你的APIKey
3. 按照您的意愿调整机器人的预设。
4. 用Python运行main.py文件。
5. 输入要连接的B站直播间编号。
6. 按下`Enter`键开始监听弹幕流。

当有观众发送弹幕消息时，机器人将自动生成回复并将其转换为语音。声音文件将被保存并立即播放。

### 许可证

MIT许可证。详情请参阅LICENSE文件。

### 特别鸣谢

[XzaiCloud/AI-Vtuber](https://github.com/XzaiCloud/AI-Vtuber)

```

```
