from django.urls import path
from graphene_django.views import GraphQLView


urlpatterns = [
    path("api/anime/graphql/", GraphQLView.as_view(graphiql=True)),
  
]
