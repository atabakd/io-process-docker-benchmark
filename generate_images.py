import cv2
import numpy as np
import os
import time

def main():
    output_path = '/data'  # This directory should be mapped from the host
    num_images = 1000
    image_size = (1024, 768, 3)  # HD RGB images

    start_time = time.time()
    
    # Generate and save images
    for i in range(num_images):
        img = np.random.randint(0, 256, image_size, dtype=np.uint8)
        cv2.imwrite(os.path.join(output_path, f'image_{i}.png'), img)
    
    generation_time = time.time() - start_time
    print(f"Time to generate and save images: {generation_time:.2f} seconds")
    
    start_time = time.time()
    
    # Load images and convert to grayscale
    for i in range(num_images):
        img = cv2.imread(os.path.join(output_path, f'image_{i}.png'))
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    processing_time = time.time() - start_time
    print(f"Time to load and convert images: {processing_time:.2f} seconds")

if __name__ == "__main__":
    main()

