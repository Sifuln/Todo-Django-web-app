from django.urls import path
from .views import MyView, TaskCreateView, TaskDetailView, TaskDeleteView, TaskSearchView

urlpatterns = [
    path('', MyView.as_view(), name='todo'),
    path('create/', TaskCreateView.as_view(), name='taskcreate'),
    path('todo_detail/<int:pk>', TaskDetailView.as_view(), name='taskdetail'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('search/', TaskSearchView.as_view(), name='task_search')
]