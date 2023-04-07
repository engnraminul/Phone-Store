from django.contrib.sitemaps import Sitemap

from .models import Phone, PhoneBrand, ProcessorBrand, Processor, GalleryImage

class PhoneSitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return Phone.objects.exclude(status="Draft")
				
		
		def lastmod(self, obj):
				return obj.updated


class PhoneBrandSitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return PhoneBrand.objects.all()


class ProcessorBrandSitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return ProcessorBrand.objects.all()


class PhoneProcessorSitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return Processor.objects.all()

class GallerySitemap(Sitemap):
		changefreq = "always"
		priority = 0.9
		
		def items(self):
				return GalleryImage.objects.all()
