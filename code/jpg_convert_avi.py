import cv2

img_root='D:\img\\'
fps =2 #保存视频的FPS，可以适当调整 
size=(380,369)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
videowriter=cv2.VideoWriter('D:/3.avi',fourcc,fps,size)

for i in range(0,24):
    frame =cv2.imread(img_root+str(i)+'.jpg')
    videowriter.write(frame) 
videowriter.release()