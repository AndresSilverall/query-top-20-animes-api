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


class UpdateTopAnimeMutation(graphene.Mutation):
    class Arguments: 
        id = graphene.Int()
        title = graphene.String()
        genre = graphene.String()
        description = graphene.String()
        year = graphene.Int()
        magazine = graphene.String()
        is_active = graphene.Int()
        episode = graphene.Int()

    update_anime = graphene.Field(TopAnimeType)


    def mutate(self, info, id, title, genre, description, year, magazine, is_active, episode):
        update_anime = TopAnime.objects.get(id=id)
        update_anime.title = title
        update_anime.description = description
        update_anime.genre = genre
        update_anime.year = year
        update_anime.magazine = magazine
        update_anime.is_active = is_active
        update_anime.episode = episode

        update_anime.save()

        return UpdateTopAnimeMutation(update_anime=update_anime)