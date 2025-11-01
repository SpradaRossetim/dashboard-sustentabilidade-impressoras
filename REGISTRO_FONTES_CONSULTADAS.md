# REGISTRO DE FONTES CONSULTADAS

**Projeto:** Dashboard de Sustentabilidade para Impressoras HP  
**Responsável:** _______________________  
**Data:** ___/___/_____

---

## 📋 **FONTES TÉCNICAS (Utilizadas no Desenvolvimento)**

### 1️⃣ **STREAMLIT**

**Fonte:** https://streamlit.io / https://docs.streamlit.io  
**Tipo:** Documentação técnica oficial  
**Data de consulta:** Durante desenvolvimento (2024)

**Para que foi utilizado:**
- Criar interface web interativa do dashboard
- Desenvolver componentes visuais para exibição de dados
- Implementar sistema de navegação entre páginas do dashboard
- Permitir visualização em tempo real das métricas ambientais

**Relação com o diagnóstico:**
- Questionário revelou necessidade de ferramenta acessível e simples
- Streamlit não requer conhecimento de HTML/CSS/JavaScript
- Interface intuitiva atende barreira tecnológica identificada no setor fiscal

**Principais achados:**
- Framework Python para criação rápida de aplicações web
- Ideal para dashboards de dados e prototipagem
- Execução local simplificada (sem necessidade de servidor complexo)
- Comunidade ativa com exemplos e documentação clara

---

### 2️⃣ **PANDAS**

**Fonte:** https://pandas.pydata.org / https://pandas.pydata.org/docs  
**Tipo:** Documentação técnica oficial  
**Data de consulta:** Durante desenvolvimento (2024)

**Para que foi utilizado:**
- Manipular dados coletados via SNMP das impressoras
- Criar DataFrames para organização estruturada de informações
- Realizar agregações (soma de páginas impressas, médias por período)
- Analisar tendências temporais de consumo
- Gerar relatórios com dados processados

**Relação com o diagnóstico:**
- Questionário mostrou ausência de dados históricos no setor fiscal
- Pandas permite armazenar e analisar dados ao longo do tempo
- Facilita comparações (mês atual vs. anterior)

**Principais achados:**
- Biblioteca essencial para análise de dados em Python
- DataFrames estruturam dados tabulares eficientemente
- Funções de agregação simplificam cálculos estatísticos
- Integração nativa com Plotly e Streamlit

---

### 3️⃣ **PLOTLY**

**Fonte:** https://plotly.com/python / https://plotly.com/python-api-reference  
**Tipo:** Documentação técnica oficial  
**Data de consulta:** Durante desenvolvimento (2024)

**Para que foi utilizado:**
- Criar gráficos interativos de visualização de dados
- Desenvolver gráficos de linha (tendências temporais)
- Implementar gráficos de barras (comparações por período)
- Gerar gráficos de pizza (distribuição de consumo)
- Visualizar equivalências ambientais (CO₂, árvores)

**Relação com o diagnóstico:**
- Questionário revelou que profissionais subestimam impacto ambiental
- Visualizações tornam dados abstratos em informações tangíveis
- Gráficos interativos aumentam engajamento

**Principais achados:**
- Biblioteca de visualização altamente interativa
- Gráficos profissionais com poucas linhas de código
- Interatividade (zoom, hover, filtros) sem JavaScript
- Integração perfeita com Streamlit e Pandas

---

## 📚 **FONTES ACADÊMICAS (Para Validação)**

### 4️⃣ **GOOGLE SCHOLAR**

**Fonte:** https://scholar.google.com  
**Tipo:** Base de dados acadêmica  
**Data de consulta:** A consultar (fase de validação)

**Para que será utilizado:**
- Buscar artigos científicos sobre impacto ambiental de impressões
- Pesquisar metodologias de educação ambiental corporativa
- Encontrar estudos sobre mudança comportamental em sustentabilidade
- Validar eficácia de sistemas de monitoramento
- Fundamentar escolhas pedagógicas da interface

**Relação com o diagnóstico:**
- Valida se abordagem educativa não-punitiva é eficaz segundo literatura
- Fundamenta estimativa de redução de 20-30% em desperdícios
- Contextualiza déficit de conscientização ambiental identificado

