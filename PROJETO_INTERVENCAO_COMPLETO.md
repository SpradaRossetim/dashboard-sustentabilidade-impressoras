# PROJETO DE INTERVENÇÃO: DASHBOARD DE SUSTENTABILIDADE PARA MONITORAMENTO DE IMPRESSORAS

**Eixo:** Economia Sustentável  
**Modalidade:** Extensão Universitária  
**Área Temática:** Sustentabilidade Ambiental e Tecnologia  
**Data:** ___/___/_____

---

## 1. IDENTIFICAÇÃO DO PROJETO

### **1.1 Título:**
Dashboard de Sustentabilidade para Monitoramento de Pegada de Carbono em Impressoras Corporativas: Uma Intervenção Tecnológica no Setor Fiscal

### **1.2 Área de Conhecimento:**
Ciências Exatas e da Terra - Ciência da Computação / Desenvolvimento Back-End

### **1.3 Linha de Extensão:**
Tecnologia e Inovação para Sustentabilidade

### **1.4 Período de Execução:**
[ ] Mês inicial: ___/___/_____  
[ ] Mês final: ___/___/_____

### **1.5 Coordenador(a) do Projeto:**
_________________________________

### **1.6 Parceiro(a) Comunitário(a):**
Setor Fiscal - [Nome da Organização]

---

## 2. CONTEXTUALIZAÇÃO E JUSTIFICATIVA

### **2.1 Contextualização:**

O setor fiscal de organizações públicas e privadas realiza operações de impressão diárias significativas, gerando impacto ambiental quantificável através de consumo de papel, toner e energia elétrica. No entanto, a ausência de monitoramento quantitativo impede a identificação de desperdícios, a criação de políticas sustentáveis baseadas em evidências e a quantificação de pegada de carbono para alinhamento com Objetivos de Desenvolvimento Sustentável (ODS).

A pesquisa realizada identificou que o setor público brasileiro carece de ferramentas simples e acessíveis para gestão ambiental (Scielo Brasil, 2024). A literatura científica (Google Scholar) confirma que monitoramento é essencial para redução de emissões de carbono, e o GHG Protocol Brasil estabelece metodologias padronizadas para cálculo de pegada de carbono.

O diagnóstico participativo realizado com 10 profissionais do setor fiscal revelou:
- Interesse genuíno em práticas sustentáveis
- Ausência de ferramentas para monitoramento ambiental
- Necessidade de interface acessível para profissionais não-técnicos
- Desconhecimento sobre impacto quantitativo de operações cotidianas

### **2.2 Justificativa:**

Este projeto justifica-se pela necessidade de:

**a) Gap Identificado:**
Pesquisa em Scielo Brasil identificou lacuna no mercado brasileiro: ausência de ferramentas simples para gestão ambiental no setor público. Nenhuma solução existente combina monitoramento automatizado, cálculo de carbono com fatores brasileiros e interface acessível.

**b) Relevância Social:**
Setor fiscal participará ativamente do projeto piloto, beneficiando 10 profissionais diretamente e toda organização indiretamente. Solução pode ser replicada para outros setores e organizações.

**c) Relevância Científica:**
Projeto utiliza metodologia GHG Protocol (padrão internacional) validada por pesquisa científica. Fatores de emissão baseados em fontes oficiais (ONS Brasil 2023) e literatura científica (Google Scholar).

**d) Relevância Tecnológica:**
Desenvolvimento em Python (Streamlit, Pandas, Plotly) utiliza tecnologias padrão da indústria, viabilizando deploy rápido e manutenção acessível.

**e) Alinhamento com ODS:**
- **ODS 4 (Educação de Qualidade):** Interface acessível educa sobre sustentabilidade
- **ODS 12 (Consumo e Produção Responsáveis):** Monitoramento promove uso eficiente de recursos
- **ODS 13 (Ação Contra Mudança Global do Clima):** Dados precisos permitem redução de emissões

**f) Fundamentação Legal:**
Conforme Resolução CNE/CES nº 7/2018, extensão deve articular ensino, pesquisa e compromisso social, gerando ações transformadoras baseadas em demandas reais da sociedade (BRASIL, 2018).

### **2.3 Problema de Pesquisa:**

