from django.db import models
from decimal import Decimal

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    handicap_index = models.DecimalField(max_digits=5, decimal_places=2)
    wensum_handicap = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    valley_handicap = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)

    def calculate_course_handicap(self, course_id):
        # Example calculation; replace this with your own logic
        if course_id == 1:
            return self.handicap_index * (Decimal('120') / Decimal('113')) + Decimal('68.8') - Decimal('72')
        elif course_id == 2:
            return self.handicap_index * (Decimal('127') / Decimal('113')) + Decimal('69.1') - Decimal('72')
           
        
        return 0

    def save(self, *args, **kwargs):
        # Calculate course handicaps before saving
        self.wensum_handicap = self.calculate_course_handicap(course_id=1)
        self.valley_handicap = self.calculate_course_handicap(course_id=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
