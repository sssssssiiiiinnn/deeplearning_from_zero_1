import sys
import os

sys.path.append(os.pardir)

import numpy as np
from PIL import Image

from dataset.mnist import load_mnist


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
img = x_train[0]
label = t_train[0]
print(label)


print(img.shape)
img = img.reshape(28, 28)
img_show(img)