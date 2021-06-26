from __future__ import annotations

class LinkError(Exception):
  """An exception that can be raised by the Link Preview service, to better
  identify why it was not possible to retrieve the details of a link.

  Attributes:
    - `code`  The HTTP status code. You can check against one of the built-in\
              error types that are included in the `LinkError` class."""

  LINK_MAX_REDIRECTS = 400
  LINK_IS_PRIVATE = 403
  LINK_DOES_NOT_EXIST = 404
  LINK_TIMED_OUT = 408
  LINK_EMPTY = 409
  LINK_PREVIEW_ERROR = 409
  LINK_UNREACHABLE = 409
  LINK_CONTENT_TOO_LARGE = 413

  def __init__(self, code: int):
    super(LinkError, self).__init__(f'Request failed with code {code}')
    self.code = code
