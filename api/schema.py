import graphene
from api.models import TopAnime, Mangaka
from api.types import TopAnimeType, MangakaType


class Query(graphene.ObjectType):
    all_animes = graphene.List(TopAnimeType)
    id_anime = graphene.Field(TopAnimeType, id=graphene.ID(required=True))

    def resolve_all_animes(self, info, **kwargs):
        return TopAnime.objects.all()

    
    def resolve_get_anime_by_name(self, id, info, **kwargs):
        try: 
            return TopAnime.objects.get(id=id)
        except TopAnime.DoesNotExist:
            return None


schema = graphene.Schema(query=Query) 