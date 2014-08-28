from django.db import models

TICKET_TYPES = ( 
        ("649", "649"), 
        ("LM", "LottoMax" ) )

# Create your models here.
class Ticket(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    choice_text = models.CharField(max_length=3,
                                   choices=TICKET_TYPES,
                                   default="649")
    image_file = models.ImageField(upload_to="tickets")

    
