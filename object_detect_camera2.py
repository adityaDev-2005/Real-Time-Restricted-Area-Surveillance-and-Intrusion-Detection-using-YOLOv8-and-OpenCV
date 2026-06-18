from ultralytics import YOLO
import cv2
from datetime import datetime
import time
# print("YOLO installed successfully!!")

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("street_people.mp4") ##
fps = cap.get(cv2.CAP_PROP_FPS) ##
delay = int(1000/fps) ##

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)

last_logged = 0 ###
intrusion_active = False

# the coordinates for ROI
roi_x1 = 400
roi_y1 = 200

roi_x2 = 800
roi_y2 = 500


while True:  ##
    ret, frame = cap.read()  ##
    #frame = cv2.flip(frame,1)

    person = 0

    if not ret:  ##
        print("Video ended!!")
        break
    
    results = model(frame,verbose = False) ##

    result = results[0]

    boxes = result.boxes


    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (roi_x1, roi_y1),
        (roi_x2, roi_y2),
        (255,0,0),
        -1
    )

    alpha = 0.15

    cv2.addWeighted(
        overlay,
        alpha,
        frame,
        1-alpha,
        0,
        frame
    )

    cv2.rectangle(
        frame,
        (roi_x1, roi_y1),
        (roi_x2, roi_y2),
        (255,0,0),
        2
    )

    cv2.putText(
        frame,
        "Restricted Area",
        (roi_x1, roi_y1-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,0,0),
        2
    )

    intruders = 0

    status = "SAFE"
    status_color = (0,255,0)

    for box in boxes:

        x1, y1, x2, y2 = box.xyxy[0]

        class_id = int(box.cls[0])

        confidence = float(box.conf[0])

        label = result.names[class_id]

        if confidence < 0.3:
            continue

        if label != "person":
            continue

        person += 1

        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        # Check whether person center lies inside ROI
        if (
            roi_x1 < center_x < roi_x2 and
            roi_y1 < center_y < roi_y2
        ):

            intruders += 1

            box_color = (0,0,255)

            status = "INTRUSION DETECTED"
            status_color = (0,0,255)

        else:

            box_color = (0,255,0)

        # Draw bounding box
        cv2.rectangle(
            frame,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            box_color,
            2
        )

        # Draw confidence label
        cv2.putText(
            frame,
            f"Person {confidence:.2f}",
            (int(x1), int(y1)-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            box_color,
            2
        )

        # Draw center point
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (255,255,0),
            -1
        )
    
    if person > 0 and intruders == 0:

        status = "PERSON DETECTED"
        status_color = (0,165,255)

    current_time = time.time() ###

    if person>0 and current_time - last_logged >=1: ###
            
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("person_log.txt", "a") as file:
            file.write(f"{timestamp} : {person}\n")

        last_logged = current_time
        
    cv2.putText(
                frame,
                f"Person Count: {person}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                status_color,
                2
            )   
    
    cv2.putText(
    frame,
    f"STATUS : {status}",
    (20,40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    status_color,
    3
    )

    cv2.putText(
    frame,
    f"Intruders in ROI: {intruders}",
    (20,120),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0,0,255),
    2
    )


    if intruders > 0 and not intrusion_active:

        intrusion_active = True

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"intrusion_{timestamp}.jpg"

        cv2.imwrite(filename, frame)

        with open("intrusion_log.txt","a") as file:

            file.write(
                f"{timestamp} : Intrusion detected ({intruders} persons)\n"
            )

    elif intruders == 0:

        intrusion_active = False

    cv2.imshow("YOLO Detection:",frame) ##

    if cv2.waitKey(delay) == ord(' '): ##
        break

cap.release() ##

cv2.destroyAllWindows() ##







