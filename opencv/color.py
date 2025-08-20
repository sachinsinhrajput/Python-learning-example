import cv2

image = cv2.imread("/home/raoinfotech/vscode/python/opencv/logo.png")

if image is None:
    print("Image not found.")
else:
    # Add a border to the image
    image = cv2.copyMakeBorder(
        image, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=0
    )

    window_name = "Image with Border"
    print(window_name)

    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
