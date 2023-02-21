from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPreference, SavedSearch
from .forms import UserPreferenceForm, SavedSearchForm


@login_required
def user_preferences(request):
    user_preference = UserPreference.objects.filter(user=request.user).first()
    form = UserPreferenceForm(request.POST or None, instance=user_preference)
    if form.is_valid():
        user_preference = form.save(commit=False)
        user_preference.user = request.user
        user_preference.save()
        return redirect('user_preferences')
    return render(request, 'userdashboard/user_preferences.html', {'form': form})


@login_required
def saved_searches(request):
    saved_searches = SavedSearch.objects.filter(user=request.user)
    form = SavedSearchForm(request.POST or None)
    if form.is_valid():
        saved_search = form.save(commit=False)
        saved_search.user = request.user
        saved_search.save()
        return redirect('saved_searches')
    return render(request, 'userdashboard/saved_searches.html', {'saved_searches': saved_searches, 'form': form})
