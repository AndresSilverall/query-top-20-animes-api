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
    anime = models.ForeignKey(
        TopAnime, on_delete=models.CASCADE,
        related_name="Authors",
        null=True
    )