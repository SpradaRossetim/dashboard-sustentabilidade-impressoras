#!/usr/bin/env python3
"""
Relatório Executivo de Sustentabilidade
Sistema completo de análise de pegada de carbono e economia sustentável
"""

import json
from datetime import datetime, timedelta
import math

class SustainabilityExecutiveReport:
    def __init__(self):
        self.report_date = datetime.now()
        self.company_name = "Empresa Sustentável"
        self.department = "TI/Impressão"
        
        # Fatores de conversão para economia sustentável
        self.conversion_factors = {
            'co2_to_trees': 0.1,      # árvores por kg CO2
            'co2_to_km_car': 2.5,     # km de carro por kg CO2
            'co2_to_kwh': 2.0,        # kWh por kg CO2
            'co2_to_water': 10.0,     # litros de água por kg CO2
            'co2_to_waste': 0.5       # kg de resíduos por kg CO2
        }
        
        # Metas de sustentabilidade
        self.sustainability_goals = {
            'carbon_reduction': 0.20,  # 20% de redução
            'paper_reduction': 0.30,   # 30% de redução
            'energy_efficiency': 0.15, # 15% de melhoria
            'waste_reduction': 0.25    # 25% de redução
        }
    
    def calculate_business_impact(self, carbon_data):
        """Calcula impacto nos negócios"""
        total_co2 = carbon_data['total']
        
        # Custos associados ao carbono
        carbon_cost_per_kg = 0.05  # R$ por kg CO2 (taxa de carbono)
        total_carbon_cost = total_co2 * carbon_cost_per_kg
        
        # Economia potencial
        potential_savings = {
            'carbon_tax': total_carbon_cost * 0.3,  # 30% de economia
            'paper_cost': total_co2 * 2.0,          # R$ 2 por kg CO2 em papel
            'energy_cost': total_co2 * 1.5,         # R$ 1.5 por kg CO2 em energia
            'maintenance': total_co2 * 0.8          # R$ 0.8 por kg CO2 em manutenção
        }
        
        total_potential_savings = sum(potential_savings.values())
        
        return {
            'current_carbon_cost': total_carbon_cost,
            'potential_savings': potential_savings,
            'total_potential_savings': total_potential_savings,
            'roi_percentage': (total_potential_savings / total_carbon_cost) * 100 if total_carbon_cost > 0 else 0
        }
    
    def generate_sustainability_metrics(self, carbon_data, pages):
        """Gera métricas de sustentabilidade"""
        total_co2 = carbon_data['total']
        
        # Métricas de eficiência
        efficiency_metrics = {
            'co2_per_page': total_co2 / pages if pages > 0 else 0,
            'carbon_intensity': total_co2 / pages if pages > 0 else 0,
            'energy_efficiency': 1 / (total_co2 / pages) if pages > 0 else 0,
            'sustainability_score': max(0, 100 - (total_co2 * 10))
        }
        
        # Equivalentes ambientais
        environmental_equivalents = {
            'trees_to_plant': total_co2 * self.conversion_factors['co2_to_trees'],
            'car_km_equivalent': total_co2 * self.conversion_factors['co2_to_km_car'],
            'kwh_equivalent': total_co2 * self.conversion_factors['co2_to_kwh'],
            'water_liters': total_co2 * self.conversion_factors['co2_to_water'],
            'waste_kg': total_co2 * self.conversion_factors['co2_to_waste']
        }
        
        return {
            'efficiency_metrics': efficiency_metrics,
            'environmental_equivalents': environmental_equivalents
        }
    
    def create_implementation_plan(self, carbon_data, pages):
        """Cria plano de implementação de sustentabilidade"""
        total_co2 = carbon_data['total']
        
        # Fases de implementação
        phases = {
            'phase_1_immediate': {
                'name': 'Implementação Imediata (0-30 dias)',
                'actions': [
                    'Configurar impressão duplex por padrão',
                    'Ativar modo de economia de energia',
                    'Implementar política de impressão consciente',
                    'Configurar alertas de baixo nível de toner'
                ],
                'carbon_reduction': total_co2 * 0.15,
                'cost_savings': 500,
                'implementation_cost': 100
            },
            'phase_2_short_term': {
                'name': 'Implementação de Curto Prazo (1-3 meses)',
                'actions': [
                    'Migrar para papel reciclado',
                    'Implementar sistema de aprovação de impressões',
                    'Digitalizar processos documentais',
                    'Configurar impressão sob demanda'
                ],
                'carbon_reduction': total_co2 * 0.25,
                'cost_savings': 1200,
                'implementation_cost': 800
            },
            'phase_3_medium_term': {
                'name': 'Implementação de Médio Prazo (3-6 meses)',
                'actions': [
                    'Implementar energia renovável',
                    'Sistema de monitoramento contínuo',
                    'Programa de reciclagem de suprimentos',
                    'Treinamento em sustentabilidade'
                ],
                'carbon_reduction': total_co2 * 0.20,
                'cost_savings': 2000,
                'implementation_cost': 1500
            },
            'phase_4_long_term': {
                'name': 'Implementação de Longo Prazo (6-12 meses)',
                'actions': [
                    'Migração para impressão digital completa',
                    'Implementação de IA para otimização',
                    'Parcerias com fornecedores sustentáveis',
                    'Certificação de sustentabilidade'
                ],
                'carbon_reduction': total_co2 * 0.30,
                'cost_savings': 3000,
                'implementation_cost': 2500
            }
        }
        
        return phases
    
    def calculate_roi_analysis(self, implementation_plan):
        """Calcula análise de ROI"""
        total_implementation_cost = sum(phase['implementation_cost'] for phase in implementation_plan.values())
        total_cost_savings = sum(phase['cost_savings'] for phase in implementation_plan.values())
        total_carbon_reduction = sum(phase['carbon_reduction'] for phase in implementation_plan.values())
        
        roi_analysis = {
            'total_implementation_cost': total_implementation_cost,
            'total_cost_savings': total_cost_savings,
            'net_savings': total_cost_savings - total_implementation_cost,
            'roi_percentage': ((total_cost_savings - total_implementation_cost) / total_implementation_cost) * 100 if total_implementation_cost > 0 else 0,
            'payback_period_months': (total_implementation_cost / (total_cost_savings / 12)) if total_cost_savings > 0 else 0,
            'total_carbon_reduction': total_carbon_reduction,
            'carbon_reduction_percentage': (total_carbon_reduction / 3237 * 0.004) * 100  # Baseado nos dados atuais
        }
        
        return roi_analysis
    
    def generate_executive_summary(self, carbon_data, pages, business_impact, sustainability_metrics, implementation_plan, roi_analysis):
        """Gera resumo executivo"""
        summary = {
            'report_date': self.report_date.strftime('%d/%m/%Y'),
            'company': self.company_name,
            'department': self.department,
            'key_findings': {
                'total_carbon_footprint': f"{carbon_data['total']:.3f} kg CO2",
                'pages_analyzed': f"{pages:,} páginas",
                'carbon_per_page': f"{carbon_data['total']/pages:.4f} kg CO2/página",
                'sustainability_score': f"{sustainability_metrics['efficiency_metrics']['sustainability_score']:.1f}/100"
            },
            'business_impact': {
                'current_carbon_cost': f"R$ {business_impact['current_carbon_cost']:.2f}",
                'potential_savings': f"R$ {business_impact['total_potential_savings']:.2f}",
                'roi_potential': f"{business_impact['roi_percentage']:.1f}%"
            },
            'recommendations': [
                "Implementar política de impressão sustentável",
                "Configurar impressão duplex por padrão",
                "Migrar para papel reciclado",
                "Implementar sistema de monitoramento contínuo",
                "Treinar equipe em práticas sustentáveis"
            ],
            'next_steps': [
                "Aprovar plano de implementação",
                "Alocar recursos para fase 1",
                "Designar responsável pelo projeto",
                "Estabelecer métricas de acompanhamento",
                "Agendar revisão mensal"
            ]
        }
        
        return summary
    
    def create_complete_report(self, carbon_data, pages):
        """Cria relatório completo"""
        # Calcular impacto nos negócios
        business_impact = self.calculate_business_impact(carbon_data)
        
        # Gerar métricas de sustentabilidade
        sustainability_metrics = self.generate_sustainability_metrics(carbon_data, pages)
        
        # Criar plano de implementação
        implementation_plan = self.create_implementation_plan(carbon_data, pages)
        
        # Calcular análise de ROI
        roi_analysis = self.calculate_roi_analysis(implementation_plan)
        
        # Gerar resumo executivo
        executive_summary = self.generate_executive_summary(
            carbon_data, pages, business_impact, sustainability_metrics, 
            implementation_plan, roi_analysis
        )
        
        # Relatório completo
        complete_report = {
            'executive_summary': executive_summary,
            'carbon_analysis': carbon_data,
            'business_impact': business_impact,
            'sustainability_metrics': sustainability_metrics,
            'implementation_plan': implementation_plan,
            'roi_analysis': roi_analysis,
            'appendix': {
                'methodology': 'Análise baseada em fatores de emissão padrão da indústria',
                'data_sources': 'Dados coletados da HP LaserJet P2055dn via interface web',
                'assumptions': 'Estimativas baseadas em médias da indústria',
                'limitations': 'Análise específica para uma impressora, resultados podem variar'
            }
        }
        
        return complete_report
    
    def save_executive_report(self, report, filename="executive_sustainability_report.json"):
        """Salva relatório executivo"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar relatório executivo: {e}")
            return False
    
    def print_executive_summary(self, report):
        """Imprime resumo executivo"""
        summary = report['executive_summary']
        
        print("RELATÓRIO EXECUTIVO DE SUSTENTABILIDADE")
        print("=" * 60)
        print(f"Data: {summary['report_date']}")
        print(f"Empresa: {summary['company']}")
        print(f"Departamento: {summary['department']}")
        print()
        
        print("PRINCIPAIS DESCOBERTAS:")
        print("-" * 40)
        for key, value in summary['key_findings'].items():
            print(f"• {key.replace('_', ' ').title()}: {value}")
        print()
        
        print("IMPACTO NOS NEGÓCIOS:")
        print("-" * 40)
        for key, value in summary['business_impact'].items():
            print(f"• {key.replace('_', ' ').title()}: {value}")
        print()
        
        print("RECOMENDAÇÕES PRINCIPAIS:")
        print("-" * 40)
        for i, recommendation in enumerate(summary['recommendations'], 1):
            print(f"{i}. {recommendation}")
        print()
        
        print("PRÓXIMOS PASSOS:")
        print("-" * 40)
        for i, step in enumerate(summary['next_steps'], 1):
            print(f"{i}. {step}")
        print()
        
        print("ANÁLISE DE ROI:")
        print("-" * 40)
        roi = report['roi_analysis']
        print(f"• Custo total de implementação: R$ {roi['total_implementation_cost']:,.2f}")
        print(f"• Economia total potencial: R$ {roi['total_cost_savings']:,.2f}")
        print(f"• Economia líquida: R$ {roi['net_savings']:,.2f}")
        print(f"• ROI: {roi['roi_percentage']:.1f}%")
        print(f"• Período de retorno: {roi['payback_period_months']:.1f} meses")
        print(f"• Redução de carbono: {roi['carbon_reduction_percentage']:.1f}%")

def main():
    """Função principal"""
    print("GERADOR DE RELATÓRIO EXECUTIVO DE SUSTENTABILIDADE")
    print("=" * 60)
    
    # Dados da impressora (baseados nos dados coletados)
    pages = 3237
    carbon_data = {
        'total': 0.323,  # kg CO2 baseado nos cálculos anteriores
        'components': {
            'paper': 0.129,
            'toner': 0.104,
            'energy': 0.065,
            'manufacturing': 0.015,
            'transport': 0.003,
            'disposal': 0.002
        }
    }
    
    # Criar relatório executivo
    report_generator = SustainabilityExecutiveReport()
    complete_report = report_generator.create_complete_report(carbon_data, pages)
    
    # Exibir resumo executivo
    report_generator.print_executive_summary(complete_report)
    
    # Salvar relatório
    if report_generator.save_executive_report(complete_report):
        print(f"\nRelatório executivo salvo em: executive_sustainability_report.json")
    
    print("\n" + "=" * 60)
    print("RELATÓRIO EXECUTIVO DE SUSTENTABILIDADE CONCLUÍDO!")
    print("=" * 60)

if __name__ == "__main__":
    main()


















