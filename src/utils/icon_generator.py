from PIL import Image, ImageDraw


def generate_icon(color, size, filled=False, outline_width=3, upscale_factor=4):
    # Draw at higher resolution for anti-aliasing
    upscale_size = size * upscale_factor
    # Create a new image with white background
    img = Image.new("RGB", (upscale_size, upscale_size), "white")
    draw = ImageDraw.Draw(img)

    margin = 10 * upscale_factor
    shape = [(margin, margin), (upscale_size - margin, upscale_size - margin)]
    if filled:
        draw.ellipse(shape, fill=color)
    else:
        draw.ellipse(
            shape, 
            outline=color, 
            width=outline_width * upscale_factor,
            fill=None)

    # Downsample to target size with anti-aliasing
    img = img.resize((size, size), Image.LANCZOS)
    return img


if __name__ == "__main__":
    _filled = False
    icon = generate_icon("blue", 100, _filled)
    icon.save("circle_icon_outline_refined.png")
    print("Icon generated and saved as icon.png")