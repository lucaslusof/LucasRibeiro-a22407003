from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    url_site = models.URLField(blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='licenciatura/', blank=True)

    def __str__(self):
        return self.sigla

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url_lusofona = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True) 
    
    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, blank=True)
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20, blank=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField(default=6)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    url_programa = models.URLField(blank=True)

    def __str__(self):
        return f"{self.sigla} - {self.nome}"

class Tecnologia(models.Model):
    CATEGORIAS = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('ferramenta', 'Ferramenta'),
        ('base_dados', 'Base de Dados'),
        ('devops', 'DevOps'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    url_site = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(default=3)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    video_demo = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    competencias = models.ManyToManyField('Competencia', related_name='projetos', blank=True)

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    ano = models.IntegerField()
    link_documento = models.URLField()
    destaque = models.BooleanField(default=False)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tfcs', blank=True)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    NIVEIS = [(i, str(i)) for i in range(1, 6)]
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    nivel = models.IntegerField(choices=NIVEIS, default=1)  # era CharField com variável inexistente
    tecnologias = models.ManyToManyField(Tecnologia, related_name='competencias', blank=True)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    instituicao = models.CharField(max_length=200)  # era ForeignKey para modelo inexistente
    descricao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    certificado = models.FileField(upload_to='certificados/', null=True, blank=True)
    competencias_adquiridas = models.ManyToManyField(Competencia, related_name='formacoes', blank=True)

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return self.descricao  # era self.designacao que não existe

class MakingOf(models.Model):
    ENTIDADES = [
        ('licenciatura', 'Licenciatura'),
        ('uc', 'Unidade Curricular'),
        ('projeto', 'Projeto'),
        ('tecnologia', 'Tecnologia'),
        ('tfc', 'TFC'),
        ('competencia', 'Competência'),
        ('formacao', 'Formação'),
        ('experiencia', 'Experiência'),
        ('geral', 'Geral'),
    ]
    titulo = models.CharField(max_length=200)
    entidade_relacionada = models.CharField(max_length=20, choices=ENTIDADES, default='geral')
    descricao = models.TextField()
    decisoes = models.TextField(blank=True)
    erros_correcoes = models.TextField(blank=True)
    foto_papel = models.ImageField(upload_to='makingof/', blank=True)
    uso_ia = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name_plural = 'Making Of'

    def __str__(self):
        return self.titulo