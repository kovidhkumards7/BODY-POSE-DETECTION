import cv2
import mediapipe as mp
import time


class poseDetector():

    def __init__(self, mode = False, upBody = False, smooth = True, detectionCon = 0.5, trackCon = 0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)


    def findPose(self, img, draw = True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        # print(results.pose_landmarks)

        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return  img


   # for id, lm in enumerate(results.pose_landmarks.landmark):
   #    h, w, c = img.shape
   # print(id, lm)
   #     cx, cy = int(lm.x*w), int(lm.y*h)
   #     cv2.circle(img, (cx, cy), 2, (255, 0, 255), cv2.FILLED)
   #     print(id, cx, cy)




def main():
    cap = cv2.VideoCapture('D:\\KOVIDH KUMAR D S\\KOVIDH KUMAR D S PYTHON\\PYTHON 2022\\PYTHON PROJECTS\\BODY POSE DETECTION\\3.mp4')
    pTime = 0
    detector = poseDectector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        ptime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(10)


if __name__ == "__main__":
    main()