from django.db import models
from ckeditor.fields import RichTextField
from uzer.models import UzerModel


class CategoryModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TagModel(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=225)
    body = RichTextField()
    img = models.ImageField(upload_to='posts/')
    create_add = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)
    # tag = models.ManyToManyField(TagModel, related_name='posts')
    user = models.ForeignKey(UzerModel, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
