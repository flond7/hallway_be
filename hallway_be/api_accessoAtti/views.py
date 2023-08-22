from django.shortcuts import render

# Create your views here.
def access_create(request):
    return True
    """ submitted = False
    cu = customUserForm()
    generic_context['form'] = cu
    generic_context['submitted'] = submitted     
    if request.method == "POST":
        cu = customUserForm(request.POST)
        if cu.is_valid():
            cu.save()
            return HttpResponseRedirect('user_profile/'+cu.id)           
    return render(request, 'user_create.html', generic_context) """