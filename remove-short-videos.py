import os
import time
import cv2
cwd1=r"D:\Videos\Captures"
cwd2=r"D:\autoVideoMerge"

flag=1
while flag:
    default_shortest_time = 10
    shortest_time = input("删除时长在几分钟以内的视频？（回车代表删除时长在{}分钟的视频）".format(default_shortest_time))
    if shortest_time == '':
        shortest_time= default_shortest_time
    elif shortest_time.isdigit():
        shortest_time=int(shortest_time)
    else:
        print("请输入数字！")
        continue
    flag=0

# https://blog.csdn.net/lilongsy/article/details/121206810
def get_duration_from_cv2(filename):
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num =cap.get(7)
        duration = frame_num/rate
        return int(duration)
    return -1

videos=list(map(lambda x:cwd1+os.sep+x, os.listdir(cwd1)))

for video in videos:
    if get_duration_from_cv2(video)<shortest_time*60:
        os.remove(video)

print("删除完成！")




