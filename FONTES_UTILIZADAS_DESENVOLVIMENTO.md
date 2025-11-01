# FONTES UTILIZADAS NO DESENVOLVIMENTO DO DASHBOARD

---

## 🔧 **FONTES QUE FORAM UTILIZADAS DURANTE O DESENVOLVIMENTO**

Como o dashboard já foi desenvolvido, é importante documentar quais fontes técnicas foram consultadas durante a implementação:

---

### 💻 **1. DOCUMENTAÇÃO TÉCNICA DE BIBLIOTECAS PYTHON**

#### **Streamlit (streamlit.io/docs)**
- **Utilizado para:** Criar interface web interativa do dashboard
- **O que foi consultado:** Documentação de componentes visuais, layout, upload de dados
- **Por que:** Framework escolhido pela simplicidade e rapidez de desenvolvimento

#### **Plotly (plotly.com/python)**
- **Utilizado para:** Gráficos interativos de visualização de dados
- **O que foi consultado:** Documentação de gráficos de linha, barras, pizza para métricas ambientais
- **Por que:** Biblioteca que gera visualizações profissionais e interativas

#### **PySNMP (pysnmp.readthedocs.io)**
- **Utilizado para:** Comunicação com impressoras HP via protocolo SNMP
- **O que foi consultado:** Documentação de comandos SNMP, OIDs (Object Identifiers), coleta de dados
- **Por que:** Biblioteca padrão para implementar cliente SNMP em Python

#### **Pandas (pandas.pydata.org/docs)**
- **Utilizado para:** Manipulação e análise de dados coletados
- **O que foi consultado:** Documentação de DataFrames, agregações, análises temporais
- **Por que:** Essencial para processar dados de impressões ao longo do tempo

---

### 📡 **2. ESPECIFICAÇÕES DE PROTOCOLOS E PADRÕES**

#### **RFC 1157 - Simple Network Management Protocol (SNMP)**
- **Utilizado para:** Entender protocolo de comunicação com impressoras
- **O que foi consultado:** Estrutura de mensagens SNMP, OIDs, comandos GET/SET
- **Por que:** Necessário para implementar coleta automática de dados das impressoras

#### **Printer MIB (Management Information Base)**
- **Utilizado para:** Identificar OIDs específicas de impressoras (contadores de página, níveis de toner)
- **O que foi consultado:** MIBs padrão de impressoras HP
- **Por que:** Para saber quais dados consultar via SNMP

---

### 🌍 **3. FONTES SOBRE CÁLCULOS AMBIENTAIS**

Aqui é onde precisamos **ser honestos**: durante o desenvolvimento, os cálculos de CO₂ e equivalências provavelmente foram baseados em:

#### **Valores encontrados online (fontes informais):**
- Sites sobre sustentabilidade com valores de "X páginas = Y árvores"
- Calculadoras online de pegada de carbono
- Artigos de blogs sobre impacto ambiental de papel

**❗ PROBLEMA:** Essas fontes não são cientificamente validadas!

**✅ SOLUÇÃO:** Agora precisamos **validar retroativamente** com fontes confiáveis!

---

### 💼 **4. EXEMPLOS DE CÓDIGO E TUTORIAIS**

#### **Stack Overflow, GitHub, Medium**
- **Utilizado para:** Resolver problemas técnicos, exemplos de implementação SNMP
- **O que foi consultado:** Soluções para erros, exemplos de dashboards Streamlit
- **Por que:** Comunidade de desenvolvedores ajuda a resolver obstáculos técnicos

#### **Documentação HP**
- **Utilizado para:** Entender modelos de impressoras HP e seus protocolos
- **O que foi consultado:** Manuais técnicos, especificações de rede
- **Por que:** Garantir compatibilidade com impressoras do setor fiscal

---

## 📚 **FONTES QUE PRECISAM SER CONSULTADAS AGORA (VALIDAÇÃO)**

Agora que o código está pronto, precisamos **fundamentar academicamente** as escolhas:

---

### 🔬 **PARA VALIDAR CÁLCULOS AMBIENTAIS:**

#### **GHG Protocol Brasil (ghgprotocolbrasil.com.br)**
- **Para validar:** Metodologia de cálculo de emissões de CO₂
- **O que buscar:** Fatores de emissão oficiais para papel, energia
- **Por que:** Padrão internacional reconhecido academicamente

#### **IPCC - Painel Intergovernamental sobre Mudanças Climáticas**
- **Para validar:** Equivalências de CO₂ (kg CO₂ = km de carro)
- **O que buscar:** Relatórios sobre emissões por setor
- **Por que:** Referência científica global

#### **WWF Brasil / Two Sides**
- **Para validar:** Equivalência páginas → árvores
- **O que buscar:** Estudos sobre ciclo de vida do papel
- **Por que:** Dados sobre consumo de recursos naturais

