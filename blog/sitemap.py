from django.contrib.sitemaps import Sitemap

from .models import Blog, Top10

class BlogSitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return Blog.objects.all()
		
		def lastmod(self, obj):
				return obj.update_date


class Top10Sitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return Top10.objects.all()
		
		def lastmod(self, obj):
				return obj.publish_date
