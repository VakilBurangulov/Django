from django.db import models

class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Advertisements'
    def __str__(self):
        return f"{self.title}, {self.description}, {self.price}, {self.auction}, {self.created_at}, {self.update_at}"


# Create your models here.