---

### 📖 **PARA FUNDAMENTAR ESCOLHAS PEDAGÓGICAS:**

#### **Google Scholar / Scielo**
- **Para validar:** Interface educativa não-punitiva
- **O que buscar:** Artigos sobre "educação ambiental corporativa", "mudança comportamental sustentabilidade"
- **Por que:** Justificar por que escolhemos abordagem educativa

---

### 🏢 **PARA CONTEXTUALIZAR SOLUÇÃO:**

#### **ABNT ISO 14001, ISO 14064**
- **Para validar:** Conformidade dos relatórios gerados
- **O que buscar:** Normas de gestão ambiental e inventários de GEE
- **Por que:** Aumentar relevância institucional

#### **Análise de concorrentes (PaperCut, GreenPrint, etc.)**
- **Para validar:** Escolhas de design (gratuito, simples)
- **O que buscar:** Comparação de funcionalidades, custos, complexidade
- **Por que:** Já fizemos (está nos arquivos), mas precisa referências formais

---

## 📝 **RESPOSTA HONESTA PARA O TRABALHO**

### **Versão 1: Transparente (~500 caracteres)**

Durante o desenvolvimento do dashboard, consultamos documentação técnica de bibliotecas Python (Streamlit, Plotly, PySNMP), especificações do protocolo SNMP (RFC 1157), e exemplos práticos da comunidade de desenvolvedores (Stack Overflow, GitHub). Para cálculos ambientais iniciais, utilizamos valores de referência disponíveis online. Agora, na fase de fundamentação acadêmica, precisamos validar esses cálculos consultando fontes científicas confiáveis (GHG Protocol, IPCC, WWF), normas técnicas (ABNT ISO 14001/14064), e literatura acadêmica sobre educação ambiental corporativa (Google Scholar, Scielo) para garantir rigor científico da solução implementada.

---

### **Versão 2: Acadêmica (mais formal, ~600 caracteres)**

O desenvolvimento do dashboard baseou-se em fontes técnicas especializadas: documentação oficial de bibliotecas Python (Streamlit para interface, Plotly para visualizações, PySNMP para comunicação SNMP), especificações de protocolos de rede (RFC 1157 - SNMP, Printer MIB), e documentação de fabricantes (manuais técnicos HP). Para resolução de desafios técnicos, consultou-se comunidades de desenvolvedores (Stack Overflow, repositórios GitHub). Os cálculos de impacto ambiental iniciais basearam-se em valores de referência disponíveis publicamente, que agora requerem validação científica. Portanto, nesta fase de aprofundamento teórico, consultaremos: GHG Protocol Brasil e IPCC para metodologias de cálculo de emissões, WWF e estudos acadêmicos para equivalências ecológicas, normas ABNT ISO 14001/14064 para conformidade, e literatura científica (Scielo, Google Scholar) para fundamentar escolhas pedagógicas da interface educativa.

---

### **Versão 3: Dividida em dois momentos**

**FONTES UTILIZADAS NO DESENVOLVIMENTO (passado):**

Documentação técnica de bibliotecas Python (Streamlit, Plotly, PySNMP, Pandas) para implementação da solução; especificações de protocolos (RFC 1157 SNMP, Printer MIB) para comunicação com impressoras; documentação de fabricantes (HP) para compatibilidade; comunidades de desenvolvedores (Stack Overflow, GitHub) para resolução de desafios técnicos; valores de referência disponíveis online para cálculos iniciais de impacto ambiental.

**FONTES QUE SERÃO CONSULTADAS PARA VALIDAÇÃO (presente/futuro):**

GHG Protocol Brasil e IPCC para validar metodologias de cálculo de CO₂; WWF e estudos científicos para confirmar equivalências ecológicas (papel-árvores); normas ABNT ISO 14001/14064 para verificar conformidade; Google Scholar e Scielo para fundamentar escolhas pedagógicas; SEBRAE e GRI para contextualizar gestão sustentável em PMEs; literatura sobre extensão universitária para situar o projeto no campo acadêmico.

---

## 🎯 **TABELA: FONTES × FINALIDADE**

| **Etapa** | **Fonte** | **Finalidade** | **Quando** |
|-----------|-----------|---------------|-----------|
| **Desenvolvimento** | Streamlit Docs | Criar interface | ✅ Já usada |
| **Desenvolvimento** | PySNMP Docs | Coletar dados SNMP | ✅ Já usada |
| **Desenvolvimento** | RFC 1157 | Entender protocolo | ✅ Já usada |
| **Desenvolvimento** | Stack Overflow | Resolver erros | ✅ Já usada |
| **Desenvolvimento** | Sites sobre CO₂ | Cálculos iniciais | ⚠️ Informal |
| **Validação** | GHG Protocol | Validar CO₂ | 🔄 Usar agora |
| **Validação** | IPCC, WWF | Validar equivalências | 🔄 Usar agora |
| **Validação** | Google Scholar | Fundamentar pedagogia | 🔄 Usar agora |
| **Validação** | ABNT ISO | Verificar normas | 🔄 Usar agora |

