from django.contrib import admin
from .models import Hero, OurService, AboutUs, WhyUs, OurTeam, CustomerReviews

# Register your models here.

admin.site.register(Hero)
admin.site.register(OurService)
admin.site.register(AboutUs)
admin.site.register(WhyUs)
admin.site.register(OurTeam)
admin.site.register(CustomerReviews)