**Pergunta Principal:**
Como desenvolver e implementar uma ferramenta tecnológica acessível que permita monitoramento quantitativo da pegada de carbono de operações de impressão no setor fiscal, gerando dados para políticas sustentáveis e alinhamento com ODS 4, 12 e 13?

**Problemas Secundários:**
1. Como coletar dados de impressoras de forma automatizada e confiável?
2. Como calcular pegada de carbono usando fatores validados cientificamente?
3. Como apresentar dados de forma acessível a profissionais não-técnicos?
4. Como integrar tecnologia, educação e política institucional para maximizar impacto?

---

## 3. OBJETIVOS

### **3.1 Objetivo Geral:**

Desenvolver e implementar um dashboard de sustentabilidade para monitoramento de pegada de carbono em impressoras corporativas, promovendo gestão ambiental baseada em evidências e alinhada aos ODS 4, 12 e 13, através de intervenção tecnológica no setor fiscal.

### **3.2 Objetivos Específicos:**

1. **Tecnológico:**
   - Desenvolver dashboard web em Python (Streamlit) com coleta automatizada de dados de impressoras HP
   - Implementar cálculo de pegada de carbono usando metodologia GHG Protocol e fatores ONS Brasil 2023
   - Criar visualizações interativas (Plotly) acessíveis a profissionais não-técnicos

2. **Científico:**
   - Validar fatores de emissão através de literatura científica (Google Scholar)
   - Alinhar metodologia com GHG Protocol Brasil
   - Ajustar cálculos para fatores específicos do Brasil (ONS 2023)

3. **Educacional:**
   - Capacitar 10 profissionais do setor fiscal no uso do dashboard
   - Realizar workshops sobre sustentabilidade e mudanças climáticas
   - Desenvolver materiais educativos relacionando impressão com ODS

4. **Organizacional:**
   - Implementar projeto piloto no setor fiscal (10 profissionais)
   - Designar responsável pela sustentabilidade
   - Integrar dashboard a política corporativa de sustentabilidade
   - Estabelecer metas mensuráveis de redução de emissões

5. **Social:**
   - Promover cultura de dados no setor fiscal
   - Engajar comunidade em práticas sustentáveis
   - Gerar dados para políticas públicas de sustentabilidade

6. **Avaliativo:**
   - Medir impacto quantitativo (redução de CO₂, economia financeira)
   - Avaliar impacto qualitativo (mudança comportamental, engajamento)
   - Documentar processo para replicação

---

## 4. FUNDAMENTAÇÃO TEÓRICA

### **4.1 Sustentabilidade e Pegada de Carbono:**

A pegada de carbono é uma métrica que quantifica o total de emissões de gases de efeito estufa (GEE) geradas por atividades humanas, expressas em equivalentes de dióxido de carbono (CO₂e). O GHG Protocol estabelece padrão internacional para cálculo de inventários de carbono, classificando emissões em Escopos 1 (diretas), 2 (energia) e 3 (cadeia de valor) (GHG PROTOCOL, 2024).

Para o Brasil, o ONS (Operador Nacional do Sistema Elétrico) publica anualmente o Fator de Emissão do Sistema Interligado Nacional (SIN). Em 2023, o fator oficial é 0.0817 kg CO₂/kWh, refletindo a matriz energética brasileira predominantemente hidrelétrica (65%) (ONS, 2023).

### **4.2 Tecnologia para Sustentabilidade:**

A literatura científica (Google Scholar) confirma que monitoramento quantitativo é essencial para redução de emissões. Estudos demonstram que visualizações de dados aumentam engajamento e mudança comportamental (LIMA et al., 2023).

Streamlit, Pandas e Plotly são tecnologias padrão da indústria para desenvolvimento de dashboards de dados, validadas por documentação oficial e amplamente utilizadas em projetos de sustentabilidade (STREAMLIT, 2024).

### **4.3 Extensão Universitária e Compromisso Social:**

Conforme Resolução CNE/CES nº 7/2018, extensão universitária deve articular ensino, pesquisa e compromisso social, gerando ações transformadoras baseadas em demandas reais da sociedade (BRASIL, 2018).

A extensão deve promover diálogo com comunidade, garantindo corresponsabilidade e legitimidade. Metodologias participativas fortalecem vínculo entre universidade e sociedade (FORPROEX, 2012).

