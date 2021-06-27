# Peekalink Python API wrapper

An API wrapper/client library for the [Peekalink][peekalink-url] link previewing
service.

## Table of Contents

- [Getting Started](#getting-started)
- [API](#api)
  - [`peekalink.Client`](#peekalinkclient)
  - [`peekalink.LinkPreview`](#peekalinklinkpreview)
  - [`peekalink.ContentType`](#peekalinkcontenttype)
  - [`peekalink.ImageAsset`](#peekalinkimageasset)
  - [`peekalink.YouTubeDetails`](#peekalinkyoutubedetails)
  - [`peekalink.TwitterDetails`](#peekalinktwitterdetails)
  - [`peekalink.LinkError`](#peekalinklinkerror)
- [Contribution](#contribution)
- [License](#license)

## Getting Started

**Install the package:**

```
pip install peekalink
```

**Instantiate the client:**

```py
from peekalink import Client

peekalink = Client(api_key='your_api_key')
```

**Preview a link:**

```py
preview = peekalink.preview('https://www.youtube.com/watch?v=2oeWbRRiN2I')
print(preview.title)

if preview.is_youtube():
  youtube_details = preview.youtube()
  print(youtube_details.duration)
```

## API

### `peekalink.Client`

Represents a Peekalink API client instance.

#### Methods

- `__init__(api_key: str, base_url: str) -> Client`

Instantiates a new API client instance with the given `api_key` and `base_url`.
If the `base_url` is not provided, it will default to https://api.peekalink.io.
The `base_url` should NOT have a trailing slash.

- `set_base_url(base_url: str)`

Sets the client's base URL. It should NOT have a trailing slash.

- `set_api_key(api_key: str)`

Sets the client's API key.

- `preview(link: str) -> LinkPreview`

Returns preview information about a given link. If the response is non-200, it
will raise a `LinkError`.

- `is_available(link: str) -> bool`

Checks whether a given link is available.

### `peekalink.LinkPreview`

Represents details about a given link's preview.

#### Attributes

- `url: str`
- `domain: str`
- `last_updated: datetime`
- `next_update: datetime`
- `content_type: ContentType`
- `mime_type: str`
- `size: int | None`
- `redirected: bool`
- `redirection_url: str | None`
- `redirection_count: int | None`
- `redirection_trail: list[str] | None`
- `title: str | None`
- `description: str | None`
- `name: str`
- `trackers_detected: bool`
- `icon: ImageAsset | None`
- `image: ImageAsset | None`

#### Methods

- `@staticmethod from_json(json: dict)`

Factory method that turns a JSON dict into a `LinkPreview`.

- `is_youtube() -> bool`

Returns `True` if the details were included in the response and they contain
information about a YouTube video.

- `is_twitter() -> bool`

Returns `True` if the details were included in the response and they contain
information about a tweet.

- `youtube() -> YouTubeDetails | None`

Returns a `YouTubeDetails` object if the link contains details to a YouTube
video, otherwise `None`.

- `twitter() -> TwitterDetails | None`

Returns a `TwitterDetails` object if the link contains details to a tweet,
otherwise `None`.

- `to_json_dict() -> dict`

Returns a JSON-compliant dictionary containing the data of the current
`LinkPreview` instance.

### `peekalink.ContentType`

Enum-like class that represents the type of the content that's available on a
given link.

#### Members

- `ContentType.HTML`
- `ContentType.IMAGE`
- `ContentType.VIDEO`
- `ContentType.GIF`

### `peekalink.ImageAsset`

Represents an image asset, such as the favicon or the OG image of the link.

#### Attributes

- `url: str`
- `width: int`
- `height: int`

#### Methods

- `@staticmethod from_json(json: dict) -> ImageAsset`

Factory method that turns a JSON dict into an `ImageAsset`.

- `to_json_dict() -> dict`

Returns a JSON-compliant dictionary containing the data of the current
`ImageAsset` instance.

### `peekalink.YouTubeDetails`

Represents a set of details regarding the YouTube video a given link points to.

#### Attributes

- `video_id: str`
- `duration: float`
- `view_count: int`
- `like_count: int`
- `dislike_count: int`
- `comment_count: int`
- `published_at: datetime`

#### Methods

- `@staticmethods from_json(json: dict) -> YouTubeDetails`

Factory method that turns a JSON dict into a `YouTubeDetails`.

- `to_json_dict() -> dict`

Returns a JSON-compliant dictionary containing the data of the current
`YouTubeDetails` instance.

### `peekalink.TwitterDetails`

Represents a set of details regarding the tweet a given link points to.

#### Attributes

- `status_id: str`
- `retweet_count: int`
- `likes_count: int`
- `published_at: datetime`

#### Methods

- `@staticmethods from_json(json: dict) -> TwitterDetails`

Factory method that turns a JSON dict into a `TwitterDetails`.

- `to_json_dict() -> dict`

Returns a JSON-compliant dictionary containing the data of the current
`TwitterDetails` instance.

### peekalink.LinkError`

An exception that can be raised by the Link Preview service, to better identify
why it was not possible to retrieve the details of a link.

#### Attributes

- `code: int` - The HTTP status code. You can check against one of the built-in
error types that are included in the `LinkError` class.

#### Members

- `LinkError.LINK_MAX_REDIRECTS = 400`
- `LinkError.LINK_IS_PRIVATE = 403`
- `LinkError.LINK_DOES_NOT_EXIST = 404`
- `LinkError.LINK_TIMED_OUT = 408`
- `LinkError.LINK_EMPTY = 409`
- `LinkError.LINK_PREVIEW_ERROR = 409`
- `LinkError.LINK_UNREACHABLE = 409`
- `LinkError.LINK_CONTENT_TOO_LARGE = 413`

## Contribution

**1. Clone the repository**

```
git clone git@github.com:jozsefsallai/peekalink.py.git
cd peekalink.py
```

**2. Create a virtual env**

```
python -m venv .venv
source .venv/bin/activate
```

**3. Install the dependencies**

```
pip install -r requirements.txt
```

Once you make your changes, please make sure the unit tests are passing:

```
python -m unittest discover -s peekalink/tests -p 'test_*.py'
```

If you add a feature, make sure to also include an appropriate unit test.

## License

MIT.

[peekalink-url]: https://www.peekalink.io/
