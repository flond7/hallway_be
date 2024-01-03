from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

# REST FRAMEWORK
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
import json

from django import template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core import serializers

# USER ASK
from django.contrib.auth import get_user_model

# LOGGING
import logging
logger = logging.getLogger(__name__)

#MAIL
from django.core.mail import send_mail
from django.conf import settings

# LOGIN
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# MY VARS
from .constants import MY_CONST
from .modelsConstants import *
from .models import customUser, askUser, PAUser, PAOffice, PACredential
from .forms import customUserForm, askUserForm
from .filters import customUserFilter
from .serializers import UserListSerializer, PAUserPEGSerializer, PAOfficeSerializer, PAOfficeAndPOSerializer, PACredentialSerializer

# CORS
from django.views.decorators.csrf import csrf_exempt


generic_context = {
  'MY_CONST': MY_CONST, 
  'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
  'MAIL_OFFICE_CHOICES': MAIL_OFFICE_CHOICES,
  'LAN_OFFICE_CHOICES':LAN_OFFICE_CHOICES, 'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES, 
  'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 
  'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':SDI_OFFICE_CHOICES,
  'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':ITERATTI_OFFICE_CHOICES,
  'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':ASCOT_OFFICE_CHOICES,
  'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 
  'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
  'SERVSCOL_ROLES_CHOICES':SERVSCOL_ROLES_CHOICES, 
  'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
  'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 
  'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
  'PMPAY_ROLES_CHOICES':PMPAY_ROLES_CHOICES,
  'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 
  'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
  'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 
  'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES, 
  'AMMTRASP_ROLES_CHOICES':AMMTRASP_ROLES_CHOICES,
  'MEPA_ROLES_CHOICES':MEPA_ROLES_CHOICES, 
  'AGENTR_ROLES_CHOICES':AGENTR_ROLES_CHOICES,
  'OSSERVATORIO_ROLES_CHOICES':OSSERVATORIO_ROLES_CHOICES,
}


