import unittest

from peekalink.models.helpers.image_asset import ImageAsset
from peekalink.tests.support.fixtures import GENERIC_PREVIEW

class TestImageAsset(unittest.TestCase):
  image_data = GENERIC_PREVIEW['image']

  def test_constructor(self):
    image_asset = ImageAsset(
      url=self.image_data['url'],
      width=self.image_data['width'],
      height=self.image_data['height']
    )

    self.assertEqual(image_asset.url, self.image_data['url'])
    self.assertEqual(image_asset.width, self.image_data['width'])
    self.assertEqual(image_asset.height, self.image_data['height'])

  def test_from_json(self):
    image_asset = ImageAsset.from_json(self.image_data)

    self.assertEqual(image_asset.url, self.image_data['url'])
    self.assertEqual(image_asset.width, self.image_data['width'])
    self.assertEqual(image_asset.height, self.image_data['height'])

  def test_to_json_dict(self):
    image_asset = ImageAsset.from_json(self.image_data)
    self.assertDictEqual(image_asset.to_json_dict(), self.image_data)
