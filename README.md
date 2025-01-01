# Photo-Conversion
This Python project allows users to convert a digital photo into a pencil sketch. It provides a simple graphical interface to select an image file, apply the sketch effect, and save the output.

---

## Features
- **Converts any digital photo into a pencil sketch.**
- **Allows the user to select an image file via a file dialog.**
- **Provides the option to save the output image to a desired location.**
- **Displays the generated sketch in a pop-up window.**

---

## Technologies Used
- **Python**
- **OpenCV**
- **Tkinter (for file dialogs)**

---

## How it works
How It Works
- **The script opens a file dialog for the user to select an input image.**
- **The image is processed as follows:**
1. Converted to grayscale.
2. Inverted to create a negative.
3. Blurred to soften the image.
4. Combined with the grayscale image to generate the sketch effect.
- **The user is prompted to select a location to save the output image.**
- **The resulting sketch is displayed in a pop-up window.**

---

## Usage
Usage

- **Run the script:**
python Photo_Conversion.py

- **Follow the prompts:**
1. Select an input image file.
2. Choose a location to save the output image.

- **View the generated sketch in the pop-up window.**
