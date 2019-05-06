import numpy as np
import scipy.misc
import os
import cv2
# the array is loaded into b
# a = np.load('test.p', allow_pickle=True)
#
# with open("annotate_test.txt","w") as f:
#     for i in range(len(a['features'])):
#         file_name = str(i)  + ".jpg"
#         scipy.misc.toimage(a['features'][i], cmin=0.0, cmax=...).save("test_images/"+file_name)
#         line = "test_images/" + file_name + ",2,2,30,30,"+str(a['labels'][i])+"\n"
#         f.write(line)

idx = 0
path = 'test_images2'
afile = open("annotate_test.txt","w")
for r, d, f in os.walk(path):
    for file in f:
        img = cv2.imread(os.path.join(path, file))
        cv2.imwrite('test_images/'+str(idx)+'.jpg', img)
        line = "test_images/" + str(idx)+'.jpg' + ",2,2,30,30,"+str(1)+"\n"
        afile.write(line)
        idx += 1
afile.close()
