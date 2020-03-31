from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

import send_email.helper as hpr


def home(request):
    context = hpr.initialize_context(request)
    return render(request, 'home.html', context)


def sign_in(request):
    sign_in_url, state = hpr.get_sign_in_url()

    # state is used to valid the call back, now we save it into session
    request.session['auth_state'] = state

    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(sign_in_url)


def callback(request):
    expected_state = request.session.pop('auth_state', '')
    token = hpr.get_token_from_code(request.get_full_path(), expected_state)

    user = hpr.get_user(token)

    # Save token and user
    hpr.store_token(request, token)
    hpr.store_user(request, user)

    return HttpResponseRedirect(reverse('home'))


def sign_out(request):
    # Clear out the user and token
    hpr.remove_user_and_token(request)

    return HttpResponseRedirect(reverse('home'))


def customers(request):
    context = hpr.initialize_context(request)
    clients = hpr.get_clients_from_file()
    context['clients'] = clients
    return render(request, 'clients.html', context)


def email(request):
    hpr.send_emails(hpr.get_token(request))

    return HttpResponseRedirect(reverse('customers'))

