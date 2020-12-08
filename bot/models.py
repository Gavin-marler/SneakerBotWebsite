from django.db import models

class contactForm(models.Model):
  name = models.TextField()
  email = models.EmailField()
  message = models.TextField()
  
class userInfo(models.Model):
  #personal info
  first_name = models.TextField()
  last_name = models.TextField()
  email = models.EmailField()
  #shipping info
  addr = models.TextField()
  city = models.TextField()
  state = models.TextField()
  zip_code = models.TextField()
  #card info
  card_number = models.IntegerField()
  exp_date = models.TextField()
  ccv = models.IntegerField()
  #product info
  product_id = models.TextField()
  shoe_size = models.FloatField()
