# 🌱 Dashboard Web de Sustentabilidade

Dashboard interativo completo para monitoramento e análise de pegada de carbono de impressoras corporativas.

## 🚀 Como Iniciar

### Opção 1: Script Automático
```bash
iniciar_dashboard.bat
```

### Opção 2: Manual
```bash
# Ativar ambiente virtual
printer_config_env\Scripts\activate

# Instalar dependências
uv pip install -r requirements_streamlit.txt

# Iniciar dashboard
streamlit run streamlit_dashboard.py
```

### Opção 3: Comando Direto
```bash
streamlit run streamlit_dashboard.py
```

## 🌐 Acesso

Após iniciar, acesse: **http://localhost:8501**

## 📊 Funcionalidades

### 🎛️ Dashboard Principal
- **Métricas em Tempo Real**: Páginas impressas, pegada de carbono, economia potencial
- **Score de Sustentabilidade**: Indicador visual de 0-100
- **Gráficos Interativos**: Componentes da pegada de carbono, economia por ação
- **Equivalentes Ambientais**: Comparações com atividades do dia a dia

### 📈 Análise Detalhada
- **Componentes da Pegada**: Papel, toner, energia, fabricação, transporte, descarte
- **Evolução Temporal**: Gráfico de tendência da pegada de carbono
- **Métricas de Eficiência**: CO₂ por página, ROI, score de sustentabilidade

### 🎯 Plano de Ação
- **4 Fases de Implementação**: Imediata, curto, médio e longo prazo
- **Análise de ROI**: Retorno sobre investimento por fase
- **Dificuldade de Implementação**: Classificação de baixa a muito alta
- **Ações Específicas**: Lista detalhada de implementações

### 🌱 Métricas de Sustentabilidade
- **Gauge de Score**: Indicador visual de sustentabilidade
- **Progresso de Objetivos**: Barra de progresso para metas
- **Impacto Ambiental**: Equivalentes detalhados

## 🎨 Interface

### Design Moderno
- **Tema Verde**: Cores sustentáveis e profissionais
- **Gradientes**: Visual atrativo e moderno
- **Cards Informativos**: Métricas em destaque
- **Gráficos Interativos**: Plotly com zoom e hover

### Navegação
- **Sidebar**: Controles e seleção de visualização
- **Menu Dropdown**: 4 opções de visualização
- **Botão de Atualização**: Coleta dados em tempo real

## 📋 Dados Coletados

### Impressora HP LaserJet P2055dn
- **IP**: 192.168.200.15
- **Páginas Impressas**: 3.237
- **Pegada de Carbono**: 117.827 kg CO₂
- **Economia Potencial**: 235.654 kg CO₂

### Componentes da Pegada
- **Papel**: 12.948 kg CO₂ (11.0%)
- **Toner**: 10.358 kg CO₂ (8.8%)
- **Energia**: 24.809 kg CO₂ (21.1%)
- **Fabricação**: 64.740 kg CO₂ (54.9%)
- **Transporte**: 3.237 kg CO₂ (2.7%)
- **Descarte**: 1.619 kg CO₂ (1.4%)

## 🔧 Tecnologias Utilizadas

### Frontend
- **Streamlit**: Framework web para Python
- **Plotly**: Gráficos interativos
- **Pandas**: Manipulação de dados
- **CSS Personalizado**: Estilização avançada

### Backend
- **Requests**: Coleta de dados da impressora
- **BeautifulSoup**: Parsing de HTML
- **JSON**: Armazenamento de dados
- **Datetime**: Timestamps e datas

## 📁 Arquivos do Dashboard

### Principais
- `streamlit_dashboard.py` - Dashboard principal
- `requirements_streamlit.txt` - Dependências
- `iniciar_dashboard.bat` - Script de inicialização
- `.streamlit/config.toml` - Configurações do Streamlit

