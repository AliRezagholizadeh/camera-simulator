###This is a second version of a simple camera-simulator created as a response to the assignment (_"Python_Test.pdf"_).

### This project contains of a package called camera-simulator which itself contains these dependencies:

- 1- BaseProcessor:
  Contains only one class named "BaseProcessor" which is an abstract class.

  "BaseProcessor" class contains:
  - a) A property "enable" (boolean type with possibility of taking its control using setter and getter). 
  - b) An abstract method "process" to process the input 2D numpy data (image) and return
output 2D numpy data (image).
  - c) "check_2D_numpy" method to check whether an input data is a numpy array and has 2 dimensions.
  - d) "check_integer" method to check whether an input data is in integer type.
  - e) "check_bool" method to check whether an input data is in boolean type.
  
- 2- Lens:
  Contains one class named "Lens" to simulate the lens functionality. It inherits from "BaseProcessor" abstract base class.

  "Lens" class contains:
  - a) A property "height" (int type with possibility of taking its control using setter and getter). 
  - b) A property "width" (int type with possibility of taking its control using setter and getter).
  - c) The "process" method validates the input image. If the image shape matches the Lens' size, it returns the image, otherwise will raise ValueError exception. 
  - Its input and output are 2D numpy array. "Assert" applied to meet these requirements.

- 3- Sensor: 
  Contains one class named "Sensor" to simulate the sensor functionality. It inherits from "BaseProcessor" abstract base class.  

  "Sensor" class contains:
  - a) A property "gain" (int type with possibility of taking its control using setter and getter).
  - b) The "process" method affects on input image by the factor of "gain" parameter.
       - Its input and output are 2D numpy array. "Assert" applied to meet these requirements.


### From Specific Skills part of the assignment, following sub-parts have been done:
  - "Packaging":
    - To make this file installable, setup.py has been added with its explanation. Afterwards, python wheels created.
    - All installed dependencies we used is only "numpy" which is defined at the top of the modules and also has been added in setup.py. 

  - "Testing":
    - Write unit tests for the package.


### From Advanced Python part of the assignment, following sub-parts have been completed:
 - Implement a Lens decorator for Sensor, such that each time the Sensor process is called, the Lens process is called.
 - Allow the Sensor to be used as an iterator of 10 elements. At each cycle, the returned image is the original image plus the index of the iteration.
 - Create a function mymean that generates a random image, passes that image through a Sensor object and returns the mean of the image.
   - This function is put in Sensor modul.
   - It is assumed that a random image is passed through Sensor.process method (as it is not mentioned in the task explaination).

 - Demonstrate the use of the concurrent package to create a pool of 5 workers and call the previously created mymean function 100 times.
   - This function is put in Sensor modul.