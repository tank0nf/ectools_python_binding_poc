import dummy_ectool

# Function to get the current fan speed
def get_fan_speed():
    return dummy_ectool.get_fan_speed()

# Function to set the fan speed
def set_fan_speed(speed):
    try:
        dummy_ectool.set_fan_speed(speed)
        print(f"Fan speed successfully set to {speed} RPM.")
    except ValueError as e:
        print("Error:", e)

# Function to get the fan status
def get_fan_status():
    return dummy_ectool.get_fan_status()

# Example usage
if __name__ == "__main__":
    # Display current status
    print("Current Fan Speed:", get_fan_speed())
    print("Fan Status:", get_fan_status())

    # Set a new fan speed and check status
    set_fan_speed(3000)
    print("Updated Fan Speed:", get_fan_speed())
    print("Fan Status:", get_fan_status())

    # Try setting an invalid speed
    set_fan_speed(6000)  # This should trigger an error
