from django.urls import path
from home.views import IndexView,DetailView
urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    #详情视图的路由
    path('detail/', DetailView.as_view(),name='detail'),
]