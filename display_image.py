import cv2
import argparse
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.Output:
    img = cv2.imread(args.Output)
    while True:
        cv2.imshow('John',img)
        if cv2.waitKey(100) == ord('q'):
            cv2.destroyAllWindows()
            break
