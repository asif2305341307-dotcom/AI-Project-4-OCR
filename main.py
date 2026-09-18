import cv2
import pytesseract

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# 1. Load input image
image = cv2.imread("input/sample.png")

if image is None:
    print("ERROR: input/sample.png not found!")
    exit()

# 2. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 4. Apply Adaptive Thresholding
thresh = cv2.adaptiveThreshold(
    blur,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# 5. Save processed image
cv2.imwrite("output/processed.png", thresh)

# 6. OCR
config = "--psm 6"

text = pytesseract.image_to_string(
    thresh,
    config=config
)

# 7. Get OCR confidence data
data = pytesseract.image_to_data(
    thresh,
    config=config,
    output_type=pytesseract.Output.DICT
)

confidences = []

for conf in data["conf"]:
    try:
        value = float(conf)

        if value >= 0:
            confidences.append(value)

    except ValueError:
        pass

# 8. Calculate average confidence
if confidences:
    average_confidence = sum(confidences) / len(confidences)
else:
    average_confidence = 0

# 9. Display result
print("\n================================")
print("          OCR RESULT")
print("================================")

print(text)

print("--------------------------------")
print("Average Confidence:",
      round(average_confidence, 2), "%")

if average_confidence >= 80:
    print("Validation: PASSED")
else:
    print("Validation: FAILED")

print("================================")

# 10. Visual confirmation
cv2.imshow("Original Image", image)
cv2.imshow("Processed Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()