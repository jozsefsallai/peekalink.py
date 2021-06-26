from __future__ import annotations

from peekalink.client import Client
from peekalink.http import HTTPService

class IsAvailableAPIService(HTTPService):
  IS_AVAILABLE_API_URL = '/is-available/'

  def __init__(self, client: Client):
    super(IsAvailableAPIService, self).__init__(client)

  def is_available(self, link: str) -> bool:
    data = {'link': link}
    response = self.post(
      url = IsAvailableAPIService.IS_AVAILABLE_API_URL,
      data = data
    )

    json = response.json()
    return json['isAvailable']
