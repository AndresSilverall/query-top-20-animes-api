from django.db import models


# Create your models here.
class TopAnime(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        unique=True
    )

    genre = models.CharField(
        max_length=6,
        null=False
    )

    description = models.TextField(
        verbose_name="Description about the anime.",
        null=False
    )

    magazine = models.CharField(
        max_length=20,
        null=True
    )

    year = models.FloatField(
        null=False
    )

    episode = models.IntegerField(
        "number of episodes",
        null=True
    )

    is_active = models.BooleanField(
        default=False
    )


    def __str__(self):
        return self.title


class Mangaka(models.Model):

    class ReviewAnime(models.TextChoices):

        ONE = "1", "one",
        TWO = "2", "two"
        THREE = "3" "three"
        FOUR = "4", "four"
        FIVE = "5", "five"
        SIX = "6", "six"
        SEVEN = "7", "seven"
        EIGHT = "8", "eight"
        NINE = "9", "nine"
        TEN = "10", "ten"

    anime = models.ForeignKey(
        TopAnime, on_delete=models.CASCADE,
        related_name="Authors",
        null=True
    )

    mangaka = models.CharField(
        max_length=20,
        null=True
    )

    review = models.CharField(
        choices=ReviewAnime.choices,
        null=True,
        max_length=6
    )


    def __str__(self):
        return str(self.anime.title)