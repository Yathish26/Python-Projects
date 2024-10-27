import cairosvg
import os

def convert_png_to_svg(png_file_path, svg_file_path):
    try:
        # Convert PNG to SVG
        cairosvg.svg_from_png(png_file_path, write_to=svg_file_path)
        print(f"Converted '{png_file_path}' to '{svg_file_path}'")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
png_file = 'beebg.png'  # Change this to your PNG file path
svg_file = 'bee.svg'  # Desired output SVG file path

# Ensure the input file exists
if os.path.exists(png_file):
    convert_png_to_svg(png_file, svg_file)
else:
    print("The specified PNG file does not exist.")
