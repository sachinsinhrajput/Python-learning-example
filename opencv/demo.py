import cv2

image = cv2.imread('/home/raoinfotech/vscode/python/opencv/city.jpg')
if image is None:
    print("Error: Image not found or failed to load.")
else:
    print("Image loaded successfully.")
    resize=cv2.resize(image, (500, 500))
    cv2.imshow('Resized Image', resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()