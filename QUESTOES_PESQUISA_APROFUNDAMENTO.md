# QUESTÕES DE PESQUISA E FONTES - APROFUNDAMENTO TEÓRICO

---

## 🔍 **QUESTÕES QUE AINDA PRECISAM SER RESPONDIDAS**

Embora o diagnóstico tenha identificado o problema e o dashboard já esteja desenvolvido, algumas questões teóricas e contextuais precisam ser aprofundadas para fundamentar academicamente a intervenção:

---

### 📌 **EIXO 1: IMPACTO AMBIENTAL QUANTIFICADO**

#### **Questão 1.1:**
**Qual o impacto ambiental real da produção de uma resma de papel A4 em termos de consumo de água, energia e emissões de CO₂?**

**Por que precisa responder:**
- Dashboard calcula equivalências (páginas → árvores → CO₂)
- Preciso validar se os cálculos do módulo `metodologia_calculos_sustentabilidade.py` estão baseados em dados científicos atualizados
- Fundamental para credibilizar as métricas apresentadas aos usuários

**O que já sabemos:** Dashboard calcula impacto, mas preciso fundamentar os valores usados

---

#### **Questão 1.2:**
**Quais são as emissões médias de CO₂ (em gramas) por página impressa, considerando todo o ciclo de vida (produção do papel, transporte, energia da impressora)?**

**Por que precisa responder:**
- Diferentes fontes apresentam valores diferentes
- Preciso justificar qual metodologia de cálculo foi adotada no código
- Importante para comparação com outras iniciativas

**O que já sabemos:** Código usa valores de conversão, mas preciso fonte científica que os valide

---

#### **Questão 1.3:**
**Qual a taxa média de desperdício de impressões em ambientes corporativos brasileiros (percentual de impressões desnecessárias ou duplicadas)?**

**Por que precisa responder:**
- Questionário revelou desperdício, mas não quantificou nacionalmente
- Preciso contextualizar se o problema do setor fiscal é comum ou excepcional
- Auxilia a dimensionar o potencial de replicação da solução

**O que já sabemos:** Setor fiscal tem desperdício, mas falta comparação com média nacional

---

### 📌 **EIXO 2: EFICÁCIA DE SOLUÇÕES TECNOLÓGICAS**

#### **Questão 2.1:**
**Qual o percentual médio de redução de consumo de papel alcançado por sistemas de monitoramento de impressão em estudos científicos?**

**Por que precisa responder:**
- Preciso estabelecer meta realista de redução (20-30% foi estimativa)
- Fundamentar expectativas de resultado do projeto piloto
- Comparar com benchmarks de soluções similares

**O que já sabemos:** Dashboard monitora, mas não sei se 20-30% é realista baseado em literatura

---

#### **Questão 2.2:**
**Quais fatores (segundo a literatura) são mais eficazes para mudança de comportamento em sustentabilidade corporativa: monitoramento + feedback, gamificação, ou educação ambiental?**

**Por que precisa responder:**
- Dashboard combina múltiplas estratégias (dados + educação + não-punição)
- Preciso fundamentar teoricamente por que essas escolhas de design
- Auxilia a entender quais funcionalidades priorizar em futuras iterações

**O que já sabemos:** Código usa várias abordagens, mas preciso teoria que justifique

---

### 📌 **EIXO 3: EDUCAÇÃO AMBIENTAL CORPORATIVA**

#### **Questão 3.1:**
**Quais são as metodologias mais eficazes de educação ambiental para adultos em contextos corporativos, segundo estudos acadêmicos recentes?**

**Por que precisa responder:**
- Interface educativa do dashboard precisa fundamentação pedagógica
- Preciso validar se abordagem de equivalências tangíveis tem respaldo teórico
- Importante para justificar escolha de não usar abordagem punitiva

**O que já sabemos:** Dashboard educa, mas sem fundamentação pedagógica formal

---

