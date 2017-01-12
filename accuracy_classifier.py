from __future__ import division

def acc_classifier(classifier_c, mask_c, img_name):
    result = 0
    for c in classifier_c:
        for b in mask_c:
            diff1, diff2,= abs(c[0] - b[0]), abs(c[1] - b[1])
            diff3, diff4 = abs(c[2] - b[2]), abs(c[3] - b[3])
            if diff1 <= 5 and diff2 <= 5 and diff3<= 5 and diff4 <= 5:
                result += 1
    actual_num_win = len(mask_c)
    accuracy = result/actual_num_win * 100
    print img_name + ":" + accuracy

m_c = [[239, 266, 27, 49], [186, 266, 28, 49], [133, 266, 28, 49], [80, 266, 25, 49], [26, 266, 26, 49], [300, 189, 27, 49], [239, 189, 27, 49], [186, 189, 28, 49], [133, 189, 28, 49], [80, 189, 25, 49], [26, 189, 26, 49], [300, 113, 27, 51], [239, 113, 27, 51], [186, 113, 28, 51], [133, 113, 28, 51], [80, 113, 25, 51], [26, 113, 26, 51], [300, 39, 27, 44], [239, 39, 27, 44], [186, 39, 28, 44], [133, 39, 28, 44], [80, 39, 25, 44], [26, 39, 26, 44]]
c_c = [[246, 266, 27, 49], [186, 266, 28, 49], [133, 266, 28, 49], [80, 266, 26, 59], [26, 266, 26, 49], [298, 189, 27, 49], [239, 199, 27, 49], [186, 189, 28, 49], [133, 189, 28, 49], [80, 189, 25, 49], [26, 189, 26, 49], [300, 113, 27, 51], [239, 113, 27, 51], [186, 113, 28, 51], [133, 113, 28, 51], [80, 163, 25, 51], [26, 113, 26, 51], [300, 39, 27, 44], [239, 39, 27, 44], [186, 39, 28, 44], [133, 39, 28, 44], [80, 39, 25, 44], [26, 39, 26, 44]]

name = "facade_0_0054919_0055060"
acc_classifier(c_c,m_c,name)
