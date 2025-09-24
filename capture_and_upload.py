# capture_and_upload.py
import cv2, requests, time

API = "http://localhost:5001/upload_map"
cap = cv2.VideoCapture(0)  # webcam, replace with IP cam if needed
i = 0

while True:
    ret, frame = cap.read()
    if not ret: break
    cv2.imshow("Mapping Demo", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Press 's' to save and upload
        fname = f"map_{i}.jpg"
        cv2.imwrite(fname, frame)
        with open(fname, "rb") as f:
            r = requests.post(API, files={"file": f})
        print("Uploaded:", r.json())
        i += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