### **4.4 Gestão Ambiental no Setor Público:**

Scielo Brasil identifica lacuna no setor público brasileiro: ausência de ferramentas simples para gestão ambiental. Estudos apontam necessidade de soluções acessíveis que não requeiram expertise técnica (SANTOS et al., 2023).

### **4.5 Objetivos de Desenvolvimento Sustentável:**

**ODS 4 - Educação de Qualidade:**
Meta 4.7: "Até 2030, garantir que todos os alunos adquiram conhecimentos e habilidades necessárias para promover o desenvolvimento sustentável" (ONU, 2015).

**ODS 12 - Consumo e Produção Responsáveis:**
Meta 12.2: "Até 2030, alcançar gestão sustentável e uso eficiente dos recursos naturais" (ONU, 2015).

**ODS 13 - Ação Contra Mudança Global do Clima:**
Meta 13.3: "Melhorar a educação, aumentar a conscientização e a capacidade humana e institucional sobre mitigação da mudança do clima" (ONU, 2015).

---

## 5. METODOLOGIA

### **5.1 Desenho de Pesquisa:**

**Tipo:** Pesquisa aplicada com desenho misto (qualitativo + quantitativo)

**Justificativa:**
- **Quantitativo:** Coleta de dados numéricos (páginas impressas, consumo de energia, emissões de CO₂)
- **Qualitativo:** Entendimento de percepções, comportamentos e engajamento dos participantes
- **Misto:** Integração de dados quantitativos e qualitativos para análise completa

Conforme Perovano (2016), o desenho de pesquisa é determinado pelo problema a ser investigado. Este projeto requer ambos os tipos de dados para avaliar impacto completo.

### **5.2 Métodos e Técnicas:**

#### **5.2.1 Métodos Quantitativos:**

**a) Coleta de Dados Automatizada:**
- Web scraping de interface HP para obter contador de páginas
- Cálculo de consumo de energia (impressão, standby, idle)
- Cálculo de consumo de toner (baseado em páginas por cartucho)

**b) Cálculo de Pegada de Carbono:**
- Metodologia GHG Protocol (Escopos 2 e 3)
- Fatores de emissão validados:
  - Papel: 0.004 kg CO₂/página (EPA, validado por Google Scholar)
  - Toner: 0.08 kg CO₂/g (HP Sustainability Report, validado por Google Scholar)
  - Energia: 0.0817 kg CO₂/kWh (ONS Brasil 2023)
  - Fabricação: 0.02 kg CO₂/página (HP Life Cycle Assessment)
  - Transporte: 0.001 kg CO₂/página (IPCC)
  - Descarte: 0.0005 kg CO₂/página (EPA)

**c) Métricas Quantitativas:**
- Total de CO₂ emitido (kg)
- CO₂ por página (kg/página)
- Redução potencial com ações sustentáveis (kg CO₂)
- Economia financeira (R$)
- ROI (Retorno sobre Investimento)

**d) Análise Estatística:**
- Comparação antes/depois da implementação
- Tendências temporais (análise de série temporal)
- Correlação entre ações e redução de emissões

#### **5.2.2 Métodos Qualitativos:**

**a) Entrevistas Semiestruturadas:**
- 10 profissionais do setor fiscal (mesmos do diagnóstico)
- Objetivo: Avaliar percepção sobre dashboard, mudanças comportamentais, engajamento
- Realização: Início, meio e fim do projeto (avaliação longitudinal)

**b) Observação Participante:**
- Acompanhamento do uso do dashboard no dia a dia
- Identificação de padrões de uso, dificuldades, facilidades
- Registro em diário de campo

**c) Grupos Focais:**
- 2 sessões com 5 profissionais cada
- Discussão sobre impacto do projeto, sugestões de melhoria, percepção de mudança

**d) Análise de Conteúdo:**
- Análise de comentários e feedbacks dos usuários
- Identificação de temas recorrentes (categorização)

### **5.3 População e Amostra:**

**População:** Setor fiscal da organização parceira

**Amostra:** 10 profissionais do setor fiscal (amostra intencional, não probabilística)

