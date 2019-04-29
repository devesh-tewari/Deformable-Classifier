import numpy as np
import cv2

test_imgs = np.load('test.p', allow_pickle=True)['features']

idx = 0
for img in test_imgs:
    cv2.imwrite('test_images/'+str(idx)+'.jpg', img)
    idx += 1
