from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (0, "Draft"), (1, "Publish")

PLATFORM = [
    ('All platforms', 'All platforms'),
    ('PC', 'PC'),
    ('Xbox', 'Xbox'),
    ('Xbox 360', 'Xbox 360'),
    ('Xbox One', 'Xbox One'),
    ('Xbox Series', 'Xbox Series'),
    ('PlayStation', 'PlayStation'),
    ('PlayStation 2', 'PlayStation 2'),
    ('PlayStation 3', 'PlayStation 3'),
    ('PlayStation 4', 'PlayStation 4'),
    ('PlayStation 5', 'PlayStation 5'),
    ('Nintendo Switch', 'Nintendo Switch'),
    ('Nintendo Wii', 'Nintendo Wii'),
]


class Game(models.Model):

    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    platform = models.CharField(max_length=20, choices=PLATFORM,
                                default='All platforms')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='connect_posts'
    )
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