#### **Questão 3.2:**
**Como a educação ambiental no ambiente de trabalho impacta práticas sustentáveis domésticas dos profissionais (efeito spillover)?**

**Por que precisa responder:**
- Potencial de impacto além do setor fiscal
- Justifica relevância social mais ampla do projeto
- Fortalece argumentação sobre importância da extensão universitária

**O que já sabemos:** Profissionais demonstraram interesse (questionário), mas não sei se aprendizado se transfere

---

### 📌 **EIXO 4: VIABILIDADE E REPLICABILIDADE**

#### **Questão 4.1:**
**Quais barreiras técnicas e organizacionais mais frequentes impedem a adoção de soluções sustentáveis em pequenas e médias organizações?**

**Por que precisa responder:**
- Dashboard foi desenvolvido para ser acessível (gratuito, simples)
- Preciso fundamentar se essas escolhas realmente eliminam barreiras identificadas na literatura
- Auxilia planejamento de estratégia de replicação

**O que já sabemos:** Soluções comerciais são caras (análise de mercado), mas preciso teoria sobre barreiras

---

#### **Questão 4.2:**
**Qual o papel do protocolo SNMP na democratização de soluções de IoT (Internet das Coisas) para sustentabilidade em organizações com recursos limitados?**

**Por que precisa responder:**
- Justificar escolha técnica de usar SNMP (aberto) vs. APIs proprietárias
- Fundamentar como tecnologia open source contribui para extensão universitária
- Relacionar escolha técnica com democratização de acesso (ODS)

**O que já sabemos:** Código usa SNMP, mas preciso teoria sobre democratização tecnológica

---

### 📌 **EIXO 5: CONTEXTO INSTITUCIONAL**

#### **Questão 5.1:**
**Quais são as principais normas e regulamentações brasileiras sobre gestão ambiental corporativa e relatórios de sustentabilidade?**

**Por que precisa responder:**
- Dashboard gera relatórios, mas preciso saber se atende alguma norma específica
- Pode aumentar relevância institucional da solução
- Auxilia a identificar outros setores que poderiam se beneficiar

**O que já sabemos:** Código gera relatórios, mas sem conhecimento de normas ISO ou ABNT aplicáveis

---

#### **Questão 5.2:**
**Como projetos de extensão universitária em sustentabilidade corporativa têm sido implementados em outras IES (Instituições de Ensino Superior) brasileiras?**

**Por que precisa responder:**
- Contextualizar o projeto dentro do campo da extensão universitária
- Identificar boas práticas de outros projetos similares
- Fortalecer argumentação sobre relevância acadêmica e social

**O que já sabemos:** Projeto é de extensão, mas não conheço outros projetos similares para comparar

---

## 📚 **FONTES DE INFORMAÇÃO PARA A PESQUISA**

### ✅ **FONTES PRIMÁRIAS (Prioritárias e Confiáveis)**

#### **1. BASES DE DADOS ACADÊMICAS**

**Google Scholar (scholar.google.com)**
- **O que buscar:** Artigos científicos sobre "impacto ambiental impressão", "educação ambiental corporativa", "mudança comportamental sustentabilidade"
- **Por que confiável:** Indexa publicações revisadas por pares
- **Foco:** Artigos dos últimos 5 anos (2019-2024)

**Scielo Brasil (scielo.br)**
- **O que buscar:** Estudos brasileiros sobre gestão ambiental corporativa, extensão universitária
- **Por que confiável:** Biblioteca científica de acesso aberto, padrões rigorosos
- **Foco:** Contexto brasileiro específico

**Portal de Periódicos CAPES**
- **O que buscar:** Artigos sobre tecnologias para sustentabilidade, SNMP, IoT ambiental
- **Por que confiável:** Acesso institucional via universidade a periódicos internacionais
- **Foco:** Literatura técnica especializada

---

#### **2. DOCUMENTOS OFICIAIS E NORMAS**

