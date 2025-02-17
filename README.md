Steps to run:
1. gcc -shared -o libdummy_ectool.so -fPIC dummy_ectool.c
2. python3 fw-fanctrl.py

# Explanation of Files
## fw-fanctrl.py
This is the Python main script that works with the dummy_ectool library. It does the following:
1. Declares functions to read and write the fan speed.
2. Declares a function to read the fan status.
3. Contains an example usage block that shows how to call the functions.

## dummy_ectool.py
This Python script is a wrapper of the libdummy_ectool.so shared library. It:
1. Loads the shared library using the ctypes module.
2. Specifies the C function signatures (i.e., argument types and return types).
3. Offers Python functions that invoke the respective C functions.

## dummy_ectool.c
This is a C source file that performs the fan control logic. It:
1. Declares functions to obtain and set the fan speed.
2. Declares a function to retrieve the fan status.
3. Utilizes a global variable to emulate the fan speed.

# How the Program Works
The dummy_ectool.c source file is compiled into a shared library (libdummy_ectool.so) with the gcc compiler. The flags:

-shared: Instructs the compiler to produce a shared library.
-fPIC: Produces position-independent code, which is necessary for shared libraries.

The dummy_ectool.py script imports the shared library with ctypes.CDLL() and declares the function signatures for the C functions. It also declares argument types and return types.

The fw-fanctrl.py command loads the dummy_ectool module, through which the access to the C functions is allowed. The program then:

Displays the fan status and current speed.
Sets the fan speed to 3000 RPM and displays the new fan status and speed.
Tries to set the fan speed to 6000 RPM, causing an error due to the correct range being 0-5000 RPM. This checks for the error handling.

THIS IS ONLY A PROOF OF CONCEPT FOR GSOC AND LARGE SCALE IMPLEMENTATION WILL FOLLOW THROUGH.