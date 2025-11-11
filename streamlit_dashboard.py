#!/usr/bin/env python3
"""
Dashboard Web de Sustentabilidade - Streamlit
Sistema completo de monitoramento e análise de pegada de carbono
"""

import streamlit as st
import json
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import time
import io
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Sustentabilidade",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card, .carbon-footprint, .savings-potential, .sustainability-score {
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-sizing: border-box;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .sustainability-score {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    }
    .carbon-footprint {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
    }
    .savings-potential {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    .metric-card h3, .carbon-footprint h3, .savings-potential h3, .sustainability-score h3 {
        font-size: 1.2rem;
        margin: 0 0 0.5rem 0;
        padding: 0;
    }
    .metric-card h2, .carbon-footprint h2, .savings-potential h2, .sustainability-score h2 {
        font-size: 2.5rem;
        margin: 0.5rem 0;
        padding: 0;
    }
    .metric-card p, .carbon-footprint p, .savings-potential p, .sustainability-score p {
        font-size: 0.85rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
        padding: 0;
    }
    .info-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

class SustainabilityDashboard:
    def __init__(self):
        self.ip_address = "192.168.200.15"
        self.base_url = f"http://{self.ip_address}"
        self.session = requests.Session()
        self.session.timeout = 10
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        
        # Fatores de emissão
        self.carbon_factors = {
            'paper': 0.004,
            'toner': 0.0032,
            'energy': 0.0077,
            'manufacturing': 0.02,
            'transport': 0.001,
            'disposal': 0.0005
        }
    
    def get_printer_data(self):
        """Coleta dados da impressora"""
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
    
    def calculate_carbon_footprint(self, pages):
        """Calcula pegada de carbono"""
        components = {}
        for component, factor in self.carbon_factors.items():
            if component == 'toner':
                toner_used = (pages / 2500) * 100
                components[component] = toner_used * factor
            elif component == 'energy':
                printing_energy = (pages / 1000) * 0.5
                standby_energy = 720 * 0.05
                idle_energy = 120 * 0.1
                total_energy = printing_energy + standby_energy + idle_energy
                # Fator ONS Brasil 2023: 0.0817 kg CO₂/kWh (matriz energética brasileira)
                components[component] = total_energy * 0.0817
            else:
                components[component] = pages * factor
        
        total = sum(components.values())
        return {'total': total, 'components': components, 'pages': pages}
    
    def calculate_sustainability_metrics(self, carbon_data):
        """Calcula métricas de sustentabilidade"""
        total_co2 = carbon_data['total']
        pages = carbon_data['pages']
        
        # Fatores de redução
        reduction_factors = {
            'paper_recycled': 0.3,
            'duplex_printing': 0.5,
            'eco_mode': 0.2,
            'digital_documents': 0.6,
            'renewable_energy': 0.4
        }
        
        savings = {}
        for action, factor in reduction_factors.items():
            savings[action] = total_co2 * factor
        
        total_savings = sum(savings.values())
        
        # ROI
        implementation_cost = 4900
        financial_savings = total_co2 * 0.5  # R$ 0.5 por kg CO2
        roi = ((financial_savings - implementation_cost) / implementation_cost) * 100
        
        return {
            'total_savings': total_savings,
            'savings_breakdown': savings,
            'roi': roi,
            'sustainability_score': max(0, 100 - (total_co2 * 0.1)),
            'co2_per_page': total_co2 / pages if pages > 0 else 0
        }
    
    def get_environmental_equivalents(self, total_co2):
        """Calcula equivalentes ambientais"""
        return {
            'car_km': total_co2 * 2.5,
            'trees': total_co2 * 0.1,
            'lightbulb_hours': total_co2 * 100,
            'shower_minutes': total_co2 * 5
        }

def main():
    """Função principal do dashboard"""
    
    # Header
    st.markdown('<h1 class="main-header">🌱 Dashboard de Sustentabilidade</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Monitoramento de Pegada de Carbono - HP LaserJet P2055dn</p>', unsafe_allow_html=True)
    
    # Resumo explicativo
    with st.expander("ℹ️ Sobre este Dashboard", expanded=False):
        st.markdown("""
        ### O que é este dashboard?
        Este é um sistema de monitoramento ambiental que calcula e visualiza o impacto de carbono 
        das operações de impressão da sua organização.
        
        ### Como funciona?
        - **Coleta dados** da impressora HP LaserJet P2055dn em tempo real
        - **Calcula** a pegada de carbono considerando múltiplos fatores
        - **Apresenta** visualizações interativas e recomendações práticas
        - **Sugere** ações para reduzir o impacto ambiental
        
        ### Por que é importante?
        Cada página impressa tem um impacto ambiental. Este dashboard ajuda a:
        - ✅ Entender o impacto real das operações de impressão
        - ✅ Identificar oportunidades de economia
        - ✅ Tomar decisões baseadas em dados
        - ✅ Contribuir para um futuro mais sustentável
        """)
    
    # Sidebar
    st.sidebar.title("🎛️ Controles")
    st.sidebar.markdown("---")
    
    # Botão para atualizar dados
    if st.sidebar.button("🔄 Atualizar Dados", use_container_width=True):
        st.rerun()
    
    st.sidebar.markdown("---")
    
    # Seção de Exportação de Dados
    st.sidebar.markdown("### 💾 Exportar Dados")
    
    # Calcular métricas para exportação (será usado depois)
    dashboard = SustainabilityDashboard()
    with st.spinner("Coletando dados da impressora..."):
        printer_data = dashboard.get_printer_data()
    
    if printer_data.get('status') != 'online':
        pages = 15000  # Dados simulados
    else:
        pages = printer_data['pages_printed']
    
    carbon_data_export = dashboard.calculate_carbon_footprint(pages)
    sustainability_metrics_export = dashboard.calculate_sustainability_metrics(carbon_data_export)
    environmental_equivalents_export = dashboard.get_environmental_equivalents(carbon_data_export['total'])
    
    # Preparar dados para exportação
    export_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'pages_printed': pages,
        'carbon_footprint': {
            'total': carbon_data_export['total'],
            'components': carbon_data_export['components']
        },
        'sustainability_metrics': sustainability_metrics_export,
        'environmental_equivalents': environmental_equivalents_export
    }
    
    # Botões de exportação
    col_exp1, col_exp2 = st.sidebar.columns(2)
    
    with col_exp1:
        # Exportar CSV
        csv_data = export_to_csv(export_data)
        st.download_button(
            label="📊 CSV",
            data=csv_data,
            file_name=f"dados_sustentabilidade_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col_exp2:
        # Exportar JSON
        json_data = export_to_json(export_data)
        st.download_button(
            label="📋 JSON",
            data=json_data,
            file_name=f"dados_sustentabilidade_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    st.sidebar.markdown("---")
    
    # Seleção de visualização
    st.sidebar.markdown("### 📊 Navegação")
    view_option = st.sidebar.selectbox(
        "Selecione a visualização:",
        ["Dashboard Principal", "Análise Detalhada", "Plano de Ação", "Métricas de Sustentabilidade"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📖 Guia Rápido")
    st.sidebar.markdown("""
    **Dashboard Principal**  
    Visão geral das métricas principais
    
    **Análise Detalhada**  
    Análise aprofundada por componente
    
    **Plano de Ação**  
    Sugestões práticas de redução
    
    **Métricas de Sustentabilidade**  
    Score e objetivos ambientais
    """)
    
    # Reutilizar dados já coletados acima (para evitar duplicação)
    if printer_data.get('status') != 'online':
        st.warning(f"⚠️ Impressora não conectada: {printer_data.get('error', 'Impressora offline')}")
        st.info("📊 Mostrando dados simulados para demonstração")
        pages = 15000  # Dados simulados
    else:
        pages = printer_data['pages_printed']
    
    # Calcular métricas (reutilizar dados já calculados)
    carbon_data = carbon_data_export
    sustainability_metrics = sustainability_metrics_export
    environmental_equivalents = environmental_equivalents_export
    
    # Dashboard Principal
    if view_option == "Dashboard Principal":
        show_main_dashboard(carbon_data, sustainability_metrics, environmental_equivalents, pages)
    
    # Análise Detalhada
    elif view_option == "Análise Detalhada":
        show_detailed_analysis(carbon_data, sustainability_metrics)
    
    # Plano de Ação
    elif view_option == "Plano de Ação":
        show_action_plan(carbon_data, sustainability_metrics)
    
    # Métricas de Sustentabilidade
    elif view_option == "Métricas de Sustentabilidade":
        show_sustainability_metrics(sustainability_metrics, environmental_equivalents)

def show_main_dashboard(carbon_data, sustainability_metrics, environmental_equivalents, pages):
    """Mostra dashboard principal"""
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📄 Páginas Impressas</h3>
            <h2>{pages:,}</h2>
            <p>Total acumulado de páginas impressas pela HP LaserJet P2055dn</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="carbon-footprint">
            <h3>🌍 Pegada de Carbono</h3>
            <h2>{carbon_data['total']:.1f} kg CO₂</h2>
            <p>Emissões totais considerando papel, toner, energia e fabricação</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="savings-potential">
            <h3>💰 Economia Potencial</h3>
            <h2>R$ {sustainability_metrics['total_savings'] * 0.5:.0f}</h2>
            <p>Economia financeira possível com ações sustentáveis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="sustainability-score">
            <h3>🌱 Score Sustentabilidade</h3>
            <h2>{sustainability_metrics['sustainability_score']:.0f}/100</h2>
            <p>Índice de eficiência ambiental das operações de impressão</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Informação sobre os gráficos
    st.markdown("""
    <div class="info-box">
        <h4>📊 Como interpretar os dados abaixo:</h4>
        <p><strong>Componentes da Pegada de Carbono:</strong> Mostra a distribuição das emissões de CO₂ por categoria (papel, toner, energia, etc.)</p>
        <p><strong>Economia Potencial:</strong> Indica quanto de CO₂ pode ser reduzido com a implementação de cada ação sustentável</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de componentes da pegada de carbono
        components_df = pd.DataFrame([
            {'Componente': 'Papel', 'CO₂ (kg)': carbon_data['components']['paper']},
            {'Componente': 'Toner', 'CO₂ (kg)': carbon_data['components']['toner']},
            {'Componente': 'Energia', 'CO₂ (kg)': carbon_data['components']['energy']},
            {'Componente': 'Fabricação', 'CO₂ (kg)': carbon_data['components']['manufacturing']},
            {'Componente': 'Transporte', 'CO₂ (kg)': carbon_data['components']['transport']},
            {'Componente': 'Descarte', 'CO₂ (kg)': carbon_data['components']['disposal']}
        ])
        
        fig_pie = px.pie(components_df, values='CO₂ (kg)', names='Componente', 
                        title="🌍 Componentes da Pegada de Carbono",
                        color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig_pie, use_container_width=True)
        st.info("💡 **Dica:** O componente com maior percentual é onde você pode focar para obter maiores reduções de emissões.")
    
    with col2:
        # Gráfico de economia potencial
        savings_df = pd.DataFrame([
            {'Ação': 'Papel Reciclado', 'Redução (kg CO₂)': sustainability_metrics['savings_breakdown']['paper_recycled']},
            {'Ação': 'Impressão Duplex', 'Redução (kg CO₂)': sustainability_metrics['savings_breakdown']['duplex_printing']},
            {'Ação': 'Modo Ecológico', 'Redução (kg CO₂)': sustainability_metrics['savings_breakdown']['eco_mode']},
            {'Ação': 'Documentos Digitais', 'Redução (kg CO₂)': sustainability_metrics['savings_breakdown']['digital_documents']},
            {'Ação': 'Energia Renovável', 'Redução (kg CO₂)': sustainability_metrics['savings_breakdown']['renewable_energy']}
        ])
        
        fig_bar = px.bar(savings_df, x='Ação', y='Redução (kg CO₂)',
                        title="💰 Economia Potencial por Ação",
                        color='Redução (kg CO₂)',
                        color_continuous_scale='Viridis')
        fig_bar.update_xaxes(tickangle=45)
        st.plotly_chart(fig_bar, use_container_width=True)
        st.info("💡 **Dica:** As barras mais altas representam ações com maior potencial de redução de emissões.")
    
    st.markdown("---")
    
    # Equivalentes ambientais
    st.markdown("### 🌍 Equivalentes Ambientais")
    st.markdown("""
    <div class="info-box">
        <p>Para facilitar a compreensão, sua pegada de carbono é equivalente a:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🚗 Quilômetros de Carro", f"{environmental_equivalents['car_km']:.0f} km", 
                  help="Distância percorrida de carro que geraria a mesma quantidade de CO₂")
    
    with col2:
        st.metric("🌳 Árvores para Compensar", f"{environmental_equivalents['trees']:.0f}",
                  help="Número de árvores necessárias para absorver esse CO₂ em um ano")
    
    with col3:
        st.metric("💡 Horas de Lâmpada LED", f"{environmental_equivalents['lightbulb_hours']:.0f} h",
                  help="Horas de uso de uma lâmpada LED de 10W que consumiriam a mesma energia")
    
    with col4:
        st.metric("🚿 Minutos de Banho Quente", f"{environmental_equivalents['shower_minutes']:.0f} min",
                  help="Minutos de banho quente com chuveiro elétrico equivalente em consumo energético")

def show_detailed_analysis(carbon_data, sustainability_metrics):
    """Mostra análise detalhada"""
    
    st.markdown("## 📊 Análise Detalhada da Pegada de Carbono")
    
    st.markdown("""
    <div class="info-box">
        <h4>📖 Sobre esta análise:</h4>
        <p>Esta página apresenta uma visão aprofundada de cada componente que contribui para a pegada de carbono 
        das suas operações de impressão. Use estas informações para identificar onde concentrar seus esforços de redução.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabela de componentes
    st.markdown("### 🔍 Componentes da Pegada de Carbono")
    st.info("💡 **O que significa:** Cada linha representa uma fonte de emissão de CO₂. O percentual indica o impacto relativo de cada componente.")
    
    components_data = []
    for component, value in carbon_data['components'].items():
        percentage = (value / carbon_data['total']) * 100
        components_data.append({
            'Componente': translate_component_name(component),
            'CO₂ (kg)': f"{value:.3f}",
            'Percentual': f"{percentage:.1f}%",
            'Descrição': get_component_description(component)
        })
    
    st.table(pd.DataFrame(components_data))
    
    st.markdown("---")
    
    # Gráfico de evolução temporal (simulado)
    st.markdown("### 📈 Evolução da Pegada de Carbono")
    st.info("💡 **O que mostra:** Tendência histórica das emissões ao longo do tempo. Use este gráfico para identificar padrões e avaliar o impacto de mudanças implementadas.")
    
    # Simular dados históricos
    dates = pd.date_range(start='2024-01-01', end='2024-10-01', freq='ME')
    carbon_history = [carbon_data['total'] * (0.8 + 0.4 * i / len(dates)) for i in range(len(dates))]
    
    fig_trend = px.line(x=dates, y=carbon_history, 
                       title="🌍 Evolução Mensal da Pegada de Carbono",
                       labels={'x': 'Data', 'y': 'CO₂ (kg)'})
    st.plotly_chart(fig_trend, use_container_width=True)
    
    st.markdown("---")
    
    # Análise de eficiência
    st.markdown("### ⚡ Análise de Eficiência")
    st.markdown("""
    <div class="info-box">
        <p><strong>Como interpretar:</strong></p>
        <ul>
            <li><strong>CO₂ por Página:</strong> Quanto CO₂ é emitido para cada página impressa</li>
            <li><strong>Score de Sustentabilidade:</strong> Avaliação geral (0-100) das práticas ambientais</li>
            <li><strong>ROI Potencial:</strong> Retorno financeiro esperado com investimentos em sustentabilidade</li>
            <li><strong>Economia Total:</strong> Quantidade de CO₂ que pode ser evitada com melhorias</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("CO₂ por Página", f"{sustainability_metrics['co2_per_page']:.4f} kg")
        st.metric("Score de Sustentabilidade", f"{sustainability_metrics['sustainability_score']:.1f}/100")
    
    with col2:
        st.metric("ROI Potencial", f"{sustainability_metrics['roi']:.1f}%")
        st.metric("Economia Total", f"{sustainability_metrics['total_savings']:.1f} kg CO₂")

def show_action_plan(carbon_data, sustainability_metrics):
    """Mostra plano de ação"""
    
    st.markdown("## 🎯 Plano de Ação para Sustentabilidade")
    
    st.markdown("""
    <div class="info-box">
        <h4>🚀 Sobre este plano:</h4>
        <p>Este plano apresenta ações práticas organizadas em 4 fases para reduzir a pegada de carbono das suas 
        operações de impressão. Cada fase contém ações específicas com estimativas de custo, economia e dificuldade de implementação.</p>
        <p><strong>Como usar:</strong> Clique em cada fase para ver os detalhes e comece pelas ações de menor dificuldade 
        para obter resultados rápidos.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fases do plano
    phases = [
        {
            'name': '🚀 Fase 1 - Imediata (0-30 dias)',
            'actions': [
                'Configurar impressão duplex por padrão',
                'Ativar modo de economia de energia',
                'Implementar política de impressão consciente',
                'Configurar alertas de baixo nível de toner'
            ],
            'reduction': carbon_data['total'] * 0.15,
            'cost': 100,
            'savings': 500,
            'difficulty': 'Baixa'
        },
        {
            'name': '📈 Fase 2 - Curto Prazo (1-3 meses)',
            'actions': [
                'Migrar para papel reciclado',
                'Implementar sistema de aprovação de impressões',
                'Digitalizar processos documentais',
                'Configurar impressão sob demanda'
            ],
            'reduction': carbon_data['total'] * 0.25,
            'cost': 800,
            'savings': 1200,
            'difficulty': 'Média'
        },
        {
            'name': '🔧 Fase 3 - Médio Prazo (3-6 meses)',
            'actions': [
                'Implementar energia renovável',
                'Sistema de monitoramento contínuo',
                'Programa de reciclagem de suprimentos',
                'Treinamento em sustentabilidade'
            ],
            'reduction': carbon_data['total'] * 0.20,
            'cost': 1500,
            'savings': 2000,
            'difficulty': 'Alta'
        },
        {
            'name': '🌟 Fase 4 - Longo Prazo (6-12 meses)',
            'actions': [
                'Migração para impressão digital completa',
                'Implementação de IA para otimização',
                'Parcerias com fornecedores sustentáveis',
                'Certificação de sustentabilidade'
            ],
            'reduction': carbon_data['total'] * 0.30,
            'cost': 2500,
            'savings': 3000,
            'difficulty': 'Muito Alta'
        }
    ]
    
    for phase in phases:
        with st.expander(phase['name']):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Redução CO₂", f"{phase['reduction']:.1f} kg")
                st.metric("Dificuldade", phase['difficulty'])
            
            with col2:
                st.metric("Custo", f"R$ {phase['cost']:,}")
                st.metric("Economia", f"R$ {phase['savings']:,}")
            
            with col3:
                st.metric("ROI", f"{((phase['savings'] - phase['cost']) / phase['cost']) * 100:.1f}%")
            
            st.markdown("**Ações:**")
            for action in phase['actions']:
                st.markdown(f"• {action}")
    
    st.markdown("---")
    
    # Gráfico de ROI por fase
    st.markdown("### 💰 ROI por Fase")
    st.info("💡 **O que mostra:** Retorno sobre Investimento (ROI) de cada fase. Quanto maior a barra, melhor o retorno financeiro. ROI acima de 100% significa que a economia supera o custo de implementação.")
    
    roi_data = []
    for phase in phases:
        roi = ((phase['savings'] - phase['cost']) / phase['cost']) * 100
        roi_data.append({
            'Fase': phase['name'].split(' - ')[1],
            'ROI (%)': roi,
            'Custo (R$)': phase['cost'],
            'Economia (R$)': phase['savings']
        })
    
    fig_roi = px.bar(pd.DataFrame(roi_data), x='Fase', y='ROI (%)',
                    title="📊 Retorno sobre Investimento por Fase",
                    color='ROI (%)',
                    color_continuous_scale='RdYlGn')
    st.plotly_chart(fig_roi, use_container_width=True)

def show_sustainability_metrics(sustainability_metrics, environmental_equivalents):
    """Mostra métricas de sustentabilidade"""
    
    st.markdown("## 🌱 Métricas de Sustentabilidade")
    
    st.markdown("""
    <div class="info-box">
        <h4>🎯 Sobre estas métricas:</h4>
        <p>Esta página apresenta indicadores-chave de desempenho (KPIs) para avaliar o nível de sustentabilidade 
        das suas operações de impressão. Use estas métricas para acompanhar seu progresso ao longo do tempo.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Score de sustentabilidade
    col1, col2 = st.columns(2)
    
    with col1:
        score = sustainability_metrics['sustainability_score']
        
        # Gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "🌱 Score de Sustentabilidade"},
            delta = {'reference': 50},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        st.plotly_chart(fig_gauge, use_container_width=True)
        st.info("💡 **Interpretação:** 0-50 (Crítico), 50-80 (Bom), 80-100 (Excelente). O delta mostra a diferença em relação à meta de 50 pontos.")
    
    with col2:
        st.markdown("### 📊 Métricas Principais")
        st.metric("CO₂ por Página", f"{sustainability_metrics['co2_per_page']:.4f} kg")
        st.metric("Economia Total", f"{sustainability_metrics['total_savings']:.1f} kg CO₂")
        st.metric("ROI Potencial", f"{sustainability_metrics['roi']:.1f}%")
        
        st.markdown("### 🎯 Objetivos")
        st.progress(score / 100)
        st.markdown(f"**Progresso:** {score:.1f}/100 pontos")
    
    st.markdown("---")
    
    # Equivalentes ambientais detalhados
    st.markdown("### 🌍 Impacto Ambiental")
    st.markdown("""
    <div class="info-box">
        <p><strong>Equivalências práticas:</strong> Para facilitar a compreensão do impacto, convertemos as emissões de CO₂ 
        em situações do dia a dia. Estas comparações ajudam a visualizar a magnitude do impacto ambiental.</p>
    </div>
    """, unsafe_allow_html=True)
    
    equivalents_data = [
        {'Métrica': 'Quilômetros de Carro', 'Valor': f"{environmental_equivalents['car_km']:.0f} km", 'Ícone': '🚗'},
        {'Métrica': 'Árvores para Compensar', 'Valor': f"{environmental_equivalents['trees']:.0f}", 'Ícone': '🌳'},
        {'Métrica': 'Horas de Lâmpada LED', 'Valor': f"{environmental_equivalents['lightbulb_hours']:.0f} h", 'Ícone': '💡'},
        {'Métrica': 'Minutos de Banho Quente', 'Valor': f"{environmental_equivalents['shower_minutes']:.0f} min", 'Ícone': '🚿'}
    ]
    
    for eq in equivalents_data:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"### {eq['Ícone']} {eq['Métrica']}")
            st.markdown(f"**{eq['Valor']}**")

def translate_component_name(component):
    """Traduz nome do componente de inglês para português"""
    translations = {
        'paper': 'Papel',
        'toner': 'Toner',
        'energy': 'Energia',
        'manufacturing': 'Fabricação',
        'transport': 'Transporte',
        'disposal': 'Descarte'
    }
    return translations.get(component, component.capitalize())

def get_component_description(component):
    """Retorna descrição do componente"""
    descriptions = {
        'paper': 'Produção de celulose, transporte, processamento',
        'toner': 'Extração de petróleo, refino, produção de plástico',
        'energy': 'Consumo de energia elétrica da impressora',
        'manufacturing': 'Fabricação da impressora (distribuída ao longo da vida útil)',
        'transport': 'Transporte de suprimentos e manutenção',
        'disposal': 'Descarte de suprimentos e componentes'
    }
    return descriptions.get(component, 'Componente da pegada de carbono')

def export_to_csv(data):
    """Exporta dados para formato CSV"""
    rows = []
    
    # Dados principais
    rows.append(["Métrica", "Valor", "Unidade"])
    rows.append(["Data/Hora", data['timestamp'], ""])
    rows.append(["Páginas Impressas", data['pages_printed'], "páginas"])
    rows.append(["Pegada de Carbono Total", f"{data['carbon_footprint']['total']:.2f}", "kg CO₂"])
    
    rows.append(["", "", ""])
    rows.append(["Componentes da Pegada de Carbono", "", ""])
    rows.append(["Componente", "Valor (kg CO₂)", "Percentual (%)"])
    
    total = data['carbon_footprint']['total']
    components = data['carbon_footprint']['components']
    
    for component, value in components.items():
        percentage = (value / total * 100) if total > 0 else 0
        rows.append([component.capitalize(), f"{value:.2f}", f"{percentage:.1f}"])
    
    rows.append(["", "", ""])
    rows.append(["Métricas de Sustentabilidade", "", ""])
    rows.append(["Métrica", "Valor", "Unidade"])
    rows.append(["Score de Sustentabilidade", f"{data['sustainability_metrics']['sustainability_score']:.1f}", "pontos"])
    rows.append(["CO₂ por Página", f"{data['sustainability_metrics']['co2_per_page']:.6f}", "kg CO₂/página"])
    rows.append(["ROI", f"{data['sustainability_metrics']['roi']:.1f}", "%"])
    rows.append(["Economia Total", f"{data['sustainability_metrics']['total_savings']:.2f}", "R$"])
    
    rows.append(["", "", ""])
    rows.append(["Equivalentes Ambientais", "", ""])
    rows.append(["Equivalente", "Valor", "Unidade"])
    rows.append(["Quilômetros de Carro", f"{data['environmental_equivalents']['car_km']:.1f}", "km"])
    rows.append(["Árvores", f"{data['environmental_equivalents']['trees']:.1f}", "árvores"])
    rows.append(["Lâmpadas (60W)", f"{data['environmental_equivalents']['lightbulb_hours']:.1f}", "horas"])
    rows.append(["Banhos", f"{data['environmental_equivalents']['shower_minutes']:.1f}", "minutos"])
    
    # Converter para CSV
    output = io.StringIO()
    for row in rows:
        output.write(','.join(str(cell) for cell in row) + '\n')
    
    return output.getvalue().encode('utf-8-sig')  # UTF-8 com BOM para Excel

def export_to_json(data):
    """Exporta dados para formato JSON"""
    json_str = json.dumps(data, indent=2, ensure_ascii=False, default=str)
    return json_str.encode('utf-8')

def export_to_excel(data):
    """Exporta dados para formato Excel"""
    output = BytesIO()
    
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Planilha 1: Resumo Geral
        summary_data = {
            'Métrica': ['Data/Hora', 'Páginas Impressas', 'Pegada de Carbono Total'],
            'Valor': [
                data['timestamp'],
                data['pages_printed'],
                f"{data['carbon_footprint']['total']:.2f} kg CO₂"
            ]
        }
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_excel(writer, sheet_name='Resumo Geral', index=False)
        
        # Planilha 2: Componentes da Pegada
        components = data['carbon_footprint']['components']
        total = data['carbon_footprint']['total']
        components_data = {
            'Componente': list(components.keys()),
            'Valor (kg CO₂)': [f"{v:.2f}" for v in components.values()],
            'Percentual (%)': [f"{(v/total*100):.1f}" for v in components.values()]
        }
        df_components = pd.DataFrame(components_data)
        df_components.to_excel(writer, sheet_name='Componentes', index=False)
        
        # Planilha 3: Métricas de Sustentabilidade
        metrics_data = {
            'Métrica': [
                'Score de Sustentabilidade',
                'CO₂ por Página',
                'ROI',
                'Economia Total'
            ],
            'Valor': [
                f"{data['sustainability_metrics']['sustainability_score']:.1f} pontos",
                f"{data['sustainability_metrics']['co2_per_page']:.6f} kg CO₂/página",
                f"{data['sustainability_metrics']['roi']:.1f}%",
                f"R$ {data['sustainability_metrics']['total_savings']:.2f}"
            ]
        }
        df_metrics = pd.DataFrame(metrics_data)
        df_metrics.to_excel(writer, sheet_name='Métricas', index=False)
        
        # Planilha 4: Equivalentes Ambientais
        equivalents_data = {
            'Equivalente': [
                'Quilômetros de Carro',
                'Árvores',
                'Lâmpadas (60W)',
                'Banhos'
            ],
            'Valor': [
                f"{data['environmental_equivalents']['car_km']:.1f} km",
                f"{data['environmental_equivalents']['trees']:.1f} árvores",
                f"{data['environmental_equivalents']['lightbulb_hours']:.1f} horas",
                f"{data['environmental_equivalents']['shower_minutes']:.1f} minutos"
            ]
        }
        df_equivalents = pd.DataFrame(equivalents_data)
        df_equivalents.to_excel(writer, sheet_name='Equivalentes', index=False)
    
    output.seek(0)
    return output.getvalue()

if __name__ == "__main__":
    main()





