# Artificial Intelligence Project 4
## Optical Character Recognition (OCR)

### Objective
The objective of this project is to extract text from an input image using Optical Character Recognition (OCR).

### Technologies Used
- Python
- OpenCV
- Pytesseract
- Tesseract OCR
- NumPy
- Pillow

### Image Pre-processing
The input image is processed using:
1. Grayscale conversion
2. Gaussian Blur
3. Adaptive Thresholding

### OCR
Tesseract OCR is used to recognize text from the processed image.

### Confidence Validation
The OCR confidence score is calculated and compared with the required 80% threshold.

### Result
Average OCR Confidence: 91.33%

Validation Status: PASSED

### Project Structure

AI_Project_4/
- main.py
- requirements.txt
- README.md
- input/sample.png
- output/processed.png

### How to Run

Install the required libraries:

pip install -r requirements.txt

Run the program:

python main.py
