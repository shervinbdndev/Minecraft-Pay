from typing import Union

from django.conf import settings
from django.contrib import messages
from django.urls.base import reverse
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from .models import UserPhoneNumber
from site_settings.models import MainSiteSettings, SignUpSettings
from .forms import LoginForm, RegisterForm, PhoneNumberForm, ResetPasswordForm, ResetPasswordConfirmForm
from .utils.token_generator import account_activation_token


        
        



class ActivateUserAccount(View):
    def get(self, request: HttpRequest, uidb64, token) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        request.session['success'] = 'حساب کاربری شما با موفقیت فعال شد'
        request.session['state'] = 'True'
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user_obj = User.objects.get(pk=uid)
        except:
            user_obj = None
        if (user_obj is not None and account_activation_token.check_token(user_obj, token)):
            user_obj.is_active = True
            user_obj.save()
            return redirect(to=reverse('verified'))
        else:
            messages.error(
                request=request,
                message='توکن شما منقضی شده است',
            )
        return render(
            request=request,
            template_name='verified.html',
            context={},
        )







def activateEmail(request: HttpRequest, user: User, to_email) -> None:
    subject: str = 'فعالسازی حساب کاربری'
    message = render_to_string(
        template_name='email/template.html',
        context={
            'user': user.username,
            'domain': get_current_site(request=request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http',
        }
    )
    send_mail(
        subject,
        message,
        'settings.EMAIL_HOST_USER',
        [to_email],
        fail_silently=False,
    )






class UserVerifyEmailView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        request.session['verification_text'] = 'لطفا جیمیل خود را چک کنید تا بخش پرداخت برای شما نمایان شود'
        if (request.user.is_superuser):
            return redirect(to=reverse('profile'))
        
        elif (request.user.is_authenticated):
            return redirect(to=reverse('profile'))
        
        return render(
            request=request,
            template_name='verify_email.html',
            context={},
        )
        
        
        
        



class UserSpecificationsView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        if (not request.user.is_authenticated):
            return redirect(to=reverse('login'))
        
        elif (not request.user.is_active):
            return redirect(to=reverse('verify'))
        
        return render(
            request=request,
            template_name='user_specifications.html',
            context={},
        )

        
        
        
        
        

class UserVerifiedEmailView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request=request,
            template_name='verified.html',
            context={},
        )







class UserProfileView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        site_settings: MainSiteSettings = MainSiteSettings()
        if (not request.user.is_authenticated):
            return redirect(to=reverse('login'))
        
        elif (not request.user.is_active):
            return redirect(to=reverse('verify'))
        
        return render(
            request=request,
            template_name='profile.html',
            context={
                'settings': site_settings,    
            },
        )








class UserResetPasswordView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        reset_password_form: ResetPasswordForm = ResetPasswordForm()
        return render(
            request=request,
            template_name='reset/reset.html',
            context={
                'reset_password_form': reset_password_form,
            },
        )
        
    def post(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        reset_password_form: ResetPasswordForm = ResetPasswordForm(request.POST or None)
        if (reset_password_form.is_valid()):
            cd = reset_password_form.cleaned_data
            user = get_user_model().objects.filter(Q(email=cd['email'])).first()
            if (user):
                subject = 'درخواست بازنشانی رمز ورود'
                message = render_to_string(
                    template_name='email/template_reset_password.html',
                    context={
                        'user': user,
                        'domain': get_current_site(request=request).domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                        'protocol': 'https' if request.is_secure() else 'http',
                    }
                )
                send_mail(
                    subject,
                    message,
                    'settings.EMAIL_HOST_USER',
                    [cd['email']],
                    fail_silently=False,
                )
                return redirect(to=reverse('reset_sent'))
            else:
                return redirect(to=reverse('reset'))
        
        return render(
            request=request,
            template_name='reset/reset.html',
            context={
                'reset_password_form': reset_password_form,
            },
        )
        
        
        
        
        



class UserResetPasswordRequestSentView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request=request,
            template_name='reset/reset-req-sent.html',
            context={},
        )
        
        
        




