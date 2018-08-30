from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):


    def test_create_post_in_blog(self):
        b = Blog('Two posts', 'Mary')
        b.create_post('Test post','This is test content')

        self.assertEqual(b.posts[0].title, 'Test post')
        self.assertEqual(b.posts[0].content, 'This is test content')

    def test_create_json(self):
        b = Blog('Two posts', 'Mary')
        b.create_post('Test post', 'This is test content')

        expected = {
            'title' : 'Two posts',
            'author' : 'Mary',
            'posts': [
                {
                    'title':'Test post',
                    'content':'This is test content'

                }
            ]}
        self.assertDictEqual(expected, b.json())

