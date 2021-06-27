from __future__ import annotations

from datetime import datetime
import dateutil.parser as date_parser

class LinkDetailType:
  """Enum-like class that specifies the type of the details associated to a
  given link preview."""
  def __init__(self, name: str):
    self.__name = name

  def __eq__(self, other):
    return isinstance(other, LinkDetailType) and self.__name == other.__name

  def __ne__(self, other):
    return not self.__eq__(other)

  def get_name(self) -> str:
    """Returns the name of the `LinkDetailType`."""
    return self.__name

LinkDetailType.YOUTUBE = LinkDetailType('youtube')
LinkDetailType.TWITTER = LinkDetailType('twitter')

class YouTubeDetails:
  """Represents a set of details regarding the YouTube video a given link points
  to."""
  video_id: str
  duration: float
  view_count: int
  like_count: int
  dislike_count: int
  comment_count: int
  published_at: datetime

  @staticmethod
  def from_json(json: dict):
    """Factory method that turns a JSON dict into a `YouTubeDetails`."""

    details = YouTubeDetails()

    details.video_id = json['videoId'] if 'videoId' in json else None
    details.duration = float(json['duration']) if 'duration' in json else None
    details.view_count = json['viewCount'] if 'viewCount' in json else None
    details.like_count = json['likeCount'] if 'likeCount' in json else None
    details.dislike_count = json['dislikeCount'] if 'dislikeCount' in json else None
    details.comment_count = json['commentCount'] if 'commentCount' in json else None
    details.published_at = date_parser.parse(json['publishedAt']) if 'publishedAt' in json else None

    return details

  def to_json_dict(self) -> dict:
    """Returns a JSON-compliant dictionary containing the data of the current
    `YouTubeDetails` instance."""

    result = {}

    if self.video_id is not None:
      result['videoId'] = self.video_id

    if self.duration is not None:
      result['duration'] = str(self.duration)

    if self.view_count is not None:
      result['viewCount'] = self.view_count

    if self.like_count is not None:
      result['likeCount'] = self.like_count

    if self.dislike_count is not None:
      result['dislikeCount'] = self.dislike_count

    if self.comment_count is not None:
      result['commentCount'] = self.comment_count

    if self.published_at is not None:
      result['publishedAt'] = self.published_at.isoformat().replace('+00:00', 'Z') # dirty hack but required for accuracy

    return result

class TwitterDetails:
  """Represents a set of details regarding the tweet a given link points to."""
  status_id: str
  retweet_count: int
  likes_count: int
  published_at: datetime

  @staticmethod
  def from_json(json: dict):
    """Factory method that turns a JSON dict into a `TwitterDetails`."""

    details = TwitterDetails()

    details.status_id = json['statusId'] if 'statusId' in json else None
    details.retweet_count = int(json['retweetCount']) if 'retweetCount' in json else None
    details.likes_count = int(json['likesCount']) if 'likesCount' in json else None
    details.published_at = date_parser.parse(json['publishedAt']) if 'publishedAt' in json else None

    return details

  def to_json_dict(self) -> dict:
    """Returns a JSON-compliant dictionary containing the data of the current
    `TwitterDetails` instance."""

    result = {}

    if self.status_id is not None:
      result['statusId'] = self.status_id

    if self.retweet_count is not None:
      result['retweetCount'] = self.retweet_count

    if self.likes_count is not None:
      result['likesCount'] = self.likes_count

    if self.published_at is not None:
      result['publishedAt'] = self.published_at.isoformat().replace('+00:00', 'Z') # dirty hack but required for accuracy

    return result

class LinkDetails:
  """General class that encapsulates the additional details associated to a link
  preview.

  Base attributes:
    - `detail_type`  The type of the link details."""
  detail_type: LinkDetailType

  def __init__(self, type: str):
    self.detail_type = LinkDetailType(type)

    self.__youtube = None
    self.__twitter = None

  def add_youtube_details(self, json: dict):
    """Adds the details of the YouTube video to the current `LinkDetails`
    instance from a given JSON object."""
    self.__youtube = YouTubeDetails.from_json(json)

  def add_twitter_details(self, json: dict):
    """Adds the details of the tweet to the current `LinkDetails` instance from
    a given JSON object."""
    self.__twitter = TwitterDetails.from_json(json)

  def youtube(self) -> YouTubeDetails:
    """Returns the YouTube video details associated to the link or `None` if the
    link does not point to a YouTube video."""
    return self.__youtube

  def twitter(self) -> TwitterDetails:
    """Returns the details of the tweet associated to the link or `None` if the
    link does not point to a tweet."""
    return self.__twitter

  def is_youtube(self) -> bool:
    """Returns `True` if the detail type of the link is `youtube` and the
    YouTube video details were assigned successfully."""
    return self.detail_type == LinkDetailType.YOUTUBE and self.__youtube is not None

  def is_twitter(self) -> bool:
    """Returns `True` if the detail type of the link is `tweet` and the tweet
    details were assigned successfully."""
    return self.detail_type == LinkDetailType.TWITTER and self.__twitter is not None

  def to_json_dict(self) -> dict:
    """Returns a JSON-compliant dictionary containing the data of the current
    `LinkDetails` instance."""

    result = {
      'type': self.detail_type.get_name()
    }

    if self.is_youtube():
      result.update(self.__youtube.to_json_dict())

    if self.is_twitter():
      result.update(self.__twitter.to_json_dict())

    return result
