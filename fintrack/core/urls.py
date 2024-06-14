from django.urls import path, include
from core.views import ProfileView, ExpenseCreateView, EditProfileView, ExpensesListView, ExpenseSearchView, \
    HomeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('account/', include('allauth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/expenses', ExpensesListView.as_view(), name='expenses'),
    path('profile/expenses/search', ExpenseSearchView.as_view(), name='expense_search'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense_create'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)