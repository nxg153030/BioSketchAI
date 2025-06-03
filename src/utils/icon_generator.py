from PIL import Image, ImageDraw


def generate_icon(color, size, filled=False, outline_width=3, upscale_factor=4, shape_type="circle"):
    # Draw at higher resolution for anti-aliasing
    upscale_size = size * upscale_factor
    # Create a new image with white background
    img = Image.new("RGB", (upscale_size, upscale_size), "white")
    draw = ImageDraw.Draw(img)

    margin = 10 * upscale_factor
    shape = [(margin, margin), (upscale_size - margin, upscale_size - margin)]

    if shape_type == "circle":
        if filled:
            draw.ellipse(shape, fill=color)
        else:
            draw.ellipse(
                shape, 
                outline=color, 
                width=outline_width * upscale_factor,
                fill=None)
    elif shape_type == "square":
        if filled:
            draw.rectangle(shape, fill=color)
        else:
            draw.rectangle(
                shape,
                outline=color,
                width=outline_width * upscale_factor,
                fill=None
            )
    elif shape_type == "rectangle":
        rect_shape = [
            (margin, upscale_size // 4),
            (upscale_size - margin, upscale_size - upscale_size // 4),
        ]
        if filled:
            draw.rectangle(rect_shape, fill=color)
        else:
            draw.rectangle(
                rect_shape,
                outline=color,
                width=outline_width * upscale_factor,
                fill=None
            )
    elif shape_type == "triangle":
        top = (upscale_size // 2, margin)
        left = (margin, upscale_size - margin)
        right = (upscale_size - margin, upscale_size - margin)
        points = [top, left, right]
        if filled:
            draw.polygon(points, fill=color)
        else:
            draw.polygon(
                points,
                outline=color,
                width=outline_width * upscale_factor,
                fill=None,
            )
    else:
        raise ValueError("Unsupported shape type. Use 'circle', 'square', 'rectangle', or 'triangle'.")

    # Downsample to target size with anti-aliasing
    img = img.resize((size, size), Image.LANCZOS)
    return img


if __name__ == "__main__":
    color = "black"
    size = 100
    filled = False  # Change to True for filled circle
    outline_width = 3  # Width of the outline in pixels
    upscale_factor = 4  # Factor to upscale for better quality
    shape_type = "square"  # Change to "square", "rectangle", or "triangle" as needed
    icon = generate_icon(color, size, filled, outline_width, upscale_factor, shape_type)
    icon.save(f"{color}_{shape_type}.png")
    print(f"Icon generated and saved as {shape_type}.png")