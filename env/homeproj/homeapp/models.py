# Create your models here.
# Place an otherwise blank app in settings.INSTALLED_APPS
# and add the following into the app's models.py:

from django.db.models import signals
from django.dispatch import dispatcher
from django.contrib.auth import models as auth_app
import new, crypt, random, string
from django.utils.encoding import smart_str

def set_password_crypt(self, raw_password):
    algo = 'crypt'
    saltchars = string.ascii_letters + string.digits + './'
    salt = ''.join(random.choice(saltchars) for i in range(2))
    hsh = crypt.crypt(smart_str(raw_password), salt)
    self.password = '%s$%s$%s' % (algo, salt, hsh)

def replace_set_password(instance=None):
    instance.set_password = new.instancemethod(
        set_password_crypt, instance, instance.__class__)

dispatcher.connect(replace_set_password,
                   sender=auth_app.User,
                   signal=signals.post_init)
