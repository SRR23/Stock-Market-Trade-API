from django.db import models
# auto_now=True: Updates the date field to the current date whenever the instance is updated.
# auto_now_add=True: Only sets the date field once when the instance is first created.
class TradeData(models.Model):
    date = models.DateField(auto_now=True)
    trade_code = models.CharField(max_length=50)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
