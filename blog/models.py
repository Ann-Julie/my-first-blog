from django.db import models
from django.utils import timezone

# Post is the name of our model. Always start it with an uppercase letter
# models.Model means that the Post is a Django Model, so Django knows that it
# should be saved in the Database
class Post(models.Model):

    # Now we define the properties we were talking about: title, text,
    # created_date, published_date and author. To do that we need to define
    # the type of each field

    # Now we define the properties we were talking about: title, text, created_date,
    # published_date and author. To do that we need to define the type of each field
    # (Is it text? A number? A date? A relation to another object, like a User?)
    #
    # models.CharField – this is how you define text with a limited number of characters.
    # models.TextField – this is for long text without a limit.
    #    Sounds ideal for blog post content, right?
    # models.DateTimeField – this is a date and time.
    # models.ForeignKey – this is a link to another model.


    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    # def means that this is a function/method and publish is the name of the method.
    # The naming rule is that we use lowercase and underscores instead of spaces

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Methods often return something. There is an example of that in the __str__ 
    # method. In this scenario, when we call __str__() we will get a text (string)
    #  with a Post title.

    def __str__(self):
        return self.title
