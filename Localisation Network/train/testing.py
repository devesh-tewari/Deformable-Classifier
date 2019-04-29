import numpy as np
import cv2
from keras import backend as K
print('**********',K.tensorflow_backend._get_available_gpus(),'************')

# data = np.load('train.p')
#
# x = data['features']
# y = data['labels']
#
# x = np.sum( x, axis=3 )
# print(x.shape)
#
# cv2.imshow('abc',x[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
