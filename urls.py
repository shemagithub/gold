
from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view 
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm


urlpatterns = [                                         
    path("", views.home),
    path("sub/", views.sub, name="sub"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    path("blog/", views.blog, name="blog"),
    path("cash/", views.cash, name="cash"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path('search/', views.product_search, name='product_search'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path("updateAdrress/<int:pk>/", views.updateAddress.as_view(), 
    name="updateAddress"),

    #carts
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="showcart"),
    path("checkout/", views.checkout.as_view(), name="checkout"),

    #creditintial urls
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name="login"),
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone') , name="passwordchange"),
    path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name="passwordchangedone"),

    path("logout/", auth_view.LogoutView.as_view(next_page='login'), name="logout"),
    
    path("password-reset/done/", auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_view.PasswordResetView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name="password_reset_complete"),

    #remove cart or add or minus
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),






 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

