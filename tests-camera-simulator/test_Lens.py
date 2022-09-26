import unittest
from os import path
import sys
sys.path.append(path.abspath('../camera-simulator'))
from Lens import Lens
import random
import numpy as np

def selcting_image(width_list, height_list):
    """Select an image (numpy or non-numpy) of different size (regarding the "width_list" and "height_list") with 1 as
       its pixels' value.

    :param width_list: The list among which we want to select the width of the image.
    :param height_list: The list among which we want to select the height of the image.
    :return: A 1D or 2D numpy array or list
    """
    # image part:
    image_width_indx = random.randint(0, len(width_list) - 1)  # randomly select a width index.
    image_height_indx = random.randint(0, len(height_list) - 1)  # randomly select a height index.
    image_dim_selection_rand = random.random()
    if image_dim_selection_rand > 0.3:  # 70% selecting 2D array
        image_width = width_list[image_width_indx]  # randomly select a width value from corresponding list.
        image_height = height_list[image_height_indx]  # randomly select a height value from corresponding list.
    else:  # 30% selecting 1D array.
        if image_dim_selection_rand > 0.15:  # 50% of the case select with the width of 1 and 50% with the
            # height of 1.
            image_width = 1
            image_height = height_list[image_height_indx]
        else:
            image_width = height_list[image_height_indx]
            image_height = 1

    if random.random() < 0.3:  # to define image as a numpy array or a list with the chance of 30%
        image_ = np.ones((image_height, image_width))  # an 2D non numpy array of specific width and height
        # is defined
        image = image_.tolist()
    else:
        image = np.ones((image_height, image_width))  # an 2D numpy array of specific width and height is
        # defined.
    # End of # image part.

    return image, image_width, image_height

class TestLens(unittest.TestCase):
    def testing_process(self):
        """
            This function will test the process function in Lens module. These elements will be teste:
            - whether the image is 2D
            - whether the image is a ndarray
            - whether the image size fit to lens' size

            For checking these elements, we run the test 1000 times after selecting the parameters with these
            considerations:

            - image: its dimension is randomly selected (with the chance of 70%) as a 2D image using "width_list" and
            "height_list" and (with the chance of 30%) as 1D image.
            - image also is type-casted to a non numpy array with the chance of 30%.
            - lens size is also selected from "width_list" and "height_list".

        """
        width_list = [100 + i* 50 for i in range(5) ]
        height_list = [100 + i* 50 for i in range(5) ]

        for i in range(1000):
            lens_width_indx  = random.randint(0,4)    # randomly select a width index.
            lens_height_indx = random.randint(0,4)   # randomly select a height index.

            lens = Lens()
            lens_width = width_list[lens_width_indx]
            lens_height = height_list[lens_height_indx]

            lens.width = lens_width        # randomly select a width value from corresponding list.
            lens.height = lens_height     # randomly select a height value from corresponding list.


            image, image_width, image_height = selcting_image(width_list, height_list)  # Select an image (numpy or non-numpy) of different size
            # (regarding the "width_list" and "height_list") with 1 as its pixels' value.

            # all side-conditions:
            image_type_array = type(image) == np.ndarray
            image_1D = 1 in np.array(image).shape
            image_lens_size = image_width == lens_width and image_height == lens_height

            # checking the Lens.process and Lens.gain performance:
            # if (image.shape[1] == lens_width and image.shape[0] == lens_height):
            if(image_type_array and not image_1D and image_lens_size): # In the case of all side-conditions are met.
                print("all side-conditions are met...")
                image_identity = lens.process(image) == image
                self.assertTrue(image_identity.all())
            elif(not image_type_array):                                 # In the case of image type is non-numpy.
                print("image type is not ndarray: ", type(image))
                self.assertRaises(AssertionError, lambda: lens.process(image))
            elif(image_1D):                                             # In the case of image dimension is 1D.
                print("image dimension is 1D: ", image.shape)
                self.assertRaises(AssertionError, lambda: lens.process(image))
            elif(not image_lens_size):                              # In the case of image and lens sizes are not
                # identical.
                print(f"image and lens size are not the same. (image_width, lens_width, image_height, lens_height): {image_width, lens_width, image_height, lens_height}")
                self.assertRaises(ValueError, lambda: lens.process(image))
            else:
                print("STRANGE!!")
                print(f"image_type_array, image_1D, image_lens_size: {image_type_array, image_1D, image_lens_size}")








if __name__ == "__main__":
    unittest.main()