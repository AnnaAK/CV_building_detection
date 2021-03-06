# detection of the color by hsv code of the image
from mask import *

bound = [
    ([160, 30, 30], [179, 230, 230], [0, 0, 0]),
    ([0, 30, 30], [22, 230, 230], [1, 0, 0]),
    ([22, 30, 30], [38, 230, 230], [2, 0, 0]),
    ([38, 30, 30], [75, 230, 230], [3, 0, 0]),
    ([75, 30, 30], [130, 230, 230], [4, 0, 0]),
    ([130, 30, 30], [160, 230, 230], [5, 0, 0]),
    ([0, 0, 0], [160, 10, 10], [7, 0, 0]),
    ([0, 90, 90], [160, 100, 100], [8, 0, 0])
]

def color(c):
    if c == 0: return "red"
    elif c == 1: return "orange"
    elif c == 2: return "yellow"
    elif c == 3: return "green"
    elif c == 5: return "violet"
    elif c == 4: return "blue"
    elif c == 6: return "pink"
    elif c == 8: return "white"
    elif c == 7: return "black"

def color_detection(win_c,bld_c,image):
    c_mask = get_mask(win_c, bld_c, image)
    output = cv2.bitwise_and(image, image, mask=c_mask)
    hsv_img = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    all_colors = np.zeros(9)
    for (lower, upper, c) in bound:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv_img, lower, upper)
        total_mask = np.logical_and(c_mask, mask)
        pix = np.count_nonzero(total_mask)
        all_colors[c[0]] += pix
    max = np.amax(all_colors)
    indx = np.where(all_colors == max)[0]
    building_color = color(indx)
    return building_color










