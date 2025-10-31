#!/usr/bin/env python3
"""
Script específico para extrair informações detalhadas do endpoint de configuração
http://192.168.200.15/hp/device/info_configuration.htm
"""

import requests
import json
import time
from bs4 import BeautifulSoup
import re

class ConfigurationInfoExtractor:
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
    
    def extract_configuration_info(self):
        """Extrai informações detalhadas da página de configuração"""
        url = f"{self.base_url}/hp/device/info_configuration.htm"
        
        print(f"Acessando: {url}")
        
        try:
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                print("Conexao estabelecida com sucesso!")
                
                soup = BeautifulSoup(response.content, 'html.parser')
                text_content = soup.get_text()
                
                # Extrair informações específicas
                config_info = self.parse_configuration_data(text_content)
                
                return {
                    'url': url,
                    'status_code': response.status_code,
                    'content_length': len(response.content),
                    'configuration_info': config_info,
                    'raw_content': response.text[:5000]  # Primeiros 5000 caracteres
                }
            else:
                print(f"Erro: Status {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Erro ao acessar URL: {e}")
            return None
    
    def parse_configuration_data(self, text_content):
        """Analisa o conteúdo da página e extrai informações específicas"""
        config_info = {}
        
        # Informações básicas do dispositivo
        device_info = {}
        
        # Procurar por modelo
        model_patterns = [
            r'HP LaserJet ([A-Za-z0-9-]+)',
            r'Model[:\s]*([^\n\r]+)',
            r'Modelo[:\s]*([^\n\r]+)'
        ]
        
        for pattern in model_patterns:
            match = re.search(pattern, text_content, re.IGNORECASE)
            if match:
                device_info['model'] = match.group(1).strip()
                break
        
        # Procurar por número de série
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
            r'Version[:\s]*([^\n\r]+)',
            r'Firmware Version[:\s]*([^\n\r]+)'
        ]
        
        for pattern in firmware_patterns:
            match = re.search(pattern, text_content, re.IGNORECASE)
            if match:
                device_info['firmware'] = match.group(1).strip()
                break
        
        if device_info:
            config_info['device_info'] = device_info
        
        # Informações de impressão
        print_info = {}
        
        # Procurar por contadores de páginas
        page_patterns = [
            r'Total de páginas[:\s]*([0-9,]+)',
            r'Total pages[:\s]*([0-9,]+)',
            r'Páginas impressas[:\s]*([0-9,]+)',
            r'Pages printed[:\s]*([0-9,]+)',
            r'Contador de páginas[:\s]*([0-9,]+)',
            r'Page counter[:\s]*([0-9,]+)',
            r'([0-9,]+)\s*páginas',
            r'([0-9,]+)\s*pages'
        ]
        
        for pattern in page_patterns:
            matches = re.findall(pattern, text_content, re.IGNORECASE)
            if matches:
                print_info['total_pages'] = matches[0].replace(',', '')
                break
        
        # Procurar por tipos de impressão
        print_types = {}
        
        type_patterns = [
            r'PCL[:\s]*([0-9,]+)',
            r'PostScript[:\s]*([0-9,]+)',
            r'PDF[:\s]*([0-9,]+)',
            r'JPEG[:\s]*([0-9,]+)',
            r'PNG[:\s]*([0-9,]+)',
            r'TIFF[:\s]*([0-9,]+)'
        ]
        
        for pattern in type_patterns:
            matches = re.findall(pattern, text_content, re.IGNORECASE)
            if matches:
                print_types[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
        
        if print_types:
            print_info['print_types'] = print_types
        
        # Procurar por tamanhos de papel
        paper_sizes = {}
        
        size_patterns = [
            r'A4[:\s]*([0-9,]+)',
            r'A3[:\s]*([0-9,]+)',
            r'Letter[:\s]*([0-9,]+)',
            r'Legal[:\s]*([0-9,]+)',
            r'Executive[:\s]*([0-9,]+)'
        ]
        
        for pattern in size_patterns:
            matches = re.findall(pattern, text_content, re.IGNORECASE)
            if matches:
                paper_sizes[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
        
        if paper_sizes:
            print_info['paper_sizes'] = paper_sizes
        
        # Procurar por orientações
        orientations = {}
        
        orientation_patterns = [
            r'Retrato[:\s]*([0-9,]+)',
            r'Portrait[:\s]*([0-9,]+)',
            r'Paisagem[:\s]*([0-9,]+)',
            r'Landscape[:\s]*([0-9,]+)'
        ]
        
        for pattern in orientation_patterns:
            matches = re.findall(pattern, text_content, re.IGNORECASE)
            if matches:
                orientations[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
        
        if orientations:
            print_info['orientations'] = orientations
        
        if print_info:
            config_info['print_info'] = print_info
        
        # Informações de rede
        network_info = {}
        
        # Procurar por IP
        ip_patterns = [
            r'IP Address[:\s]*([0-9.]+)',
            r'IP[:\s]*([0-9.]+)',
            r'Endereço IP[:\s]*([0-9.]+)',
            r'IPv4[:\s]*([0-9.]+)'
        ]
        
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
            config_info['network_info'] = network_info
        
        # Informações de suprimentos
        supplies_info = {}
        
        # Procurar por nível de toner
        toner_patterns = [
            r'Toner[:\s]*([0-9]+)%',
            r'Cartucho[:\s]*([0-9]+)%',
            r'Cartridge[:\s]*([0-9]+)%',
            r'Nível[:\s]*([0-9]+)%',
            r'Level[:\s]*([0-9]+)%'
        ]
        
        for pattern in toner_patterns:
            matches = re.findall(pattern, text_content, re.IGNORECASE)
            if matches:
                supplies_info['toner_level'] = matches[0]
                break
        
        if supplies_info:
            config_info['supplies_info'] = supplies_info
        
        return config_info
    
    def generate_detailed_report(self):
        """Gera relatório detalhado das informações extraídas"""
        print("EXTRAINDO INFORMACOES DETALHADAS DA CONFIGURACAO")
        print("=" * 60)
        
        result = self.extract_configuration_info()
        
        if result:
            print("\nINFORMACOES EXTRAIDAS:")
            print("-" * 40)
            
            config_info = result['configuration_info']
            
            # Informações do dispositivo
            if 'device_info' in config_info:
                print("\nINFORMACOES DO DISPOSITIVO:")
                for key, value in config_info['device_info'].items():
                    print(f"   {key}: {value}")
            
            # Informações de impressão
            if 'print_info' in config_info:
                print("\nINFORMACOES DE IMPRESSAO:")
                print_info = config_info['print_info']
                
                if 'total_pages' in print_info:
                    print(f"   Total de paginas impressas: {print_info['total_pages']}")
                
                if 'print_types' in print_info:
                    print("   Tipos de impressao:")
                    for print_type, count in print_info['print_types'].items():
                        print(f"     {print_type}: {count}")
                
                if 'paper_sizes' in print_info:
                    print("   Tamanhos de papel:")
                    for size, count in print_info['paper_sizes'].items():
                        print(f"     {size}: {count}")
                
                if 'orientations' in print_info:
                    print("   Orientacoes:")
                    for orientation, count in print_info['orientations'].items():
                        print(f"     {orientation}: {count}")
            
            # Informações de rede
            if 'network_info' in config_info:
                print("\nINFORMACOES DE REDE:")
                for key, value in config_info['network_info'].items():
                    print(f"   {key}: {value}")
            
            # Informações de suprimentos
            if 'supplies_info' in config_info:
                print("\nINFORMACOES DE SUPRIMENTOS:")
                for key, value in config_info['supplies_info'].items():
                    print(f"   {key}: {value}")
            
            # Salvar resultados
            self.save_results(result, "configuration_detailed_results.json")
            
            return result
        else:
            print("Nao foi possivel extrair informacoes da pagina de configuracao")
            return None
    
    def save_results(self, data, filename="configuration_detailed_results.json"):
        """Salva os resultados em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\nResultados salvos em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")

def main():
    """Função principal"""
    print("EXTRAIDOR DE INFORMACOES DETALHADAS DE CONFIGURACAO")
    print("=" * 60)
    
    # Criar instância do extrator
    extractor = ConfigurationInfoExtractor("192.168.200.15")
    
    # Extrair informações detalhadas
    result = extractor.generate_detailed_report()

if __name__ == "__main__":
    main()




