from django.urls import path, include

from rest_framework import routers

from apps.todo.api.viewsets import TaskViewSets

#o carinha que vai criar a endpoint
router = routers.DefaultRouter()

router.register("",TaskViewSets,basename="task")

urlpatterns = [
    path("",include(router.urls)),
]