class UserResetPasswordConfirm(View):
    def get(self, request: HttpRequest, uidb64, token) -> HttpResponse:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user_obj = User.objects.get(pk=uid)
        except:
            user_obj = None
        if (user_obj is not None and account_activation_token.check_token(user_obj, token)):
            form: ResetPasswordConfirmForm = ResetPasswordConfirmForm()
        else:
            messages.error(
                request=request,
                message='توکن شما منقضی شده است',
            )
        return render(
            request=request,
            template_name='reset/reset-confirm.html',
            context={
                'form': form,
                'uidb64': uidb64,
                'token': token,
            },
        )
    
    def post(self, request: HttpRequest, uidb64, token) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse]:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user_obj = User.objects.get(pk=uid)
        except:
            user_obj = None
        if (user_obj is not None and account_activation_token.check_token(user_obj, token)):
            form: ResetPasswordConfirmForm = ResetPasswordConfirmForm(request.POST or None)
            if (form.is_valid()):
                cd = form.cleaned_data
                if (cd['new_password'] != cd['con_new_password']):
                    form.add_error(
                        field='new_password',
                        error='رمز ورود شما با یکدیگر مطابقت ندارد',
                    )
                else:
                    user_obj.set_password(raw_password=cd['new_password'])
                    user_obj.save()
                    return redirect(to=reverse('reset_complete'))
            else:
                form.add_error(
                    field='new_password',
                    error='رمز ورود شما با یکدیگر مطابقت ندارد',
                )
            return render(
                request=request,
                template_name='reset/reset-confirm.html',
                context={
                    'form': form,
                    'uidb64': uidb64,
                    'token': token,
                },
            )
        else:
            messages.error(
                request=request,
                message='توکن شما منقضی شده است',
            )
        return render(
            request=request,
            template_name='reset/reset-confirm.html',
            context={
                'form': form,
                'uidb64': uidb64,
                'token': token,
            },
        )









class UserResetPasswordCompleteView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request=request,
            template_name='reset/reset-complete.html',
            context={},
        )








class UserLoginView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        login_form: LoginForm = LoginForm()
        if (request.user.is_authenticated):
            return redirect(to=reverse('profile'))
        else:
            return render(
            request=request,
            template_name='auth/login.html',
            context={
                'login_form': login_form,
            }
        )
    
    def post(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        login_form: LoginForm = LoginForm(request.POST or None)
        if (login_form.is_valid()):
            cd = login_form.cleaned_data
            user = authenticate(
                request=request,
                username=cd['username'],
                password=cd['password'],
            )
            if (user is not None):
                login(
                    request=request,
                    user=user,
                )
                return redirect(to=reverse('profile'))
            else:
                login_form.add_error(
                    field='username',
                    error='نام کاربری با این مشخصات وجود ندارد',
                )
        return render(
            request=request,
            template_name='auth/login.html',
            context={
                'login_form': login_form,
            },
        )
    
    
    


class UserRegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        register_form: RegisterForm = RegisterForm()
        site_settings: SignUpSettings = SignUpSettings.objects.first()
        if (request.user.is_authenticated):
            return redirect(to=reverse('verify'))
        else:
            return render(
                request=request,
                template_name='index.html',
                context={
                    'register_form': register_form,
                    'settings': site_settings,
                }
            )
    
    def post(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        register_form: RegisterForm = RegisterForm(request.POST or None)
        site_settings: SignUpSettings = SignUpSettings.objects.first()
        if (register_form.is_valid()):
            cd = register_form.cleaned_data
            if (cd['password'] != cd['con_password']):
                register_form.add_error(
                    field='password',
                    error='رمز ورود شما با یکدیگر مطابقت ندارد',
                )
            elif (User.objects.filter(username=cd['username']).exists()):
                register_form.add_error(
                    field='username',
                    error='این نام کاربری قبلا استفاده شده است',
                )
            else:
                user = User.objects.create_user(
                    username=cd['username'],
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    email=cd['email'],
                    password=cd['password'],
                    is_active=False,
                )
                activateEmail(
                    request=request,
                    user=user,
                    to_email=cd['email']
                )
                request.session['state'] = 'False'
                return redirect(to=reverse(viewname='verify'))
        else:
            register_form.add_error(
                field='password',
                error='اطلاعات خواسته شده به درستی وارد نشده',
            )
        return render(
            request=request,
            template_name='index.html',
            context={
                'register_form': register_form,
                'settings': site_settings,
            },
        )
        
        
        
        
                
class UserLogoutView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
        logout(request=request)
        return redirect(to=reverse('login'))