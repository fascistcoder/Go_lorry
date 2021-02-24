####### Custom CharField for username case-insensitivity #######
from django.db.models.fields import CharField
from django.contrib import admin
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
class iunicode(unicode):
    def __init__(self, value):
        super(iunicode, self).__init__(value)
        self.value = value

    def __eq__(self, other):
        if isinstance(other, str) or isinstance(other, unicode):
            return self.value.lower() == other.lower()
        if isinstance(other, self.__class__):
            return other == self.value
class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\-; ]+$'
class MyUser(AbstractUser):
    username_validator = MyValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and ;/@/./+/-/_ only.'),
        validators=[username_validator],
            error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
def custom_getattribute(self, name):
    val = object.__getattribute__(self, name)
    if name == "username":
        val = iunicode(val)
    return val

def auth_user_save(self, *args, **kwargs): # Ensures lowercase usernames
    username = self.username
    if username and type(username) in [unicode, str, iunicode]:
        self.username = username.lower()  
    super(User, self).save(*args, **kwargs)

User.__getattribute__ = custom_getattribute
User.save = MethodType(auth_user_save, None, User)
#####################################################