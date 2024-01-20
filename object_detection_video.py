import cv2 as cv
import numpy as np
import time
import sys

video = cv.VideoCapture("D:/YOMTECH PROJECTS/my python/test/lane1.avi")

if not video.isOpened():
    sys.exit("unable to load video frame")
    

    

while True:
    
    __, frame = video.read()
        
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #cvt = np.uint8(absolute)
    
    canny = cv.Canny(gray, 255, 255, apertureSize=3)
    
    
    kervel = np.ones((5,5), np.uint8)
    
    close1 = cv.morphologyEx(canny, cv.MORPH_CLOSE, kervel)
    
    #close = cv.morphologyEx(close1, cv.MORPH_CLOSE, kervel)"""
    
    
    line = cv.HoughLinesP(close1, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    
    try:
        for lines in line:
            flag = 1
            x1,y1,x2,y2 = lines[0]

            print(lines[0])

            cv.line(frame, (x1,y1),(x2,y2), (255,0,0), 2)
            
            font = cv.FONT_HERSHEY_SIMPLEX
            
            #cv.putText(gray, "keep going", (500,500), font, 3, (255,0,0), 5)
                   
    
    except TypeError:
            
            #cv.putText(gray, "Oh!! i cant see", (500,500), font, 3, 255, 5)
            
            continue
    
    def mainfunc():
        
        
        i = -1
        
        value1 = 1
        
        sign = "null"
        
        def verify():
            
            nonlocal i, value1, sign
            
            i += 1
            
            global min_val, max_val, min_loc, max_loc, car
            
            objects = ["car","Sign Board","Sign Board","car","car","car"]
            
            c1 = "D:/YOMTECH PROJECTS/my python/test/c1.png"
            s1 = "D:/YOMTECH PROJECTS/my python/test/s1.png"
            s2 = "D:/YOMTECH PROJECTS/my python/test/s2.png"
            c2 = "D:/YOMTECH PROJECTS/my python/test/c2.png"
            c3 = "D:/YOMTECH PROJECTS/my python/test/c3.png"
            c4 = "D:/YOMTECH PROJECTS/my python/test/c4.png"
            
            cars = [c1,s1,s2,c2,c3,c4]
        
            car1 = cv.imread(cars[i], cv.IMREAD_GRAYSCALE)
    
            car = cv.Canny(car1, 200, 255, apertureSize=3)
    

            match = cv.matchTemplate(canny, car, cv.TM_CCOEFF_NORMED)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(match)
            
            value1 = max_val*100
            
            sign = objects[i]
            
            
        
        while i < 5 and value1 < 30:
            verify()
        
        return i, value1, sign
    
       
    
    mainfunc()
    
    i, value1, sign = mainfunc()
    
    if value1 >= 43:
        flag = 1
    else:
        flag = 0
        
    
    print("flag = %s"%flag)
    print("value = %s"%value1)
    
    top_left = max_loc

    w, h = car.shape[::-1]

    bottom_right = (top_left[0]+w, top_left[1]+h)
    
    value1 = max_val*100
        
    if flag == 1:
        cv.rectangle(frame, (top_left),(bottom_right), (0,255,0), 5)
        #cv.circle(frame, (top_left), 5, 255,4)

        

        value1 = "Name: {}"
        
        value = value1.format(sign)
        
        color = "Colour: Null"

        w, h = gray.shape

        print(w,h)

        x = bottom_right[0]
        y = bottom_right[1]

        font = cv.FONT_HERSHEY_SIMPLEX
        print("flag %s"%flag)
        cv.putText(frame, value, (x,y-40), font, 1, (0,0,255), 2 )
        cv.putText(frame, color, (x,y), font, 1, (0,0,255), 2 )
                
    
    cv.imshow("my video", frame)
    
    #cv.imshow("close", close)"""
    
    
    key = cv.waitKey(1)
    
    if flag == 1:
        time.sleep(1)
    
    i = 0
    flag = 0
    
    if key == ord("q"):
        break
        
video.release()
cv.destroyAllWindows()
