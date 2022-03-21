import cv2
import argparse
# Initialize parser

parser = argparse.ArgumentParser()
# Adding optional argument
parser.add_argument("-i1", "--Input1", help = "Enter first image location")
parser.add_argument("-i2", "--Input2", help = "Enter second image location")
#    Read arguments from command line
args = parser.parse_args()

img1 = cv2.imread(args.Input1)
Img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)


img2 = cv2.imread(args.Input2)
Img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
if args.Input2:
    blended = cv2.addWeighted(src1=Img1,alpha=0.5,src2=Img2,beta=1,gamma=0)
    while True:
        cv2.imshow('John',blended)
        if cv2.waitKey(100) == ord('q'):
            cv2.destroyAllWindows()
            break