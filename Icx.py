import requests
import base64
import json
import pandas as pd
from dotenv import load_dotenv
import os

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

    def get_client_data(self, page=1, records_per_page=20):
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

    def listar_cliente_contrato(self, page=1, records_per_page=20):
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

    def listar_cliente_contrato(self, page=1, records_per_page=20):
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

    def listar_cliente_contrato(self, page=1, records_per_page=20):
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


# Usage example:
#api_client = ListarCliente('NomeDaEmpresa')
#df = api_client.get_client_data(page=1, records_per_page=20)
#print(df)
