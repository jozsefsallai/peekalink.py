from __future__ import annotations

from peekalink.models.link_preview import LinkPreview
from peekalink.client import Client
from peekalink.http import HTTPService
from peekalink.errors import LinkError

class LinkPreviewAPIService(HTTPService):
  LINK_PREVIEW_API_URL = ''

  def __init__(self, client: Client):
    super(LinkPreviewAPIService, self).__init__(client)

  def preview(self, link: str) -> LinkPreview:
    data = {'link': link}
    response = self.post(
      url = LinkPreviewAPIService.LINK_PREVIEW_API_URL,
      data = data
    )

    if response.status_code != 200:
      raise LinkError(response.status_code)

    json = response.json()
    return LinkPreview.from_json(json)
