import unittest

from datetime import datetime
from dateutil.tz import tzutc

from peekalink.models.helpers.link_details import LinkDetailType, YouTubeDetails, TwitterDetails, LinkDetails
from peekalink.tests.support.fixtures import YOUTUBE_PREVIEW, TWITTER_PREVIEW

class TestLinkDetailType(unittest.TestCase):
  def test_eq_operator(self):
    link_detail_type = LinkDetailType('youtube')
    self.assertTrue(link_detail_type == LinkDetailType.YOUTUBE)

  def test_ne_operator(self):
    link_detail_type = LinkDetailType('youtube')
    self.assertTrue(link_detail_type != LinkDetailType.TWITTER)

  def test_get_name(self):
    link_detail_type = LinkDetailType('geocities')
    self.assertEqual(link_detail_type.get_name(), 'geocities')

class TestYouTubeDetails(unittest.TestCase):
  youtube_details = YOUTUBE_PREVIEW['details']

  def test_from_json(self):
    details = YouTubeDetails.from_json(self.youtube_details)
    self.assertEqual(details.video_id, 'dQw4w9WgXcQ')
    self.assertEqual(details.duration, 213.0)
    self.assertEqual(details.view_count, 915578000)
    self.assertEqual(details.like_count, 9182302)
    self.assertEqual(details.dislike_count, 272157)
    self.assertEqual(details.comment_count, 1519506)

    expected_published_at = datetime(2009, 10, 25, 6, 57, 33, tzinfo=tzutc())
    self.assertEqual(details.published_at, expected_published_at)

  def test_to_json(self):
    details = YouTubeDetails.from_json(self.youtube_details)
    self.assertDictEqual({**self.youtube_details, **details.to_json_dict()}, self.youtube_details)

class TestTwitterDetails(unittest.TestCase):
  twitter_details = TWITTER_PREVIEW['details']

  def test_from_json(self):
    details = TwitterDetails.from_json(self.twitter_details)
    self.assertEqual(details.status_id, '1278897629221588992')
    self.assertEqual(details.retweet_count, 285)
    self.assertEqual(details.likes_count, 2172)

    expected_published_at = datetime(2020, 7, 3, 3, 45, 30, tzinfo=tzutc())
    self.assertEqual(details.published_at, expected_published_at)

  def test_to_json(self):
    details = TwitterDetails.from_json(self.twitter_details)
    self.assertDictEqual({**self.twitter_details, **details.to_json_dict()}, self.twitter_details)

class TestLinkDetails(unittest.TestCase):
  youtube_details = YOUTUBE_PREVIEW['details']
  twitter_details = TWITTER_PREVIEW['details']

  def test_constructor(self):
    details = LinkDetails('youtube')
    self.assertEqual(details.detail_type, LinkDetailType.YOUTUBE)

  def test_add_youtube_details(self):
    details = LinkDetails('youtube')

    self.assertFalse(details.is_youtube())
    self.assertIsNone(details.youtube())

    details.add_youtube_details(self.youtube_details)

    self.assertTrue(details.is_youtube())
    self.assertIsNotNone(details.youtube())

  def test_add_twitter_details(self):
    details = LinkDetails('twitter')

    self.assertFalse(details.is_twitter())
    self.assertIsNone(details.twitter())

    details.add_twitter_details(self.twitter_details)

    self.assertTrue(details.is_twitter())
    self.assertIsNotNone(details.twitter())

  def test_youtube(self):
    details = LinkDetails('twitter')
    self.assertIsNone(details.youtube())

    details = LinkDetails('youtube')
    self.assertIsNone(details.youtube())

    details.add_youtube_details(self.youtube_details)
    self.assertIsNotNone(details.youtube())

    youtube = YouTubeDetails.from_json(self.youtube_details)
    self.assertDictEqual(youtube.to_json_dict(), details.youtube().to_json_dict())

  def test_twitter(self):
    details = LinkDetails('youtube')
    self.assertIsNone(details.twitter())

    details = LinkDetails('twitter')
    self.assertIsNone(details.twitter())

    details.add_twitter_details(self.twitter_details)
    self.assertIsNotNone(details.twitter())

    twitter = TwitterDetails.from_json(self.twitter_details)
    self.assertDictEqual(twitter.to_json_dict(), details.twitter().to_json_dict())

  def test_is_youtube(self):
    details = LinkDetails('twitter')
    self.assertFalse(details.is_youtube())

    details = LinkDetails('youtube')
    self.assertFalse(details.is_youtube())

    details.add_youtube_details(self.youtube_details)
    self.assertTrue(details.is_youtube())

  def test_is_twitter(self):
    details = LinkDetails('youtube')
    self.assertFalse(details.is_twitter())

    details = LinkDetails('twitter')
    self.assertFalse(details.is_twitter())

    details.add_twitter_details(self.twitter_details)
    self.assertTrue(details.is_twitter())

  def test_to_json_dict(self):
    details = LinkDetails('youtube')
    self.assertDictEqual(details.to_json_dict(), { 'type': 'youtube' })

    details.add_youtube_details(self.youtube_details)
    self.assertDictEqual(details.to_json_dict(), self.youtube_details)
