from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# JRK - extend user models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# JRK
from api.credhandler import encryptCreds
from api.cards import processBadgeHex

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Api(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='api',
                              on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class ConnectLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=100, blank=True, default='')
    fqdn = models.CharField(max_length=100, blank=True, default='')
    ip_addr = models.GenericIPAddressField()
    os = models.CharField(max_length=100, blank=True, default='')
    user = models.CharField(max_length=30, blank=True, default='')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """

        super(ConnectLog, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pw = models.CharField(max_length=180, blank=True)
    badge = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    desktop = models.CharField(max_length=40, blank=True)
    #
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def save(self, **kwargs):
        if self.id:
            # editing existing
            # process raw badge hex into id and hash with pw
            if self.badge[:2] == '0x':
                badgeHex = self.badge
                badgeid = processBadgeHex(self.badge)
                self.badge = badgeid[1]  # store just the id
                pw = encryptCreds(badgeHex, self.pw)  # create encrypted pw
                self.pw = pw
        else:
            # new
            # self.created_date = datetime.now()
            pass
        super(Profile, self).save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    # birth_date = models.DateField(null=True, blank=True)
