# Peekalink Python API wrapper

**(this library is a work in progress)**

An API wrapper/client library for the [Peekalink][peekalink-url] link previewing
service.

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

## License

MIT.

[peekalink-url]: https://www.peekalink.io/
