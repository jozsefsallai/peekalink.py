from __future__ import annotations

class ContentType:
  """Enum-like class that represents the type of the content that's available on
  a given link."""

  def __init__(self, name: str):
    self.__name = name

  def __eq__(self, other) -> bool:
    return isinstance(other, ContentType) and self.__name == other.__name

  def __ne__(self, other) -> bool:
    return not self.__eq__(other)

  def get_name(self) -> str:
    """Returns the name of the `ContentType`."""
    return self.__name

ContentType.HTML = ContentType('html')
ContentType.IMAGE = ContentType('image')
ContentType.VIDEO = ContentType('video')
ContentType.GIF = ContentType('gif')
