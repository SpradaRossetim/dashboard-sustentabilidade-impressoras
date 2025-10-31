#!/usr/bin/env python3
"""
Script específico para impressoras HP LaserJet P2055dn
Baseado na análise do HTML da impressora
"""

import requests
import json
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

class HPPrinterScanner:
    def __init__(self, ip_address="192.168.200.15"):
        self.ip_address = ip_address
        self.base_url = f"http://{ip_address}"
        self.session = requests.Session()
        self.session.timeout = 10
        
        # Headers específicos para HP
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
    
    def get_hp_specific_endpoints(self):
        """Endpoints específicos para HP LaserJet P2055dn baseados no HTML encontrado"""
        return [
            "/hp/device/index.htm",  # Status
            "/hp/device/Auth/set_config_deviceinfo.htm",  # Configurações
            "/hp/jetdirect/",  # Rede
            "/hp/device/InternalPages/Index?id=ConfigurationPage",
            "/hp/device/InternalPages/Index?id=NetworkSummary",
            "/hp/device/InternalPages/Index?id=NetworkStatus",
            "/hp/device/InternalPages/Index?id=NetworkConfig",
            "/hp/device/InternalPages/Index?id=NetworkTCPIP",
            "/hp/device/InternalPages/Index?id=NetworkWireless",
            "/hp/device/InternalPages/Index?id=DeviceStatus",
            "/hp/device/InternalPages/Index?id=SuppliesStatus",
            "/hp/device/InternalPages/Index?id=UsagePage",
            "/hp/device/InternalPages/Index?id=SecurityPage",
            "/hp/device/InternalPages/Index?id=SystemInfo",
            "/hp/device/InternalPages/Index?id=NetworkSummary",
            "/hp/device/InternalPages/Index?id=NetworkStatus",
            "/hp/device/InternalPages/Index?id=NetworkConfig",
            "/hp/device/InternalPages/Index?id=NetworkTCPIP",
            "/hp/device/InternalPages/Index?id=NetworkWireless",
            "/hp/device/InternalPages/Index?id=DeviceStatus",
            "/hp/device/InternalPages/Index?id=SuppliesStatus",
            "/hp/device/InternalPages/Index?id=UsagePage",
            "/hp/device/InternalPages/Index?id=SecurityPage",
            "/hp/device/InternalPages/Index?id=SystemInfo"
        ]
    
    def scan_hp_endpoints(self):
        """Escaneia endpoints específicos da HP"""
        results = {}
        endpoints = self.get_hp_specific_endpoints()
        
        print(f"Escaneando endpoints especificos da HP...")
        
        for endpoint in endpoints:
            try:
                url = urljoin(self.base_url, endpoint)
                response = self.session.get(url, timeout=5)
                
                if response.status_code == 200:
                    print(f"   Encontrado: {endpoint}")
                    results[endpoint] = {
                        'url': url,
                        'status_code': response.status_code,
                        'content_type': response.headers.get('content-type', ''),
                        'content_length': len(response.content),
                        'content': response.text[:3000]  # Primeiros 3000 caracteres
                    }
                    
                    # Extrair informações do HTML
                    if 'text/html' in response.headers.get('content-type', ''):
                        soup = BeautifulSoup(response.content, 'html.parser')
                        title = soup.find('title')
                        if title:
                            results[endpoint]['title'] = title.get_text().strip()
                        
                        # Extrair informações específicas
                        self.extract_hp_info(soup, results[endpoint])
                        
                elif response.status_code == 401:
                    print(f"   {endpoint} (Autenticacao necessaria)")
                    results[endpoint] = {'status_code': 401, 'requires_auth': True}
                elif response.status_code == 403:
                    print(f"   {endpoint} (Acesso negado)")
                    results[endpoint] = {'status_code': 403, 'access_denied': True}
                elif response.status_code == 404:
                    print(f"   {endpoint} (Nao encontrado)")
                    results[endpoint] = {'status_code': 404, 'not_found': True}
                    
            except requests.exceptions.RequestException as e:
                print(f"   {endpoint}: {e}")
                continue
            except Exception as e:
                print(f"   {endpoint}: {e}")
                continue
        
        return results
    
    def extract_hp_info(self, soup, result_dict):
        """Extrai informações específicas da HP do HTML"""
        try:
            text_content = soup.get_text()
            
            # Informações de rede
            network_info = {}
            
            # Procurar por IP
            ip_patterns = [
                r'IP Address[:\s]*([0-9.]+)',
                r'IP[:\s]*([0-9.]+)',
                r'Endereço IP[:\s]*([0-9.]+)',
                r'IPv4[:\s]*([0-9.]+)',
                r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
            ]
            
            for pattern in ip_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    network_info['ip_addresses'] = matches
                    break
            
            # Procurar por Gateway
            gateway_patterns = [
                r'Gateway[:\s]*([0-9.]+)',
                r'Default Gateway[:\s]*([0-9.]+)',
                r'Roteador[:\s]*([0-9.]+)'
            ]
            
            for pattern in gateway_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    network_info['gateway'] = match.group(1)
                    break
            
            # Procurar por DNS
            dns_patterns = [
                r'DNS[:\s]*([0-9.]+)',
                r'Primary DNS[:\s]*([0-9.]+)',
                r'DNS Primário[:\s]*([0-9.]+)'
            ]
            
            for pattern in dns_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    network_info['dns'] = match.group(1)
                    break
            
            # Procurar por MAC Address
            mac_patterns = [
                r'MAC[:\s]*([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})',
                r'MAC Address[:\s]*([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})',
                r'Endereço MAC[:\s]*([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
            ]
            
            for pattern in mac_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    network_info['mac_address'] = match.group(0)
                    break
            
            if network_info:
                result_dict['network_info'] = network_info
            
            # Informações do dispositivo
            device_info = {}
            
            # Procurar por modelo
            model_patterns = [
                r'HP LaserJet ([A-Za-z0-9-]+)',
                r'Model[:\s]*([^\n\r]+)',
                r'Modelo[:\s]*([^\n\r]+)',
                r'Product[:\s]*([^\n\r]+)',
                r'Produto[:\s]*([^\n\r]+)'
            ]
            
            for pattern in model_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    device_info['model'] = match.group(1).strip()
                    break
            
            # Procurar por serial
            serial_patterns = [
                r'Serial[:\s]*([^\n\r]+)',
                r'Série[:\s]*([^\n\r]+)',
                r'Serial Number[:\s]*([^\n\r]+)',
                r'Número de Série[:\s]*([^\n\r]+)'
            ]
            
            for pattern in serial_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    device_info['serial'] = match.group(1).strip()
                    break
            
            # Procurar por firmware
            firmware_patterns = [
                r'Firmware[:\s]*([^\n\r]+)',
                r'Versão[:\s]*([^\n\r]+)',
                r'Version[:\s]*([^\n\r]+)'
            ]
            
            for pattern in firmware_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    device_info['firmware'] = match.group(1).strip()
                    break
            
            if device_info:
                result_dict['device_info'] = device_info
            
            # Status dos suprimentos
            supplies_info = {}
            
            # Procurar por nível de toner
            toner_patterns = [
                r'Toner[:\s]*([0-9]+)%',
                r'Cartridge[:\s]*([0-9]+)%',
                r'Nível[:\s]*([0-9]+)%'
            ]
            
            for pattern in toner_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    supplies_info['toner_levels'] = matches
                    break
            
            if supplies_info:
                result_dict['supplies_info'] = supplies_info
                
        except Exception as e:
            print(f"   Erro ao extrair informacoes: {e}")
    
    def run_hp_scan(self):
        """Executa scan específico para HP"""
        print(f"SCANNER ESPECIFICO PARA HP LASERJET P2055DN")
        print("=" * 60)
        print(f"IP da impressora: {self.ip_address}")
        print("=" * 60)
        
        results = {
            'ip_address': self.ip_address,
            'scan_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'printer_model': 'HP LaserJet P2055dn',
            'endpoints': {},
            'network_info': {},
            'device_info': {},
            'supplies_info': {}
        }
        
        # Escanear endpoints específicos da HP
        results['endpoints'] = self.scan_hp_endpoints()
        
        # Consolidar informações
        self.consolidate_hp_info(results)
        
        # Salvar resultados
        self.save_results(results, "hp_printer_results.json")
        
        # Mostrar resumo
        self.show_hp_summary(results)
        
        return results
    
    def consolidate_hp_info(self, results):
        """Consolida informações extraídas de todos os endpoints"""
        network_info = {}
        device_info = {}
        supplies_info = {}
        
        for endpoint_data in results['endpoints'].values():
            if isinstance(endpoint_data, dict):
                if 'network_info' in endpoint_data:
                    network_info.update(endpoint_data['network_info'])
                if 'device_info' in endpoint_data:
                    device_info.update(endpoint_data['device_info'])
                if 'supplies_info' in endpoint_data:
                    supplies_info.update(endpoint_data['supplies_info'])
        
        results['network_info'] = network_info
        results['device_info'] = device_info
        results['supplies_info'] = supplies_info
    
    def save_results(self, data, filename="hp_printer_results.json"):
        """Salva os resultados em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Resultados salvos em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def show_hp_summary(self, results):
        """Mostra resumo dos resultados"""
        print("\n" + "=" * 60)
        print("RESUMO DO SCAN HP")
        print("=" * 60)
        print(f"IP da impressora: {results['ip_address']}")
        print(f"Modelo: {results['printer_model']}")
        
        total_endpoints = len(results['endpoints'])
        found_endpoints = len([k for k, v in results['endpoints'].items() if v.get('status_code') == 200])
        print(f"Endpoints testados: {total_endpoints}")
        print(f"Endpoints encontrados: {found_endpoints}")
        
        if results['network_info']:
            print("\nINFORMACOES DE REDE:")
            for key, value in results['network_info'].items():
                print(f"   {key}: {value}")
        
        if results['device_info']:
            print("\nINFORMACOES DO DISPOSITIVO:")
            for key, value in results['device_info'].items():
                print(f"   {key}: {value}")
        
        if results['supplies_info']:
            print("\nINFORMACOES DOS SUPRIMENTOS:")
            for key, value in results['supplies_info'].items():
                print(f"   {key}: {value}")
        
        print("\nENDPOINTS ENCONTRADOS:")
        for endpoint, data in results['endpoints'].items():
            if data.get('status_code') == 200:
                title = data.get('title', 'Sem titulo')
                print(f"   {endpoint} - {title}")

def main():
    """Função principal"""
    print("SCANNER ESPECIFICO PARA HP LASERJET P2055DN")
    print("=" * 60)
    
    # Criar instância do scanner HP
    scanner = HPPrinterScanner("192.168.200.15")
    
    # Executar scan específico para HP
    results = scanner.run_hp_scan()

if __name__ == "__main__":
    main()




