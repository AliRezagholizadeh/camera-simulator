
from BaseProcessor import BaseProcessor
from numpy import ndarray
# from Lens import Lens_decorator
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
    @Lens
    def process(self, image: ndarray) -> ndarray:
        """Abstract method.

        Args:
            image: Only parameter. 2D Numpy array.

        Returns:
            A 2D Numpy array as a result of "gain * image".

        Raises:
            AssertionError: If the input/output image is not in numpy array format or if its dimension is not 2D.
        """
        print("sensor process")
        self.check_2D_numpy(image)
        result = self.gain * image
        self.check_2D_numpy(result)
        return result



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




#small trial
import numpy as np
#
s = Sensor()
s.gain = 10
print(s.process(np.ones((10,10))))