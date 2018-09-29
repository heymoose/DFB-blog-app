from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post


# Test that the Post model is working correctly
class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user
        )

    # Test the __str__ implementation of the Post model
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)


# Test the PostListView
# 1. Test that the Home URL is there
# 2. Test that the response contains the test post content
# 3. Test that the template used for the home page is 'home.html'
def test_post_list_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Nice body content')
    self.assertTemplateUsed(response, 'home.html')


# Test the PostDetailView
# 1. Test that an actual page is there
# 2. Test that a page that shouldn't be there actually isn't there
# 3. Test that the response contains the correct title
# 4. Test that the page is using the correct template
def test_post_defail_view(self):
    response = self.client.get('/post/1/')
    no_response = self.client.get('/post/1000000')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response, 404)
    self.assertContains(response, 'A good title')
    self.assertTemplateUsed(response, 'post_detail.html')
