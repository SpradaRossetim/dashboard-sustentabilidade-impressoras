#!/usr/bin/env python3
"""
Script específico para extrair informações de impressões da HP LaserJet P2055dn
Foca em quantidade de impressões, tipos de impressão e estatísticas de uso
"""

import requests
import json
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

class PrinterUsageScanner:
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
    
    def get_usage_endpoints(self):
        """Endpoints específicos para informações de uso e impressões"""
        return [
            "/hp/device/supply_status.htm",  # Status de suprimentos
            "/hp/device/info_configuration.htm",  # Configuração do dispositivo
            "/hp/device/info_specialpages.htm",  # Páginas de informações
            "/hp/device/info_eventlog.htm",  # Log de eventos
            "/hp/device/usage.htm",  # Uso geral
            "/hp/device/usage_info.htm",  # Informações de uso
            "/hp/device/usage_page.htm",  # Página de uso
            "/hp/device/usage_summary.htm",  # Resumo de uso
            "/hp/device/usage_statistics.htm",  # Estatísticas de uso
            "/hp/device/print_statistics.htm",  # Estatísticas de impressão
            "/hp/device/page_count.htm",  # Contagem de páginas
            "/hp/device/page_counters.htm",  # Contadores de páginas
            "/hp/device/print_counters.htm",  # Contadores de impressão
            "/hp/device/device_usage.htm",  # Uso do dispositivo
            "/hp/device/device_statistics.htm",  # Estatísticas do dispositivo
            "/hp/device/maintenance_info.htm",  # Informações de manutenção
            "/hp/device/maintenance_status.htm",  # Status de manutenção
            "/hp/device/supplies_status.htm",  # Status de suprimentos
            "/hp/device/supplies_info.htm",  # Informações de suprimentos
            "/hp/device/supplies_usage.htm",  # Uso de suprimentos
        ]
    
    def scan_usage_endpoints(self):
        """Escaneia endpoints relacionados a uso e impressões"""
        results = {}
        endpoints = self.get_usage_endpoints()
        
        print(f"Escaneando endpoints de uso e impressoes...")
        
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
                        'content': response.text[:4000]  # Primeiros 4000 caracteres
                    }
                    
                    # Extrair informações do HTML
                    if 'text/html' in response.headers.get('content-type', ''):
                        soup = BeautifulSoup(response.content, 'html.parser')
                        title = soup.find('title')
                        if title:
                            results[endpoint]['title'] = title.get_text().strip()
                        
                        # Extrair informações específicas de uso
                        self.extract_usage_info(soup, results[endpoint])
                        
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
    
    def extract_usage_info(self, soup, result_dict):
        """Extrai informações específicas de uso e impressões do HTML"""
        try:
            text_content = soup.get_text()
            
            # Informações de contadores de páginas
            page_counters = {}
            
            # Procurar por contadores de páginas
            page_patterns = [
                r'Total de páginas[:\s]*([0-9,]+)',
                r'Total pages[:\s]*([0-9,]+)',
                r'Páginas impressas[:\s]*([0-9,]+)',
                r'Pages printed[:\s]*([0-9,]+)',
                r'Contador de páginas[:\s]*([0-9,]+)',
                r'Page counter[:\s]*([0-9,]+)',
                r'Páginas totais[:\s]*([0-9,]+)',
                r'Total pages printed[:\s]*([0-9,]+)',
                r'([0-9,]+)\s*páginas',
                r'([0-9,]+)\s*pages'
            ]
            
            for pattern in page_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    page_counters['total_pages'] = matches[0].replace(',', '')
                    break
            
            # Procurar por tipos de impressão
            print_types = {}
            
            # Padrões para tipos de impressão
            type_patterns = [
                r'PCL[:\s]*([0-9,]+)',
                r'PostScript[:\s]*([0-9,]+)',
                r'PDF[:\s]*([0-9,]+)',
                r'JPEG[:\s]*([0-9,]+)',
                r'PNG[:\s]*([0-9,]+)',
                r'TIFF[:\s]*([0-9,]+)',
                r'Color[:\s]*([0-9,]+)',
                r'Preto e branco[:\s]*([0-9,]+)',
                r'Black and white[:\s]*([0-9,]+)',
                r'Monocromático[:\s]*([0-9,]+)',
                r'Monochrome[:\s]*([0-9,]+)'
            ]
            
            for pattern in type_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    print_types[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
            
            # Procurar por tamanhos de papel
            paper_sizes = {}
            
            size_patterns = [
                r'A4[:\s]*([0-9,]+)',
                r'A3[:\s]*([0-9,]+)',
                r'Letter[:\s]*([0-9,]+)',
                r'Legal[:\s]*([0-9,]+)',
                r'Executive[:\s]*([0-9,]+)',
                r'B4[:\s]*([0-9,]+)',
                r'A5[:\s]*([0-9,]+)',
                r'B5[:\s]*([0-9,]+)'
            ]
            
            for pattern in size_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    paper_sizes[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
            
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
            
            # Procurar por qualidade de impressão
            quality_stats = {}
            
            quality_patterns = [
                r'Rascunho[:\s]*([0-9,]+)',
                r'Draft[:\s]*([0-9,]+)',
                r'Normal[:\s]*([0-9,]+)',
                r'Normal[:\s]*([0-9,]+)',
                r'Alta qualidade[:\s]*([0-9,]+)',
                r'High quality[:\s]*([0-9,]+)',
                r'Máxima qualidade[:\s]*([0-9,]+)',
                r'Maximum quality[:\s]*([0-9,]+)'
            ]
            
            for pattern in quality_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    quality_stats[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
            
            # Procurar por informações de suprimentos
            supplies_info = {}
            
            supplies_patterns = [
                r'Toner[:\s]*([0-9]+)%',
                r'Cartucho[:\s]*([0-9]+)%',
                r'Cartridge[:\s]*([0-9]+)%',
                r'Nível[:\s]*([0-9]+)%',
                r'Level[:\s]*([0-9]+)%'
            ]
            
            for pattern in supplies_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    supplies_info['toner_level'] = matches[0]
                    break
            
            # Procurar por informações de manutenção
            maintenance_info = {}
            
            maintenance_patterns = [
                r'Limpeza[:\s]*([0-9,]+)',
                r'Cleaning[:\s]*([0-9,]+)',
                r'Alinhamento[:\s]*([0-9,]+)',
                r'Alignment[:\s]*([0-9,]+)',
                r'Calibração[:\s]*([0-9,]+)',
                r'Calibration[:\s]*([0-9,]+)'
            ]
            
            for pattern in maintenance_patterns:
                matches = re.findall(pattern, text_content, re.IGNORECASE)
                if matches:
                    maintenance_info[pattern.split(':')[0].lower()] = matches[0].replace(',', '')
            
            # Consolidar informações extraídas
            usage_info = {}
            
            if page_counters:
                usage_info['page_counters'] = page_counters
            if print_types:
                usage_info['print_types'] = print_types
            if paper_sizes:
                usage_info['paper_sizes'] = paper_sizes
            if orientations:
                usage_info['orientations'] = orientations
            if quality_stats:
                usage_info['quality_stats'] = quality_stats
            if supplies_info:
                usage_info['supplies_info'] = supplies_info
            if maintenance_info:
                usage_info['maintenance_info'] = maintenance_info
            
            if usage_info:
                result_dict['usage_info'] = usage_info
                
        except Exception as e:
            print(f"   Erro ao extrair informacoes de uso: {e}")
    
    def run_usage_scan(self):
        """Executa scan específico para informações de uso"""
        print(f"SCANNER DE INFORMACOES DE USO E IMPRESSOES")
        print("=" * 60)
        print(f"IP da impressora: {self.ip_address}")
        print("=" * 60)
        
        results = {
            'ip_address': self.ip_address,
            'scan_timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'printer_model': 'HP LaserJet P2055dn',
            'endpoints': {},
            'usage_summary': {},
            'print_statistics': {},
            'supplies_status': {},
            'maintenance_info': {}
        }
        
        # Escanear endpoints de uso
        results['endpoints'] = self.scan_usage_endpoints()
        
        # Consolidar informações
        self.consolidate_usage_info(results)
        
        # Salvar resultados
        self.save_results(results, "printer_usage_results.json")
        
        # Mostrar resumo
        self.show_usage_summary(results)
        
        return results
    
    def consolidate_usage_info(self, results):
        """Consolida informações de uso de todos os endpoints"""
        usage_summary = {}
        print_statistics = {}
        supplies_status = {}
        maintenance_info = {}
        
        for endpoint_data in results['endpoints'].values():
            if isinstance(endpoint_data, dict) and 'usage_info' in endpoint_data:
                usage_info = endpoint_data['usage_info']
                
                # Consolidar contadores de páginas
                if 'page_counters' in usage_info:
                    usage_summary.update(usage_info['page_counters'])
                
                # Consolidar estatísticas de impressão
                if 'print_types' in usage_info:
                    print_statistics.update(usage_info['print_types'])
                if 'paper_sizes' in usage_info:
                    print_statistics.update(usage_info['paper_sizes'])
                if 'orientations' in usage_info:
                    print_statistics.update(usage_info['orientations'])
                if 'quality_stats' in usage_info:
                    print_statistics.update(usage_info['quality_stats'])
                
                # Consolidar informações de suprimentos
                if 'supplies_info' in usage_info:
                    supplies_status.update(usage_info['supplies_info'])
                
                # Consolidar informações de manutenção
                if 'maintenance_info' in usage_info:
                    maintenance_info.update(usage_info['maintenance_info'])
        
        results['usage_summary'] = usage_summary
        results['print_statistics'] = print_statistics
        results['supplies_status'] = supplies_status
        results['maintenance_info'] = maintenance_info
    
    def save_results(self, data, filename="printer_usage_results.json"):
        """Salva os resultados em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Resultados salvos em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def show_usage_summary(self, results):
        """Mostra resumo das informações de uso"""
        print("\n" + "=" * 60)
        print("RESUMO DE USO E IMPRESSOES")
        print("=" * 60)
        print(f"IP da impressora: {results['ip_address']}")
        print(f"Modelo: {results['printer_model']}")
        
        total_endpoints = len(results['endpoints'])
        found_endpoints = len([k for k, v in results['endpoints'].items() if v.get('status_code') == 200])
        print(f"Endpoints testados: {total_endpoints}")
        print(f"Endpoints encontrados: {found_endpoints}")
        
        if results['usage_summary']:
            print("\nCONTADORES DE PAGINAS:")
            for key, value in results['usage_summary'].items():
                print(f"   {key}: {value}")
        
        if results['print_statistics']:
            print("\nESTATISTICAS DE IMPRESSAO:")
            for key, value in results['print_statistics'].items():
                print(f"   {key}: {value}")
        
        if results['supplies_status']:
            print("\nSTATUS DOS SUPRIMENTOS:")
            for key, value in results['supplies_status'].items():
                print(f"   {key}: {value}")
        
        if results['maintenance_info']:
            print("\nINFORMACOES DE MANUTENCAO:")
            for key, value in results['maintenance_info'].items():
                print(f"   {key}: {value}")
        
        print("\nENDPOINTS ENCONTRADOS:")
        for endpoint, data in results['endpoints'].items():
            if data.get('status_code') == 200:
                title = data.get('title', 'Sem titulo')
                print(f"   {endpoint} - {title}")

def main():
    """Função principal"""
    print("SCANNER DE INFORMACOES DE USO E IMPRESSOES")
    print("=" * 60)
    
    # Criar instância do scanner de uso
    scanner = PrinterUsageScanner("192.168.200.15")
    
    # Executar scan de uso
    results = scanner.run_usage_scan()

if __name__ == "__main__":
    main()




