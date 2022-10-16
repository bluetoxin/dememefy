import random
from typing import Tuple

import requests
import requests.auth
from PIL import Image

from dememefy.posts.posts import BasePosts


class RedditPosts(BasePosts):
    _AUTH = "https://www.reddit.com/api/v1/access_token"

    def __init__(self, username: str, password: str, token: str, client_id: str, thread: str = "memes"):
        if not all(isinstance(arg, str) for arg in [username, password, token, client_id, thread]):
            raise TypeError("All credentials must be str")
        self.__username = username
        self.__password = password
        self.__token = token
        self.__client_id = client_id

        self.__limit = 10
        self.__thread = f"https://oauth.reddit.com/r/{thread}/hot?limit={self.__limit}"
        self.__auth_headers = self.__auth()

    def get_post(self) -> Tuple[str, Image.Image]:
        posts = requests.get(self.__thread, headers=self.__auth_headers).json()[
            "data"]["children"][-self.__limit:]
        if posts[0]["data"]["title"] is posts[0]["data"]["url"] is None:
            raise ValueError("Can't parse title/url in post")
        random.shuffle(posts)
        return (posts[0]["data"]["title"], self._download_pic(posts[0]["data"]["url"]))  # noqa: E501

    def __auth(self) -> dict:
        auth = requests.auth.HTTPBasicAuth(self.__client_id, self.__token)
        user_agent = {"User-Agent": "Dememefy"}
        res = requests.post(self._AUTH,
                            auth=auth,
                            data={"grant_type": "password",
                                  "username": self.__username,
                                  "password": self.__password},
                            headers=user_agent)
        token = res.json()["access_token"]
        return {**user_agent, **{"Authorization": f"bearer {token}"}}
