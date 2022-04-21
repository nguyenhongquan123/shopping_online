from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
def DiscountValidate(value):
    if not (0<=value<=100):
        raise ValidationError(">=0 and <=100")
    
class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    discount=models.IntegerField(validators=[DiscountValidate])
    active=models.BooleanField()
    def __str__(self):
        return self.code[:10]+"..."
    