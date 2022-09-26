
from BaseProcessor import BaseProcessor
from numpy import ndarray
from Lens import Lens


class Sensor(BaseProcessor):
    """A basic sensor simulator. Inherits from BaseProcessor abstract base class. The process function will be implemented
        inside the class.

    Attributes:
        gain (int): Is going to affect on the image pixels. It is a property with the ability of setter and getter.
    """
    def __init__(self):
        self._gain = 0
        super().__init__()

    # @Lens_decorator
    def process(self, image: ndarray) -> ndarray:
        """Abstract method.

        Args:
            image: Only parameter. 2D Numpy array.

        Returns:
            A 2D Numpy array as a result of "gain * image".

        Raises:
            AssertionError: If the input/output image is not in numpy array format or if its dimension is not 2D.
        """
        print("process in Sensor class")
        self.check_2D_numpy(image)
        result = self.gain * image
        self.check_2D_numpy(result)
        return result

    @Lens.process_decorator
    def process_with_lens_decorator(self, image):
        """Will call Lens' process before calling the Sensor's process function.
        Assumption: The size properties of Lens are fitted to the input image.
        Args:
            image: Only parameter. 2D Numpy array.
        Returns:
            numpy 2D array image
        Raises:
            AssertionError, as it is in process method.
        """
        print("Now calling process from Sensor.")
        return self.process(image)

    def process_10_item_iterator(self, image):
        for i in range(10):
            yield image, i
    # --------- Gain -----------
    def set_gain(self, g: int) ->None:
        """To set 'gain' property.

        Args:
            h: Only parameter. A value to set the 'gain' property.

        Raises:
            AssertionError: If the input argument is not integer.
        """
        self.check_integer(g)
        self._gain = g

    def get_gain(self) -> int:
        """To set gain property.

        Returns:
            The value of 'gain' property.
        """
        return self._gain

    gain = property(get_gain, set_gain)





def mymean(*args)->int:
    """This function create a random image and pass it through Sensor.process method with its gain of "1". Finally, it
    calculates the average of pixels' value.

    Args:
        args: Do nothing. Used in the case of concurrent calling this function.

    Returns:
        The average of pixels' value in image.
    """
    import random
    import numpy as np
    from functools import reduce
    # randomly select the width and height:
    width = random.randint(100, 1000)
    height = random.randint(100, 1000)

    # random image:
    image_ = np.array([[random.randint(0,255) for w in range(width)] for h in range(height)])
    # pass it through Sensor object
    s = Sensor()
    s.gain = 1
    image = s.process(image_)

    # calculates the average of its pixels' value using "reduce" method in "functools" package.
    av_im = reduce(lambda a,b : a+ sum(b), image,0)

    return av_im

def concurrent_mymean(times: int)->list:
    """ It calls "mymean" function "times" times, concurrently.

    Args:
        times: The number of calling "mymean" function.

    Returns:
         A list of averages as a result of calling "mymean".
    """

    from multiprocessing import Pool

    num_worker = 5
    with Pool(num_worker) as p:
        results = p.map(mymean, [i for i in range(times)])

    return results







# #small trial
# import numpy as np
#
# s = Sensor()
# s.gain = 10
# image = np.ones((10,10))
# # Sample Runs:
# # ---------------
# # print(s.process(image))
# # ---------------
# # print(s.process_with_lens_decorator(image)   # calling sensor's process but after calling Lens' process
# # ---------------
# # As iterator:
# for im,indx in s.process_10_item_iterator(image):
#     print(indx)
# # ---------------
# #  calling "mymean" function:
# print("The average of pixels in random image: ", mymean())
# # ---------------
# calling "concurrent_mymean" function

if __name__ == "__main__":
    print("100 times calling mymean in concurrent manner: ", concurrent_mymean(100))

