import graphene
from api.models import TopAnime, Mangaka
from api.types import TopAnimeType, MangakaType


class Query(graphene.ObjectType):
    all_animes = graphene.List(TopAnimeType)
    get_anime = graphene.Field(TopAnimeType, anime_id=graphene.Int(required=True))

    def resolve_all_animes(self, info, **kwargs):
        return TopAnime.objects.all()

    
    def resolve_get_anime(self, info, anime_id):
        try: 
            return TopAnime.objects.get(id=anime_id)
        except TopAnime.DoesNotExist:
            return None


schema = graphene.Schema(query=Query) 