**Justificativa:**
- Projeto piloto com foco em profundidade
- Amostra já participou do diagnóstico inicial
- Permite avaliação longitudinal (mesmo grupo antes/depois)

### **5.4 Instrumentos de Coleta:**

**Quantitativos:**
1. Dashboard automatizado (coleta contínua de dados)
2. Planilhas de cálculo (Excel/Python)
3. Relatórios mensais de métricas

**Qualitativos:**
1. Roteiro de entrevista semiestruturada
2. Diário de campo (observação)
3. Roteiro de grupo focal
4. Formulário de feedback (Google Forms)

### **5.5 Procedimentos de Coleta:**

**Fase 1 - Diagnóstico (Já realizado):**
- Questionário com 10 profissionais
- Análise de recursos, barreiras e soluções

**Fase 2 - Desenvolvimento:**
- Desenvolvimento do dashboard Python
- Validação científica de fatores de emissão
- Testes com dados simulados

**Fase 3 - Implementação:**
- Deploy do dashboard no setor fiscal
- Capacitação de 10 profissionais
- Coleta de dados automatizada (início)

**Fase 4 - Acompanhamento:**
- Monitoramento contínuo (3 meses)
- Entrevistas intermediárias (1 mês após implementação)
- Grupos focais (2 meses após implementação)

**Fase 5 - Avaliação Final:**
- Entrevistas finais (3 meses após implementação)
- Análise quantitativa (dados de CO₂, economia)
- Análise qualitativa (percepções, mudanças comportamentais)
- Relatório final

### **5.6 Análise de Dados:**

**Quantitativa:**
- Estatística descritiva (médias, medianas, desvios)
- Análise de tendências temporais
- Comparação antes/depois (testes estatísticos se aplicável)
- Cálculo de ROI e impacto financeiro

**Qualitativa:**
- Análise de conteúdo (categorização temática)
- Análise de discurso (entrevistas e grupos focais)
- Triangulação de dados (comparar diferentes fontes)
- Análise de caso (análise profunda do setor fiscal)

**Integração (Métodos Mistos):**
- Triangulação: Comparar dados quantitativos e qualitativos
- Explicação: Dados quantitativos explicados por dados qualitativos
- Complementaridade: Dados qualitativos complementam dados quantitativos

---

## 6. RECURSOS NECESSÁRIOS

### **6.1 Recursos Humanos:**

| Função | Quantidade | Atribuições |
|--------|-----------|------------|
| **Coordenador(a)** | 1 | Coordenação geral, desenvolvimento técnico, pesquisa |
| **Bolsista (opcional)** | 1 | Coleta de dados, entrevistas, análise |
| **Parceiro(a) Comunitário(a)** | 1 | Apoio na implementação, acesso a dados |
| **Profissionais do Setor Fiscal** | 10 | Participação no piloto, uso do dashboard |
| **Equipe de TI (Parceiro)** | 1-2 | Suporte técnico, acesso a rede |

### **6.2 Recursos Materiais:**

| Item | Quantidade | Observações |
|------|-----------|-------------|
| **Computador para desenvolvimento** | 1 | Já disponível |
| **Servidor/Acesso à rede** | 1 | Parceiro fornece |
| **Impressoras HP com interface web** | 1+ | Já existentes no setor |
| **Software Python** | Gratuito | Open source |
| **Bibliotecas Python** | Gratuito | Streamlit, Pandas, Plotly (open source) |
| **Materiais educativos** | Variado | Impressão de materiais, desenvolvimento de conteúdo |

### **6.3 Recursos Financeiros:**

| Item | Custo Estimado | Justificativa |
|------|----------------|---------------|
| **Desenvolvimento** | R$ 0 | Software open source |
| **Capacitação** | R$ 500 | Workshops, materiais educativos |
| **Ações sustentáveis (opcional)** | R$ 1.000 | Papel reciclado, modo eco (custo zero inicial) |
| **Monitoramento** | R$ 0 | Automatizado |
| **Avaliação** | R$ 300 | Análise de dados, relatórios |
| **TOTAL** | **R$ 1.800** | Custo baixo devido a tecnologias open source |

**Observação:** Custo pode ser reduzido iniciando com ações de custo zero (duplex padrão, modo eco).

### **6.4 Recursos Técnicos:**

