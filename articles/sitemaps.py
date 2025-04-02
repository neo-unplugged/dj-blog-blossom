from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Content  # Assuming you have a Content model

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'account', 'signup', 'login', 'logout', 'create', 'search']

    def location(self, item):
        return reverse(item)

class ContentSitemap(Sitemap):
    priority = 0.6
    changefreq = 'daily'

    def items(self):
        return Content.objects.all()  # Assuming Content has dynamic URLs

    def location(self, obj):
        return reverse('detail', args=[obj.id])

sitemaps = {
    'static': StaticViewSitemap(),
    'content': ContentSitemap(),
}
