from django.urls import path
from . import views

urlpatterns = [
    # 設置路徑、接收view回傳的頁面
    path('main/', views.main, name= "main"),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('guide_generateData/', views.guide_generateData, name='guide_generateData'),
    path('project/', views.project, name='project'),
    path('search/', views.search, name='search'),
    path('searchTable', views.searchTable, name='searchTable'),
    path('updateData', views.updateData, name='updateData'),
    path('uploadData', views.uploadData, name='uploadData'),
    path('actionLog', views.actionLog, name='actionLog'),
    path('searchActionTable', views.searchActionTable, name='searchActionTable'),

]