import cv2

#Image input (PATH is personalized)
pic=cv2.imread('C:/Users/mikaz/source/repos/kazuma7000_C++/x64/Release/data/chicky_512.png')

#Video output (PATH is personalized)
video_path="close_up.avi"

#Advanced Video Settings(for .avi)
fps=30
height,width,chanel=pic.shape
frame_size=(height,width)
output =cv2.VideoWriter(video_path,cv2.VideoWriter_fourcc('M','J','P','G'),fps,frame_size)


for r in range(int(width*0.07)):
    
    #Cropping
    pic=pic[r:height-r,r:width-r]

    #Resize
    pic=cv2.resize(pic,(height,width))

    #display
    cv2.imshow('a',pic)

    #save
    output.write(pic)
    cv2.waitKey(10)


output.release()