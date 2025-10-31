#!/usr/bin/env python3
"""
Script avançado para acessar configurações específicas de impressoras
Suporte para HP, Canon, Epson, Brother, Samsung, etc.
"""

import requests
import json
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import re

class AdvancedPrinterScanner:
    def __init__(self, ip_address="192.168.200.15"):
        self.ip_address = ip_address
        self.base_url = f"http://{ip_address}"
        self.session = requests.Session()
        self.session.timeout = 10
        
        # Headers específicos para diferentes marcas
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
    
    def detect_printer_brand(self):
        """Tenta detectar a marca da impressora"""
        print(f"Detectando marca da impressora...")
        
        try:
            response = self.session.get(self.base_url, timeout=5)
            content = response.text.lower()
            
            # Padrões para detectar marcas
            brand_patterns = {
                'HP': ['hp', 'hewlett', 'packard', 'hp eprint', 'hp smart'],
                'Canon': ['canon', 'imageclass', 'pixma', 'maxify'],
                'Epson': ['epson', 'workforce', 'ecotank', 'expression'],
                'Brother': ['brother', 'mfc', 'dcp', 'hl-'],
                'Samsung': ['samsung', 'clx-', 'scx-', 'ml-'],
                'Xerox': ['xerox', 'workcentre', 'phaser'],
                'Lexmark': ['lexmark', 'ms', 'cs', 'cx'],
                'Ricoh': ['ricoh', 'aficio', 'sp'],
                'Kyocera': ['kyocera', 'fs-', 'km-', 'taskalfa'],
                'Konica Minolta': ['konica', 'minolta', 'bizhub', 'magicolor']
            }
            
            detected_brands = []
            for brand, patterns in brand_patterns.items():
                for pattern in patterns:
                    if pattern in content:
                        detected_brands.append(brand)
                        break
            
            if detected_brands:
                print(f"   Marca(s) detectada(s): {', '.join(set(detected_brands))}")
                return list(set(detected_brands))
            else:
                print(f"   Marca nao identificada")
                return ['Desconhecida']
                
        except Exception as e:
            print(f"   Erro na deteccao: {e}")
            return ['Erro na deteccao']
    
    def get_hp_endpoints(self):
        """Endpoints específicos para impressoras HP"""
        return [
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
    
    def get_canon_endpoints(self):
        """Endpoints específicos para impressoras Canon"""
        return [
            "/canon/network/",
            "/canon/network/tcpip/",
            "/canon/network/wireless/",
            "/canon/network/status/",
            "/canon/device/status/",
            "/canon/device/info/",
            "/canon/device/supplies/",
            "/canon/device/maintenance/",
            "/canon/device/usage/",
            "/canon/security/",
            "/canon/system/",
            "/canon/network/network_config.html",
            "/canon/network/tcpip_config.html",
            "/canon/network/wireless_config.html",
            "/canon/device/device_status.html",
            "/canon/device/device_info.html",
            "/canon/device/supplies_status.html",
            "/canon/device/maintenance_info.html",
            "/canon/device/usage_info.html",
            "/canon/security/security_config.html",
            "/canon/system/system_info.html"
        ]
    
    def get_epson_endpoints(self):
        """Endpoints específicos para impressoras Epson"""
        return [
            "/PRESENTATION/HTML/TOP/PRTTOP.HTML",
            "/PRESENTATION/HTML/TOP/PRTTOP.HTM",
            "/PRESENTATION/HTML/ADVANCED/NETWORK.HTML",
            "/PRESENTATION/HTML/ADVANCED/NETWORK.HTM",
            "/PRESENTATION/HTML/ADVANCED/TCPIP.HTML",
            "/PRESENTATION/HTML/ADVANCED/TCPIP.HTM",
            "/PRESENTATION/HTML/ADVANCED/WIRELESS.HTML",
            "/PRESENTATION/HTML/ADVANCED/WIRELESS.HTM",
            "/PRESENTATION/HTML/ADVANCED/STATUS.HTML",
            "/PRESENTATION/HTML/ADVANCED/STATUS.HTM",
            "/PRESENTATION/HTML/ADVANCED/SUPPLIES.HTML",
            "/PRESENTATION/HTML/ADVANCED/SUPPLIES.HTM",
            "/PRESENTATION/HTML/ADVANCED/MAINTENANCE.HTML",
            "/PRESENTATION/HTML/ADVANCED/MAINTENANCE.HTM",
            "/PRESENTATION/HTML/ADVANCED/SYSTEM.HTML",
            "/PRESENTATION/HTML/ADVANCED/SYSTEM.HTM",
            "/PRESENTATION/HTML/ADVANCED/SECURITY.HTML",
            "/PRESENTATION/HTML/ADVANCED/SECURITY.HTM"
        ]
    
    def get_brother_endpoints(self):
        """Endpoints específicos para impressoras Brother"""
        return [
            "/general/status.html",
            "/general/information.html",
            "/general/network.html",
            "/general/network_config.html",
            "/general/tcpip.html",
            "/general/wireless.html",
            "/general/wireless_config.html",
            "/general/security.html",
            "/general/security_config.html",
            "/general/maintenance.html",
            "/general/maintenance_config.html",
            "/general/supplies.html",
            "/general/supplies_config.html",
            "/general/usage.html",
            "/general/usage_config.html",
            "/general/system.html",
            "/general/system_config.html"
        ]
    
    def get_generic_endpoints(self):
        """Endpoints genéricos para qualquer impressora"""
        return [
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
            "/maintenance",
            "/supplies",
            "/usage",
            "/security",
            "/tcpip",
            "/ethernet",
            "/wifi",
            "/wireless",
            "/lan",
            "/network_config",
            "/network_settings",
            "/device_status",
            "/device_info",
            "/system_info",
            "/printer_status",
            "/supplies_status",
            "/usage_info",
            "/maintenance_info",
            "/security_config",
            "/network_status"
        ]
    
    def scan_endpoints(self, endpoints, description):
        """Escaneia uma lista de endpoints"""
        results = {}
        print(f"Escaneando {description}...")
        
        for endpoint in endpoints:
            try:
                url = urljoin(self.base_url, endpoint)
                response = self.session.get(url, timeout=5)
                
                if response.status_code == 200:
                    print(f"   {endpoint}")
                    results[endpoint] = {
                        'url': url,
                        'status_code': response.status_code,
                        'content_type': response.headers.get('content-type', ''),
                        'content_length': len(response.content),
                        'content': response.text[:2000]  # Primeiros 2000 caracteres
                    }
                    
                    # Tentar extrair informações do HTML
                    if 'text/html' in response.headers.get('content-type', ''):
                        soup = BeautifulSoup(response.content, 'html.parser')
                        title = soup.find('title')
                        if title:
                            results[endpoint]['title'] = title.get_text().strip()
                        
                        # Extrair informações específicas
                        self.extract_printer_info(soup, results[endpoint])
                        
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
    
    def extract_printer_info(self, soup, result_dict):
        """Extrai informações específicas da impressora do HTML"""
        try:
            # Informações de rede
            network_info = {}
            
            # Procurar por IP, Gateway, DNS, etc.
            ip_patterns = [
                r'IP Address[:\s]*([0-9.]+)',
                r'IP[:\s]*([0-9.]+)',
                r'Endereço IP[:\s]*([0-9.]+)',
                r'IPv4[:\s]*([0-9.]+)'
            ]
            
            text_content = soup.get_text()
            for pattern in ip_patterns:
                match = re.search(pattern, text_content, re.IGNORECASE)
                if match:
                    network_info['ip_address'] = match.group(1)
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
            
            if device_info:
                result_dict['device_info'] = device_info
            
            # Status dos suprimentos
            supplies_info = {}
            
            # Procurar por nível de tinta/toner
            ink_patterns = [
                r'Ink[:\s]*([0-9]+)%',
                r'Tinta[:\s]*([0-9]+)%',
                r'Toner[:\s]*([0-9]+)%',
                r'Cartridge[:\s]*([0-9]+)%'
            ]
            
            for pattern in ink_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    supplies_info['ink_levels'] = matches
                    break
            
            if supplies_info:
                result_dict['supplies_info'] = supplies_info
                
        except Exception as e:
            print(f"   Erro ao extrair informacoes: {e}")
    
    def run_advanced_scan(self):
        """Executa scan avançado da impressora"""
        print(f"Iniciando scan avancado da impressora {self.ip_address}")
        print("=" * 60)
        
        results = {
            'ip_address': self.ip_address,
            'scan_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'detected_brands': [],
            'endpoints': {},
            'network_info': {},
            'device_info': {},
            'supplies_info': {}
        }
        
        # Detectar marca
        results['detected_brands'] = self.detect_printer_brand()
        
        # Escanear endpoints genéricos
        generic_endpoints = self.get_generic_endpoints()
        results['endpoints']['generic'] = self.scan_endpoints(generic_endpoints, "endpoints genéricos")
        
        # Escanear endpoints específicos por marca
        for brand in results['detected_brands']:
            if brand == 'HP':
                hp_endpoints = self.get_hp_endpoints()
                results['endpoints']['hp'] = self.scan_endpoints(hp_endpoints, "endpoints HP")
            elif brand == 'Canon':
                canon_endpoints = self.get_canon_endpoints()
                results['endpoints']['canon'] = self.scan_endpoints(canon_endpoints, "endpoints Canon")
            elif brand == 'Epson':
                epson_endpoints = self.get_epson_endpoints()
                results['endpoints']['epson'] = self.scan_endpoints(epson_endpoints, "endpoints Epson")
            elif brand == 'Brother':
                brother_endpoints = self.get_brother_endpoints()
                results['endpoints']['brother'] = self.scan_endpoints(brother_endpoints, "endpoints Brother")
        
        # Consolidar informações extraídas
        self.consolidate_info(results)
        
        # Salvar resultados
        self.save_results(results, "printer_advanced_results.json")
        
        # Mostrar resumo
        self.show_summary(results)
        
        return results
    
    def consolidate_info(self, results):
        """Consolida informações extraídas de todos os endpoints"""
        network_info = {}
        device_info = {}
        supplies_info = {}
        
        for brand_endpoints in results['endpoints'].values():
            for endpoint_data in brand_endpoints.values():
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
    
    def save_results(self, data, filename="printer_advanced_results.json"):
        """Salva os resultados em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Resultados salvos em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def show_summary(self, results):
        """Mostra resumo dos resultados"""
        print("\n" + "=" * 60)
        print("RESUMO DO SCAN AVANCADO")
        print("=" * 60)
        print(f"IP da impressora: {results['ip_address']}")
        print(f"Marca(s) detectada(s): {', '.join(results['detected_brands'])}")
        
        total_endpoints = sum(len(endpoints) for endpoints in results['endpoints'].values())
        print(f"Total de endpoints testados: {total_endpoints}")
        
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

def main():
    """Função principal"""
    print("SCANNER AVANCADO DE CONFIGURACAO DE IMPRESSORA")
    print("=" * 60)
    
    # Criar instância do scanner avançado
    scanner = AdvancedPrinterScanner("192.168.200.15")
    
    # Executar scan avançado
    results = scanner.run_advanced_scan()

if __name__ == "__main__":
    main()
