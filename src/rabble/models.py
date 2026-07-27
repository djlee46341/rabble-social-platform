from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(default='')
    interests = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        through='Following'
    )
    class Meta:
        unique_together = ("username", "email")

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_relationships')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_relationships')
    
    class Meta:
        unique_together = ("user", "following")

class Communities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community_name = models.TextField()

class Community_Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Communities, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

class Subrabbles(models.Model):
    community = models.ForeignKey(Communities, on_delete=models.CASCADE)
    subrabble_name = models.TextField()
    identifier = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    is_public = models.BooleanField(default = True)
    num_posts = models.IntegerField(default = 0)
    num_comments = models.IntegerField(default = 0)
    allow_anon = models.BooleanField(default = False)

class SubrabbleMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble = models.ForeignKey(Subrabbles, on_delete=models.CASCADE)

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble = models.ForeignKey(Subrabbles, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    num_likes = models.IntegerField(default=0)
    num_comments = models.IntegerField(default=0)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    body = models.TextField()
    num_likes = models.IntegerField(default=0)
    num_replies = models.IntegerField(default=0)

class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    body = models.TextField()
    num_likes = models.IntegerField(default=0)

class Conversations(models.Model):
    title = models.TextField()

class ConversationMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)

class ConversationMessages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    body = models.TextField()

class CommunityInvites(models.Model):
    community = models.ForeignKey(Communities, on_delete=models.CASCADE)
    email = models.EmailField(unique = True)