### Suporte
- `demo_dashboard.py` - Demonstração dos dados
- `demo_dashboard_data.json` - Dados de exemplo
- `README_DASHBOARD.md` - Esta documentação

## 🎯 Casos de Uso

### Para Empresas
- **Relatórios Executivos**: Apresentações para diretoria
- **Monitoramento Contínuo**: Acompanhamento de métricas
- **Tomada de Decisão**: Baseado em dados reais
- **Compliance**: Relatórios de sustentabilidade

### Para Acadêmicos
- **Trabalhos de Faculdade**: Projetos de sustentabilidade
- **Pesquisas**: Análise de pegada de carbono
- **Apresentações**: Visualizações interativas
- **Metodologia**: Base científica documentada

### Para Profissionais
- **Auditorias**: Análise de impacto ambiental
- **Consultoria**: Recomendações baseadas em dados
- **Treinamento**: Educação em sustentabilidade
- **Certificações**: Suporte para ISO 14001, LEED

## 🔄 Atualizações em Tempo Real

### Coleta Automática
- **Dados da Impressora**: Coletados via interface web
- **Cálculos Dinâmicos**: Métricas atualizadas automaticamente
- **Gráficos Interativos**: Atualização em tempo real
- **Cache Inteligente**: Performance otimizada

### Botão de Atualização
- **Coleta Manual**: Botão para atualizar dados
- **Feedback Visual**: Spinner durante coleta
- **Tratamento de Erros**: Mensagens informativas
- **Status da Conexão**: Indicador de conectividade

## 📊 Métricas Disponíveis

### Principais
- **Páginas Impressas**: Contador total
- **Pegada de Carbono**: kg CO₂ total
- **Economia Potencial**: R$ e kg CO₂
- **Score de Sustentabilidade**: 0-100

### Detalhadas
- **CO₂ por Página**: Eficiência de impressão
- **ROI**: Retorno sobre investimento
- **Equivalentes Ambientais**: Comparações
- **Progresso de Objetivos**: Metas de sustentabilidade

## 🎨 Personalização

### Cores
- **Verde Principal**: #2E8B57
- **Gradientes**: Azul, verde, laranja
- **Cards**: Diferentes cores por métrica
- **Tema**: Configurável via config.toml

### Layout
- **Wide Mode**: Layout amplo por padrão
- **Sidebar**: Controles e navegação
- **Colunas**: Organização responsiva
- **Expansores**: Conteúdo colapsável

## 🚀 Próximas Funcionalidades

### Planejadas
- **Múltiplas Impressoras**: Suporte a várias impressoras
- **Histórico**: Dados históricos e tendências
- **Alertas**: Notificações de problemas
- **Exportação**: PDF, Excel, CSV

### Avançadas
- **IA**: Predições e otimizações
- **Mobile**: Versão para dispositivos móveis
- **API**: Integração com outros sistemas
- **Cloud**: Hospedagem na nuvem

## 📞 Suporte

### Problemas Comuns
1. **Impressora Offline**: Verificar conectividade
2. **Erro de Dependências**: Reinstalar requirements
3. **Porta Ocupada**: Usar porta diferente
4. **Encoding**: Verificar configuração do sistema

### Soluções
- **Reiniciar Dashboard**: Parar e iniciar novamente
- **Verificar IP**: Confirmar endereço da impressora
- **Logs**: Verificar mensagens de erro
- **Documentação**: Consultar este README

## 🎓 Uso Acadêmico

### Trabalhos de Faculdade
- **Projetos de Sustentabilidade**: Análise completa
- **Apresentações**: Dashboard interativo
- **Relatórios**: Dados científicos
- **Metodologia**: Base teórica sólida

### Pesquisas
- **Análise de Ciclo de Vida**: ACV completa
- **Fatores de Emissão**: Baseados em estudos
- **Validação**: Metodologia científica
- **Reprodutibilidade**: Código aberto

---

**Dashboard criado com ❤️ para promover sustentabilidade corporativa**


















