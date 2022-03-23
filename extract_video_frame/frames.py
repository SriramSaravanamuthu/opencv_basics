import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--Input1", help = "Enter first image location")
parser.add_argument("-o", "--Output1", help = "Enter frame location")
args = parser.parse_args()

path = args.Input1

cap = cv2.VideoCapture(path)
i = 1
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        cv2.imwrite(args.Output1+'frame_'+str(i)+'.jpg',frame)
        i+=1
#         cv2.imshow('Counter',frame)
#         if cv2.waitKey() == ord('q'):
#             cv2.destroyAllWindows()
    
cv2.destroyAllWindows()
cap.release()
