from dataclasses import dataclass

from PIL import Image, ImageDraw, ImageFont


@dataclass
class Font:
    font_filename: str
    size: int
    font_y: int


class Text:
    def __init__(self, font: Font):
        self.__font = font

    def draw(self, image: Image.Image, text: str):
        font_path = f"./fonts/{self.__font.font_filename}"
        draw = ImageDraw.Draw(image)
        text_font = ImageFont.truetype(font_path, self.__font.size)
        text_width = text_font.getsize(text)[0]
        while text_width >= image.width - 10*2:
            text_font = ImageFont.truetype(font_path, self.__font.size)
            text_width = text_font.getsize(text)[0]
            self.__font.size -= 1

        draw.text(
            ((image.width - text_width) / 2, self.__font.font_y), text, font=text_font,
        )
