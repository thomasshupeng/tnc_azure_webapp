import os
from cntk import load_model
from cntk.ops import softmax
from PIL import Image
import numpy as np


image_name = "L-LJS17-EBF-0045.JPG"
image_width, image_height = 682, 512

model_path = os.path.join(os.getcwd(),"..", "models")
MODEL_NAME = '21CResNet18'
_base_model_name = "ResNet18_ImageNet_CNTK.model"
name = "TNC_" + _base_model_name
model_path = os.path.join(model_path, MODEL_NAME)
model_file = os.path.join(model_path, name)

print("Loading model: ", model_file)
trained_model = load_model(model_file)

if trained_model is not None:
    img = Image.open(image_name)
    if image_name.endswith("png"):
        temp = Image.new("RGB", img.size, (255, 255, 255))
        temp.paste(img, img)
        img = temp
    re_sized = img.resize((image_width, image_height), Image.ANTIALIAS)
    bgr_image = np.asarray(re_sized, dtype=np.float32)[..., [2, 1, 0]]
    hwc_format = np.ascontiguousarray(np.rollaxis(bgr_image, 2))

        # Alternatively: if you want to use opencv-python
        # cv_img = cv2.imread(image_path)
        # resized = cv2.resize(cv_img, (image_width, image_height), interpolation=cv2.INTER_NEAREST)
        # bgr_image = np.asarray(resized, dtype=np.float32)
        # hwc_format = np.ascontiguousarray(np.rollaxis(bgr_image, 2))

        # compute model output
    arguments = {trained_model.arguments[0]: [hwc_format]}
    output = trained_model.eval(arguments)

        # return softmax probabilities
    sm = softmax(output[0])
    prob = sm.eval()

    for probability in prob:
        print("{:f}".format(probability))