**ONU Brasil (brasil.un.org/pt-br/sdgs)**
- **O que buscar:** Metas detalhadas dos ODS 4, 12 e 13, indicadores oficiais
- **Por que confiável:** Fonte oficial dos Objetivos de Desenvolvimento Sustentável
- **Foco:** Fundamentação sobre alinhamento com ODS

**ABNT - Associação Brasileira de Normas Técnicas**
- **O que buscar:** Normas ISO 14001 (gestão ambiental), ISO 14064 (emissões de GEE)
- **Por que confiável:** Normas técnicas reconhecidas internacionalmente
- **Foco:** Metodologias de cálculo e gestão ambiental

**Ministério do Meio Ambiente (mma.gov.br)**
- **O que buscar:** Dados sobre geração de resíduos sólidos, reciclagem de papel no Brasil
- **Por que confiável:** Dados governamentais oficiais
- **Foco:** Contexto nacional de gestão de resíduos

---

#### **3. INSTITUIÇÕES DE PESQUISA ESPECIALIZADAS**

**GHG Protocol Brasil (ghgprotocolbrasil.com.br)**
- **O que buscar:** Metodologias de cálculo de emissões de CO₂, fatores de emissão
- **Por que confiável:** Padrão internacional para inventários de gases de efeito estufa
- **Foco:** Validar cálculos do módulo de sustentabilidade

**IPCC - Painel Intergovernamental sobre Mudanças Climáticas (ipcc.ch)**
- **O que buscar:** Relatórios sobre impacto climático, mitigação de emissões
- **Por que confiável:** Referência científica global em mudanças climáticas
- **Foco:** Fundamentação sobre ODS 13

**WWF Brasil (wwf.org.br)**
- **O que buscar:** Estudos sobre pegada ecológica, consumo de recursos naturais
- **Por que confiável:** ONG ambiental com estudos técnicos rigorosos
- **Foco:** Equivalências ambientais (papel → árvores)

---

#### **4. LITERATURA TÉCNICA DE DESENVOLVIMENTO**

**Python Software Foundation (python.org/doc)**
- **O que buscar:** Documentação sobre bibliotecas PySNMP, Streamlit, Plotly
- **Por que confiável:** Documentação oficial das tecnologias utilizadas
- **Foco:** Fundamentação técnica das escolhas de implementação

**RFCs (Request for Comments) - IETF**
- **O que buscar:** RFC 1157 (especificação SNMP), protocolos de rede
- **Por que confiável:** Padrões oficiais de protocolos de internet
- **Foco:** Justificar escolha de SNMP como tecnologia aberta

---

#### **5. ESTUDOS DE CASO E RELATÓRIOS CORPORATIVOS**

**GRI - Global Reporting Initiative (globalreporting.org)**
- **O que buscar:** Padrões de relatórios de sustentabilidade corporativa
- **Por que confiável:** Padrão global de relatórios ESG
- **Foco:** Estrutura de relatórios executivos do dashboard

**SEBRAE (sebrae.com.br)**
- **O que buscar:** Estudos sobre sustentabilidade em PMEs, economia circular
- **Por que confiável:** Instituição de apoio a empreendimentos, dados nacionais
- **Foco:** Viabilidade para organizações de pequeno/médio porte

---

### ✅ **FONTES SECUNDÁRIAS (Complementares)**

#### **6. ORGANIZAÇÕES SETORIAIS**

**Two Sides Brasil (twosides.org.br)**
- **O que buscar:** Dados sobre ciclo de vida do papel, reciclagem
- **Por que usar com cautela:** Representa indústria de papel (possível viés)
- **Foco:** Dados técnicos sobre produção de papel, se cruzados com outras fontes

**ABICP - Associação Brasileira da Indústria de Celulose e Papel**
- **O que buscar:** Estatísticas de consumo de papel no Brasil
- **Por que usar com cautela:** Representa indústria (viés possível)
- **Foco:** Dados quantitativos nacionais

---

#### **7. PUBLICAÇÕES DE REFERÊNCIA**

