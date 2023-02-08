import os
import random
from urllib.parse import urlencode

import requests

from .logger import log
from .openapi import OpenAI

NUM_IMAGES = 3


class OpenDnD:
    """
    _summary_

    Returns:
        _type_: _description_
    """

    API_URL = "https://www.dnd5eapi.co/api"

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
    def get_count(cls, resource):
        """
        _summary_

        Returns:
            _type_: _description_
        """

    @classmethod
    def get_monsters(cls, number=1, **kwargs):
        results = []
        url = f"{cls.API_URL}/monsters"
        cr_range = range(int(kwargs.get("crmin", 0)), int(kwargs.get("crmax", 20)) + 1)
        crs = ",".join([str(i) for i in cr_range])
        mob_list = cls._request(url + f"?challenge_rating={crs}")["results"]
        for _ in range(int(number)):
            mob = random.choice(mob_list)["index"]
            res = cls._request(f"{url}/{mob}")
            res["image"] = cls.get_image(res["name"])
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
        if not cls.has_image(name):
            prompt = f"A Photorealistic image of a {name} from Dungeons and Dragons 5E in an arena setting {description}"
            OpenAI().generate_image(
                prompt, path=f"static/images/mobs/{name.replace(' ', '')}", n=NUM_IMAGES
            )
        return f"/static/images/mobs/{name.replace(' ', '')}-{random.randint(1,NUM_IMAGES)}.png"
