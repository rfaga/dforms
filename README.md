===============
dforms - Django Dynamic Forms
===============

I'm starting to upload and organize what I did to make dynamic forms in Django.

To explain how it works, I'll give an example:

    class SubscriberType(Model):
        name = CharField(max_length=255)
        extra_fields = PickledObjectField()
        
    class Subscriber(Model)
        subs_type = ForeignKey('SubscriberType')
        extra_fields = PickledObjectField()
        
        
Then you can create the fields in the "Type" related and put values in Subscriber.
