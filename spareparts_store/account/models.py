from django.utils import timezone
import mongoengine as me

class users(me.Document):
    ROLE_CHOICES = ('admin', 'staff')

    username = me.StringField(required=True, unique=True)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)
    role = me.StringField(choices=ROLE_CHOICES,required=True)
    phone = me.StringField()
    created_at = me.DateTimeField(default=timezone.now)
    meta = {'collection': 'users'}

    def __str__(self):
        return self.username

