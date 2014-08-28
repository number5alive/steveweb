from django.db import models

# Create your models here.
class Ticket(models.Model):
    SIXFOURNINE = "649"
    LOTTOMAX = "LM"
    TICKET_TYPES = ( 
        (SIXFOURNINE, "649"), 
        (LOTTOMAX, "LottoMax" ) )

    start_date = models.DateField()
    end_date = models.DateField()
    choice_text = models.CharField(max_length=3,
                                   choices=TICKET_TYPES,
                                   default=SIXFOURNINE)
    image_file = models.ImageField(upload_to="tickets")
    cost = models.IntegerField()

    
