import cv2

img = cv2.imread("data/raw/op01.jpg")

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pixel coordinate: ({x}, {y})")

cv2.imshow("op01", img)
cv2.setMouseCallback("op01", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()