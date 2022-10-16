import io
import re

import requests
from PIL import Image


class BasePosts:
    _AUTH = NotImplemented

    def _download_pic(self, url: str) -> Image.Image:
        if re.search(r"\.(jpeg|jpg|png)", url) is None:
            raise ValueError(
                f"Can't download pic, file has invalid extension. Url: {url}")

        image_bytes = b''
        response = requests.get(url, stream=True)
        for chunk in response:
            image_bytes += chunk

        return Image.open(io.BytesIO(image_bytes))
