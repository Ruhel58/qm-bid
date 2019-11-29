"""QM_Bid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authentication
from user_profile.views import user_view, login_view, register, profile_view
from item.views import item_json, item_view, add_item_form
from auction.views import auction_json, auction_view, all_auction_json, home_view, add_auction_view, search, set_bid, all_auctions
from django.conf import settings
from django.conf.urls.static import static

# consider URL reversing for cleaner and organized URL patterns

urlpatterns = [
    path('', home_view, name='home_view'),
    path('register/', register, name='register'),
    path('add_item/', add_item_form, name='add_item'),
    path('add_auction/', add_auction_view, name='add_auction'),
    path('login/', authentication.LoginView.as_view(template_name='user_profile/login_form.html'), name='login'),
    path('logout/', authentication.LogoutView.as_view(template_name='user_profile/logout.html'), name='logout'),
    path('password-reset/', authentication.PasswordResetView.as_view(template_name='user_profile/password_reset.html'), name='password_reset'),
    path('password-reset/done', authentication.PasswordResetDoneView.as_view(template_name='user_profile/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', authentication.PasswordResetConfirmView.as_view(template_name='user_profile/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', authentication.PasswordResetCompleteView.as_view(template_name='user_profile/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('profile/<str:username>', user_view, name='public_profile'),
    path('item/<int:id>.json', item_json, name='item_json'),
    path('item/<int:id>', item_view, name='item_view'),
    path('auction/<int:id>.json', auction_json, name='auction_json'),
    path('auction/<int:id>', auction_view, name='auction_view'),
    path('listofauction.json', all_auction_json, name='list of auctions'),
    path('my_profile/', profile_view, name='profile'),
    path('search_result/', search, name='search'),
    path('bid/<int:id>', set_bid, name='set_bid'),
    path('all_auctions/', all_auctions, name='all_auctions'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


