from django.urls import path
from api.views import PostTask, GetAllTasks


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# path('', include(router.urls)),
urlpatterns = [
    path('posttask/', PostTask, name='posttask'),
    path('getalltasks/', GetAllTasks, name='getalltasks')
]