@login_required
@permission_required('api.view_customuser', raise_exception=True)
def user_overview(request):
    #custom css for avatar
    cssPage = 'avatar me-3'
    userList = customUser.objects.all().order_by('name')

    # if the dictionary has some values the boolean is true, otherwise false
    if bool(request.GET):
      user_filter = customUserFilter(request.GET, queryset=userList)
      # get params from url
      name = request.GET.get('name')
      surname = request.GET.get('surname')
      office = request.GET.get('office')
      active = request.GET.get('active')
      employed = request.GET.get('employed')

      # ATTENTION: django-filters puts the result inside a qs so you have to pass user_filter.qs
      return render(request, 'user_overview.html', {
        'userList': user_filter.qs, 
        'cssPage':cssPage,
        'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 'url_office':office, 'surname':surname,'name':name })
    else:
      return render(request, 'user_overview.html', {'userList': userList, 
        'cssPage':cssPage,
        'MY_CONST': MY_CONST, 'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES}) 

@login_required
@permission_required('customuser.add_choice', raise_exception=True)
def user_create(request):
    submitted = False
    cu = customUserForm()
    generic_context['form'] = cu
    generic_context['submitted'] = submitted     
    if request.method == "POST":
        cu = customUserForm(request.POST)
        if cu.is_valid():
            cu.save()
            return HttpResponseRedirect('user_profile/'+cu.id)           
    return render(request, 'user_create.html', generic_context)

    """ if request.method == "POST":
        cu = customUserForm(request.POST)
        if cu.is_valid():
            cu.save()
            return HttpResponseRedirect('user_create?submitted=True')
        else:
            generic_context['form'] = cu
            generic_context['submitted'] = submitted
            render(request, 'user_create.html', generic_context)
    else:
        cu = customUserForm()
        if 'submitted' in request.GET:
            submitted = True
    generic_context['form'] = cu
    generic_context['submitted'] = submitted        
    return render(request, 'user_create.html', generic_context) """

@login_required
@permission_required('customuser.add_choice', raise_exception=True)
def user_edit(request, pk):
    submitted = request.GET.get('submitted')
    u = customUser.objects.get(id=pk)

    # MAIL iterate the office to check the selected ones
    checked_mail_offices = list(MAIL_OFFICE_CHOICES)
    for i in range(len(MAIL_OFFICE_CHOICES)):
      checked_mail_offices[i] = list(checked_mail_offices[i])
      if MAIL_OFFICE_CHOICES[i][0] in u.mailOffice:
        checked_mail_offices[i].append('checked')
      else:
        checked_mail_offices[i].append('unchecked')
    
    # LAN iterate the office to check the selected ones
    checked_lan_offices = list(LAN_OFFICE_CHOICES)
    for i in range(len(LAN_OFFICE_CHOICES)):
      checked_lan_offices[i] = list(checked_lan_offices[i])
      if LAN_OFFICE_CHOICES[i][0] in u.lanOffice:
        checked_lan_offices[i].append('checked')
      else:
        checked_lan_offices[i].append('unchecked')

    # ADWEB iterate the office to check the selected ones
    checked_adweb_offices = list(ADWEB_OFFICE_CHOICES)
    for i in range(len(ADWEB_OFFICE_CHOICES)):
      checked_adweb_offices[i] = list(checked_adweb_offices[i])
      if ADWEB_OFFICE_CHOICES[i][0] in u.adwebOffice:
        checked_adweb_offices[i].append('checked')
      else:
        checked_adweb_offices[i].append('unchecked')

    # ASCOT iterate the office to check the selected ones
    checked_ascot_offices = list(ASCOT_OFFICE_CHOICES)
    for i in range(len(ASCOT_OFFICE_CHOICES)):
      checked_ascot_offices[i] = list(checked_ascot_offices[i])
      if ASCOT_OFFICE_CHOICES[i][0] in u.ascotOffice:
        checked_ascot_offices[i].append('checked')
      else:
        checked_ascot_offices[i].append('unchecked')

    # SDI iterate the office to check the selected ones
    checked_sdi_offices = list(SDI_OFFICE_CHOICES)
    for i in range(len(SDI_OFFICE_CHOICES)):
      checked_sdi_offices[i] = list(checked_sdi_offices[i])
      if SDI_OFFICE_CHOICES[i][0] in u.sdiOffice:
        checked_sdi_offices[i].append('checked')
      else:
        checked_sdi_offices[i].append('unchecked')

    # ITERATTI iterate the office to check the selected ones
    checked_iteratti_offices = list(ITERATTI_OFFICE_CHOICES)
    for i in range(len(ITERATTI_OFFICE_CHOICES)):
      checked_iteratti_offices[i] = list(checked_iteratti_offices[i])
      if ITERATTI_OFFICE_CHOICES[i][0] in u.iterattiOffice:
        checked_iteratti_offices[i].append('checked')
      else:
        checked_iteratti_offices[i].append('unchecked')

    if request.method == "POST":

        #u.save()
        cu = customUserForm(request.POST)

        if cu.is_valid():
            cu.save()
            print("VALID")
            return HttpResponseRedirect('profile.html')
        else:
            print("PRINT")
    else:
        cu = customUserForm()
        return render(request, 'user_create.html', {'u':u, 'submitted': submitted, 'MY_CONST': MY_CONST, 
        'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
        'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES,'LAN_OFFICE_CHOICES':checked_lan_offices, 
        'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': checked_adweb_offices, 
        'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':checked_sdi_offices,
        'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':checked_iteratti_offices,
        'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':checked_ascot_offices,
        'MAIL_OFFICE_CHOICES': checked_mail_offices,
        'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
        'SERVSCOL_ROLES_CHOICES': SERVSCOL_ROLES_CHOICES, 'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
        'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
        'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
        'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES, 'AMMTRASP_ROLES_CHOICES':AMMTRASP_ROLES_CHOICES,
        'MEPA_ROLES_CHOICES':MEPA_ROLES_CHOICES, 'AGENTR_ROLES_CHOICES':AGENTR_ROLES_CHOICES})

def iterateOffices(selectedField, officeList):
    # MAIL iterate the office to check the selected ones
    checked_offices = list(officeList)
    for i in range(len(officeList)):
      checked_offices[i] = list(checked_offices[i])
      if officeList[i][0] in selectedField:
        checked_offices[i].append('checked')
      else:
        checked_offices[i].append('unchecked')
    return checked_offices

def checkOffices(request, selectedField, officeList):
    print(request)
    print("REQUEST SOPRA")
    checked_offices =[]
    for i in range(len(officeList)):
      #checked_offices[i] = list(checked_offices[i])
      if officeList[i][0] in request:
        print('officeList[i][0]')
        print(officeList[i][0])
        checked_offices.append(officeList[i][1])
    print(checked_offices)
    return checked_offices

# function for a separated create/edit page
def user_update(request, pk):
    submitted = request.GET.get('submitted')
    u = customUser.objects.get(id=pk)
    cssPage = "w-100 border-radius-lg shadow-sm"

    checked_mail_offices = iterateOffices(u.mailOffice, MAIL_OFFICE_CHOICES)
    checked_lan_offices = iterateOffices(u.lanOffice, LAN_OFFICE_CHOICES)
    checked_adweb_offices = iterateOffices(u.adwebOffice, ADWEB_OFFICE_CHOICES)
    checked_ascot_offices = iterateOffices(u.ascotOffice, ASCOT_OFFICE_CHOICES)
    checked_sdi_offices = iterateOffices(u.sdiOffice, SDI_OFFICE_CHOICES)
    checked_iteratti_offices = iterateOffices(u.iterattiOffice, ITERATTI_OFFICE_CHOICES)

    # prepare the new generic_context
    generic_context['u'] = u
    #generic_context['form'] = cu
    generic_context['submitted'] = submitted
    generic_context['cssPage'] = cssPage
    generic_context['LAN_OFFICE_CHOICES'] = checked_lan_offices
    generic_context['ADWEB_OFFICE_CHOICES'] = checked_adweb_offices
    generic_context['SDI_OFFICE_CHOICES'] = checked_sdi_offices
    generic_context['ITERATTI_OFFICE_CHOICES'] = checked_iteratti_offices
    generic_context['ASCOT_OFFICE_CHOICES'] = checked_ascot_offices
    generic_context['MAIL_OFFICE_CHOICES'] = checked_mail_offices

    # if I'm sending a post request it means I want to save
    if request.method == "POST":
        cu = customUserForm(request.POST)
        print("POST")
        submitted = True
        # fetch the object related to passed id
        obj = get_object_or_404(customUser, id = pk)
        
        # pass the object as instance in form
        cu = customUserForm(request.POST or None, instance = obj)
        generic_context['form'] = cu

        if cu.is_valid():
            print('form VALID')
            cu.save()
            u = customUser.objects.get(id=pk)
            return render(request, 'profile.html', generic_context)
            
        else:
          print('form is not valid')
          print(cu.errors)
          return render(request, 'user_update.html', generic_context)


          return render(request, 'user_update.html', {
        'u':u, 'form': cu, 'submitted': submitted, 'MY_CONST': MY_CONST, 
        'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
        'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES,'LAN_OFFICE_CHOICES':checked_lan_offices, 
        'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': checked_adweb_offices, 
        'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':checked_sdi_offices,
        'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':checked_iteratti_offices,
        'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':checked_ascot_offices,
        'MAIL_OFFICE_CHOICES': checked_mail_offices,
        'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 
        'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
        'SERVSCOL_ROLES_CHOICES': SERVSCOL_ROLES_CHOICES, 
        'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
        'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 
        'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
        'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 
        'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
        'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 
        'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES, 
        'AMMTRASP_ROLES_CHOICES':AMMTRASP_ROLES_CHOICES,
        'MEPA_ROLES_CHOICES':MEPA_ROLES_CHOICES, 
        'AGENTR_ROLES_CHOICES':AGENTR_ROLES_CHOICES})
    
    # if I just want to visualize the page with a GET request
    else:
        cu = customUserForm()
        return render(request, 'user_update.html', generic_context)

        return render(request, 'user_update.html', {
        'u':u, 'submitted': submitted, 'MY_CONST': MY_CONST, 
        'MAIN_OFFICE_CHOICES': MAIN_OFFICE_CHOICES, 
        'LAN_ROLES_CHOICES':LAN_ROLES_CHOICES,'LAN_OFFICE_CHOICES':checked_lan_offices, 
        'ADWEB_ROLES_CHOICES':ADWEB_ROLES_CHOICES,'ADWEB_OFFICE_CHOICES': checked_adweb_offices, 
        'SDI_ROLES_CHOICES': SDI_ROLES_CHOICES,'SDI_OFFICE_CHOICES':checked_sdi_offices,
        'ITERATTI_ROLES_CHOICES':ITERATTI_ROLES_CHOICES, 'ITERATTI_OFFICE_CHOICES':checked_iteratti_offices,
        'ASCOT_ROLES_CHOICES':ASCOT_ROLES_CHOICES, 'ASCOT_OFFICE_CHOICES':checked_ascot_offices,
        'MAIL_OFFICE_CHOICES': checked_mail_offices,
        'BOXAPP_ROLES_CHOICES':BOXAPP_ROLES_CHOICES, 
        'WEBSITE_ROLES_CHOICES':WEBSITE_ROLES_CHOICES, 
        'SERVSCOL_ROLES_CHOICES': SERVSCOL_ROLES_CHOICES, 
        'CRM_ROLES_CHOICES':CRM_ROLES_CHOICES,
        'AVCP_ROLES_CHOICES':AVCP_ROLES_CHOICES, 
        'FVGPAY_ROLES_CHOICES':FVGPAY_ROLES_CHOICES,
        'SUE_ROLES_CHOICES':SUE_ROLES_CHOICES, 
        'SUAP_ROLES_CHOICES':SUAP_ROLES_CHOICES,
        'MASTERDATA_ROLES_CHOICES':MASTERDATA_ROLES_CHOICES, 
        'ALBOPRET_ROLES_CHOICES': ALBOPRET_ROLES_CHOICES, 
        'AMMTRASP_ROLES_CHOICES':AMMTRASP_ROLES_CHOICES,
        'MEPA_ROLES_CHOICES':MEPA_ROLES_CHOICES, 
        'AGENTR_ROLES_CHOICES':AGENTR_ROLES_CHOICES})

@permission_required('api.add_askuser', raise_exception=True)
def user_ask(request):
    au = askUserForm()
    user = request.user
    # find and use the username
    generic_context['username'] = user.get_username()
    # if I want to send the request
    if request.method == "POST":
        au = askUserForm(request.POST)
        if au.is_valid():
            send_mail(
            subject='Richiesta nuovo utente',
            message = '',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list= [settings.RECIPIENT_ADDRESS] )
            au.save()
            print('mail sent')
            return render(request,'user_ask.html')
        else:
            generic_context['form'] = au
            print('FORM INVALID')
            return render(request, 'user_ask.html', generic_context)

    # if I just want to see the form
    else:
        generic_context['form'] = au
        return render(request, 'user_ask.html', generic_context)


def index(request):
    userList = customUser.objects.all()
    return render(request, 'index.html', {'userList': userList, 'MY_CONST': MY_CONST})

@api_view(['GET'])
def info(request):
    return render(request, 'account_info.html', {'MY_CONST': MY_CONST})

@api_view(['GET'])
def profile(request, pk):
  #custom css for avatar
  cssPage = "w-100 border-radius-lg shadow-sm"
  u = customUser.objects.get(id=pk)
  return render(request, 'profile.html', {'u': u,  'cssPage':cssPage, 'MY_CONST': MY_CONST, 
  'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES, 'ITERATTI_OFFICE_CHOICES': ITERATTI_OFFICE_CHOICES })

@api_view(['GET'])
def adweb(request):
  #custom css for avatar
  cssPage = 'avatar me-3'
  u = customUser.objects.all()
  return render(request, 'adweb.html', {'userList': u, 'cssPage':cssPage, 'MY_CONST': MY_CONST, 'ADWEB_OFFICE_CHOICES': ADWEB_OFFICE_CHOICES })

@api_view(['GET'])
def iteratti(request):
  #custom css for avatar
  cssPage = 'avatar me-3'
  u = customUser.objects.all()
  return render(request, 'iteratti.html', {'userList': u, 'cssPage':cssPage, 'MY_CONST': MY_CONST, 'ITERATTI_OFFICE_CHOICES': ITERATTI_OFFICE_CHOICES })

@api_view(['GET'])
def sdi(request):
  #custom css for avatar
  cssPage = 'avatar me-3'
  u = customUser.objects.all()
  return render(request, 'sdi.html', {'userList': u, 'cssPage':cssPage, 'MY_CONST': MY_CONST, 'SDI_OFFICE_CHOICES': SDI_OFFICE_CHOICES })




# BE SIMPLE API
@api_view(['GET'])
def user_list(request):
    userList = customUser.objects.all().order_by('name')
    serializer = UserListSerializer(userList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def office_list(request):
    return Response(MAIN_OFFICE_CHOICES)


# NEW VERSION
def pauser_list(request):
  if request.method == "GET":
    PAUserList = PAUser.objects.all()
    serializer = PAUserPEGSerializer(PAUserList, many=True)
    data = {'data': serializer.data, 'status': 201}
  return JsonResponse(data, status=201)


def pauser_po_list(request):
  if request.method == "GET":
    PAUserList = PAUser.objects.filter(manager = True)
    serializer = PAUserPEGSerializer(PAUserList, many=True)
    data = {'data': serializer.data, 'status': 201}
  return JsonResponse(data, status=201)

def user_constants_list(request):
  if request.method == "GET":
    constants = {
        'main_office_choices': MAIN_OFFICE_CHOICES,
    }
  return JsonResponse(constants, status=201)

def paoffice_list(request):
  if request.method == "GET":
    PAOfficeList = PAOffice.objects.all()
    serializer = PAOfficeSerializer(PAOfficeList, many=True)
    data = {'data': serializer.data, 'status': 201}
  return JsonResponse(data, status=201)

def paoffice_and_po_list(request):
  if request.method == "GET":
    PAOfficeList = PAOffice.objects.all()
    serializer = PAOfficeAndPOSerializer(PAOfficeList, many=True)
    data = {'data': serializer.data, 'status': 201}
  return JsonResponse(data, status=201)




@csrf_exempt
def get_user_pacredential(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            idPerson = data['id']
            credentialList = PACredential.objects.filter(
                user__id=idPerson,
            )
            serializer = PACredentialSerializer(credentialList, many=True)
            return JsonResponse({"data": serializer.data}, status=200)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {e}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)