**Livros Acadêmicos:**
- "Educação Ambiental: Princípios e Práticas" (Dias, Genebaldo Freire)
- "Gestão Ambiental Empresarial" (Donaire, Denis)
- "Sustentabilidade Corporativa" (Almeida, Fernando)

**Revistas Científicas Relevantes:**
- Revista Brasileira de Educação Ambiental (RevBEA)
- Revista de Gestão Ambiental e Sustentabilidade (GeAS)
- Sustainability (MDPI) - internacional

---

## 📋 **ESTRATÉGIA DE PESQUISA**

### **Passo 1: Pesquisa por Questão**

Para cada questão identificada:
1. Definir palavras-chave específicas
2. Buscar em 2-3 fontes diferentes
3. Priorizar publicações dos últimos 5 anos
4. Verificar credibilidade (revisão por pares, instituição)

### **Passo 2: Organização das Informações**

Criar fichamento com:
- Fonte completa (ABNT)
- Questão que responde
- Principais achados
- Citações relevantes
- Aplicação no projeto

### **Passo 3: Validação Cruzada**

- Comparar dados de múltiplas fontes
- Identificar consensos e divergências
- Priorizar fontes mais recentes e confiáveis

---

## 📝 **RESPOSTA RESUMIDA PARA O TRABALHO**

### **Questões que faltam responder (~500 caracteres):**

Precisamos aprofundar: (1) Quantificação científica do impacto ambiental de impressões (CO₂, água, árvores) para validar cálculos do dashboard; (2) Eficácia de sistemas de monitoramento na redução de desperdícios segundo literatura; (3) Metodologias eficazes de educação ambiental corporativa; (4) Barreiras à adoção de soluções sustentáveis em organizações; (5) Normas brasileiras de gestão ambiental aplicáveis. Estas questões fundamentarão teoricamente escolhas técnicas já implementadas e estabelecerão metas realistas de impacto.

---

### **Fontes de informação (~500 caracteres):**

Utilizaremos: (1) Bases acadêmicas (Google Scholar, Scielo) para fundamentação científica sobre impacto ambiental e educação; (2) Documentos oficiais (ONU, ABNT ISO 14001, GHG Protocol) para metodologias de cálculo e alinhamento com ODS; (3) Instituições especializadas (WWF, IPCC) para dados sobre pegada ecológica; (4) Literatura técnica (Python docs, RFCs) para justificar escolhas tecnológicas; (5) Relatórios corporativos (GRI, SEBRAE) sobre gestão sustentável. Priorizaremos publicações dos últimos 5 anos com revisão por pares.

---

## 🎯 **COMO AS RESPOSTAS FORTALECERÃO O PROJETO**

| **Questão** | **Como fortalece o projeto** |
|------------|----------------------------|
| Impacto quantificado | Credibiliza métricas do dashboard |
| Eficácia de soluções | Estabelece metas realistas |
| Metodologias educativas | Fundamenta design da interface |
| Barreiras organizacionais | Justifica escolhas de acessibilidade |
| Normas brasileiras | Aumenta relevância institucional |

---

## 📖 **REFLEXÃO: RELAÇÃO ENSINO-PESQUISA-EXTENSÃO**

A Resolução CNE/CES nº 7/2018 destaca que extensão deve articular ensino e pesquisa. Este aprofundamento teórico cumpre essa função ao:

- **Ensino:** Aplicar conhecimentos técnicos do curso (desenvolvimento back-end) em contexto real
- **Pesquisa:** Investigar literatura científica para fundamentar solução desenvolvida
- **Extensão:** Conectar conhecimento acadêmico com necessidades do setor fiscal

O ciclo não é linear (pesquisa → desenvolvimento → aplicação), mas **recursivo**: desenvolvemos primeiro (prática), agora aprofundamos teoria (pesquisa) para refinar e justificar (ensino + extensão).

---

**Data:** ___/___/_____  
**Responsável:** _______________________

