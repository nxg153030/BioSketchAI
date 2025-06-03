import numpy as np
from PIL import Image

def draw_circle(img, center, radius, color, filled=True, thickness=2):
    h, w, _ = img.shape
    for y in range(h):
        for x in range(w):
            dist = ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5
            if filled:
                if dist <= radius:
                    img[y, x] = color
            else:
                if radius - thickness/2 <= dist <= radius + thickness/2:
                    img[y, x] = color


if __name__ == "__main__":
    # Example usage
    color = (0, 0, 0)  # Black color
    size = 100
    img = np.ones((size, size, 3), dtype=np.uint8) * 255 # White background

    # Draw a filled circle in the center of the image
    draw_circle(img, (size // 2, size // 2), 40, color, filled=True)
    Image.fromarray(img).save("circle_manual_filled.png")

    # Draw unfilled circle
    img2 = np.ones((size, size, 3), dtype=np.uint8) * 255 # White background
    draw_circle(img2, (size // 2, size // 2), 40, color, filled=False, thickness=3)
    Image.fromarray(img2).save("circle_manual_unfilled.png")