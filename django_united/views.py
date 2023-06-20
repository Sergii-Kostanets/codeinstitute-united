from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AccountSettingsForm


@login_required
def account_settings(request):
    form = AccountSettingsForm(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('game_list')
        else:
            messages.error(request, 'Error updating account.')

    return render(request, 'account_settings.html', {'form': form})
