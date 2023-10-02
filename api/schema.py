import graphene
from api.models import TopAnime, Mangaka
from api.types import TopAnimeType, MangakaType
from api.mutations import EditTopAnimeMutation


class Query(graphene.ObjectType):
    all_animes = graphene.List(TopAnimeType)
    get_anime = graphene.Field(TopAnimeType, anime_id=graphene.Int(required=True))
    mangaka = graphene.List(MangakaType)
    get_mangaka = graphene.Field(MangakaType, mangaka_id=graphene.Int(required=True))

    def resolve_all_animes(self, info, **kwargs):
        return TopAnime.objects.all()

    
    def resolve_get_anime(self, info, anime_id: int):
        try: 
            return TopAnime.objects.get(id=anime_id)
        except TopAnime.DoesNotExist:
            return "Anime not found!"


    def resolve_mangaka(self, info, **kwargs):
        return Mangaka.objects.all() 
    

    def resolve_get_mangaka(sekf, info, mangaka_id:int):
        try:
            return Mangaka.objects.get(id=mangaka_id)
        except Mangaka.DoesNotExist:
            return "Mangaka not found!"
    

class Mutation(graphene.ObjectType):
    add_anime = EditTopAnimeMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation) 