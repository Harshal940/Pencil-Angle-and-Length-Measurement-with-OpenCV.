import cv2
import numpy as np
import math

path = "2_pencils.jpg"
img = cv2.imread(path)
pointsList = []


scale_factor = 10


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            if len(pointsList) >= 3:
                prev_point = pointsList[-3]
                # Calculate and display the length in centimeters
                length_pixels = np.sqrt(
                    (x - prev_point[0]) ** 2 + (y - prev_point[1]) ** 2
                )
                length_cm = length_pixels / scale_factor
                print(f"Length: {length_cm:.2f} cm")
                cv2.putText(
                    img,
                    f"Length: {length_cm:.2f} cm",
                    (x, y),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.5,
                    (0, 0, 255),
                    2,
                )
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x, y])


def gradient(pt1, pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])


def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2 - m1) / (1 + (m2 * m1)))
    angD = round(math.degrees(angR))

    cv2.putText(
        img,
        str(angD),
        (pt1[0] - 40, pt1[1] - 20),
        cv2.FONT_HERSHEY_COMPLEX,
        1.5,
        (0, 0, 255),
        2,
    )


cv2.waitKey(0)  # Wait until a key is pressed to start
cv2.destroyAllWindows()  # Close all OpenCV windows when done

while True:
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)

    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
# press q to destroy the window.
