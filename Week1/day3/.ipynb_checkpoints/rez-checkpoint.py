import cv2
from matplotlib import pyplot as plt

def display_image(image_path, scale_percent):
    # Read the original image
    img = cv2.imread(image_path)

    # Get the original dimensions
    original_dimensions = img.shape[:2]  # height, width
    print(f"Original Dimensions: {original_dimensions}")

    # Calculate the new dimensions
    new_width = scale_percent 
    new_height = scale_percent
    new_dimensions = (new_width, new_height)
    print(f"New Dimensions: {new_dimensions}")

    # Resize the image
    resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_AREA)

    # Convert BGR to RGB
    resized_img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

    display_images([resized_img_rgb,],  [f'Resized Image ({new_width}x{new_height})',])
    

def display_images(images, titles):
    num_images = len(images)
    rows = (num_images + 1) // 2  # Calculate the number of rows needed
    plt.figure(figsize=(15, 5 * rows))
    
    for i in range(num_images):
        plt.subplot(rows, 2, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def change_image_color(image_path):
    # Read the original image
    img = cv2.imread(image_path)

    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to Grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a color map
    img_colormap = cv2.applyColorMap(img, cv2.COLORMAP_JET)

    # Split the channels and merge them in different orders
    b, g, r = cv2.split(img)
    img_bgr = cv2.merge([b, g, r])
    img_gbr = cv2.merge([g, b, r])
    img_rbg = cv2.merge([r, b, g])

    # Prepare images and titles for display
    images = [img_rgb, img_gray, img_colormap, img_bgr, img_gbr, img_rbg]
    titles = ['Original (RGB)', 'Grayscale', 'Color Map (JET)', 'BGR', 'GBR', 'RBG']

    # Convert grayscale to RGB for consistent display with matplotlib
    images[1] = cv2.cvtColor(images[1], cv2.COLOR_GRAY2RGB)

    # Display the images
    display_images(images, titles)