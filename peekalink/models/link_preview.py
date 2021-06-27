from __future__ import annotations

from datetime import datetime
import dateutil.parser as date_parser

from .helpers.content_type import ContentType
from .helpers.image_asset import ImageAsset
from .helpers.link_details import LinkDetailType, LinkDetails

class LinkPreview:
  """Represents details about a given link's preview."""

  url: str
  domain: str
  last_updated: datetime
  next_update: datetime
  content_type: ContentType
  mime_type: str
  size: int
  redirected: bool
  redirection_url: str
  redirection_count: int
  redirection_trail: list[str]
  title: str
  description: str
  name: str
  trackers_detected: bool
  icon: ImageAsset
  image: ImageAsset
  __details: LinkDetails

  @staticmethod
  def from_json(json: dict):
    """Factory method that turns a JSON dict into a `LinkPreview`."""

    link_preview = LinkPreview()

    link_preview.url = json['url']
    link_preview.domain = json['domain']
    link_preview.last_updated = date_parser.parse(json['lastUpdated'])
    link_preview.next_update = date_parser.parse(json['nextUpdate'])
    link_preview.content_type = ContentType(json['contentType'])
    link_preview.mime_type = json['mimeType']
    link_preview.size = json['size'] if 'size' in json else None
    link_preview.redirected = json['redirected']
    link_preview.redirection_url = json['redirectionUrl'] if 'redirectionUrl' in json else None
    link_preview.redirection_count = json['redirectionCount'] if 'redirectionCount' in json else None
    link_preview.redirection_trail = json['redirectionTrail'] if 'redirectionTrail' in json else None
    link_preview.title = json['title'] if 'title' in json else None
    link_preview.description = json['description'] if 'description' in json else None
    link_preview.name = json['name']
    link_preview.trackers_detected = json['trackersDetected']
    link_preview.icon = ImageAsset.from_json(json['icon']) if 'icon' in json else None
    link_preview.image = ImageAsset.from_json(json['image']) if 'image' in json else None

    if 'details' in json and 'type' in json['details']:
      details = LinkDetails(type = json['details']['type'])

      if details.detail_type == LinkDetailType.YOUTUBE:
        details.add_youtube_details(json['details'])

      if details.detail_type == LinkDetailType.TWITTER:
        details.add_twitter_details(json['details'])

      link_preview.__details = details
    else:
      link_preview.__details = None

    return link_preview

  def is_youtube(self) -> bool:
    """Returns `True` if the details were included in the response and they
    contain information about a YouTube video."""
    return self.__details is not None and self.__details.is_youtube()

  def is_twitter(self) -> bool:
    """Returns `True` if the details were included in the response and they
    contain information about a tweet."""
    return self.__details is not None and self.__details.is_twitter()

  def youtube(self):
    """Returns a `YouTubeDetails` object if the link contains details to a
    YouTube video, otherwise `None`."""
    if not self.is_youtube():
      return None

    return self.__details.youtube()

  def twitter(self):
    """Returns a `TwitterDetails` object if the link contains details to a
    tweet, otherwise `None`."""
    if not self.is_twitter():
      return None

    return self.__details.twitter()

  def to_json_dict(self) -> dict:
    """Returns a JSON-compliant dictionary containing the data of the current
    `LinkPreview` instance."""

    result = {}

    result['url'] = self.url
    result['domain'] = self.domain
    result['lastUpdated'] = self.last_updated.isoformat().replace('+00:00', 'Z')
    result['nextUpdate'] = self.next_update.isoformat().replace('+00:00', 'Z')
    result['contentType'] = self.content_type.get_name()
    result['mimeType'] = self.mime_type
    result['size'] = self.size
    result['redirected'] = self.redirected

    if self.redirection_url is not None:
      result['redirectionUrl'] = self.redirection_url

    if self.redirection_count is not None:
      result['redirectionCount'] = self.redirection_count

    if self.redirection_trail is not None:
      result['redirectionTrail'] = self.redirection_trail

    if self.title is not None:
      result['title'] = self.title

    if self.description is not None:
      result['description'] = self.description

    result['name'] = self.name
    result['trackersDetected'] = self.trackers_detected

    if self.icon is not None:
      result['icon'] = self.icon.to_json_dict()

    if self.image is not None:
      result['image'] = self.image.to_json_dict()

    if self.__details is not None:
      result['details'] = self.__details.to_json_dict()

    return result
