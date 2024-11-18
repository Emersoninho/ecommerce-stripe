from django.shortcuts import render
from django.contrib.auth.models import User

def vendor_details(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_details.html', {'user': user})