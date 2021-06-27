import unittest

from peekalink.models.helpers.content_type import ContentType

class TestContentType(unittest.TestCase):
  def test_eq_operator(self):
    content_type = ContentType('html')
    self.assertTrue(content_type == ContentType.HTML)

  def test_ne_operator(self):
    content_type = ContentType('html')
    self.assertTrue(content_type != ContentType.IMAGE)

  def test_get_name(self):
    content_type = ContentType('flowerpot')
    self.assertEqual(content_type.get_name(), 'flowerpot')
