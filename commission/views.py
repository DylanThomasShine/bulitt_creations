from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render

from .models import Commission
from .forms import CommissionForm

def commission(request):
    template = "commission/commission.html"

    if request.method == "POST":
        form = CommissionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "commission/confirmation.html")

    else:
        form = CommissionForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


# Request a Creation
@login_required
def add_commission(request):
    """ Request a Commission from the store """

    form = CommissionForm()(request.POST, request.FILES)

    if request.method == 'POST':
        
        if form.is_valid():
            #commission = form.save()
            messages.success(request, 'Successfully requested creation!')
            #return redirect(reverse('commission_detail', args=[commission.first_name]))
        else:
            messages.error(request, 'Failed to request product. Please ensure the form is valid.')
    else:
        form = CommissionForm()

    template = 'commission/commission.html'
    context = {
        'form': form,
    }

    return render(request, template, context)    