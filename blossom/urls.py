from django.contrib import admin
from django.urls import path
from .views import home_view, detail_view, create_view, search_view, account_view, signup_view, login_view, logout_view
from django.contrib.sitemaps.views import sitemap
from articles.sitemaps import sitemaps

urlpatterns = [
    path('', home_view, name="home"),
    path('account/', account_view, name="account"),
    path('account/signup', signup_view, name="signup"),
    path('account/login', login_view, name="login"),
    path('account/logout', logout_view, name="logout"),
    path('create/', create_view, name="create"),
    path('search/', search_view, name="search"),
    path('detail/<int:content_id>', detail_view, name="detail"),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
