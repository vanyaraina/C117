import cv2

video = cv2.VideoCapture("PRO-C105-Teacher-Boilerplate-main/AnthonyShkraba.mp4")
print(video)

if video.isOpened() == False:
    print("unable to read the video")

height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame = int(video.get(cv2.CAP_PROP_FPS))

print(height, width, frame)

newvideo =cv2.VideoWriter("Boxing.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 5, (width, height) )

while True:
    dummy, frame = video.read()
    cv2.imshow("video", frame)
    newvideo.write(frame)
    if cv2.waitKey(25)==32:
        break

video.release()
newvideo.release()
cv2.destroyAllWindows()