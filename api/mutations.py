import graphene
from api.models import TopAnime, Mangaka
from api.types import TopAnimeType, MangakaType


class AddTopAnimeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        genre = graphene.String()
        description = graphene.String()
        year = graphene.Int()
        magazine = graphene.String()
        is_active = graphene.Int()
        episode = graphene.Int()

    top_anime = graphene.Field(TopAnimeType)


    def mutate(self, info, title, genre, description, year, magazine, is_active, episode):
        top_anime = TopAnime.objects.create(
            genre=genre,
            episode=episode,
            title=title,
            description=description,
            year=year,
            magazine=magazine,
            is_active=is_active
        )
        top_anime.save()

        return AddTopAnimeMutation(top_anime=top_anime)


    def update_anime(self, info, id, title, genre, description, year, magazine, is_active ):

        top_anime = TopAnime.objects.get(id=id)
        top_anime.title = title
        top_anime.genre = genre
        top_anime.description = description
        top_anime.year = year
        top_anime.magazine = magazine
        top_anime.is_active = is_active
        top_anime.save()

        return AddTopAnimeMutation(top_anime=top_anime)