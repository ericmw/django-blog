from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts' : PostSitemap
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'blog/', include('blog.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^sitemap\.xml$',sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  
]