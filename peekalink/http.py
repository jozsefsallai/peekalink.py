from __future__ import annotations

import requests

from peekalink.client import Client

class HTTPService:
  def __init__(self, client: Client):
    self.__client = client

  def __build_url(self, url: str) -> str:
    return f'{self.__client.base_url}/{url}'

  def post(self, url: str, data, include_api_key = True):
    url = self.__build_url(url)
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }

    if include_api_key:
      headers['X-API-Key'] = self.__client.api_key

    return requests.post(url, headers=headers, json=data)
