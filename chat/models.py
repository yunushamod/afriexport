from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    user_from = models.ForeignKey(User, related_name='messages_from', on_delete=models.CASCADE)  # type: ignore
    user_to = models.ForeignKey(User, related_name='messages_to', on_delete=models.CASCADE) # type: ignore
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField()
    message = models.CharField(max_length=400, null=False, blank=False)
    parent = models.ForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='replies')

    @property
    def children(self):
        return Messages.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        return self.parent is None
