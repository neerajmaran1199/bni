from django.urls import path
from .views import HomePage, UserPost, CountryCreateView, CountryDetailView, CategoryView,  CountryUpdateView, CountryDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePage, name='news-home'),
    path('country/new/', CountryCreateView.as_view(template_name="news_app/country_form.html"), name='country-new-post'),
    path('detail/<int:pk>/',CountryDetailView.as_view, name='country-detail' ),
    path('country/<int:pk>/', CountryDetailView.as_view(template_name="news_app/detail.html"), name='country-detail'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category/Entertainment/',CategoryView, name='category-ent' ),
    path('category/World/',CategoryView, name='category-wo' ),
    path('category/Politics/',CategoryView, name='category-po' ),
    path('category/Tech/',CategoryView, name='category-te' ),
    path('category/Country/',CategoryView, name='category-co' ),
    path('category/Business/',CategoryView, name='category-bu' ),
    path('category/Carrier/',CategoryView, name='category-ca' ),
    path('category/Sports/',CategoryView, name='category-sp' ),
    path('category/Startup/',CategoryView, name='category-st' ),
    path('country/<int:pk>/update/', CountryUpdateView.as_view(), name='country-update'),
    path('country/<int:pk>/delete/', CountryDeleteView.as_view(), name='country-delete'),
    path('userpost/',UserPost, name='user-post' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)