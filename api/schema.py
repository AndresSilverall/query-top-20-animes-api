import graphene
from api.types import TopAnimeType, MangakaType


class Query(graphene.ObjectType):
    all_animes = graphene.List(TopAnimeType)


schema = graphene.Schema(query=Query) 