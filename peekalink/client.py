from __future__ import annotations

from peekalink.models import LinkPreview

class Client:
  """Represents a Peekalink API client instance."""

  def __init__(self, api_key: str, base_url: str = 'https://api.peekalink.io'):
    self.api_key = api_key
    self.base_url = base_url

    from peekalink.apis import LinkPreviewAPIService, IsAvailableAPIService

    self.__preview_api = LinkPreviewAPIService(client=self)
    self.__availability_api = IsAvailableAPIService(client=self)

  def set_base_url(self, base_url: str):
    """Setter for the client's base URL."""

    if base_url.endswith('/'):
      base_url = base_url[:-1]

    self.base_url = base_url

  def set_api_key(self, api_key: str):
    """Setter for the client's API key."""
    self.api_key = api_key

  def preview(self, link: str) -> LinkPreview:
    """Returns preview information about a given link."""
    return self.__preview_api.preview(link)

  def is_available(self, link: str) -> bool:
    """Checks whether a given link is available."""
    return self.__availability_api.is_available(link)
