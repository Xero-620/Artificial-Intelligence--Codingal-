import cv2
image = cv2.imread("alghozy-Zy2Df1hdguo-unsplash.jpg")
if image is None:
    print ("This is embarrasing, your image hasn't loaded through, check again!")
    exit()
cv2.namedWindow("Image Loaded", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Loaded", 800, 500)
cv2.imshow('Image Loaded', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image Dimensions: {image.shape}")
