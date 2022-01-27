from rest_framework.routers import SimpleRouter
from .views import TeamViewSet, PlayerViewSet

routes = SimpleRouter()

routes.register(r'team', TeamViewSet, basename='teams-team')
routes.register(r'player', PlayerViewSet, basename='teams-player')

urlpatterns = [
    *routes.urls
]
