import cv2
import numpy as np
import urllib.request

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

url = "http://192.168.137.97:8080/shot.jpg"  # keep your IP

while True:
    try:
        img_resp = urllib.request.urlopen(url, timeout=3)
        img_np = np.frombuffer(img_resp.read(), dtype=np.uint8)
        frame = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        frame = cv2.resize(frame, (480, 360))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Improve contrast so face stands out more
        gray = cv2.equalizeHist(gray)

        # More sensitive detection settings
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,   # was 1.3, lower = more sensitive
            minNeighbors=3,    # was 5, lower = more sensitive
            minSize=(60, 60)   # minimum face size to detect
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, "Face", (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except:
        continue

cv2.destroyAllWindows()