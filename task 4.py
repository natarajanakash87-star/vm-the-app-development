from ultralytics import YOLO
import argparse
import cv2
import time

# -----------------------------------
# PARSE INPUT SOURCE
# -----------------------------------

parser = argparse.ArgumentParser(description="Real-time object detection and tracking")
parser.add_argument("--source", default="0", help="Video source: webcam index or video file path")
args = parser.parse_args()

source = args.source
if source.isdigit():
    source = int(source)

# -----------------------------------
# LOAD YOLO MODEL
# -----------------------------------

model = YOLO("yolov8n.pt")

# -----------------------------------
# OPEN VIDEO SOURCE
# -----------------------------------

if isinstance(source, int):
    cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print(f"Warning: Webcam index {source} failed.")
        fallback_index = source + 1 if source == 0 else 0
        print(f"Trying fallback webcam index {fallback_index}...")
        cap = cv2.VideoCapture(fallback_index, cv2.CAP_DSHOW)
else:
    cap = cv2.VideoCapture(source)

if not cap.isOpened():
    if isinstance(source, int):
        print("Error: Cannot open webcam. Check camera connection or use a different device.")
    else:
        print(f"Error: Cannot open video source '{source}'. Check the file path.")
    exit(1)

print("Press Q to Exit")

# -----------------------------------
# FPS VARIABLES
# -----------------------------------

prev_time = 0

# -----------------------------------
# MAIN LOOP
# -----------------------------------

while True:

    # Read frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # -----------------------------------
    # OBJECT DETECTION + TRACKING
    # -----------------------------------

    results = model.track(
        frame,
        persist=True,
        conf=0.5
    )

    # -----------------------------------
    # DRAW RESULTS
    # -----------------------------------

    annotated_frame = results[0].plot()

    # -----------------------------------
    # CALCULATE FPS
    # -----------------------------------

    current_time = time.time()
    if prev_time == 0:
        fps = 0.0
    else:
        fps = 1 / (current_time - prev_time)

    prev_time = current_time

    fps_text = f"FPS: {int(fps)}"

    cv2.putText(
        annotated_frame,
        fps_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # -----------------------------------
    # DISPLAY WINDOW
    # -----------------------------------

    cv2.imshow(
        "Real-Time Object Detection and Tracking",
        annotated_frame
    )

    # -----------------------------------
    # EXIT KEY
    # -----------------------------------

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------------
# RELEASE RESOURCES
# -----------------------------------

cap.release()

cv2.destroyAllWindows()

print("Program Closed Successfully")