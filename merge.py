import os
import time
import cv2
cwd1=r"D:\Videos\Captures"
cwd2=r"D:\autoVideoMerge"

# https://blog.csdn.net/lilongsy/article/details/121206810
def get_duration_from_cv2(filename):
  cap = cv2.VideoCapture(filename)
  if cap.isOpened():
    rate = cap.get(5)
    frame_num =cap.get(7)
    duration = frame_num/rate
    return f"{duration//60}分{int(duration-(duration//60)*60)}秒"
  return -1

videos=list(map(lambda x:cwd1+os.sep+x, os.listdir(cwd1)))
videos=sorted(videos,key=os.path.getmtime)[1:]

for idx,i in enumerate(videos,1):
    print("第{}个：\t{}\t视频时长：{}".format(idx,i,get_duration_from_cv2(i)))
print("\n\n")
ask_start=input("从第几个视频开始（包括该视频）：")
ask_end=input("到第几个视频结束（包括该视频）：")

videos=videos[int(ask_start)-1:int(ask_end)]

for idx,i in enumerate(videos,1):
    print("第{}个：\t{}".format(idx,i))
print("\n\n")

os.chdir(cwd1)
name_idx,name=0,None
for vdo in videos:
    vdo_file=vdo
    # print(vdo)
    with open("mylist.txt","a",encoding="gbk") as f:
        f.write(f"file \'{vdo_file}\'\n")
    if name_idx==0:
        name=vdo.replace(".mp4", "_all.mp4")
        name_idx+=1

finish_file=name

start=time.time()

concat_comm=f"ffmpeg -f concat -safe 0 -i mylist.txt -c copy \"{finish_file}\" -y"
os.system(concat_comm)

end=time.time()

print("one done.")
print("Time Used:{}".format(end-start))
os.remove("mylist.txt")

# print(videos)