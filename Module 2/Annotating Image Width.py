import cv2
import numpy as np

image = np.ones((400, 600, 3), dtype=np.uint8) * 255

height, width, channels = image.shape

start_x = 50
end_x = width - 50
y_position = 200

cv2.line(image, (start_x, y_position), (end_x, y_position), (0, 0, 255), 2)
cv2.arrowedLine(image, (start_x + 20, y_position), (start_x, y_position), (0, 0, 255), 2, tipLength=0.3)
cv2.arrowedLine(image, (end_x - 20, y_position), (end_x, y_position), (0, 0, 255), 2, tipLength=0.3)

cv2.line(image, (start_x, y_position - 10), (start_x, y_position + 10), (0, 0, 255), 2)
cv2.line(image, (end_x, y_position - 10), (end_x, y_position + 10), (0, 0, 255), 2)

text = f"Width: {width}px"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
thickness = 2
color = (0, 0, 0)

text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
text_width, text_height = text_size
text_x = (width - text_width) // 2
text_y = y_position - 15

cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)

cv2.imshow("Image Dimension Annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()