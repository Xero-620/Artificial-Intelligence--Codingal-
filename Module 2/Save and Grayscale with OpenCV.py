import cv2
image = cv2.imread("alghozy-Zy2Df1hdguo-unsplash.jpg")
if image is None:
    print ("This is embarrasing, your image hasn't loaded through, check again!")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resize_image = cv2.resize(gray_image, (221, 221))
cv2.imshow("Proccessed Image", resize_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("resize_image.jpg", resize_image)
    print ("Image saved!")
else:
    print ("Image unable to save!")
cv2.destroyAllWindows()
print(f"Proccessed Image Dimensions: {resize_image.shape}")