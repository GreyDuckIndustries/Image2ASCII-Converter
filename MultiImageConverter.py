import os
from PIL import Image
import numpy as np

# Function to map grayscale values to ASCII characters
def grayscale_to_ascii(value):
    ascii_chars = "@%#*+=-:. "
    return ascii_chars[int(value / 255 * (len(ascii_chars) - 1))]

# Function to convert an image to ASCII art
def image_to_ascii(image_path, output_width=100):
    # Load the image
    image = Image.open(image_path)
    
    # Convert to grayscale
    grayscale_image = image.convert("L")
    
    # Calculate the aspect ratio
    aspect_ratio = grayscale_image.height / grayscale_image.width
    new_height = int(output_width * aspect_ratio)
    
    # Resize the image
    resized_image = grayscale_image.resize((output_width, new_height))
    
    # Convert the image to a numpy array
    image_array = np.array(resized_image)
    
    # Map the grayscale values to ASCII characters
    ascii_art = "\n".join(
        "".join(grayscale_to_ascii(value) for value in row)
        for row in image_array
    )
    
    return ascii_art

# Function to save ASCII art to a text file
def save_ascii_art(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)

# Main function
def main(images_folder):
    # Create the output folder if it doesn't exist
    output_folder = os.path.join(images_folder, "ascii_art")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each jpg file in the images folder
    for filename in os.listdir(images_folder):
        if filename.lower().endswith(".jpg"):
            image_path = os.path.join(images_folder, filename)
            ascii_art = image_to_ascii(image_path)
            
            # Determine the output filename and path
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)
            
            # Save the ASCII art to the text file
            save_ascii_art(ascii_art, output_path)
            print(f"ASCII art for {filename} has been written to {output_path}")

# Example usage
if __name__ == "__main__":
    images_folder = "YOUR/FILE/PATH/HERE"  # Path to the images folder
    main(images_folder)
