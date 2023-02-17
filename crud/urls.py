from django.contrib import admin
from django.urls import path, include
from gastos.views import contas, nova_conta, atualizacao, deletar

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('gastos/', include('gastos.urls')),
    #path('contas/', contas.view, name="contas"),
    path('contas/', contas, name="contas"),
    path('nova/', nova_conta, name="nova_conta"),
    path('atualiza_conta/<int:pk>/', atualizacao, name="atualiza_conta"),
    path('deletar_conta/<int:pk>/', deletar, name="deletar_conta"),
]
 