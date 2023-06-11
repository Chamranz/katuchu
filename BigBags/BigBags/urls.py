from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', views.index, name='index'),
    path('admin/', admin.site.urls),
    re_path (r'^bags/$', views.BagsListView.as_view(), name='Bag'),
    re_path (r'^bag/(?P<pk>\d+)$', views.BagDetailView.as_view(),name='bag-detail'),
    path ('order/', views.madeorder, name='order'),
    path ('check/', views.check, name='check'),
    re_path (r'^register/$', views.RegisterUser.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('basket/', views.LoanedBagByUserListView.as_view(), name='my-basket')
]


