import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)



        
print(len(images))
count = len(images)

image1 = cv2.imread(images[0])
print(image1)

height,width,channels = image1.shape

size=(width,height)
print(size)

newvideo = cv2.VideoWriter("Sunset.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 5, size)
while True:
    for i in range(count-1, 0, -1):
        frame = cv2.imread(images[i])

        newvideo.write(frame)

    break

newvideo.release()
cv2.destroyAllWindows()

# Sunrise
# while True:
#     for i in range(0, count):
#         frame = cv2.imread(images[i])

#         newvideo.write(frame)

