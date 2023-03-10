from django.urls import path  # , re_path
from .views import index, about, addpage, contact,\
    login, show_category, show_post, adminmenu


urlpatterns = [
    path('', index, name='home'),
    path('admin/', adminmenu, name='adminmenu'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    # re_path(r'^archive/(?P<year>[0-9]{4})', archive),
]
