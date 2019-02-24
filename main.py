import numpy as np
import cognitive_face as CF
import cv2

'''

Key 1: 2b52e26916e64eeba2703fed6e75c7a2

Key 2: dd39248b082f444584ee69796ef5ba28

'''

key = 'dd39248b082f444584ee69796ef5ba28'
CF.Key.set(key)
vision_base_url = "https://westus.api.cognitive.microsoft.com/vision/v2.0/"
CF.BaseUrl.set(vision_base_url)

# analyze_url = vision_base_url + 'analyze'


if __name__ == '__main__':
    while True:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        cv2.imwrite('frame.jpg', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()