# Proof of Concept for GSoC: Create Python bindings for ectool.
Mentor: Carlos Fernandez

**This is only a proof of concept, large scale implementation will follow through.**

## Steps to Run
1. Compile the C source code into a shared library:
    ```bash
    gcc -shared -o libdummy_ectool.so -fPIC dummy_ectool.c
    ```

2. Run the Python script:
    ```bash
    python3 fw-fanctrl.py
    ```

---

## Explanation of Files

### `fw-fanctrl.py`
This is the Python main script that works with the `dummy_ectool` library. 
It does the following:
1. Declares functions to read and write the fan speed.
2. Declares a function to read the fan status.
3. Contains an example usage block that shows how to call the functions.

### `dummy_ectool.py`
This Python script is a wrapper for the `libdummy_ectool.so` shared library, as it:
1. Loads the shared library using the `ctypes` module.
2. Specifies the C function signatures (i.e., argument types and return types).
3. Offers Python functions that invoke the respective C functions.

### `dummy_ectool.c`
This is a C source file that performs the fan control logic, as it:
1. Declares functions to obtain and set the fan speed.
2. Declares a function to retrieve the fan status.
3. Utilizes a global variable to emulate the fan speed.

---

## How the Program Works

The `dummy_ectool.c` source file is compiled into a shared library (`libdummy_ectool.so`) with the `gcc` compiler. The flags:

- `-shared`: Instructs the compiler to produce a shared library.
- `-fPIC`: Produces position-independent code, which is necessary for shared libraries.

The `dummy_ectool.py` script imports the shared library with `ctypes.CDLL()` and declares the function signatures for the C functions. It also specifies argument types and return types.

The `fw-fanctrl.py` script loads the `dummy_ectool` module, allowing access to the C functions. The program then:
1. Displays the fan status and current speed.
2. Sets the fan speed to 3000 RPM and displays the new fan status and speed.
3. Attempts to set the fan speed to 6000 RPM, causing an error due to the correct range being 0-5000 RPM. This step tests the error handling mechanism.
