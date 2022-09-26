from abc import ABC, abstractmethod

from numpy import ndarray

class BaseProcessor(ABC):
    """A base class inherited from Abstract Base Class (ABC). Process method is its only abstract method.

    Attributes:
        enable (bool): Is a property with the ability of setter and getter.
    """
    def __init__(self):
        self._enable = False
        super().__init__()

    @abstractmethod
    def process(self, image: ndarray):
        """Abstract method.
        Args:
            image: 2D Numpy array

        Returns:
            Processed image or instead raise an exception.
        """
        pass

    def check_2D_numpy(self, data: ndarray) -> None:
        """To check whether an input data is numpy array and has 2 dimensions.

        Args:
            data: Only parameter. A 2D Numpy array.

        Raises:
            AssertionError: If the input 'data' is not in numpy array format or if its dimension is not 2D.
        """

        try:
            assert type(data) is ndarray
        except:
            print("Input data is not a numpy array.")
            raise

        try:
            assert 1 not in data.shape
        except:
            print("The shape of the input data is not 2D. Its shape is: ", data.shape)
            raise
        return


    def check_integer(self, value: int) -> None:
        """To check whether an input data is in integer type.

        Args:
            value: Only parameter.

        Raises:
            AssertionError: If the input parameter ('value') is not in integer type.
        """
        try:
            assert type(value) == int
        except:
            print("The value is supposed to be integer.")
            raise

    def check_bool(self, value: bool) -> None:
        """To check whether an input data is in boolean type.

        Args:
            value: Only parameter.

        Raises:
            AssertionError: If the input parameter ('value') is not in boolean type.
        """

        try:
            assert type(value) == bool
        except:
            print("The value is supposed to be boolean.")
            raise

    def set_enable(self, bool_val: bool) -> None:
        """To set 'enable' property.

        Args:
            bool_val: A value to set the 'enable' property.

        Raises:
            AssertionError: If the input argument is not boolean.
        """
        self.check_bool(bool_val)
        self._enable = bool_val


    def get_enable(self) -> bool:
        """To set 'enable' property.

        Returns:
            The value of 'enable' property.
        """
        return self._enable

    enable = property(get_enable, set_enable)


