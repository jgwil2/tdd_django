from django.conf.urls import include, url
from django.contrib import admin
import lists.urls

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^lists/', include(lists.urls, namespace='lists')),
    url(r'^admin/', include(admin.site.urls)),
]