**Termos de busca planejados:**
- "educação ambiental corporativa"
- "monitoramento consumo papel empresas"
- "mudança comportamental sustentabilidade"
- "corporate environmental awareness"
- "print management systems effectiveness"

---

### 5️⃣ **SCIELO BRASIL**

**Fonte:** https://scielo.br  
**Tipo:** Biblioteca científica digital  
**Data de consulta:** A consultar (fase de validação)

**Para que será utilizado:**
- Buscar estudos brasileiros sobre gestão ambiental corporativa
- Pesquisar projetos de extensão universitária em sustentabilidade
- Encontrar dados sobre consumo de papel no Brasil
- Contextualizar projeto dentro da realidade nacional
- Identificar experiências similares em IES brasileiras

**Relação com o diagnóstico:**
- Contextualiza problema identificado no setor fiscal no cenário brasileiro
- Valida relevância do projeto no contexto nacional
- Fundamenta articulação ensino-pesquisa-extensão

**Termos de busca planejados:**
- "gestão ambiental empresarial Brasil"
- "extensão universitária sustentabilidade"
- "consumo papel corporativo"
- "educação ambiental organizações"
- "pegada ecológica escritórios"

---

## 🌍 **FONTES ESPECIALIZADAS (Para Validação de Cálculos)**

### 6️⃣ **GHG PROTOCOL BRASIL**

**Fonte:** https://ghgprotocolbrasil.com.br  
**Tipo:** Instituição especializada em inventários de GEE  
**Data de consulta:** A consultar (fase de validação)

**Para que será utilizado:**
- Validar metodologia de cálculo de emissões de CO₂ implementada no código
- Verificar fatores de emissão utilizados (kg CO₂ por página impressa)
- Confirmar se cálculos estão de acordo com padrões internacionais
- Fundamentar cientificamente as métricas apresentadas no dashboard
- Garantir credibilidade dos relatórios gerados

**Relação com o diagnóstico:**
- Dashboard calcula CO₂ das impressões
- Valores precisam validação científica para credibilidade
- Relatórios executivos devem seguir padrões reconhecidos

**O que buscar especificamente:**
- Fatores de emissão para papel (kg CO₂/tonelada ou kg CO₂/resma)
- Metodologia de cálculo do ciclo de vida (produção + transporte + energia)
- Padrões ISO 14064 para inventários de gases de efeito estufa
- Exemplos de cálculo aplicados ao setor corporativo

**Comparação necessária:**
- Verificar se valores implementados no módulo `metodologia_calculos_sustentabilidade.py` coincidem com fatores oficiais
- Se divergirem, ajustar código para conformidade

---

## 📊 **TABELA RESUMO: FONTE × APLICAÇÃO NO PROJETO**

| **Fonte** | **Tipo** | **Quando Usada** | **Para Quê** | **Status** |
|-----------|----------|------------------|--------------|------------|
| **Streamlit** | Técnica | Desenvolvimento | Interface web do dashboard | ✅ Utilizada |
| **Pandas** | Técnica | Desenvolvimento | Manipulação de dados SNMP | ✅ Utilizada |
| **Plotly** | Técnica | Desenvolvimento | Gráficos interativos | ✅ Utilizada |
| **Google Scholar** | Acadêmica | Validação | Fundamentar pedagogia educativa | 🔄 A consultar |
| **Scielo Brasil** | Acadêmica | Validação | Contexto brasileiro e extensão | 🔄 A consultar |
| **GHG Protocol** | Especializada | Validação | Validar cálculos de CO₂ | 🔄 A consultar |

---

## 🔗 **CONEXÃO: DIAGNÓSTICO → FONTES → SOLUÇÃO**

### **Fluxo de utilização das fontes:**

```
DIAGNÓSTICO PARTICIPATIVO (Questionário + Observação)
         ↓
    Identificou:
    - Desperdício de recursos
    - Falta de conscientização
    - Ausência de dados
         ↓
DESENVOLVIMENTO DA SOLUÇÃO
         ↓
    Consultou FONTES TÉCNICAS:
    ├─ Streamlit → Interface simples
    ├─ Pandas → Análise de dados
    └─ Plotly → Visualizações
         ↓
    Desenvolveu: Dashboard funcional
         ↓
VALIDAÇÃO ACADÊMICA (fase atual)
         ↓
    Consultará FONTES CIENTÍFICAS:
    ├─ Google Scholar → Fundamentação pedagógica
    ├─ Scielo Brasil → Contexto nacional
    └─ GHG Protocol → Validação de cálculos
         ↓
    Validará: Escolhas técnicas e métricas
```

