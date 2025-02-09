from django.urls import path , include 
from rest_framework_nested import routers
from asyncio import Task
from . import views



# router = routers.DefaultRouter()
# router.register('mytodolist', views.ToDoListViewSet,basename='Task')
# router.register('mytodolist/update', views.TaskUpdatingSet,basename='Task')
urlpatterns = [

    
    path('mytodolist/',views.ToDoListViewSet.as_view({'get':'todo_view_list','post':'todo_view_list'})),
    path('mytodolist/update/<int:id1>',views.TaskUpdatingSet.as_view({'put':'taskupdate','delete':'taskupdate'})),
    
]