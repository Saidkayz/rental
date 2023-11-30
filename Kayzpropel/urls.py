
from django.contrib import admin
from django.urls import path
from Kayzpropel import views
from django.conf import settings
from django.conf.urls.static import static

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add, name='add'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('index2/', views.index2, name='index2'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('site/', views.site, name='site'),
    path('showimage/', views.show_property, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

    path('invoice/', views.printinvoice, name='invoice'),
    path('dashboard-package/', views.package, name='package'),
    path('dashboard-favorite/', views.favorite, name='favorite'),
    path('dashboard-message/', views.message, name='message'),
    path('dashboard-order/', views.order, name='order'),
    path('dashboard-profile/', views.show_profile, name='profile'),
    path('dashboard-review/', views.review, name='review'),
    path('dashboard-save-search/', views.savesearch2, name='savesearch2'),
    path('dashboard-savesearch/', views.savesearch, name='savesearch'),
    path('dashboard-categories/', views.categories, name='categories'),
    path('agency/', views.agency, name='agency'),
    path('agency-single/', views.agencysingle, name='agency-single'),
    path('agent-list/', views.agentlist, name='agent-list'),
    path('agent-single/', views.agentsingle, name='agent-single'),
    path('banner/', views.banner, name='banner'),
    path('blog-single/', views.blogsingle, name='blog-single'),
    path('blog-v1/', views.blog1, name='blog1'),
    path('blog-v2/', views.blog2, name='blog2'),
    path('blog-v3/', views.blog3, name='blog3'),
    path('compare/', views.compare, name='compare'),
    path('error/', views.error, name='error'),
    path('grid-default/', views.griddefault, name='grid-default'),
    path('property-1-col/', views.property1col, name='property-1'),
    path('property-2-col/', views.property2col, name='property-2'),
    path('property-half1-map/', views.half1, name='property-half1'),
    path('property-half2-map/', views.half2, name='property-half2'),
    path('property-header-map/', views.mapheaderstyle, name='property-header'),
    path('property-list/', views.list, name='property-list'),
    path('error/', views.error, name='error'),
    path('property-list-all/', views.listall, name='listall'),
    path('property-single-v1/', views.single, name='single'),
    path('property-single-v2/', views.single2, name='single2'),
    path('property-single-v3/', views.single3, name='single3'),
    path('shop-cart/', views.cart, name='shop_cart'),
    path('update/<int:id>', views.update, name='update'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
path('print/', views.print_page, name='print_page'),
    path('send-email/', views.send_email, name='send_email')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)