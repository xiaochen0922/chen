
from moviepy.editor import VideoFileClip

# 加载视频文件
clip = VideoFileClip("C://Users//10111//Desktop//玩玩//微信图片_20240523180655.jpg")

# 转换格式并输出
clip.write_videofile("output.FLV", codec="libxvid")  # 使用不同的codec以适应不同的格式

# 注意：codec参数取决于你想要输出的格式，例如"libx264"常用于MP4，"libxvid"常用于AVI等