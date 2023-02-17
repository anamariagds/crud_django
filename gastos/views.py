from django.shortcuts import redirect, render, HttpResponse
from .models import Conta
from .forms import contasForm

def contas(request):
    contas = Conta.objects.all()
    return render(request, 'gastos/home.html', {'contas': contas})

def nova_conta(request):
    form = contasForm(request.POST or None) #instancia do formulario
    if form.is_valid():
        form.save()
        return redirect('contas') #redirect evita repetir
    
    return render(request, 'gastos/nova_conta.html', {'form': form})

def atualizacao(request, pk):
    gasto = Conta.objects.get(pk=pk)
    form = contasForm(request.POST or None, instance=gasto)

    if form.is_valid():
        form.save()
        return redirect('contas') #redirect evita repetir
        
    return render(request, 'gastos/nova_conta.html', {'form': form, 
                                                      'gasto': gasto})

def deletar(request, pk):
    gasto = Conta.objects.get(pk=pk)
    gasto.delete()
    return redirect('contas')
