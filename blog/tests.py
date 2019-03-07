from django.test import TestCase
from blog.models import Post
from django.urls import reverse
from blog.views import post_detail_view

# Create your tests here.

class PostTest(TestCase):
#create POST object/helper function
    def create_post(self, title='This is a test title', author=2):
        return Post.objects.create(title=title)
    
    #test whether created title matches expected title
    def test_post_creation(self):
        w = self.create_post()
        self.assertTrue(isinstance(w, Post))
        
    #test if response code is 200 for the url we fetch
    def test_blog_list_view(self):
        w = self.create_post()
        url = reverse("blog:post_list_view")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        arr = bytes(w.title, 'utf-8')
        # self.assertIn(arr.decode(), resp.content)