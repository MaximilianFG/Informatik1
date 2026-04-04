from tools.toolbox import input

width_px = int(input("Enter the width of the image in pixels: "))
height_px = int(input("Enter the height of the image in pixels: "))
bits_per_pixel = int(input("Enter the number of bits per pixel: "))
amount_of_colors = int(input("Enter the amount of color_channels: "))

total_bits = width_px * height_px * bits_per_pixel * amount_of_colors
total_mb = total_bits / (8 * 1000 * 1000)
total_mib = total_bits / (8 * 1024 * 1024)

print(
    f"The memory required for an image of {width_px}x{height_px} pixels is {total_mb:.2f} MB or {total_mib:.2f} MiB."
)
