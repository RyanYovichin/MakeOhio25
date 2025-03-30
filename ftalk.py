import serial
import time

# Define the serial port (replace 'COM4' with your correct port)
arduino = serial.Serial('COM4', 9600, timeout=1)  # COM4 is just an example, replace it with your actual port
print("Y1")

# Give time for the Arduino to reset after connection
time.sleep(3)

# Check if the serial port is open
if arduino.is_open:
    print("Serial port is open!")
else:
    print("Failed to open serial port.")
    exit()

# Open the .txt file and send it line by line
try:
    with open('text.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove any unwanted newline or extra spaces from each line
            if line:  # Only send non-empty lines
                arduino.write(line.encode())  # Send each line as bytes
                arduino.flush()  # Ensure the data is written to the serial port immediately
                print("Y2: Sent:", line)  # Print the line being sent
                time.sleep(0.1)  # Optional: add delay between lines

                # Now, read the response from the Arduino
                while arduino.in_waiting > 0:  # Check if there's data available to read
                    response = arduino.readline().decode('utf-8').strip()  # Read the response line
                    if response:
                        print(f"Arduino: {response}")
            else:
                print("Y2: Skipped empty line.")
except FileNotFoundError:
    print("Error: 'text.txt' file not found.")
except Exception as e:
    print(f"Error during communication: {e}")

# Close the serial connection
arduino.close()
print("Serial connection closed.")
