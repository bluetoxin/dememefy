from typing import Tuple

from PIL import Image

from dememefy.text import Font, Text


class Demotivator:
    def __init__(self, image: Image.Image, text: str, x_start: int, y_start: int):
        self.__image = image
        self.__text = text
        self.__x_start = x_start
        self.__y_start = y_start

    def create(self):
        self.__image = self.__add_border(
            5, (0, 0, 0), self.__image)  # add black border
        self.__image = self.__add_border(
            2, (255, 255, 255), self.__image)  # add white border
        template = Image.new(mode="RGB", size=(
            self.__image.width+(self.__x_start*2), self.__image.height+(self.__y_start*2)+200))
        template.paste(self.__image, self.__get_coords(
            self.__image))  # paste image to template
        Text(Font(font_filename="Symbola.ttf", size=45, font_y=self.__image.height+self.__y_start+70)).draw(
            template, self.__text)  # paste text to template

        return template

    def __get_coords(self, image: Image.Image) -> Tuple[int, int, int, int]:
        return (self.__x_start, self.__y_start, image.width+self.__x_start, image.height+self.__y_start)

    def __add_border(self, size: int, color: Tuple[int, int, int], image: Image.Image) -> Image.Image:
        img_with_border = Image.new("RGB", (image.width+(size*2),
                                            image.height+(size*2)), color)  # type: ignore
        img_with_border.paste(
            image, (size, size, self.__image.width+size, image.height+size))
        return img_with_border
