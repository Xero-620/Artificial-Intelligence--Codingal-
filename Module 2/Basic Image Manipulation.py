import cv2
import numpy as np

def main():
    image_path = 'input.jpg'
    img = cv2.imread(image_path)
    
    if img is None:
        return

    height, width, channels = img.shape

    start_y, end_y = int(height * 0.25), int(height * 0.75)
    start_x, end_x = int(width * 0.25), int(width * 0.75)
    cropped_img = img[start_y:end_y, start_x:end_x]

    center = (width // 2, height // 2)
    angle = 45
    scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    bright_img = cv2.convertScaleAbs(img, alpha=1.0, beta=50)

    tx, ty = 70, 40
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_img = cv2.warpAffine(img, translation_matrix, (width, height))

    cv2.imwrite('manipulated_cropped.jpg', cropped_img)
    cv2.imwrite('manipulated_rotated.jpg', rotated_img)
    cv2.imwrite('manipulated_bright.jpg', bright_img)
    cv2.imwrite('manipulated_translated.jpg', translated_img)
    
    cv2.imshow('Original Image', img)
    cv2.imshow('Cropped Area', cropped_img)
    cv2.imshow('Rotated 45 Deg', rotated_img)
    cv2.imshow('Increased Brightness', bright_img)
    cv2.imshow('Shifted/Translated', translated_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
