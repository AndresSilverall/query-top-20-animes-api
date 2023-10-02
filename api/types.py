from graphene_django import DjangoObjectType
from api.models import TopAnime, Mangaka


class TopAnimeType(DjangoObjectType):
    class Meta:
        model = TopAnime
        fields = (
            "id", 
            "title", 
            "genre", 
            "description", 
            "magazine", 
            "year", 
            "episode",
            "is_active"
        )


class MangakaType(DjangoObjectType):
    class Meta:
        model = Mangaka
        fields = ("id", "anime")
