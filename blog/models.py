from django.db import models
from django.utils.timezone import now
# Create your models here.


class Action(models.Model):
	datatime = models.DateTimeField(auto_now_add=True)
	action = models.CharField(max_length=255)
	user = models.CharField(max_length=255)

	def __str__(self):
		item = (str(self.id), str(self.user), str(self.action), str(self.datatime))
		return ','.join(item)


