---

## 📝 **PRINCIPAIS ACHADOS POR CATEGORIA**

### **TECNOLOGIA (Streamlit, Pandas, Plotly):**

✅ **Achado 1:** Python possui ecossistema completo para dashboards de sustentabilidade
- Streamlit (interface), Pandas (dados), Plotly (visualização) integram-se perfeitamente
- Permite desenvolvimento rápido sem equipe grande

✅ **Achado 2:** Ferramentas são gratuitas e open source
- Elimina barreira de custo identificada no diagnóstico
- Permite replicação por outras organizações sem licenciamento

✅ **Achado 3:** Documentação técnica é acessível e atualizada
- Facilita aprendizado e manutenção do código
- Comunidades ativas oferecem suporte

---

### **VALIDAÇÃO CIENTÍFICA (Google Scholar, Scielo, GHG Protocol):**

🔄 **A ser investigado 1:** Percentual real de redução alcançado por sistemas similares
- Estimativa inicial: 20-30%
- Buscar: Estudos de caso em Google Scholar

🔄 **A ser investigado 2:** Contexto de projetos de extensão em sustentabilidade no Brasil
- Buscar: Scielo Brasil - experiências em outras IES
- Objetivo: Identificar boas práticas replicáveis

🔄 **A ser investigado 3:** Valores oficiais de emissões de CO₂
- Buscar: GHG Protocol Brasil - fatores de emissão
- Objetivo: Validar ou corrigir cálculos implementados

---

## 🎯 **PRÓXIMOS PASSOS**

### **Tarefas de pesquisa pendentes:**

1. ☐ **Google Scholar:**
   - Buscar artigos sobre educação ambiental corporativa (últimos 5 anos)
   - Identificar 3-5 artigos relevantes
   - Extrair conclusões sobre eficácia de abordagens não-punitivas

2. ☐ **Scielo Brasil:**
   - Buscar "extensão universitária sustentabilidade"
   - Identificar projetos similares em outras IES
   - Documentar metodologias utilizadas

3. ☐ **GHG Protocol Brasil:**
   - Baixar/acessar documento de fatores de emissão atualizados
   - Comparar com valores usados no código
   - Se necessário, ajustar módulo `metodologia_calculos_sustentabilidade.py`

---

## 📖 **OBSERVAÇÕES IMPORTANTES**

### **Sobre o processo de pesquisa:**

**Transparência acadêmica:**
Durante o desenvolvimento do dashboard, priorizamos fontes técnicas que permitissem implementar solução funcional rapidamente para atender demanda do setor fiscal. Os cálculos de impacto ambiental basearam-se em valores de referência disponíveis online. Agora, na fase de fundamentação acadêmica, estamos validando essas escolhas com fontes científicas rigorosas. Esta abordagem recursiva (prática → teoria → refinamento) é compatível com projetos de extensão universitária, onde atendimento à comunidade não pode aguardar conclusão de toda pesquisa teórica prévia.

**Critérios de qualidade das fontes:**
- ✅ Fontes técnicas: Documentação oficial, padrões reconhecidos
- ✅ Fontes acadêmicas: Revisão por pares, publicações recentes (2019-2024)
- ✅ Fontes especializadas: Instituições reconhecidas nacional/internacionalmente

---

## 📌 **MODELO DE REGISTRO INDIVIDUAL (Para cada nova fonte consultada)**

**Fonte:** [Nome completo]  
**URL/Referência:** [Link ou citação ABNT]  
**Tipo:** [Acadêmica / Técnica / Especializada / Oficial]  
**Data de acesso:** [dd/mm/aaaa]

**Objetivo da consulta:**  
[Por que esta fonte foi consultada? Qual questão busca responder?]

**Principais achados:**  
[Resumo das informações mais relevantes]

**Relação com o projeto:**  
[Como esses achados se conectam com diagnóstico ou validam código?]

**Citações importantes:**  
[Trechos relevantes para usar no trabalho]

**Ações resultantes:**  
[Algo precisa ser ajustado no código ou documentação?]

---

**Data de criação:** ___/___/_____  
**Última atualização:** ___/___/_____  
**Responsável:** _______________________

