from rest_framework import routers
from database.viewsets import martabakbestsellerViewSet, martabakViewSet, RatingViewSet, UserRatingViewSet
router = routers.DefaultRouter()
router.register(r'martabak/bestseller', martabakbestsellerViewSet)
router.register(r'martabak', martabakViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'userrating', UserRatingViewSet)