from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaulRouter()
router.register('api/leads',LeadViewSet,'leads')

urlpatterns =routers.urls
