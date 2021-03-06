from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField
import re


class FileManage(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(default=timezone.now)
    article_num = models.CharField(default=0, max_length=10)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextUploadingField(null=True, blank=True)
    abstract = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='upload', null=True, blank=True)
    url_img = models.URLField(null=True, blank=True)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(to=Tag, related_name='article', blank=True)
    comment_num = models.IntegerField(default=0)
    view_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# 新建文章时取前200字符作摘要
@receiver(post_save, sender=Article)
def create_article_abstract(sender, instance, created, **kwargs):
    if created:
        content = instance.content
        content_text1 = content.replace('<p>', '').replace('</p>', '').replace('&#39;', '')
        # 去掉图片链接
        content_text2 = re.sub('!\[\]\((.*?)\)', '', content_text1)
        # 去掉markdown标签
        pattern = '[\\\`\*\_\[\]\#\+\-\!\>]'
        content_text3 = re.sub(pattern, '', content_text2)
        instance.abstract = content_text3[:150]
        instance.save()


class Comment(models.Model):
    belong_to = models.ForeignKey(to=Article, related_name='comments')
    parent = models.ForeignKey(to='self', related_name='child_comments', null=True, blank=True)
    reply = models.ForeignKey(to='self', related_name='who_reply', null=True, blank=True)
    content = models.TextField()
    comment_user = models.CharField(default='匿名', max_length=30)
    user_ip = models.CharField(null=True, blank=True, max_length=100)
    send_email = models.BooleanField(default=False)
    user_email = models.EmailField(max_length=30, null=True, blank=True)
    create_time = models.DateTimeField(default=timezone.now)
    child_reply_input = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_user


class ViewInfo(models.Model):
    view_ip = models.CharField(default=0, max_length=100)
    view_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.all_view_num

# from faker import Factory
# fake = Factory.create()
# for i in range(0, 10):
#     A = Article(
#         title=fake.text(max_nb_chars=50),
#         content=fake.text(max_nb_chars=3000)
#     )
#     A.save()
