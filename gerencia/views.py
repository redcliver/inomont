from django.shortcuts import render
from website.models import funcaoModel, cadastroSite, fornecedorModel, colaboradorModel
import datetime
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/home.html', {'title':'Home', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradores(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            return render (request, 'gerencia/colaboradores/home.html', {'title':'Home', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradoresNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('nome') != None:
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
                novoColaborador = cadastroSite(nome=nome, 
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
                novoColaborador.save()
                msgConfirmacao = "Colaborador salvo com sucesso!"
                return render (request, 'gerencia/colaboradores/colaboradorNovo.html', {'title':'Novo Colaborador', 
                                                                                        'msgTelaInicial':msgTelaInicial,
                                                                                        'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/colaboradores/colaboradorNovo.html', {'title':'Novo Colaborador', 
                                                                                    'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradoresVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name()
            colaboradoresCadastrados = colaboradorModel.objects.all().order_by('funcao')
 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('colaboradorID') != None:
                colaboradorID = request.POST.get('colaboradorID')
                colaboradorObj = colaboradorModel.objects.filter(id=colaboradorID).get()
                return render (request, 'gerencia/colaboradores/colaboradorVisualizar1.html', {'title':'Visualizar Colaborador', 
                                                                                            'msgTelaInicial':msgTelaInicial,
                                                                                            'colaboradorObj':colaboradorObj})            
                
            return render (request, 'gerencia/colaboradores/colaboradorVisualizar.html', {'title':'Visualizar Colaborador', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'colaboradoresCadastrados':colaboradoresCadastrados})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradoresSite(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            colaboradoresSite = cadastroSite.objects.filter(estado=1).all().order_by('dataCadastro')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/colaboradores/colaboradorSite.html', {'title':'Colaboradores Site', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'colaboradoresSite':colaboradoresSite})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradoresSiteVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name()
            colaboradoresSite = cadastroSite.objects.all().order_by('funcao')
 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()

            if request.method == "POST" and request.POST.get('colaboradorID') != None:
                colaboradorID = request.POST.get('colaboradorID')
                colaboradorObj = cadastroSite.objects.all().filter(id=colaboradorID).get()
                return render (request, 'gerencia/colaboradores/colaboradorSiteVisualizar.html', {'title':'Visualizar Colaborador', 
                                                                                            'msgTelaInicial':msgTelaInicial,
                                                                                            'colaboradorObj':colaboradorObj})            
                
            return render (request, 'gerencia/colaboradores/colaboradorSiteVisualizar.html', {'title':'Visualizar Colaborador', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'colaboradoresSite':colaboradoresSite,
                                                            'colaboradorObj':colaboradorObj})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def fornecedores(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/fornecedores/home.html', {'title':'Home', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def fornecedoresNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST":
                nome = request.POST.get('nome')
                contatoPrincipal = request.POST.get('contatoPrincipal')
                email = request.POST.get('email')
                cnpj = request.POST.get('cnpj')
                cep = request.POST.get('cep')
                telefone = request.POST.get('telefone')
                celular = request.POST.get('celular')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidade = request.POST.get('cidade')
                uf = request.POST.get('uf')
                fornecedorObj = fornecedorModel(nome=nome, contatoPrincipal=contatoPrincipal, email=email, cnpj=cnpj, telefone=telefone, celular=celular, cep=cep, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, uf=uf)
                fornecedorObj.save()
                msgConfirmacao = "Fornecedor salvo com sucesso!"
                return render (request, 'gerencia/fornecedores/fornecedorNovo.html', {'title':'Novo Fornecedor', 
                                                                                      'msgTelaInicial':msgTelaInicial,
                                                                                      'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/fornecedores/fornecedorNovo.html', {'title':'Novo Fornecedor', 
                                                                                  'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def fornecedoresVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            fornecedores = fornecedorModel.objects.all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('fornecedorID') != None:
                fornecedorID = request.POST.get('fornecedorID')
                fornecedorObj = fornecedorModel.objects.filter(id=fornecedorID).get()
                  
                return render (request, 'gerencia/fornecedores/fornecedorVisualizar1.html', {'title':'Visualizar Fornecedor', 
                                                                                            'msgTelaInicial':msgTelaInicial,
                                                                                            'fornecedorObj':fornecedorObj})
            return render (request, 'gerencia/fornecedores/fornecedorVisualizar.html', {'title':'Visualizar Fornecedor', 
                                                                                        'msgTelaInicial':msgTelaInicial,
                                                                                        'fornecedores':fornecedores})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def fornecedoresEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            fornecedores = fornecedorModel.objects.all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('fornecedorID') != None:
                fornecedorID = request.POST.get('fornecedorID')
                fornecedorObj = fornecedorModel.objects.filter(id=fornecedorID).get()
                  
                return render (request, 'gerencia/fornecedores/fornecedorEditar.html', {'title':'Editar Fornecedor', 
                                                                                            'msgTelaInicial':msgTelaInicial,
                                                                                            'fornecedorObj':fornecedorObj})
            return render (request, 'gerencia/fornecedores/fornecedorVisualizar.html', {'title':'Visualizar Fornecedor', 
                                                                                        'msgTelaInicial':msgTelaInicial,
                                                                                        'fornecedores':fornecedores})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def fornecedoresSalvar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST":
                fornecedorID = request.POST.get('fornecedorID')
                fornecedorObj = fornecedorModel.objects.filter(id=fornecedorID).get()
                nome = request.POST.get('nome')
                contatoPrincipal = request.POST.get('contatoPrincipal')
                email = request.POST.get('email')
                cnpj = request.POST.get('cnpj')
                cep = request.POST.get('cep')
                telefone = request.POST.get('telefone')
                celular = request.POST.get('celular')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidade = request.POST.get('cidade')
                uf = request.POST.get('uf')
                fornecedorObj.nome = nome
                fornecedorObj.contatoPrincipal = contatoPrincipal
                fornecedorObj.email = email
                fornecedorObj.cnpj = cnpj
                fornecedorObj.cep = cep
                fornecedorObj.telefone = telefone
                fornecedorObj.celular = celular
                fornecedorObj.endereco = endereco
                fornecedorObj.numero = numero
                fornecedorObj.bairro = bairro
                fornecedorObj.cidade = cidade
                fornecedorObj.uf = uf
                fornecedorObj.save()
                msgConfirmacao = "Fornecedor editado com sucesso!"
                return render (request, 'gerencia/fornecedores/fornecedorEditar.html', {'title':'Editar Fornecedor', 
                                                                                      'msgTelaInicial':msgTelaInicial,
                                                                                      'msgConfirmacao':msgConfirmacao,
                                                                                      'fornecedorObj':fornecedorObj})
            return render (request, 'gerencia/fornecedores/fornecedorNovo.html', {'title':'Novo Fornecedor', 
                                                                                  'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def funcaoHome(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/funcoes/home.html', {'title':'Funeções', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def funcaoNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('nome'):
                nome = request.POST.get('nome')
                observacao = request.POST.get('observacao')
                novaFuncao = funcaoModel(nome=nome, observacao=observacao)
                novaFuncao.save()
                msgConfirmacao = "Nova função cadastrada com sucesso!"
                return render (request, 'gerencia/funcoes/funcaoNovo.html', {'title':'Nova Função', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/funcoes/funcaoNovo.html', {'title':'Nova Função', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def funcaoVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            funcoes = funcaoModel.objects.all().order_by('id')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('funcaoID'):
                funcaoID = request.POST.get('funcaoID')
                funcaoObj = funcaoModel.objects.filter(id=funcaoID).get()
                return render (request, 'gerencia/funcoes/funcaoEditar.html', {'title':'Editar Função', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'funcaoObj':funcaoObj})
            return render (request, 'gerencia/funcoes/funcaoVisualizar.html', {'title':'Visualizar Função', 
                                                                               'msgTelaInicial':msgTelaInicial,
                                                                               'funcoes':funcoes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def funcaoSalvar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            funcoes = funcaoModel.objects.all().order_by('id')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('funcaoID'):
                funcaoID = request.POST.get('funcaoID')
                funcaoObj = funcaoModel.objects.filter(id=funcaoID).get()
                nome = request.POST.get('nome')
                observacao = request.POST.get('observacao')
                funcaoObj.nome = nome
                funcaoObj.observacao = observacao
                funcaoObj.save()
                msgConfirmacao = "Função editada com sucesso!"
                return render (request, 'gerencia/funcoes/funcaoVisualizar.html', {'title':'Visualizar Função', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'funcoes':funcoes,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/funcoes/funcaoVisualizar.html', {'title':'Visualizar Função', 
                                                                               'msgTelaInicial':msgTelaInicial,
                                                                               'funcoes':funcoes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})