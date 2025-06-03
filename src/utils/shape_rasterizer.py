import numpy as np
from PIL import Image

def draw_filled_circle(img, center, radius, color):
    h, w, _ = img.shape
    for y in range(h):
        for x in range(w):
            if (x - center[0]) ** 2 + (y - center[1]) ** 2 <= radius ** 2:
                img[y, x] = color


if __name__ == "__main__":
    # Example usage
    # Create a white image and draw a filled black circle in the center
    size = 100
    img = np.ones((size, size, 3), dtype=np.uint8) * 255 # White background
    draw_filled_circle(img, (size // 2, size // 2), 40, (0, 0, 0)) # Black circle
    Image.fromarray(img).save("circle_manual.png")