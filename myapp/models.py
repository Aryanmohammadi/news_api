from django.db import models


class News(models.Model):
    title= models.CharField(max_length=900) 
    content_html= models.PositiveBigIntegerField()
    summary= models.PositiveBigIntegerField
    image= models.ImageField()
    date_published=models.DateField() 
    author= models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.title} => {self.content_html} => {self.summary} => {self.image} => {self.date_published} => {self.author}"