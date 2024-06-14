from django.urls import include, path
from api.views import RegisterView, ExpenseListCreateView, ExpenseDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', RegisterView.as_view(), name='account-register'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)