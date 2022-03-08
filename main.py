import datetime

""" Importando a lib. """
from requests import get

""" Url do site que vai servir os dados."""
url = 'http://gastosluxu.com.br/api/v1/comercio/'

""" Requisição ao site acima """
resp = get(url)

""" Se a requisição der certo retorna 200 """
if resp.status_code == 200:
    """ Para pegar a hora do sistema usei a lib datetime que é a mais indicada para quando se quer trabalhar com datas """
    print(f'Requisição recebida às..: {datetime.datetime.now()}')
else:
    """ Se a requisição falhar, será retornado o motivo. """
    print('Requisição não pode ser atendida pois o site está OFFLINE!!!')
