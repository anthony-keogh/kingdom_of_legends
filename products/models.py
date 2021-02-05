from django.db import models

# Create your models here.

class Product_item(models.Model):
    name = models.CharField(max_length=200, default='', primary_key=True)
    description = models.TextField(max_length=600,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
   

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200, default='', primary_key=True)
    author = models.CharField(max_length=200, default='')
    about_author = models.TextField(max_length=900,default='Write about author')
    full_book = models.TextField(max_length=10000,default='Write novel here')
    description = models.TextField(max_length=600,)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    DRAGON_AND_WITCHES_NOVELS = 'DW'
    FANTASY_NOVELS = 'FT'
    HEROS_OF_THE_NIGHT_NOVELS = 'HOTN'
    JUNGLE_NOVELS = 'JG'
    TRAVEL_NOVELS = 'TL'
    INTO_SPACE_NOVELS = 'IS'
    
    CATEGORY_BOOK_CHOICES = [
        (DRAGON_AND_WITCHES_NOVELS, 'Dragons and Witches Novels'),
        (FANTASY_NOVELS, 'Fantasy Novels'),
        (HEROS_OF_THE_NIGHT_NOVELS, 'Heros of the Night Novels'),
        (JUNGLE_NOVELS, 'Jungle Novels'),
        (TRAVEL_NOVELS, 'Travel Novels'),
        (INTO_SPACE_NOVELS, 'Into Space Novels'),
    ]
    book_category_novel = models.CharField(
        max_length=32,
        choices=CATEGORY_BOOK_CHOICES,
        default=FANTASY_NOVELS,
    )

    def __str__(self):
        return self.name


