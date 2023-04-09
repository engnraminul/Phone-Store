from django.shortcuts import render
from http import HTTPStatus

from django.test import TestCase

from django.http import HttpResponse
from django.views.decorators.http import require_GET
from Phone.models import  Phone


def home(request):
    phone = Phone.objects.filter(status='Released').order_by('-created')[:12]
    u_phone= Phone.objects.filter(status='Upcoming').order_by('-created')[:8]
    
    


    context = {
        'u_phone': u_phone,
        'phone': phone,
        
    }
    return render(request, 'home.html', context)
# @require_GET
# def robots_txt(request):
#     lines = [
#         "User-Agent: *",
#         "Disallow: /dashboard/",
#         "Disallow: /dashboard-login/",
#         "Disallow: /testimonials/",
#     ]
#     return HttpResponse("\n".join(lines), content_type="text/plain")


# from http import HTTPStatus

# from django.test import TestCase


# class RobotsTxtTests(TestCase):
#     def test_get(self):
#         response = self.client.get("/robots.txt")

#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertEqual(response["content-type"], "text/plain")
#         lines = response.content.decode().splitlines()
#         self.assertEqual(lines[0], "User-Agent: *")

#     def test_post_disallowed(self):
#         response = self.client.post("/robots.txt")

#         self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, response.status_code)