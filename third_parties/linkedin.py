import os
from typing import Optional
import requests
from dotenv import load_dotenv
import json


def scrape_linkedin_profile(
    linkedin_profile_url: Optional[str] = None, mock: bool = False
):
    data = ""
    if mock:
        with open("third_parties/tom.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    elif linkedin_profile_url is not None:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
        data = response.json()
    else:
        data = json.dumps({"error": "Url not provided"})
        return data

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", " ", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
