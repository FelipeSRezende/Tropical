from django.test import TestCase,Client
from django.core.urlresolvers import reverse
from django.urls.base import reverse_lazy
from model_mommy import mommy
from django.core.files.uploadedfile import SimpleUploadedFile
from acesso.models import Estabelecimento
from tropical import settings


class RegistroEstabelecimentoViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_teste = reverse('acesso:nova_conta')

    
    def test_registrar_nova_conta_ok(self):
        data = {'nome_estabelecimento': 'teste estab','username': 'maique','email':'maique.rosa@gmail.com', 'password1':'teste123', 'password2': 'teste123'}
        response = self.client.post(self.url_teste,data)
        estabelecimento = Estabelecimento.objects.get(username='maique')
        self.assertRedirects(response,reverse('acesso:login'))
        self.assertIsNotNone(estabelecimento)

    def test_registrar_nova_conta__sem_username(self):
        data = {'nome_estabelecimento': 'teste estab','username': '', 'password1': 'troca123',
                'password2': 'teste123'}
        response = self.client.post(self.url_teste, data)
        self.assertFormError(response, 'form','username','Este campo é obrigatório.')

    def test_registrar_nova_conta__sem_nome_estabelecimento(self):
        data = {'nome_estabelecimento': ' ','username': 'cuzao', 'password1': 'troca123',
                'password2': 'troca123'}
        response = self.client.post(self.url_teste, data)
        self.assertFormError(response,'form','nome_estabelecimento','Este campo é obrigatório.')

    def test_registrar_nova_conta_com_mesmo_nome_estabelecimento(self):

        data = {'nome_estabelecimento': 'teste estab', 'username': 'cuzao','email':'dpro@ddrol.com', 'password1': 'troca123',
                'password2': 'troca123'}

        self.client.post(self.url_teste, data)
        response = self.client.post(self.url_teste, data)

        self.assertFormError(response, 'form', 'nome_estabelecimento', 'Estabelecimento com este Nome do Estabelecimento já existe.')

    def test_registrar_nova_conta_com_mesmo_username(self):

        data = {'nome_estabelecimento': 'teste estab', 'username': 'cuzao','email':'dpro@ddrol.com', 'password1': 'troca123',
                'password2': 'troca123'}

        self.client.post(self.url_teste, data)
        response = self.client.post(self.url_teste, data)

        self.assertFormError(response, 'form', 'username', 'Estabelecimento com este Login já existe.')

    def test_registrar_nova_conta_com_mesmo_email(self):

        data = {'nome_estabelecimento': 'teste estab', 'username': 'cuzao','email':'dpro@ddrol.com', 'password1': 'troca123',
                'password2': 'troca123'}

        self.client.post(self.url_teste, data)
        response = self.client.post(self.url_teste, data)

        self.assertFormError(response, 'form', 'email', 'Estabelecimento com este Email já existe.')

    def test_registrar_nova_conta_redireciona_para_login(self):

        data = {'nome_estabelecimento': 'teste estab', 'username': 'cuzao', 'email': 'dpro@ddrol.com',
                'password1': 'troca123','password2': 'troca123'}

        response = self.client.post(self.url_teste, data)
        self.assertRedirects(response,reverse('acesso:login'))


class MinhaContaViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse_lazy('acesso:minha_conta')
        self.client = Client()
        self.estabelecimento_autenticado = mommy.prepare(settings.AUTH_USER_MODEL)
        self.estabelecimento_autenticado.set_password('troca123')
        self.estabelecimento_autenticado.save()

    def test_acessando_minha_conta_sem_esta_logado(self):
        # verificando se redireciona para o login
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.url,'/login/?next=/minha_conta/')

    def test_acessando_minha_conta_logado(self):
        #verificando se acessa minha conta ja logado
        self.client.login(username=self.estabelecimento_autenticado.username,password='troca123')
        response = self.client.get(self.url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,template_name='acesso/minha_conta.html')

    def test_atualizando_dados_da_conta_sem_a_imagem(self):
        dados = {
            'nome_estabelecimento': 'Maique Empresa', 'telefone_principal': '21988162861',
            'username': 'domzinhuu', 'email': 'maique.rosa@gmail.com', 'cep': '24760900',
            'logradouro': 'Rua Faz quem quer', 'municipio': 'sao goncalo', 'estado': 'rj',
            'complemento': 'sem numero'}


        # verificando se a view registra a atualizacao
        self.client.login(username=self.estabelecimento_autenticado.username, password='troca123')
        response = self.client.post(self.url,data=dados)
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.url,'/minha_conta/')

        # verificando se os dados foram atualizados no banco
        self.estabelecimento_autenticado.refresh_from_db()
        self.assertEquals(self.estabelecimento_autenticado.email,'maique.rosa@gmail.com')
        self.assertEquals(self.estabelecimento_autenticado.nome_estabelecimento, 'Maique Empresa')

    def test_atualizando_imagem_do_estabelecimento(self):
        self.client.login(username=self.estabelecimento_autenticado.username, password='troca123')
        pass






