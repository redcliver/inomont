from django.db import models
from django.utils import timezone

# Create your models here.
class cidadeModel(models.Model):
    LB = (
        ('1', 'Ativa'),
        ('2', 'Bloqueada'),
        ('3', 'Inativa'),
    )
    ES = (
        ('01', 'Acre (AC)'),
        ('02', 'Alagoas (AL)'),
        ('03', 'Amapá (AP)'),
        ('04', 'Amazonas (AM)'),
        ('05', 'Bahia (BA)'),
        ('06', 'Ceará (CE)'),
        ('07', 'Distrito Federal (DF)'),
        ('08', 'Espírito Santo (ES)'),
        ('09', 'Goiás (GO)'),
        ('10', 'Maranhão (MA)'),
        ('11', 'Mato Grosso (MT)'),
        ('12', 'Mato Grosso do Sul (MS)'),
        ('13', 'Minas Gerais (MG)'),
        ('14', 'Pará (PA)'),
        ('15', 'Paraíba (PB)'),
        ('16', 'Paraná (PR)'),
        ('17', 'Pernambuco (PE)'),
        ('18', 'Piauí (PI)'),
        ('19', 'Rio de Janeiro (RJ)'),
        ('20', 'Rio Grande do Norte (RN)'),
        ('21', 'Rio Grande do Sul (RS)'),
        ('22', 'Rondônia (RO)'),
        ('23', 'Roraima (RR)'),
        ('24', 'Santa Catarina (SC)'),
        ('25', 'São Paulo (SP)'),
        ('26', 'Sergipe (SE)'),
        ('27', 'Tocantins (TO)'),
    )
    liberacao = models.CharField(max_length=2, choices=LB, default='1')
    nome = models.CharField(max_length=300, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ES, default='12')
    dataCadastro = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.nome

class funcaoModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    observacao = models.CharField(max_length=300, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class cadastroSite(models.Model):
    ES = (
        ('1', 'Não visualizado'),
        ('2', 'Visualizado'),
    )
    EC = (
        ('1', 'Solteiro(a)'),
        ('2', 'Casado(a)'),
        ('3', 'Separado(a)'),
        ('4', 'Divorciado(a)'),
        ('5', 'Viúvo(a)'),
    )
    EX = (
        ('1', 'Menos de 1 ano'),
        ('2', '1 ano'),
        ('3', '2 anos'),
        ('4', '3 anos'),
        ('5', 'Mais de 3 anos'),
    )
    SN = (
        ('1', 'Sim'),
        ('2', 'Não'),
    )
    SC = (
        ('1', 'Ensino Fundamental Incompleto'),
        ('2', 'Ensino Fundamental Completo'),
        ('3', 'Ensino Médio Incompleto'),
        ('4', 'Ensino Médio Completo'),
        ('5', 'Superior Incompleto'),
        ('6', 'Superior Completo'),
    )
    PR = (
        ('1', 'De 1 a 6 meses'),
        ('2', 'De 6 a 12 meses'),
        ('3', 'De 1 ano a 1 ano e meio'),
        ('4', 'De 1 ano e meio a 2 anos'),
        ('5', 'Mais de 2 anos'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ES, default=1)
    estadoCivil = models.CharField(max_length=1, choices=EC, default=1)
    experiencia = models.CharField(max_length=1, choices=EX)
    escolaridade = models.CharField(max_length=1, choices=SC, default=1)
    ehDeTresLagoas = models.CharField(max_length=1, choices=SN, default=1, null=True, blank=True)
    trabalhouInomont = models.CharField(max_length=1, choices=SN, default=1, null=True, blank=True)
    pqInomont = models.CharField(max_length=400, null=True, blank=True)
    nome = models.CharField(max_length=300, null=True, blank=True)
    sobrenome = models.CharField(max_length=400, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=15, null=True, blank=True)
    funcao = models.ForeignKey(funcaoModel, on_delete="models.CASCADE")
    telefone = models.CharField(max_length=14, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)
    empresa1 = models.CharField(max_length=300, null=True, blank=True)
    funcao1 = models.CharField(max_length=300, null=True, blank=True)
    periodo1 = models.CharField(max_length=1, choices=PR)
    empresa2 = models.CharField(max_length=300, null=True, blank=True)
    funcao2 = models.CharField(max_length=300, null=True, blank=True)
    periodo2 = models.CharField(max_length=1, choices=PR)
    empresa3 = models.CharField(max_length=300, null=True, blank=True)
    funcao3 = models.CharField(max_length=300, null=True, blank=True)
    periodo3 = models.CharField(max_length=1, choices=PR)
    dataNasc = models.DateTimeField(default=timezone.now())
    dataCadastro = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.nome

class fornecedorModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    contatoPrincipal = models.CharField(max_length=200)
    email = models.CharField(max_length=300, null=True, blank=True)
    cnpj = models.CharField(max_length=30, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=400, null=True, blank=True)
    numero = models.CharField(max_length=5, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=300, null=True, blank=True)
    uf = models.CharField(max_length=300, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class colaboradorModel(models.Model):
    ST = (
        ('1', 'Disponível'),
        ('2', 'Alocado'),
        ('3', 'Afastado'),
        ('4', 'Desligado'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    funcao = models.CharField(max_length=300, null=True, blank=True)
    dataAdmissao = models.DateTimeField(default=timezone.now)
    dataDesligamento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=ST, default=1)
    encarregado = models.CharField(max_length=300, null=True, blank=True)
    setor = models.CharField(max_length=300, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=400, null=True, blank=True)
    numero = models.CharField(max_length=5, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=300, null=True, blank=True)
    uf = models.CharField(max_length=300, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class clienteModel(models.Model):
    ST = (
        ('1', 'Disponível'),
        ('2', 'Bloqueado'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=300)
    contato = models.CharField(max_length=300, null=True, blank=True)
    cnpj = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=1, choices=ST, default=1)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=400, null=True, blank=True)
    numero = models.CharField(max_length=5, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=300, null=True, blank=True)
    uf = models.CharField(max_length=300, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome