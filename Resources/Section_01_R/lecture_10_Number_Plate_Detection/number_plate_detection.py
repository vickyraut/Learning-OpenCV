import cv2
cap = cv2.VideoCapture("../Videos/demo.mp4")

NumberPlateCascade=cv2.CascadeClassifier("../haarcascades/haarcascade_russian_plate_number.xml")

count=0

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    if ret:
        print("Frame Shape", frame.shape)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        number_plate = NumberPlateCascade.detectMultiScale(frame_gray, 1.1, 10)
        for x, y, w, h in number_plate:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 255), 3)
            cv2.putText(frame, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
            frameROI = frame[y:y+h, x:x+w]
        cv2.imshow("Frame ROI", frameROI)
        cv2.imshow("Output Video", frame)
        if cv2.waitKey(1) & 0xFF==ord('1'):
            cv2.imwrite("../Resources/NumberPlate/NoPlate_"+str(count)+".jpg", frameROI)
            cv2.rectangle(frame, (0,200), (640, 300), (0,255,0), cv2.FILLED)
            cv2.putText(frame, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), 2)
            cv2.imshow("Output Video", frame)
            cv2.waitKey(500)
            count+=1

    else:
        break
