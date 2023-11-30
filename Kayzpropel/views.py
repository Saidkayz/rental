import base64
import json

import requests
from django.shortcuts import render, redirect,get_object_or_404
from Kayzpropel.models import Member, Property, Transactions
from Kayzpropel.forms import PropertyForm, ProfileForm
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from Kayzpropel.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword


# create your views here
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        email=request.POST['email'], username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def pricing(request):
    return render(request, 'pricing.html')


def faq(request):
    return render(request, 'faq.html')


def add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/showimage")
    else:
        form = PropertyForm()
    return render(request, 'add-property.html', {'form': form})


# def update(request, id):
#     property = Property.objects.get(id=id)
#     form = PropertyForm(request.POST, instance=property)
#     print(id)
#     if form.is_valid():
#         form.save()
#         return redirect('/image')
#     else:
#         return render(request, 'edit.html', {'property': property})

def print_page(request):
    # Retrieve data or perform any necessary logic here
    context = {
        'data': 'This is the data to be printed on the page',  # Add your data here
    }

    # Render a template with the provided context
    return render(request, 'invoice.html', context)

def update(request, id):
    instance = get_object_or_404(Property, id=id)  # Get the object to update
    print(id)

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
            # Redirect to a success page or do something else upon successful update
    else:
        form = PropertyForm(instance=instance)

    return render(request, 'edit.html', {'form': form})

def update_profile(request, id):
    member = Member.objects.get(id=id)
    form = ProfileForm(request.POST, instance=member)
    if form.is_valid():
        form.save()
        return redirect('/profile')
    else:
        return render(request, 'edit.html', {'profile': profile})


def show_property(request):
    images = Property.objects.all()
    return render(request, 'show_property.html', {'images': images})


def show_profile(request):
    members = Member.objects.all()
    return render(request, 'dashboard-profile.html', {'members': members})



def imagedelete(request, id):
    image = Property.objects.get(id=id)
    image.delete()
    return redirect('/showimage')


def printinvoice(request):
    return render(request, 'invoice.html')


def agency(request):
    return render(request, 'agency.html')


def index2(request):
    return render(request, 'index2.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')


def site(request):
    return render(request, 'sitemap.html')


def agencysingle(request):
    return render(request, 'agency-single.html')


def agentlist(request):
    return render(request, 'agent-list.html')


def agentsingle(request):
    return render(request, 'agent-single.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def blog1(request):
    return render(request, 'blog-v1.html')


def blog2(request):
    return render(request, 'blog-v2.html')


def blog3(request):
    return render(request, 'blog-v3.html')


def compare(request):
    return render(request, 'compare.html')


def categories(request):
    return render(request, 'dashboard-categories.html')


def favorite(request):
    return render(request, 'dashboard-favorite.html')


def message(request):
    return render(request, 'dashboard-message.html')


def order(request):
    return render(request, 'dashboard-order.html')


def package(request):
    return render(request, 'dashboard-package.html')


def profile(request):
    return render(request, 'dashboard-profile.html')


def review(request):
    return render(request, 'dashboard-review.html')


def savesearch2(request):
    return render(request, 'dashboard-save-search.html')


def savesearch(request):
    return render(request, 'dashboard-savesearch.html')


def error(request):
    return render(request, 'error.html')


def griddefault(request):
    return render(request, 'grid-default.html')


def property1col(request):
    return render(request, 'property-1-col.html')


def property2col(request):
    return render(request, 'property-2-col.html')


def banner(request):
    return render(request, 'banner.html')


def half1(request):
    return render(request, 'property-half1-map.html')


def half2(request):
    return render(request, 'property-half2-map.html')


def mapheaderstyle(request):
    return render(request, 'property-header-map.html')


def list(request):
    return render(request, 'property-list.html')


def listall(request):
    return render(request, 'property-list-all.html')


def single(request):
    return render(request, 'property-single-v1.html')


def single2(request):
    return render(request, 'property-single-v2.html')


def single3(request):
    return render(request, 'property-single-v3.html')


def cart(request):
    return render(request, 'shop-cart.html')


def ui(request):
    return render(request, 'ui-element.html')

def pay(request):
    return render(request, 'paymembership.html')
def token(request):
    consumer_key = '6tfEP6dTGGVNZTmfi4A8qXGTMqozqX43'
    consumer_secret = '27TzlY0zA2rgGIoQ'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Kayzpropel Company",
            "TransactionDesc": "Rent charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        # transaction_data(request, response)
        # print(request)
        return HttpResponse("success")

# def transaction_data(request, response):
#     # if request.method == 'POST':
#     #     transaction = Transactions(amount=request.POST[request['Amount']], phone_number=request.POST[request['PhoneNumber']],
#     #                     transaction_date=request.POST[request['Timestamp']],)
#     #     transaction.save()
#     #     return redirect('/')
#
#     if 'Amount' in request.POST and 'PhoneNumber' in request.POST and 'Timestamp' in request.POST:
#         transaction = Transactions(
#             amount=request.POST['Amount'],
#             phone_number=request.POST['PhoneNumber'],
#             transaction_date=request.POST['Timestamp'],
#         )
#         transaction.save()
#         return redirect('/')
#     else:
#     # Handle missing POST data accordingly
#
#         print(request)
#

