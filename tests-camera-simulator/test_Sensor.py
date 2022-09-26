from os import path
import sys
sys.path.append(path.abspath('../camera-simulator'))
from Sensor import Sensor
import unittest
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

    return image

class TestLens(unittest.TestCase):
    def testing_scensor(self):
        """
        This function will test the process function in Sensor module. These elements will be teste:
        - whether the image is 2D
        - whether the image is a ndarray
        - whether the gain is not an integer
        - the correct multiplication of image with gain

        For checking these elements, we run the test 1000 times after selecting the parameters with these considerations:

        - gain: is randomly selected among a mixed list of integer and float numbers, themselves selected randomly
                from a range of [0, 100].
        - image: its dimension is randomly selected (with the chance of 70%) as a 2D image using "width_list" and
        "height_list" and (with the chance of 30%) as 1D image.
        - image also is type-casted to a non numpy array with the chance of 30%.

        """
        width_list = [100 + i* 50 for i in range(5) ]
        height_list = [100 + i* 50 for i in range(5) ]

        gain_int_list = [random.randint(1,100) for i in range(100)]
        gain_float_list = [random.random() * random.randint(1,100) for i in range(100)]
        gain_mixed_list = gain_int_list + gain_float_list

        for i in range(1000):

            sensor = Sensor()   # instantiating from Sensor.

            gain = gain_mixed_list[random.randint(0, len(gain_mixed_list)-1)]   # randomly set a local gain variable
            # from its corresponding list.

            image = selcting_image(width_list, height_list) # Select an image (numpy or non-numpy) of different size
            # (regarding the "width_list" and "height_list") with 1 as its pixels' value.


            # all side-conditions:
            image_type_array = type(image) == np.ndarray
            image_1D = 1 in np.array(image).shape
            gain_type_int = type(gain) == int
            # checking the Sensor.process and Sensor.gain performance:
            if(image_type_array and not image_1D and gain_type_int):   # In the case of all side-conditions are met.
                print("all side-conditions are met...")
                sensor.gain = gain
                result = gain * image
                sen_result = sensor.process(image)
                self.assertTrue((sen_result == result).all())
            elif(not gain_type_int):                                   # In the case of gain is float.
                print("gain is float: ", gain)
                self.assertRaises(AssertionError, lambda: sensor.set_gain(gain))
            elif(not image_type_array):                                # In the case of image type is non-numpy.
                print("image type is not ndarray: ", type(image))
                self.assertRaises(AssertionError, lambda: sensor.process(image))
            elif(image_1D):                                            # In the case of image dimension is 1D.
                print("image dimension is 1D: ", image.shape)
                self.assertRaises(AssertionError, lambda: sensor.process(image))
            else:
                print("STRANGE!!")
                print(f"image_type_array, image_1D, gain_type_int: {image_type_array ,image_1D, gain_type_int}")






            # if(type(image) == np.ndarray and type(gain) == int):       # In the case of all side-conditions is suitable.
            #     print("all side-conditions is suitable...")
            #     sensor.gain = gain
            #     result = gain * image
            #     sen_result = sensor.process(image)
            #     print("res: ", result)
            #     print("sen_res: ", sen_result)
            #     print("check : ", sen_result == result)
            #     self.assertTrue((sen_result == result).all())
            # elif(type(image) == np.ndarray ):                          # In the case of gain is float.
            #     print("gain is float: ", gain)
            #     self.assertRaises(AssertionError, lambda: sensor.set_gain(gain))
            # elif(type(gain) == int):                                  # In the case of image type is not ndarray:
            #     print("image type is not ndarray: ", type(image))
            #     self.assertRaises(AssertionError, lambda: sensor.process(image))








if __name__ == "__main__":
    unittest.main()
