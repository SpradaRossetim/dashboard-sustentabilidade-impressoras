#!/usr/bin/env python3
"""
Calculadora de Pegada de Carbono para Impressora
Projeto de Economia Sustentável
"""

import json
import time
from datetime import datetime, timedelta
import math

class CarbonFootprintCalculator:
    def __init__(self):
        # Fatores de emissão de carbono (kg CO2 por unidade)
        self.carbon_factors = {
            'paper_a4': 0.004,  # kg CO2 por página A4
            'toner_black': 0.08,  # kg CO2 por grama de toner
            'electricity': 0.0817,  # kg CO2 por kWh - ONS Brasil 2023 (matriz energética brasileira)
            'manufacturing': 0.02,  # kg CO2 por página (fabricação da impressora)
            'transport': 0.001,  # kg CO2 por página (transporte)
            'disposal': 0.0005   # kg CO2 por página (descarte)
        }
        
        # Consumo de energia da HP LaserJet P2055dn
        self.energy_consumption = {
            'printing': 0.5,  # kWh por 1000 páginas
            'standby': 0.05,  # kWh por hora em standby
            'idle': 0.1       # kWh por hora em idle
        }
        
        # Dados da impressora
        self.printer_data = {
            'model': 'HP LaserJet P2055dn',
            'pages_per_toner': 2500,  # páginas por cartucho
            'toner_weight': 100,      # gramas por cartucho
            'lifespan_years': 5,      # vida útil da impressora
            'recyclability': 0.85     # % de materiais recicláveis
        }
    
    def calculate_paper_carbon_footprint(self, pages):
        """Calcula pegada de carbono do papel"""
        return pages * self.carbon_factors['paper_a4']
    
    def calculate_toner_carbon_footprint(self, pages):
        """Calcula pegada de carbono do toner"""
        toner_used = (pages / self.printer_data['pages_per_toner']) * self.printer_data['toner_weight']
        return toner_used * self.carbon_factors['toner_black']
    
    def calculate_energy_carbon_footprint(self, pages, hours_standby=0, hours_idle=0):
        """Calcula pegada de carbono do consumo de energia"""
        printing_energy = (pages / 1000) * self.energy_consumption['printing']
        standby_energy = hours_standby * self.energy_consumption['standby']
        idle_energy = hours_idle * self.energy_consumption['idle']
        
        total_energy = printing_energy + standby_energy + idle_energy
        return total_energy * self.carbon_factors['electricity']
    
    def calculate_manufacturing_carbon_footprint(self, pages):
        """Calcula pegada de carbono da fabricação"""
        return pages * self.carbon_factors['manufacturing']
    
    def calculate_transport_carbon_footprint(self, pages):
        """Calcula pegada de carbono do transporte"""
        return pages * self.carbon_factors['transport']
    
    def calculate_disposal_carbon_footprint(self, pages):
        """Calcula pegada de carbono do descarte"""
        return pages * self.carbon_factors['disposal']
    
    def calculate_total_carbon_footprint(self, pages, hours_standby=0, hours_idle=0):
        """Calcula pegada de carbono total"""
        components = {
            'paper': self.calculate_paper_carbon_footprint(pages),
            'toner': self.calculate_toner_carbon_footprint(pages),
            'energy': self.calculate_energy_carbon_footprint(pages, hours_standby, hours_idle),
            'manufacturing': self.calculate_manufacturing_carbon_footprint(pages),
            'transport': self.calculate_transport_carbon_footprint(pages),
            'disposal': self.calculate_disposal_carbon_footprint(pages)
        }
        
        total = sum(components.values())
        
        return {
            'total': total,
            'components': components,
            'pages': pages
        }
    
    def calculate_equivalent_impacts(self, total_co2_kg):
        """Calcula equivalentes de impacto ambiental"""
        equivalents = {
            'km_car': total_co2_kg * 2.5,  # km de carro (média 0.4 kg CO2/km)
            'trees_planted': total_co2_kg * 0.1,  # árvores para compensar
            'lightbulb_hours': total_co2_kg * 100,  # horas de lâmpada LED
            'shower_minutes': total_co2_kg * 5,  # minutos de banho quente
            'smartphone_charges': total_co2_kg * 200  # carregamentos de smartphone
        }
        return equivalents
    
    def generate_sustainability_report(self, pages, hours_standby=0, hours_idle=0):
        """Gera relatório completo de sustentabilidade"""
        carbon_data = self.calculate_total_carbon_footprint(pages, hours_standby, hours_idle)
        equivalents = self.calculate_equivalent_impacts(carbon_data['total'])
        
        report = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'printer_info': self.printer_data,
            'usage_data': {
                'pages_printed': pages,
                'hours_standby': hours_standby,
                'hours_idle': hours_idle
            },
            'carbon_footprint': carbon_data,
            'environmental_equivalents': equivalents,
            'sustainability_metrics': self.calculate_sustainability_metrics(carbon_data, pages),
            'recommendations': self.generate_recommendations(carbon_data, pages)
        }
        
        return report
    
    def calculate_sustainability_metrics(self, carbon_data, pages):
        """Calcula métricas de sustentabilidade"""
        total_co2 = carbon_data['total']
        
        metrics = {
            'co2_per_page': total_co2 / pages if pages > 0 else 0,
            'efficiency_score': max(0, 100 - (total_co2 * 10)),  # Score de 0-100
            'carbon_intensity': total_co2 / pages if pages > 0 else 0,
            'renewable_potential': total_co2 * 0.3,  # Potencial de redução com energia renovável
            'recycling_benefit': total_co2 * 0.15   # Benefício da reciclagem
        }
        
        return metrics
    
    def generate_recommendations(self, carbon_data, pages):
        """Gera recomendações de sustentabilidade"""
        recommendations = []
        
        # Análise por componente
        components = carbon_data['components']
        
        if components['paper'] > components['toner']:
            recommendations.append("Considere imprimir frente e verso para reduzir uso de papel")
            recommendations.append("Use papel reciclado para reduzir pegada de carbono em 30%")
        
        if components['energy'] > components['paper']:
            recommendations.append("Configure modo de economia de energia")
            recommendations.append("Desligue a impressora quando não estiver em uso")
        
        if components['toner'] > 0.1:
            recommendations.append("Use modo de rascunho para documentos internos")
            recommendations.append("Considere impressão em escala de cinza")
        
        # Recomendações gerais
        recommendations.extend([
            "Implemente política de impressão consciente",
            "Use serviços de impressão sob demanda",
            "Digitalize documentos quando possível",
            "Configure impressão duplex por padrão",
            "Monitore regularmente o consumo de suprimentos"
        ])
        
        return recommendations
    
    def save_report(self, report, filename="carbon_footprint_report.json"):
        """Salva relatório em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao salvar relatório: {e}")
            return False

def main():
    """Função principal"""
    print("CALCULADORA DE PEGADA DE CARBONO - IMPRESSORA")
    print("=" * 60)
    
    calculator = CarbonFootprintCalculator()
    
    # Dados da impressora (baseados nos dados coletados)
    pages_printed = 3237  # Total de páginas impressas
    hours_standby = 24 * 30  # Estimativa: 30 dias em standby
    hours_idle = 24 * 5     # Estimativa: 5 dias em idle
    
    print(f"Analisando pegada de carbono da HP LaserJet P2055dn")
    print(f"Páginas impressas: {pages_printed:,}")
    print(f"Horas em standby: {hours_standby:,}")
    print(f"Horas em idle: {hours_idle:,}")
    print()
    
    # Gerar relatório
    report = calculator.generate_sustainability_report(pages_printed, hours_standby, hours_idle)
    
    # Exibir resultados
    carbon_data = report['carbon_footprint']
    equivalents = report['environmental_equivalents']
    metrics = report['sustainability_metrics']
    
    print("RESULTADOS DA PEGADA DE CARBONO:")
    print("-" * 40)
    print(f"Total de CO2: {carbon_data['total']:.3f} kg")
    print(f"CO2 por página: {metrics['co2_per_page']:.4f} kg")
    print(f"Score de eficiência: {metrics['efficiency_score']:.1f}/100")
    print()
    
    print("COMPONENTES DA PEGADA DE CARBONO:")
    print("-" * 40)
    for component, value in carbon_data['components'].items():
        percentage = (value / carbon_data['total']) * 100
        print(f"{component.capitalize()}: {value:.3f} kg ({percentage:.1f}%)")
    print()
    
    print("EQUIVALENTES AMBIENTAIS:")
    print("-" * 40)
    print(f"Quilômetros de carro: {equivalents['km_car']:.1f} km")
    print(f"Árvores para compensar: {equivalents['trees_planted']:.1f}")
    print(f"Horas de lâmpada LED: {equivalents['lightbulb_hours']:.0f} horas")
    print(f"Minutos de banho quente: {equivalents['shower_minutes']:.0f} minutos")
    print()
    
    print("RECOMENDAÇÕES DE SUSTENTABILIDADE:")
    print("-" * 40)
    for i, recommendation in enumerate(report['recommendations'], 1):
        print(f"{i}. {recommendation}")
    
    # Salvar relatório
    if calculator.save_report(report):
        print(f"\nRelatório salvo em: carbon_footprint_report.json")
    
    print("\n" + "=" * 60)
    print("ANÁLISE DE SUSTENTABILIDADE CONCLUÍDA!")
    print("=" * 60)

if __name__ == "__main__":
    main()




