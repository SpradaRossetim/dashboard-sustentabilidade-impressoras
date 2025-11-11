#!/usr/bin/env python3
"""
PROJETO COMPLETO DE ECONOMIA SUSTENTÁVEL
Sistema integrado de monitoramento e análise de pegada de carbono
para impressoras corporativas
"""

import json
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

class ProjetoSustentabilidadeCompleto:
    def __init__(self, ip_address="192.168.200.15"):
        self.ip_address = ip_address
        self.base_url = f"http://{ip_address}"
        self.session = requests.Session()
        self.session.timeout = 10
        
        # Headers para requisições
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        
        # Fatores de sustentabilidade
        self.sustainability_factors = {
            'paper_recycled': 0.7,
            'duplex_printing': 0.5,
            'eco_mode': 0.3,
            'digital_documents': 0.8,
            'renewable_energy': 0.4
        }
    
    def coletar_dados_impressora(self):
        """Coleta dados atuais da impressora"""
        try:
            url = f"{self.base_url}/hp/device/info_configuration.htm"
            response = self.session.get(url, timeout=5)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                text_content = soup.get_text()
                
                # Extrair contador de páginas
                page_patterns = [
                    r'Total de páginas[:\s]*([0-9,]+)',
                    r'Total pages[:\s]*([0-9,]+)',
                    r'([0-9,]+)\s*páginas',
                    r'([0-9,]+)\s*pages'
                ]
                
                pages = 0
                for pattern in page_patterns:
                    matches = re.findall(pattern, text_content, re.IGNORECASE)
                    if matches:
                        pages = int(matches[0].replace(',', ''))
                        break
                
                return {
                    'pages_printed': pages,
                    'timestamp': datetime.now().isoformat(),
                    'status': 'online'
                }
            else:
                return {'status': 'offline', 'error': f'HTTP {response.status_code}'}
                
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def calcular_pegada_carbono(self, pages):
        """Calcula pegada de carbono baseada nas páginas impressas"""
        # Fatores de emissão (kg CO2 por página)
        factors = {
            'paper': 0.004,
            'toner': 0.0032,
            'energy': 0.0077,
            'manufacturing': 0.02,
            'transport': 0.001,
            'disposal': 0.0005
        }
        
        components = {}
        for component, factor in factors.items():
            components[component] = pages * factor
        
        total = sum(components.values())
        
        return {
            'total': total,
            'components': components,
            'pages': pages
        }
    
    def calcular_economia_sustentavel(self, carbon_data):
        """Calcula economia sustentável potencial"""
        total_co2 = carbon_data['total']
        
        # Economia por ação sustentável
        savings = {
            'paper_recycled': total_co2 * 0.3,  # 30% de redução
            'duplex_printing': total_co2 * 0.5,  # 50% de redução
            'eco_mode': total_co2 * 0.2,        # 20% de redução
            'digital_documents': total_co2 * 0.6, # 60% de redução
            'renewable_energy': total_co2 * 0.4  # 40% de redução
        }
        
        # Economia financeira (R$ por kg CO2)
        financial_savings = {
            'carbon_tax': total_co2 * 0.05,
            'paper_cost': total_co2 * 2.0,
            'energy_cost': total_co2 * 1.5,
            'maintenance': total_co2 * 0.8
        }
        
        return {
            'carbon_savings': savings,
            'financial_savings': financial_savings,
            'total_carbon_savings': sum(savings.values()),
            'total_financial_savings': sum(financial_savings.values())
        }
    
    def gerar_plano_acao(self, carbon_data, pages):
        """Gera plano de ação para sustentabilidade"""
        total_co2 = carbon_data['total']
        
        plan = {
            'imediato': {
                'nome': 'Ações Imediatas (0-30 dias)',
                'acoes': [
                    'Configurar impressão duplex por padrão',
                    'Ativar modo de economia de energia',
                    'Implementar política de impressão consciente',
                    'Configurar alertas de baixo nível de toner'
                ],
                'reducao_co2': total_co2 * 0.15,
                'economia_financeira': 500,
                'custo_implementacao': 100,
                'dificuldade': 'Baixa'
            },
            'curto_prazo': {
                'nome': 'Ações de Curto Prazo (1-3 meses)',
                'acoes': [
                    'Migrar para papel reciclado',
                    'Implementar sistema de aprovação de impressões',
                    'Digitalizar processos documentais',
                    'Configurar impressão sob demanda'
                ],
                'reducao_co2': total_co2 * 0.25,
                'economia_financeira': 1200,
                'custo_implementacao': 800,
                'dificuldade': 'Média'
            },
            'medio_prazo': {
                'nome': 'Ações de Médio Prazo (3-6 meses)',
                'acoes': [
                    'Implementar energia renovável',
                    'Sistema de monitoramento contínuo',
                    'Programa de reciclagem de suprimentos',
                    'Treinamento em sustentabilidade'
                ],
                'reducao_co2': total_co2 * 0.20,
                'economia_financeira': 2000,
                'custo_implementacao': 1500,
                'dificuldade': 'Alta'
            },
            'longo_prazo': {
                'nome': 'Ações de Longo Prazo (6-12 meses)',
                'acoes': [
                    'Migração para impressão digital completa',
                    'Implementação de IA para otimização',
                    'Parcerias com fornecedores sustentáveis',
                    'Certificação de sustentabilidade'
                ],
                'reducao_co2': total_co2 * 0.30,
                'economia_financeira': 3000,
                'custo_implementacao': 2500,
                'dificuldade': 'Muito Alta'
            }
        }
        
        return plan
    
    def calcular_roi_completo(self, plano_acao):
        """Calcula ROI completo do projeto"""
        total_custo = sum(fase['custo_implementacao'] for fase in plano_acao.values())
        total_economia = sum(fase['economia_financeira'] for fase in plano_acao.values())
        total_reducao_co2 = sum(fase['reducao_co2'] for fase in plano_acao.values())
        
        roi = {
            'custo_total_implementacao': total_custo,
            'economia_total_potencial': total_economia,
            'economia_liquida': total_economia - total_custo,
            'roi_percentual': ((total_economia - total_custo) / total_custo) * 100 if total_custo > 0 else 0,
            'periodo_retorno_meses': (total_custo / (total_economia / 12)) if total_economia > 0 else 0,
            'reducao_total_co2': total_reducao_co2,
            'reducao_percentual_co2': (total_reducao_co2 / 117.711) * 100  # Baseado nos dados atuais
        }
        
        return roi
    
    def gerar_relatorio_completo(self):
        """Gera relatório completo do projeto"""
        print("PROJETO COMPLETO DE ECONOMIA SUSTENTÁVEL")
        print("=" * 60)
        print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Impressora: HP LaserJet P2055dn ({self.ip_address})")
        print("=" * 60)
        
        # Coletar dados atuais
        print("Coletando dados da impressora...")
        dados_impressora = self.coletar_dados_impressora()
        
        if dados_impressora.get('status') != 'online':
            print(f"Erro: {dados_impressora.get('error', 'Impressora offline')}")
            return
        
        pages = dados_impressora['pages_printed']
        print(f"Páginas impressas: {pages:,}")
        
        # Calcular pegada de carbono
        print("\nCalculando pegada de carbono...")
        carbon_data = self.calcular_pegada_carbono(pages)
        
        # Calcular economia sustentável
        print("Calculando economia sustentável...")
        economia = self.calcular_economia_sustentavel(carbon_data)
        
        # Gerar plano de ação
        print("Gerando plano de ação...")
        plano_acao = self.gerar_plano_acao(carbon_data, pages)
        
        # Calcular ROI
        print("Calculando ROI...")
        roi = self.calcular_roi_completo(plano_acao)
        
        # Exibir resultados
        self.exibir_resultados(carbon_data, economia, plano_acao, roi)
        
        # Salvar relatório
        relatorio = {
            'timestamp': datetime.now().isoformat(),
            'dados_impressora': dados_impressora,
            'pegada_carbono': carbon_data,
            'economia_sustentavel': economia,
            'plano_acao': plano_acao,
            'roi': roi
        }
        
        self.salvar_relatorio(relatorio)
        
        return relatorio
    
    def exibir_resultados(self, carbon_data, economia, plano_acao, roi):
        """Exibe resultados do projeto"""
        print("\n" + "=" * 60)
        print("RESULTADOS DO PROJETO DE SUSTENTABILIDADE")
        print("=" * 60)
        
        # Pegada de carbono
        print(f"\nPEGADA DE CARBONO ATUAL:")
        print("-" * 40)
        print(f"Total: {carbon_data['total']:.3f} kg CO2")
        print(f"Por página: {carbon_data['total']/carbon_data['pages']:.4f} kg CO2")
        
        print("\nComponentes:")
        for component, value in carbon_data['components'].items():
            percentage = (value / carbon_data['total']) * 100
            print(f"  {component.capitalize()}: {value:.3f} kg ({percentage:.1f}%)")
        
        # Economia sustentável
        print(f"\nECONOMIA SUSTENTÁVEL POTENCIAL:")
        print("-" * 40)
        print(f"Redução total de CO2: {economia['total_carbon_savings']:.3f} kg")
        print(f"Economia financeira: R$ {economia['total_financial_savings']:.2f}")
        
        print("\nEconomia por ação:")
        for action, savings in economia['carbon_savings'].items():
            print(f"  {action.replace('_', ' ').title()}: {savings:.3f} kg CO2")
        
        # ROI
        print(f"\nANÁLISE DE ROI:")
        print("-" * 40)
        print(f"Custo total: R$ {roi['custo_total_implementacao']:,.2f}")
        print(f"Economia total: R$ {roi['economia_total_potencial']:,.2f}")
        print(f"Economia líquida: R$ {roi['economia_liquida']:,.2f}")
        print(f"ROI: {roi['roi_percentual']:.1f}%")
        print(f"Período de retorno: {roi['periodo_retorno_meses']:.1f} meses")
        print(f"Redução de CO2: {roi['reducao_percentual_co2']:.1f}%")
        
        # Plano de ação
        print(f"\nPLANO DE AÇÃO:")
        print("-" * 40)
        for fase, dados in plano_acao.items():
            print(f"\n{dados['nome']}:")
            print(f"  Dificuldade: {dados['dificuldade']}")
            print(f"  Redução CO2: {dados['reducao_co2']:.3f} kg")
            print(f"  Economia: R$ {dados['economia_financeira']:,.2f}")
            print(f"  Custo: R$ {dados['custo_implementacao']:,.2f}")
            print("  Ações:")
            for acao in dados['acoes']:
                print(f"    • {acao}")
    
    def salvar_relatorio(self, relatorio):
        """Salva relatório completo"""
        filename = f"projeto_sustentabilidade_completo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(relatorio, f, indent=2, ensure_ascii=False)
            print(f"\nRelatório salvo em: {filename}")
        except Exception as e:
            print(f"Erro ao salvar relatório: {e}")

def main():
    """Função principal"""
    projeto = ProjetoSustentabilidadeCompleto("192.168.200.15")
    relatorio = projeto.gerar_relatorio_completo()
    
    print("\n" + "=" * 60)
    print("PROJETO DE ECONOMIA SUSTENTÁVEL CONCLUÍDO!")
    print("=" * 60)
    
    print("\nPRÓXIMOS PASSOS RECOMENDADOS:")
    print("-" * 40)
    print("1. Apresentar resultados para a diretoria")
    print("2. Aprovar orçamento para implementação")
    print("3. Designar responsável pelo projeto")
    print("4. Implementar ações imediatas")
    print("5. Estabelecer métricas de acompanhamento")
    print("6. Agendar revisões mensais")
    print("7. Expandir para outras impressoras")
    print("8. Buscar certificações de sustentabilidade")

if __name__ == "__main__":
    main()


