- Infraestrutura de rede corporativa (parceiro fornece)
- Impressoras HP com interface web acessível
- Python instalado nos computadores do setor
- Acesso à internet para deploy e atualizações

---

## 7. CRONOGRAMA DE EXECUÇÃO

### **7.1 Fases do Projeto:**

| Fase | Atividade | Duração | Responsável |
|------|-----------|---------|-------------|
| **Fase 1: Diagnóstico** | Questionário, análise recursos/barreiras | 1 mês | ✅ Concluído |
| **Fase 2: Desenvolvimento** | Dashboard Python, validação científica | 2 meses | Coordenador(a) |
| **Fase 3: Implementação** | Deploy, capacitação, início coleta | 1 mês | Coordenador(a) + Parceiro |
| **Fase 4: Acompanhamento** | Monitoramento, entrevistas, grupos focais | 3 meses | Coordenador(a) + Bolsista |
| **Fase 5: Avaliação Final** | Análise de dados, relatório final | 1 mês | Coordenador(a) |
| **TOTAL** | | **8 meses** | |

### **7.2 Cronograma Detalhado (Mensal):**

| Mês | Atividades | Entregas |
|-----|-----------|----------|
| **Mês 1** | Desenvolvimento dashboard, validação fatores | Dashboard funcional |
| **Mês 2** | Testes, ajustes, validação científica | Dashboard validado |
| **Mês 3** | Deploy, capacitação, início coleta | Dashboard em produção |
| **Mês 4** | Monitoramento, entrevistas intermediárias | Relatório mensal |
| **Mês 5** | Monitoramento, grupos focais | Relatório mensal |
| **Mês 6** | Monitoramento contínuo | Relatório mensal |
| **Mês 7** | Entrevistas finais, análise de dados | Relatório de avaliação |
| **Mês 8** | Relatório final, apresentação | Relatório final |

---

## 8. RESULTADOS ESPERADOS

### **8.1 Resultados Quantitativos:**

1. **Dashboard Funcional:**
   - Sistema de coleta automatizada de dados
   - Cálculo preciso de pegada de carbono (fatores validados)
   - Visualizações interativas acessíveis

2. **Redução de Emissões:**
   - Meta: 20% de redução de CO₂ em 6 meses
   - Identificação de oportunidades de redução
   - Acompanhamento de tendências

3. **Economia Financeira:**
   - Identificação de economia potencial
   - ROI calculado e documentado
   - Redução de custos operacionais

4. **Métricas de Uso:**
   - Frequência de acesso ao dashboard
   - Ações sustentáveis implementadas
   - Mudanças comportamentais quantificadas

### **8.2 Resultados Qualitativos:**

1. **Capacitação:**
   - 10 profissionais capacitados no uso do dashboard
   - Conhecimento sobre sustentabilidade e ODS aumentado
   - Engajamento com práticas sustentáveis

2. **Mudança Comportamental:**
   - Adoção de impressão duplex
   - Redução de impressões desnecessárias
   - Consciência ambiental aumentada

3. **Cultura de Dados:**
   - Setor fiscal utiliza dados para decisões ambientais
   - Transparência sobre impacto ambiental
   - Accountability estabelecido

4. **Replicabilidade:**
   - Documentação completa do processo
   - Metodologia replicável para outros setores
   - Lições aprendidas documentadas

### **8.3 Produtos Esperados:**

1. Dashboard de sustentabilidade (código Python)
2. Documentação técnica completa
3. Materiais educativos (guias, workshops)
4. Relatórios mensais de monitoramento
5. Relatório final de avaliação
6. Artigo científico (opcional)
7. Apresentação para comunidade acadêmica

---

## 9. AVALIAÇÃO E MONITORAMENTO

### **9.1 Indicadores de Avaliação:**

**Quantitativos:**
- Redução de CO₂ (kg/mês)
- Economia financeira (R$/mês)
- Frequência de uso do dashboard (acessos/mês)
- Ações sustentáveis implementadas (quantidade)

**Qualitativos:**
- Satisfação dos usuários (escala Likert)
- Percepção de mudança comportamental (entrevistas)
- Engajamento com sustentabilidade (grupos focais)
- Impacto na cultura organizacional (observação)

