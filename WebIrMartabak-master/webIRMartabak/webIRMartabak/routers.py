from rest_framework import routers
from database.viewsets import martabakhomeViewSet
router = routers.DefaultRouter()
router.register(r'database', martabakhomeViewSet)