import unittest

from datetime import datetime
from dateutil.tz import tzutc

from peekalink.models.link_preview import LinkPreview
from peekalink.models.helpers.image_asset import ImageAsset
from peekalink.models.helpers.link_details import TwitterDetails, YouTubeDetails
from peekalink.models.helpers.content_type import ContentType
from peekalink.tests.support.fixtures import *

class TestLinkPreview(unittest.TestCase):
  def test_from_json(self):
    preview = LinkPreview.from_json(YOUTUBE_PREVIEW)

    self.assertEqual(preview.url, YOUTUBE_PREVIEW['url'])
    self.assertEqual(preview.domain, YOUTUBE_PREVIEW['domain'])
    self.assertEqual(preview.last_updated, datetime(2021, 4, 9, 23, 28, 10, 364301, tzinfo=tzutc()))
    self.assertEqual(preview.next_update, datetime(2021, 4, 10, 23, 28, 9, 16859, tzinfo=tzutc()))
    self.assertEqual(preview.content_type, ContentType.HTML)
    self.assertEqual(preview.mime_type, YOUTUBE_PREVIEW['mimeType'])
    self.assertEqual(preview.size, YOUTUBE_PREVIEW['size'])
    self.assertTrue(preview.redirected)
    self.assertIsNotNone(preview.redirection_url)
    self.assertEqual(preview.redirection_url, YOUTUBE_PREVIEW['redirectionUrl'])
    self.assertIsNotNone(preview.redirection_count)
    self.assertEqual(preview.redirection_count, YOUTUBE_PREVIEW['redirectionCount'])
    self.assertIsNotNone(preview.redirection_trail)
    self.assertListEqual(preview.redirection_trail, YOUTUBE_PREVIEW['redirectionTrail'])
    self.assertIsNotNone(preview.title)
    self.assertEqual(preview.title, YOUTUBE_PREVIEW['title'])
    self.assertIsNotNone(preview.description)
    self.assertEqual(preview.description, YOUTUBE_PREVIEW['description'])
    self.assertEqual(preview.name, YOUTUBE_PREVIEW['name'])
    self.assertTrue(preview.trackers_detected)
    self.assertIsNotNone(preview.icon)
    self.assertIsInstance(preview.icon, ImageAsset)
    self.assertIsNotNone(preview.image)
    self.assertIsInstance(preview.image, ImageAsset)

  def test_is_youtube(self):
    preview = LinkPreview.from_json(GENERIC_PREVIEW)
    self.assertFalse(preview.is_youtube())

    preview = LinkPreview.from_json(YOUTUBE_PREVIEW)
    self.assertTrue(preview.is_youtube())

  def test_is_twitter(self):
    preview = LinkPreview.from_json(GENERIC_PREVIEW)
    self.assertFalse(preview.is_twitter())

    preview = LinkPreview.from_json(TWITTER_PREVIEW)
    self.assertTrue(preview.is_twitter())

  def test_youtube(self):
    preview = LinkPreview.from_json(GENERIC_PREVIEW)
    self.assertIsNone(preview.youtube())

    preview = LinkPreview.from_json(YOUTUBE_PREVIEW)
    self.assertIsNotNone(preview.youtube())
    self.assertIsInstance(preview.youtube(), YouTubeDetails)

  def test_twitter(self):
    preview = LinkPreview.from_json(GENERIC_PREVIEW)
    self.assertIsNone(preview.twitter())

    preview = LinkPreview.from_json(TWITTER_PREVIEW)
    self.assertIsNotNone(preview.twitter())
    self.assertIsInstance(preview.twitter(), TwitterDetails)

  def test_to_json_dict(self):
    preview = LinkPreview.from_json(YOUTUBE_PREVIEW)
    self.assertDictEqual(preview.to_json_dict(), YOUTUBE_PREVIEW)
