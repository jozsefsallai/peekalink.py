from __future__ import annotations

class ImageAsset:
  """Represents an image asset, such as the favicon or the OG image of the
  link.

  Attributes:
    - `url`     The URL address of the image asset.
    - `width`   The width of the image.
    - `height`  The height of the image."""
  def __init__(self, url: str, width: int, height: int):
    self.url = url
    self.width = width
    self.height = height

  @staticmethod
  def from_json(json: dict):
    """Factory method that turns a JSON dict into an `ImageAsset`."""
    return ImageAsset(
      url    = json['url'],
      width  = json['width'],
      height = json['height']
    )

  def to_json_dict(self) -> dict:
    """Returns a JSON-compliant dictionary containing the data of the current
    `ImageAsset` instance."""

    return {
      'url': self.url,
      'width': self.width,
      'height': self.height
    }
