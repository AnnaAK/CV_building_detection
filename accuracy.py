from __future__ import division

actual_color = open("actual_color.txt","r")
predicted_color = open("detected_color.txt", "r")
result = []
lines_a = actual_color.readlines()
lines_p = predicted_color.readlines()
for line_a in lines_a:
    name_act, color_act = line_a.split(":")
    for line_p in lines_p:
        name_pred, color_pred = line_p.split(":")
        if (name_act == name_pred): result.append(color_act == color_pred)
right = result.count(True)
all = len(lines_a)
accuracy = right/all * 100
print "Accuracy detection of color is {} %".format(accuracy)


