import cv2
original_image = cv2.imread("alghozy-Zy2Df1hdguo-unsplash.jpg")
if original_image is None:
    print(f"Error: Could not open or find the image at {image_path}")
else:
    predefined_sizes = [
        ("small", (300, 200)),
        ("medium", (600, 400)),
        ("large", (1200, 800))
    ]
    for label, dimensions in predefined_sizes:
        resized_image = cv2.resize(original_image, dimensions, interpolation=cv2.INTER_LINEAR)
        output_filename = f"resized_{label}.jpg"
        cv2.imwrite(output_filename, resized_image)
        print(f"Saved: {output_filename} with dimensions {dimensions}")
        cv2.imshow(f"Resized Image - {label.capitalize()}", resized_image)    
    print("Press any key on an image window to close and exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()