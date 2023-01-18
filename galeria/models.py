from django.db import models

class PixelArt(models.Model):

    category_options = [
        ("PERSONAGEM", "Personagem"),
        ("ORIGINAL", "Original")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    path = models.ImageField(upload_to="pixelArts/", blank=False)#models.CharField(max_length=100, null= False, blank= False)
    category = models.CharField(max_length=100, choices= category_options, default="")
    description = models.TextField(null= False, blank= False)

    def __str__(self):
        return f"PixelArt: [name={self.name}]"