---

## 💡 **QUESTÕES AJUSTADAS (baseado no que JÁ FOI FEITO)**

### **1. Os valores de CO₂ usados no código estão corretos segundo fontes científicas?**
- **O que temos:** Cálculos implementados em `metodologia_calculos_sustentabilidade.py`
- **O que falta:** Validar se valores estão de acordo com GHG Protocol/IPCC
- **Como fazer:** Comparar valores do código com literatura científica

### **2. As equivalências "páginas → árvores" são cientificamente precisas?**
- **O que temos:** Conversões implementadas no dashboard
- **O que falta:** Fonte científica que justifique os números
- **Como fazer:** Buscar estudos de ciclo de vida do papel (WWF, Two Sides, artigos científicos)

### **3. A abordagem educativa não-punitiva é eficaz segundo literatura pedagógica?**
- **O que temos:** Interface que educa sem punir
- **O que falta:** Fundamentação teórica dessa escolha
- **Como fazer:** Artigos sobre educação ambiental corporativa

### **4. O protocolo SNMP é realmente democratizante?**
- **O que temos:** Código usa SNMP (aberto) em vez de APIs proprietárias
- **O que falta:** Literatura sobre democratização tecnológica via padrões abertos
- **Como fazer:** Artigos sobre open source, IoT acessível

### **5. A solução está em conformidade com normas brasileiras?**
- **O que temos:** Relatórios gerados pelo código
- **O que falta:** Verificar se atendem ISO 14001/14064
- **Como fazer:** Consultar as normas e comparar

### **6. Como outros projetos similares foram implementados?**
- **O que temos:** Nossa experiência prática
- **O que falta:** Contextualização acadêmica
- **Como fazer:** Buscar projetos de extensão em sustentabilidade (Scielo, Portal CAPES)

---

## 📖 **REFLEXÃO: DESENVOLVIMENTO × VALIDAÇÃO**

### **O ciclo real do projeto:**

```
FASE 1: DESENVOLVIMENTO (prático)
  ↓
Consultou: Docs técnicas, Stack Overflow, RFCs
Criou: Dashboard funcional
  ↓
FASE 2: DOCUMENTAÇÃO ACADÊMICA (atual)
  ↓
Consulta: Literatura científica, normas, estudos
Valida: Escolhas técnicas já feitas
  ↓
FASE 3: REFINAMENTO (futuro)
  ↓
Ajusta: Valores/metodologias se necessário
Melhora: Baseado em evidências científicas
```

**Isso NÃO é problema!** É comum em projetos de extensão:
- Prática vem primeiro (atender necessidade urgente)
- Teoria valida depois (rigor acadêmico)

**A Resolução CNE/CES nº 7/2018 apoia isso:**
> "Articulação entre ensino, pesquisa e extensão"

Não precisa ser linear! Pode ser recursivo:
- Extensão (desenvolveu solução) →
- Pesquisa (valida escolhas) →
- Ensino (refina conhecimento)

---

## ✅ **CONCLUSÃO: COMO RESPONDER NO TRABALHO**

### **Seja transparente:**

1. **Reconheça** que desenvolvimento usou fontes técnicas práticas
2. **Admita** que cálculos iniciais precisam validação científica
3. **Justifique** que agora está fazendo aprofundamento teórico
4. **Demonstre** maturidade acadêmica ao buscar validação

### **Exemplo de resposta honesta:**

"Durante a fase de desenvolvimento do dashboard, consultei principalmente fontes técnicas (documentação Python, RFCs, comunidades de desenvolvedores) que permitiram implementar a solução funcional. Os cálculos de impacto ambiental basearam-se em valores de referência disponíveis, mas reconheço que necessitam validação científica rigorosa. Portanto, nesta fase de aprofundamento teórico, consultarei literatura científica especializada (GHG Protocol, IPCC, artigos revisados por pares) para validar e, se necessário, ajustar os valores implementados. Esta abordagem recursiva — prática seguida de fundamentação teórica — é compatível com a natureza iterativa de projetos de extensão, onde atendimento à demanda social (dashboard funcional) precede rigor acadêmico (validação científica)."

---

**Arquivo:** `FONTES_UTILIZADAS_DESENVOLVIMENTO.md`  
**Criado para:** Documentar honestamente o processo real de desenvolvimento

