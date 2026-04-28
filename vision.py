import cv2
class Vision:
    def opencamera(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            return
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) == 27:  # Press 'ESC' to exit
                break
        cap.release()
        cv2.destroyAllWindows()