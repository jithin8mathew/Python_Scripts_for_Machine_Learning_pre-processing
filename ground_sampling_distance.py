altitude = 380 # in feet
sensor_width = 35.9 # in mm
sensor_height = 24 # in mm
focal_length = 35 # in mm
image_width = 8192 # in pixels
image_height = 5460 # in pixels

mavic_3_classic = {"image_width":5280, "image_height":3956, "focal_length":24, "sensor_width":17.3, "sensor_height":13}

# Convert altitude to meters
altitude_m = altitude * 0.3048

# Calculate the ground sample distance (GSD) in centimeters per pixel
mavic_3_classic_GSD = (altitude_m * mavic_3_classic["sensor_width"]) / (mavic_3_classic["focal_length"] * mavic_3_classic["image_width"])

GSD = (altitude_m * sensor_width) / (focal_length * image_width)

# Calculate the size of each pixel in millimeters
pixel_size = sensor_width / image_width
mavic_3_classic_pixel_size = mavic_3_classic["sensor_width"] / mavic_3_classic["image_width"]

# Print the results
print(pixel_size)
print("Ground Sample Distance: {:.4f} cm/pixel".format(GSD))
print("Pixel size: {:.4f} mm".format(pixel_size))

print("Ground Sample Distance Mavic 3 classic: {:.4f} cm/pixel".format(mavic_3_classic_GSD))
print("Pixel size of mavic 3 classic : {:.4f} mm".format(mavic_3_classic_pixel_size))

