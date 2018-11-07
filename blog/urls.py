from django.urls import path
from . import views
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
    re_path(r'^accueil', views.accueil,name='aa'),
    re_path(r'^article/(?P<id_article>\d{3})', views.view_article,name='afficher_article'),
    # re_path(r'^articles/(?P<tag>.+)', views.list_articles_by_tag),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
    # path('articles/<int:year>/<int:month',views.view_redirection),

]
# urlpatterns = [
#     path('accueil', views.home),
#     path('article/<id_article>',views.view_article),
#     path('articles/<str:tag>',views.list_artilces_by_tag),
#     path('articles/<int:year>/<int:month',views.list_articles),
# ]