from django.db import models
from main.models import MyUser


class Money(models.Model):
    user = models.ForeignKey(MyUser,  on_delete=models.CASCADE)
    message = models.CharField()
    date_of_add = models.CharField()
    summa = models.IntegerField()

    def __str__(self):
        return self.message+' '+ str(self.summa)+' ' +str(self.date_of_add)

