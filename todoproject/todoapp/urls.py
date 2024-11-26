from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:taskid>/',views.detail, name='detail'),

    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('update/<int:taskid>/', views.update, name="update"),
    path('classhome/',views.Tasklist.as_view(),name='classhome'),
    path('classdetail/<int:pk>/',views.Taskdetail.as_view(),name='classdetail'),
    path('classupdate/<int:pk>/',views.Taskupdate.as_view(),name='classupdate'),
    path('classdelete/<int:pk>/',views.Taskdelete.as_view(),name='classdelete')
]

