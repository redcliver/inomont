from django.shortcuts import render
from .models import cadastroSite, funcaoModel

# Create your views here.
def home(request):
    colabRegistrados = 156
    colabTrabalhando = 64
    trabRealizado = 123
    todasFuncoes = funcaoModel.objects.all().order_by('nome')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        dataNasc = request.POST.get('dataNasc')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        telefone = request.POST.get('telefone')
        estadoCivil = request.POST.get('estadoCivil')
        funcaoID = request.POST.get('funcaoID')
        tempoExperiencia = request.POST.get('tempoExperiencia')
        escolaridade = request.POST.get('escolaridade')
        resideEmTresLagoas = request.POST.get('resideEmTresLagoas')
        trabalhouInomont = request.POST.get('trabalhouInomont')
        pqInomont = request.POST.get('pqInomont')
        empresa1 = request.POST.get('empresa1')
        funcao1 = request.POST.get('funcao1')
        periodo1 = request.POST.get('periodo1')
        empresa2 = request.POST.get('empresa2')
        funcao2 = request.POST.get('funcao2')
        periodo2 = request.POST.get('periodo2')
        empresa3 = request.POST.get('empresa3')
        funcao3 = request.POST.get('funcao3')
        periodo3 = request.POST.get('periodo3')
        funcaoObj = funcaoModel.objects.filter(id=funcaoID).get()
        novo_site = cadastroSite(nome=nome, 
                                 sobrenome=sobrenome, 
                                 telefone=telefone, 
                                 celular=celular,
                                 cpf=cpf,
                                 rg=rg,
                                 dataNasc=dataNasc,
                                 email=email,
                                 estadoCivil=estadoCivil,
                                 escolaridade=escolaridade,
                                 ehDeTresLagoas=resideEmTresLagoas,
                                 trabalhouInomont=trabalhouInomont,
                                 pqInomont=pqInomont,
                                 experiencia=tempoExperiencia,
                                 funcao=funcaoObj,
                                 empresa1=empresa1,
                                 funcao1=funcao1,
                                 periodo1=periodo1,
                                 empresa2=empresa2,
                                 funcao2=funcao2,
                                 periodo2=periodo2,
                                 empresa3=empresa3,
                                 funcao3=funcao1,
                                 periodo3=periodo3)
        novo_site.save()
        msgConfirmacao = "O seu cadastro foi realizado com sucesso!"
        return render(request, 'site/home.html', {'title':'Home',
                                                  'colabRegistrados':colabRegistrados,
                                                  'colabTrabalhando':colabTrabalhando,
                                                  'trabRealizado':trabRealizado,
                                                  'msgConfirmacao':msgConfirmacao,
                                                  'todasFuncoes':todasFuncoes})
    return render(request, 'site/home.html', {'title':'Home',
                                              'colabRegistrados':colabRegistrados,
                                              'colabTrabalhando':colabTrabalhando,
                                              'trabRealizado':trabRealizado,
                                              'todasFuncoes':todasFuncoes})


def proposta(request):
    return render(request, 'site/proposta.html')