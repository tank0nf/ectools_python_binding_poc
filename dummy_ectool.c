#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdlib.h>

// Global variable to simulate fan speed
static int fan_speed = 2500;

// Function to get the current fan speed
int get_fan_speed() {
    return fan_speed;
}

// Function to set the fan speed (for simulation purposes)
int set_fan_speed(int speed) {
    if (speed < 0 || speed > 5000) {
        fprintf(stderr, "Error: Invalid fan speed. Must be between 0 and 5000.\n");
        return -1; // Return error code
    }
    fan_speed = speed;
    printf("Fan speed set to: %d\n", fan_speed);
    return 0; // Success
}

// Function to check the fan status (running or idle)
const char* get_fan_status() {
    if (fan_speed == 0) {
        return "Idle";
    }
    return "Running";
}

#ifdef __cplusplus
}
#endif
