import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def sketch_photo(input_path, output_path):
    # Read the input image
    image = cv2.imread(input_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Blur the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)

    # Invert the blurred image
    inverted_blur = cv2.bitwise_not(blurred_image)

    # Create the sketch by blending the grayscale image with the inverted blur
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

    # Save the final output
    cv2.imwrite(output_path, sketch)

    print(f"Sketch saved at {output_path}")

def main():
    # Hide the root window
    Tk().withdraw()

    # Ask the user to select an input image file
    print("Please select an input image file.")
    input_file = askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])

    if not input_file:
        print("No file selected. Exiting.")
        return

    # Ask the user to select a location to save the output image
    print("Please select a location to save the sketched image.")
    output_file = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png"), ("Bitmap Image", "*.bmp")])

    if not output_file:
        print("No output file selected. Exiting.")
        return

    # Call the sketch_photo function
    sketch_photo(input_file, output_file)

    # Display the result
    output_image = cv2.imread(output_file)
    cv2.imshow("Sketched Photo", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

