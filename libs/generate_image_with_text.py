"""
    Script that generates image in binary format
    containing the word passed into it.

"""

import io

from PIL import Image, ImageDraw, ImageFont

def generate_image_with_text(text_string: str, height=100, width=300, mode="RGB", background="white", text_color="black", format="JPEG"):
    """
        Create an image with the specified text and return it as a binary string.
    """

    image_size = (width, height)

    image = Image.new(mode, image_size, color=background)
    drawing_context = ImageDraw.Draw(image)
    text_font = ImageFont.load_default()

    """
        Get the size of the text
        and subtract each from the size of the image
        resulting in leftover space.
        Divide the space in two, to get the starting coordinate for text
        so that the text is centered.

        // is for integer division
    
    """
    left, top, right, bottom = drawing_context.textbbox((0,0), text_string, font=text_font)

    text_width = right - left
    text_height = bottom - top

    text_x = (image_size[0] - text_width) // 2
    text_y = (image_size[1] - text_height) // 2

    text_coords = (text_x, text_y)

    drawing_context.text(text_coords, text_string, fill=text_color, font=text_font)

    buffer = io.BytesIO()
    image.save(buffer, format)

    return buffer.getvalue()
