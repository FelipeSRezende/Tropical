from django.test import TestCase,Client
from  django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from model_mommy import mommy

from acesso.models import Estabelecimento
from produto.models import EstabelecimentoProduto
from utils.models import Categoria


class ProdutoIndexViewTestCase(TestCase):


    def setUp(self):
        user = get_user_model().objects.create_superuser(username='tropical',email='maique.rosa@gmail.com',password='troca123')
        self.client = Client()
        self.client.login(username='tropical',password='troca123')
        self.url = reverse('home:inicio')

    def tearDown(self):
        pass

    def test_status_code_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200);


    def test_esta_usando_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,"home/produto/meus_produtos.html")

class CadastroProdutoViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('produto:cadastrar_produto')
        self.estab_logado = mommy.prepare(Estabelecimento)
        self.estab_logado.set_password('troca123')
        self.estab_logado.save()
        self.secao = mommy.make(Categoria)
        self.secao2 = mommy.make(Categoria)
        self.produto_test = mommy.prepare(EstabelecimentoProduto)
        self.produto_test.secao = self.secao

        self.produto_data = {
            'nome_produto' : self.produto_test.nome_produto,
            'ref' : self.produto_test.ref,
            'preco_normal' : self.produto_test.preco_normal,
            'secao' : self.produto_test.secao.id,
        }

    def test_verificar_se_usuario_esta_logado(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response,reverse('acesso:login')+'?next='+self.url)

    def test_verificar_se_produto_esta_sendo_salvo(self):
        # realizando o login
        self.client.login(username=self.estab_logado.username,password='troca123')

        # verificando se foi redirecionado com sucesso
        response = self.client.post(self.url,self.produto_data)
        self.assertRedirects(response, reverse('home:inicio'))

        # verificando se o produto foi salvo no banco
        self.assertGreater(EstabelecimentoProduto.objects.count(),0)

        produtoDB = EstabelecimentoProduto.objects.all().first()
        self.assertEqual(produtoDB.nome_produto,self.produto_test.nome_produto)
        self.assertEqual(produtoDB.secao.nome,self.secao.nome)

    def test_verificar_se_formulario_esta_sendo_validado(self):
        # realizando o login
        self.client.login(username=self.estab_logado.username, password='troca123')

        response = self.client.post(self.url,{})
        self.assertFormError(response,'form','nome_produto','Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'preco_normal', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'secao', 'Este campo é obrigatório.')
