import mongoengine as me
from django.utils import timezone

class Category(me.Document):
    name = me.StringField(required=True)
    description = me.StringField()

    meta = {'collection':'categories'}

    def __self__(self):
        return self.name
    

class Part(me.Document):
    VEHICLE_CHOICES = ('car','bike','truck')

    name = me.StringField(required = True)
    category = me.ReferenceField(Category,required = True)
    brand = me.StringField(required=True)
    vehicle_type = me.StringField(choices=VEHICLE_CHOICES)
    purchase_price = me.DecimalField(precision=2)
    selling_price = me.DecimalField(precision=2)
    stock = me.IntField(default = 0)
    created_at = me.DateTimeField(default=timezone.now)

    meta = {'collection':'parts'}

    def __str__(self):
        return self.name
     