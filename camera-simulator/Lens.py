
from BaseProcessor import BaseProcessor
from numpy import ndarray

class Lens(BaseProcessor):
    """A basic lens simulator. Inherits from BaseProcessor abstract base class. The process function will be implemented
        inside the class.

    Attributes:
        width (int): A property of the lens' size. It is a property with the ability of setter and getter.
        height (int): A property of the lens' size. It is a property with the ability of setter and getter.

    """
    def __init__(self):
        self._width = 0
        self._height = 0
        super().__init__()


    def process(self, image: ndarray) -> ndarray:
        """Abstract method.

        Args:
            image: Only parameter. A 2D Numpy array.

        Returns:
            The input image if the size of the input image does match to the lens' size, otherwise raise an exception.


        Raises:
            AssertionError: If the input image is not in Numpy array format or if its size is not 2D.
            ValueError: If the size of the input image does not match to the lens' size

        """
        print("Lens process")
        # check being a numpy array
        self.check_2D_numpy(image)
        # check that the image size fit to the lens dimension.
        h = image.shape[0]
        w = image.shape[1]
        if(h == self.height and w == self.width):
            return image
        else:
            raise ValueError("The size of the input image is not matching to the Lens' size.")
            # return ValueError

    @staticmethod
    def process_decorator(sensor_process):
        # print("process_decorator function in Lens class.")
        from numpy import array
        def handler(cls_self, image):
            """Calling with Lens's process with assumption that the height and width of the Lens are fitted to the
               input image.
            """
            print("handler function in wrapped in proces_decorator")

            lens = Lens()
            lens.height = array(image).shape[0]
            lens.width = array(image).shape[1]
            lens.process(image)
            #-----------
            return sensor_process(cls_self, image)

        return handler

    # --------- Width -----------

    def set_width(self, w: int) -> None:
        """To set width property.

        Args:
            w: A value to set the 'width' property.

        Raises:
            AssertionError: If the input argument is not integer.
        """
        self.check_integer(w)
        self._width = w

    def get_width(self) -> int:
        """To set width property.

        Returns:
            The value of 'width' property.
        """
        return self._width

    width = property(get_width, set_width)

    # --------- Height -----------
    def set_height(self, h: int) -> None:
        """To set height property.

        Args:
            h: A value to set the 'height' property.

        Raises:
            AssertionError: If the input argument is not integer.
        """
        self.check_integer(h)
        self._height = h


    def get_height(self) -> int:
        """To set height property.

        Returns:
            The value of 'height' property.
        """
        return self._height

    height = property(get_height, set_height)





# small trial on decorator
# class Lens_decorator:
#     def __init__(self, f):
#         self.f = f
#
#
#     def __call__(self, *args):  # decorator to call lens' process
#         print("lens dec")
#         l = Lens()
#         l.width = 10
#         l.height = 10
#         l.process(*args)
#         return self.f.process(*args)
