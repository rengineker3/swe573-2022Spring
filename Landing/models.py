from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from PIL import Image
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager




def validate_date(date):
    if date < timezone.now():
        raise ValidationError("Date cannot be in the past.")    



class Category(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
    image = models.ImageField(default='category-default.jpg',
                              upload_to='category_images')
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_articles',
                       kwargs={'slug': self.slug})


class Article(models.Model):

  
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='articles')
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='articles')
    image = models.ImageField(default='article-default.jpg',
                              upload_to='article_pics')
    image_credit = models.CharField(max_length=250, null=True, blank=True)
    body = models.CharField(max_length=500, default='Some Description', null=False, blank=False)
    tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='DRAFT')
    views = models.PositiveIntegerField(default=0)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})





class Comment(models.Model):

    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField()
    comment = models.TextField(null=False, blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"
