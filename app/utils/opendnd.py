import os
import random
from urllib.parse import urlencode

import requests

from .openapi import OpenAI

NUM_IMAGES = 3


class OpenDnD:
    """
    _summary_

    Returns:
        _type_: _description_
    """

    API_URL = "https://api.open5e.com/"

    @classmethod
    def _request(cls, url):
        """
        request from each object API resource

        Returns:
            _type_: _description_
        """
        response = requests.get(url)
        return response.json()

    @classmethod
    def get_monsters(cls, number):
        results = []
        for _ in range(number):
            res = cls._request(
                f"https://api.open5e.com/monsters/?limit=1&page={random.randint(1, 1469)}"
            )["results"][0]
            if not cls.has_image(res["name"]):
                cls.get_image(res["name"])
            res[
                "image"
            ] = f"/static/images/mobs/{res['name'].replace(' ', '')}-{random.randint(1,NUM_IMAGES)}.png"
            results.append(res)
        return results

    @classmethod
    def has_image(cls, name):
        return os.path.isfile(f"static/images/mobs/{name}-1.jpg")

    @classmethod
    def get_image(cls, name, description="preparing for battle"):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        prompt = f"A Photorealistic image of a {name} from Dungeons and Dragons 5E in an arena setting {description}"
        OpenAI().generate_image(
            prompt, path=f"static/images/mobs/{name.replace(' ', '')}", n=NUM_IMAGES
        )
