from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('New blog title', 'Test author')

        self.assertEqual('New blog title',b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([],b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test author')
        b1 = Blog('My first post', 'Mary')
        self.assertEqual('Test by Test author (0 blog posts)', b.__repr__())
        self.assertEqual('My first post by Mary (0 blog posts)', b1.__repr__())


    def test_repr_multiple(self):
        b=Blog('Two posts','Mary')
        b.posts=['test','test2']
        b2=Blog('One post','Harry')
        b2.posts['first post']

        self.assertEqual('Two posts by Mary (2 blog posts)', b.__repr__())
        self.assertEqual('One post by Harry (1 blog post', b2.__repr__())


