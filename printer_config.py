#!/usr/bin/env python3
"""
Script para acessar configurações de impressora via IP
Desenvolvido para acessar impressora no IP 192.168.200.15
"""

import requests
import json
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

class PrinterConfig:
    def __init__(self, ip_address="192.168.200.15"):
        self.ip_address = ip_address
        self.base_url = f"http://{ip_address}"
        self.session = requests.Session()
        self.session.timeout = 10
        
        # Headers comuns para impressoras
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
    
    def test_connection(self):
        """Testa se a impressora está acessível"""
        try:
            print(f"Testando conexao com {self.ip_address}...")
            response = self.session.get(self.base_url, timeout=5)
            print(f"Conexao estabelecida! Status: {response.status_code}")
            return True
        except requests.exceptions.ConnectTimeout:
            print(f"Timeout ao conectar com {self.ip_address}")
            return False
        except requests.exceptions.ConnectionError:
            print(f"Erro de conexao com {self.ip_address}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    
    def get_printer_info(self):
        """Obtém informações básicas da impressora"""
        info = {}
        
        # URLs comuns para configurações de impressoras
        common_paths = [
            "/",
            "/status",
            "/config",
            "/info",
            "/printer",
            "/web",
            "/admin",
            "/settings",
            "/network",
            "/system",
            "/maintenance"
        ]
        
        print(f"Explorando endpoints da impressora...")
        
        for path in common_paths:
            try:
                url = urljoin(self.base_url, path)
                print(f"   Tentando: {url}")
                
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    print(f"   Encontrado: {url}")
                    info[path] = {
                        'status_code': response.status_code,
                        'content_type': response.headers.get('content-type', ''),
                        'content_length': len(response.content),
                        'url': url
                    }
                    
                    # Se for HTML, tenta extrair informações
                    if 'text/html' in response.headers.get('content-type', ''):
                        soup = BeautifulSoup(response.content, 'html.parser')
                        title = soup.find('title')
                        if title:
                            info[path]['title'] = title.get_text().strip()
                        
                        # Procura por informações úteis
                        info[path]['forms'] = len(soup.find_all('form'))
                        info[path]['links'] = len(soup.find_all('a'))
                        info[path]['tables'] = len(soup.find_all('table'))
                        
                elif response.status_code == 401:
                    print(f"   Autenticacao necessaria: {url}")
                    info[path] = {'status_code': 401, 'requires_auth': True}
                elif response.status_code == 403:
                    print(f"   Acesso negado: {url}")
                    info[path] = {'status_code': 403, 'access_denied': True}
                    
            except requests.exceptions.RequestException as e:
                print(f"   Erro em {path}: {e}")
                continue
            except Exception as e:
                print(f"   Erro inesperado em {path}: {e}")
                continue
        
        return info
    
    def get_network_config(self):
        """Tenta obter configurações de rede"""
        network_info = {}
        
        # Endpoints específicos para configuração de rede
        network_paths = [
            "/network",
            "/tcpip",
            "/ethernet",
            "/wifi",
            "/wireless",
            "/lan",
            "/network_config",
            "/network_settings"
        ]
        
        print(f"Buscando configuracoes de rede...")
        
        for path in network_paths:
            try:
                url = urljoin(self.base_url, path)
                response = self.session.get(url, timeout=5)
                
                if response.status_code == 200:
                    print(f"   Configuracao de rede encontrada: {url}")
                    network_info[path] = {
                        'url': url,
                        'content_type': response.headers.get('content-type', ''),
                        'content': response.text[:1000]  # Primeiros 1000 caracteres
                    }
                    
            except Exception as e:
                print(f"   Erro em {path}: {e}")
                continue
        
        return network_info
    
    def get_printer_status(self):
        """Obtém status atual da impressora"""
        status_info = {}
        
        # Endpoints para status
        status_paths = [
            "/status",
            "/printer_status",
            "/device_status",
            "/system_status",
            "/info",
            "/device_info"
        ]
        
        print(f"Obtendo status da impressora...")
        
        for path in status_paths:
            try:
                url = urljoin(self.base_url, path)
                response = self.session.get(url, timeout=5)
                
                if response.status_code == 200:
                    print(f"   Status encontrado: {url}")
                    status_info[path] = {
                        'url': url,
                        'content_type': response.headers.get('content-type', ''),
                        'content': response.text[:2000]  # Primeiros 2000 caracteres
                    }
                    
            except Exception as e:
                print(f"   Erro em {path}: {e}")
                continue
        
        return status_info
    
    def save_results(self, data, filename="printer_config_results.json"):
        """Salva os resultados em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Resultados salvos em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def run_full_scan(self):
        """Executa scan completo da impressora"""
        print(f"Iniciando scan completo da impressora {self.ip_address}")
        print("=" * 60)
        
        results = {
            'ip_address': self.ip_address,
            'scan_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'connection_test': None,
            'printer_info': {},
            'network_config': {},
            'printer_status': {}
        }
        
        # Teste de conexão
        if not self.test_connection():
            print("Nao foi possivel estabelecer conexao. Verifique:")
            print("   - Se o IP esta correto")
            print("   - Se a impressora esta ligada")
            print("   - Se esta na mesma rede")
            return results
        
        # Obter informações gerais
        results['printer_info'] = self.get_printer_info()
        
        # Obter configurações de rede
        results['network_config'] = self.get_network_config()
        
        # Obter status da impressora
        results['printer_status'] = self.get_printer_status()
        
        # Salvar resultados
        self.save_results(results)
        
        # Resumo
        print("\n" + "=" * 60)
        print("RESUMO DO SCAN")
        print("=" * 60)
        print(f"IP da impressora: {self.ip_address}")
        print(f"Endpoints encontrados: {len([k for k, v in results['printer_info'].items() if v.get('status_code') == 200])}")
        print(f"Configuracoes de rede: {len(results['network_config'])}")
        print(f"Status disponiveis: {len(results['printer_status'])}")
        
        return results

def main():
    """Função principal"""
    print("SCANNER DE CONFIGURACAO DE IMPRESSORA")
    print("=" * 60)
    
    # Criar instância do scanner
    scanner = PrinterConfig("192.168.200.15")
    
    # Executar scan completo
    results = scanner.run_full_scan()
    
    # Mostrar alguns resultados importantes
    if results['printer_info']:
        print("\nENDPOINTS ENCONTRADOS:")
        for path, info in results['printer_info'].items():
            if info.get('status_code') == 200:
                print(f"   {path} - {info.get('title', 'Sem titulo')}")
    
    if results['network_config']:
        print("\nCONFIGURACOES DE REDE:")
        for path in results['network_config'].keys():
            print(f"   {path}")
    
    if results['printer_status']:
        print("\nSTATUS DA IMPRESSORA:")
        for path in results['printer_status'].keys():
            print(f"   {path}")

if __name__ == "__main__":
    main()
