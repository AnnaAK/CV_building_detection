import glob
import argparse
from color_detection import *
result = open("detected_color.txt", "w+")

def bound(color):
    if color == "red": return [0,0,255]
    elif color == "blue": return [255,85,0]
    elif color == "white": return [255,255,255]
    elif color == "yellow": return [0,255,255]
    elif color == "black": return [0,0,0]
    elif color == "dark_blue": return [255,0,0]

def detectRect(color, image):
    boundaries = bound(color)
    boundaries = np.array(boundaries, dtype="uint8")
    mask = cv2.inRange(image, boundaries, boundaries)
    output = cv2.bitwise_and(image, image, mask=mask)
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 10, 250, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                           cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1]
    cv2.waitKey()
    rect_coordinates = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        rect = [x,y,w,h]
        rect_coordinates.append(rect)
    #print rect_coordinates
    return rect_coordinates

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True)
ap.add_argument("-l", "--labels", required=True)
args = vars(ap.parse_args())
color_win = "yellow"
color_bld = "dark_blue"
for imagePath in glob.glob("cmp/"+ args["images"] + "/*"):
    name = imagePath.split("\\")[1]
    name = name[0:len(name) - 4]
    labelPath = "cmp/"+ args["labels"] + "/" + name + ".png"
    label = cv2.imread(labelPath)
    image = cv2.imread(imagePath)
    win_c = detectRect(color_win,label)
    bld_c = detectRect(color_bld,label)
    c = color_detection(win_c,bld_c,image)
    result.write(name + ":")
    result.write(c + "\n")
result.close()


