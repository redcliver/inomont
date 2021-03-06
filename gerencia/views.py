from django.shortcuts import render
from website.models import funcaoModel, cadastroSite, fornecedorModel, colaboradorModel, clienteModel, contaPagarModel, contaReceberModel
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

#Colaboradores
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
            if request.method == 'GET' and request.GET.get('colaboradorSiteID') != None:
                colaboradorSiteID = request.GET.get('colaboradorSiteID')
                colaboradorSiteObj = cadastroSite.objects.filter(id=colaboradorSiteID).get()
                todasFuncoes = funcaoModel.objects.all().order_by('nome')
            return render (request, 'gerencia/colaboradores/colaboradorNovo.html', {'title':'Novo Colaborador', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'colaboradorSiteObj':colaboradorSiteObj,
                                                                                    'todasFuncoes':todasFuncoes})
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

#Fornecedores
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

#Funções
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

#Clientes
def clientesHome(request):
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
                
            return render (request, 'gerencia/clientes/home.html', {'title':'Clientes', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesNovo(request):
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
                contato = request.POST.get('contato')
                cnpj = request.POST.get('cnpj')
                email = request.POST.get('email')
                telefone = request.POST.get('telefone')
                cep = request.POST.get('cep')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidade = request.POST.get('cidade')
                uf = request.POST.get('uf')
                novoCliente = clienteModel(nome=nome, contato=contato, cnpj=cnpj, email=email, telefone=telefone, cep=cep, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, uf=uf)
                novoCliente.save()
                msgConfirmacao = "Novo cliente cadastrado com sucesso!"
                return render (request, 'gerencia/clientes/clienteNovo.html', {'title':'Novo Cliente', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/clientes/clienteNovo.html', {'title':'Novo Cliente', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            clientes = clienteModel.objects.all().order_by('id')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('clienteID'):
                clienteID = request.POST.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteID).get()
                return render (request, 'gerencia/clientes/clienteVisualizar1.html', {'title':'Visualizar Cliente', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'clienteObj':clienteObj})
            return render (request, 'gerencia/clientes/clienteVisualizar.html', {'title':'Visualizar Cliente', 
                                                                               'msgTelaInicial':msgTelaInicial,
                                                                               'clientes':clientes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesEditar(request):
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
            if request.method == 'GET':
                clienteID = request.GET.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteID).get()
                return render (request, 'gerencia/clientes/clienteEditar.html', {'title':'Editar Cliente', 
                                                                                'msgTelaInicial':msgTelaInicial,
                                                                                'clienteObj':clienteObj})
            if request.method == 'POST' and request.POST.get('clienteID'):
                clienteID = request.POST.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteID).get()
                nome = request.POST.get('nome')
                contato = request.POST.get('contato')
                cnpj = request.POST.get('cnpj')
                email = request.POST.get('email')
                telefone = request.POST.get('telefone')
                cep = request.POST.get('cep')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidade = request.POST.get('cidade')
                uf = request.POST.get('uf')
                clienteObj.nome = nome
                clienteObj.contato = contato
                clienteObj.cnpj = cnpj
                clienteObj.email = email
                clienteObj.telefone = telefone
                clienteObj.cep = cep
                clienteObj.endereco = endereco
                clienteObj.numero = numero
                clienteObj.bairro = bairro
                clienteObj.cidade = cidade
                clienteObj.uf = uf
                clienteObj.save()
                msgConfirmacao = "Cliente editado com sucesso!"
                return render (request, 'gerencia/clientes/clienteVisualizar1.html', {'title':'Visualizar Cliente', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'clienteObj':clienteObj,
                                                                'msgConfirmacao':msgConfirmacao})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

#Orçamentos
def orcamentosHome(request):
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
                
            return render (request, 'gerencia/orcamentos/home.html', {'title':'Orçamentos', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
#Estoque
def estoqueHome(request):
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
                
            return render (request, 'gerencia/estoque/home.html', {'title':'Estoque', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

#Equipamentos
def equipamentosHome(request):
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
                
            return render (request, 'gerencia/estoque/equipamentos/home.html', {'title':'Serviços', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def equipamentosNovo(request):
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
                msgConfirmacao = "Novo serviço cadastrado com sucesso!"
                return render (request, 'gerencia/estoque/equipamentos/equipamentoNovo.html', {'title':'Novo Serviços', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/estoque/equipamentos/equipamentoNovo.html', {'title':'Novo Serviços', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def equipamentosVisualizar(request):
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
                return render (request, 'gerencia/estoque/equipamentos/equipamentoEditar.html', {'title':'Editar Serviço', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'funcaoObj':funcaoObj})
            return render (request, 'gerencia/estoque/equipamentos/equipamentoVisualizar.html', {'title':'Visualizar Serviço', 
                                                                               'msgTelaInicial':msgTelaInicial,
                                                                               'funcoes':funcoes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def equipamentosSalvar(request):
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
                return render (request, 'gerencia/estoque/equipamentos/equipamentoVisualizar.html', {'title':'Visualizar Serviços', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'funcoes':funcoes,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/estoque/equipamentos/equipamentoVisualizar.html', {'title':'Visualizar Serviços', 
                                                                               'msgTelaInicial':msgTelaInicial,
                                                                               'funcoes':funcoes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

#Contas
def contasHome(request):
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
            return render (request, 'gerencia/contas/home.html', {'title':'Contas', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasRelatorioHome(request):
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
            return render (request, 'gerencia/contas/relatorios.html', {'title':'Relatórios', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasPagarHome(request):
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
            return render (request, 'gerencia/contas/pagar/home.html', {'title':'Contas a pagar', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasReceberHome(request):
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
            return render (request, 'gerencia/contas/receber/home.html', {'title':'Contas a receber', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasPagarNovo(request):
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
                dataVencimento = request.POST.get('dataVencimento')
                if request.POST.get('fixa') != None:
                    fixa = "1"
                else:
                    fixa = "2"
                observacao = request.POST.get('observacao')
                valor = request.POST.get('valor')
                novaContaPagar = contaPagarModel(nome=nome, observacao=observacao, dataVencimento=dataVencimento, fixa=fixa, valor=valor)
                novaContaPagar.save()
                msgConfirmacao = "Conta registrada com sucesso!"
                return render (request, 'gerencia/contas/pagar/pagarNovo.html', {'title':'Nova conta a pagar', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/contas/pagar/pagarNovo.html', {'title':'Nova conta a pagar', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasPagarVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            contas = contaPagarModel.objects.all()
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('contaID') != None:
                contaID = request.POST.get('contaID')
                contaObj = contaPagarModel.objects.filter(id=contaID).get()
                return render (request, 'gerencia/contas/pagar/pagarVisualizar.html', {'title':'Visualizar conta a pagar', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contaObj':contaObj})
            return render (request, 'gerencia/contas/pagar/pagarBusca.html', {'title':'Visualizar conta a pagar', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contas':contas})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasPagarEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            try:
                contaID = request.GET.get('contaID')
                contaObj = contaPagarModel.objects.filter(id=contaID).get()
            except:
                print("Erro ao procurar com GET")
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('contaID') != None:
                contaID = request.POST.get('contaID')
                contaObj = contaPagarModel.objects.filter(id=contaID).get()
                nome = request.POST.get('nome')
                dataVencimento = request.POST.get('dataVencimento')
                if request.POST.get('fixa') != None:
                    fixa = "1"
                else:
                    fixa = "2"
                observacao = request.POST.get('observacao')
                valor = request.POST.get('valor')
                contaObj.nome = nome
                contaObj.dataVencimento = dataVencimento
                contaObj.fixa = fixa
                contaObj.observacao = observacao
                contaObj.valor = valor
                contaObj.save()
                msgConfirmacao = "Conta alterada com sucesso!"
                contas = contaPagarModel.objects.all()
                return render (request, 'gerencia/contas/pagar/pagarBusca.html', {'title':'Editar conta a pagar', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contaObj':contaObj,
                                                                                    'msgConfirmacao':msgConfirmacao,
                                                                                    'contas':contas})
            return render (request, 'gerencia/contas/pagar/pagarEditar.html', {'title':'Editar conta a pagar', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contaObj':contaObj})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasReceberNovo(request):
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
            if request.method == "POST" and request.POST.get != None:
                nome = request.POST.get('nome')
                dataVencimento = request.POST.get('dataVencimento')
                if request.POST.get('fixa') != None:
                    fixa = "1"
                else:
                    fixa = "2"
                observacao = request.POST.get('observacao')
                valor = request.POST.get('valor')
                novaContaReceber = contaReceberModel(nome=nome, observacao=observacao, dataVencimento=dataVencimento, fixa=fixa, valor=valor)
                novaContaReceber.save()
                msgConfirmacao = "Conta registrada com sucesso!"
                return render (request, 'gerencia/contas/receber/receberNovo.html', {'title':'Nova conta a receber', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/contas/receber/receberNovo.html', {'title':'Nova conta a receber', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasReceberVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            contas = contaReceberModel.objects.all()
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('contaID') != None:
                contaID = request.POST.get('contaID')
                contaObj = contaReceberModel.objects.filter(id=contaID).get()
                return render (request, 'gerencia/contas/receber/receberVisualizar.html', {'title':'Visualizar conta a receber', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contaObj':contaObj})
            return render (request, 'gerencia/contas/receber/receberBusca.html', {'title':'Visualizar conta a receber', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contas':contas})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def contasReceberEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            try:
                contaID = request.GET.get('contaID')
                contaObj = contaReceberModel.objects.filter(id=contaID).get()
            except:
                print("Erro ao procurar com GET")
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == "POST" and request.POST.get('contaID') != None:
                contaID = request.POST.get('contaID')
                contaObj = contaReceberModel.objects.filter(id=contaID).get()
                nome = request.POST.get('nome')
                dataVencimento = request.POST.get('dataVencimento')
                if request.POST.get('fixa') != None:
                    fixa = "1"
                else:
                    fixa = "2"
                observacao = request.POST.get('observacao')
                valor = request.POST.get('valor')
                contaObj.nome = nome
                contaObj.dataVencimento = dataVencimento
                contaObj.fixa = fixa
                contaObj.observacao = observacao
                contaObj.valor = valor
                contaObj.save()
                msgConfirmacao = "Conta alterada com sucesso!"
                contas = contaPagarModel.objects.all()
                return render (request, 'gerencia/contas/receber/receberBusca.html', {'title':'Editar conta a receber', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contaObj':contaObj,
                                                                                    'msgConfirmacao':msgConfirmacao,
                                                                                    'contas':contas})
            return render (request, 'gerencia/contas/receber/receberEditar.html', {'title':'Editar conta a receber', 
                                                                                    'msgTelaInicial':msgTelaInicial,
                                                                                    'contaObj':contaObj})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


#Caixa
def caixaHome(request):
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
            return render (request, 'gerencia/caixa/home.html', {'title':'Caixa', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def caixaEntradaNovo(request):
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
            return render (request, 'gerencia/caixa/entradaNovo.html', {'title':'Nova entrada', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def caixaSaidaNovo(request):
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
            return render (request, 'gerencia/caixa/saidaNovo.html', {'title':'Nova saída', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def balancoHome(request):
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
            return render (request, 'gerencia/caixa/balanco.html', {'title':'Balanço', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})