import requests
import base64
import json
import pandas as pd
from dotenv import load_dotenv
import os

# ------------------- Cliente -------------------#
class ListarCliente:
    def __init__(self,host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/cliente"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches client data from the API."""
        payload = {
            'qtype': 'cliente.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'cliente.id',
            'sortorder': 'asc'
        }
        response = requests.post(self.base_url, data=payload, headers=self.headers)
        
        if response.status_code == 200:
            response_json = response.json()
            return pd.json_normalize(response_json['registros'])
        else:
            response.raise_for_status()

class ListarClienteContrato:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/cliente_contrato"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches cliente_contrato data from the API."""
        payload = {
            'qtype': 'cliente_contrato.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'cliente_contrato.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()

# ------------------- Produtos ------------------#
class ListarProdutos:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/produtos"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches cliente_contrato data from the API."""
        payload = {
            'qtype': 'produtos.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'produtos.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()

# ------------------- Fornecedores --------------#
class ListarFornecedores:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/fornecedor"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches cliente_contrato data from the API."""
        payload = {
            'qtype': 'fornecedor.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'fornecedor.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()

#------------------- Provedor -------------------#
class ListarPlanodeVelocidade:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/radgrupos"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches cliente_contrato data from the API."""
        payload = {
            'qtype': 'radgrupos.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'radgrupos.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()

class ListarClientesFibra:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/radpop_radio_cliente_fibra"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def listar_cliente_fibra(self, page=1, records_per_page=20):
        """Fetches cliente_contrato data from the API."""
        payload = {
            'qtype': 'radpop_radio_cliente_fibra.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'radpop_radio_cliente_fibra.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()

# ------------------- Suporte -------------------#
class ListarOrdemdeServico:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/su_oss_chamado"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches cliente_contrato data from the API."""
        payload = {
            'qtype': 'su_oss_chamado.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'su_oss_chamado.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()

class ListarAtendimento:
    def __init__(self, host):
        # Load environment variables from .env file
        load_dotenv()
        self.host = host
        self.base_url = f"https://{self.host}.com.br/webservice/v1/su_ticket"
        self.token = os.getenv('API_TOKEN')
        self.headers = {
            'ixcsoft': 'listar',
            'Authorization': self._get_auth_header(),
            'Content-Type': 'application/json'
        }

    def _get_auth_header(self):
        """Generates the Authorization header from the token."""
        token_bytes = self.token.encode('utf-8')
        auth_header = 'Basic {}'.format(base64.b64encode(token_bytes).decode('utf-8'))
        return auth_header

    def executar(self, page=1, records_per_page=20):
        """Fetches cliente_atendimentos data from the API."""
        payload = {
            'qtype': 'su_ticket.id',
            'query': '0',
            'oper': '>',
            'page': str(page),
            'rp': str(records_per_page),
            'sortname': 'su_ticket.id',
            'sortorder': 'asc'
        }

        response = requests.post(self.base_url, data=payload, headers=self.headers)

        if response.status_code == 200:
            return response.text  # You can process it further, like converting to JSON if needed
        else:
            response.raise_for_status()





# Usage example:
api_client = ListarAtendimento('SuaEmpresa')
df = api_client.executar(page=1, records_per_page=20)
print(df)
