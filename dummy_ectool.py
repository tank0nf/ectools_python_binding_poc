import ctypes
import os

# Explicitly set the absolute path if needed
lib_path = os.path.abspath("./libdummy_ectool.so")
lib = ctypes.CDLL(lib_path)

# Define the return types and argument types for the C functions
lib.get_fan_speed.restype = ctypes.c_int
lib.set_fan_speed.argtypes = [ctypes.c_int]
lib.set_fan_speed.restype = ctypes.c_int
lib.get_fan_status.restype = ctypes.c_char_p

def get_fan_speed():
    return lib.get_fan_speed()

def set_fan_speed(speed):
    result = lib.set_fan_speed(speed)
    if result == -1:
        raise ValueError("Invalid fan speed. Must be between 0 and 5000.")
    return result

def get_fan_status():
    return lib.get_fan_status().decode('utf-8')
