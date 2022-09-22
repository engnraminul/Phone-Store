from django.shortcuts import render


from django.http import HttpResponse
from django.views.decorators.http import require_GET
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /dashboard/",
        "Disallow: /dashboard-login/",
        "Disallow: /testimonials/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")