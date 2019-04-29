import numpy as np
import scipy.misc
# the array is loaded into b
a = np.load('train.p')

with open("annotate.txt","w") as f:
    for i in range(len(a['features'])):
        file_name = str(i)  + ".jpg"
        scipy.misc.toimage(a['features'][i], cmin=0.0, cmax=...).save("train_images/"+file_name)
        line = "train_images/" + file_name + ",2,2,30,30,"+str(a['labels'][i])+"\n"
        f.write(line)
