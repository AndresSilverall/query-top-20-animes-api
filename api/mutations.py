import graphene
from api.models import TopAnime, Mangaka
from api.types import TopAnimeType, MangakaType


class EditTopAnimeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        genre = graphene.String()
        description = graphene.String()
        year = graphene.Int()
        magazine = graphene.String()
        is_active = graphene.Int()

    top_anime = graphene.Field(TopAnimeType)


    def mutate(self, info, title, genre, description, year, magazine, is_active):
        top_anime = TopAnime.objects.create(
            genre=genre,
            title=title,
            description=description,
            year=year,
            magazine=magazine,
            is_active=is_active
        )
        top_anime.save()

        return EditTopAnimeMutation(top_anime=top_anime)

    def update_anime(self, info, id):
        pass