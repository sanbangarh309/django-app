from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import sandeep.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", sandeep.views.index, name="home"),
    path("about/", sandeep.views.about, name="about"),
    path("portfolio/", sandeep.views.portfolio, name="portfolio"),
    path("portfolio/<int:portfolio_id>", sandeep.views.portfolio_detail, name="portfolio"),
    # path("db/", sandeep.views.db, name="db"),
    # path("db/", sandeep.views.db, name="db"),
    path("admin/", admin.site.urls),
]