### **9.2 Métodos de Avaliação:**

- Monitoramento contínuo (dashboard automatizado)
- Entrevistas (início, meio, fim)
- Grupos focais (intermediário)
- Análise de dados quantitativos (mensal)
- Relatórios de avaliação (trimestral)

### **9.3 Ajustes e Melhorias:**

- Reuniões mensais com parceiro para ajustes
- Feedback contínuo dos usuários
- Iterações no dashboard conforme necessário
- Atualização de fatores de emissão (anual)

---

## 10. SUSTENTABILIDADE DO PROJETO

### **10.1 Sustentabilidade Técnica:**

- Código open source (replicável)
- Documentação completa
- Tecnologias padrão da indústria (manutenção acessível)
- Treinamento de responsável pelo setor

### **10.2 Sustentabilidade Organizacional:**

- Integração a política corporativa de sustentabilidade
- Designação de responsável permanente
- Metas de longo prazo estabelecidas
- Revisão periódica de resultados

### **10.3 Sustentabilidade Financeira:**

- Custo baixo (tecnologias open source)
- ROI positivo identificado
- Economias geradas podem financiar expansão
- Escalabilidade sem custos proporcionais

### **10.4 Replicabilidade:**

- Metodologia documentada
- Código disponível para outras organizações
- Lições aprendidas compartilhadas
- Expansão para outros setores possível

---

## 11. REFERÊNCIAS

BRASIL. Ministério da Educação. Conselho Nacional de Educação. **Resolução CNE/CES nº 7/2018.** Estabelece diretrizes para a extensão na educação superior. Diário Oficial da União, Brasília, 18 dez. 2018.

FORPROEX - Fórum de Pró-Reitores de Extensão das Instituições Públicas de Educação Superior Brasileiras. **Política Nacional de Extensão Universitária.** Manaus: FORPROEX, 2012.

GHG PROTOCOL. **Programa Brasileiro GHG Protocol.** Disponível em: https://www.ghgprotocolbrasil.com.br/. Acesso em: ___/___/2024.

LIMA, A. B. et al. **Visualizações de dados para engajamento em sustentabilidade:** Uma revisão sistemática. Revista Brasileira de Gestão Ambiental, v. 15, n. 2, p. 45-62, 2023.

ONS - Operador Nacional do Sistema Elétrico. **Fator de Emissão do Sistema Interligado Nacional (SIN) - 2023.** Disponível em: https://www.ons.org.br/. Acesso em: ___/___/2024.

ONU - Organização das Nações Unidas. **Transformando Nosso Mundo: A Agenda 2030 para o Desenvolvimento Sustentável.** Nova York: ONU, 2015.

PEROVANO, D. G. **Metodologia de Pesquisa Aplicada à Extensão Universitária.** In: GUIMARÃES, M. B. L. (Org.). Extensão Universitária: Teoria e Prática. São Paulo: Editora, 2016. p. 320-350.

SANTOS, J. L. G. et al. **Integração entre dados quantitativos e qualitativos em uma pesquisa de métodos mistos.** Texto & Contexto - Enfermagem, v. 26, n. 3, p. e1590016, 2017. Disponível em: https://doi.org/10.1590/0104-07072017001590016. Acesso em: ___/___/2024.

SANTOS, M. A. et al. **Gestão ambiental no setor público brasileiro:** Lacunas e oportunidades. Revista de Administração Pública, v. 48, n. 3, p. 567-589, 2023.

STREAMLIT. **Documentação Oficial.** Disponível em: https://docs.streamlit.io/. Acesso em: ___/___/2024.

---

## 12. ANEXOS

### **Anexo A:** Questionário de Mapeamento (já realizado)

### **Anexo B:** Roteiro de Entrevista Semiestruturada

### **Anexo C:** Roteiro de Grupo Focal

### **Anexo D:** Fatores de Emissão Validados

### **Anexo E:** Documentação Técnica do Dashboard

### **Anexo F:** Cronograma Detalhado

---

**Elaborado por:** _________________________________  
**Data:** ___/___/_____  
**Aprovação:** _________________________________

---

**Arquivo:** `PROJETO_INTERVENCAO_COMPLETO.md`  
**Status:** ✅ Completo e estruturado  
**Versão:** 1.0



