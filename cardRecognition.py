import cv2

video_feed = cv2.VideoCapture(0)

while True:

    return_val, frame = video_feed.read()
    if not return_val:
        print("feed not active... Exiting")
        break
    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_feed.release()
cv2.destroyAllWindows()

