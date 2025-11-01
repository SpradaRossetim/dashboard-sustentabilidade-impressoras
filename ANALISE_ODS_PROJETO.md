# ANÁLISE DOS ODS NO PROJETO - Dashboard de Sustentabilidade

---

## 🎯 ODS SELECIONADOS PARA O PROJETO

Baseado na análise do dashboard desenvolvido e dos desafios identificados no setor fiscal, selecionamos os seguintes ODS:

### ✅ **ODS PRINCIPAIS (Conexão Direta e Forte)**

#### 🌍 **ODS 12 - Consumo e Produção Responsáveis**
**Justificativa de seleção:**
Este é o ODS central do projeto. Nosso dashboard foi desenvolvido especificamente para promover uso consciente de recursos em ambientes corporativos. O sistema monitora consumo de papel, toner e energia das impressoras, identificando desperdícios e incentivando práticas de impressão responsável. A redução de consumo de recursos naturais (celulose, água na produção de papel, minérios em cartuchos) está no cerne da solução desenvolvida.

**Conexão com o código:**
- Módulo `hp_printer_scanner.py`: monitora consumo de recursos em tempo real
- Dashboard Streamlit: visualiza padrões de desperdício
- Relatórios: quantificam economia de recursos alcançada

**Meta 12.2:** "Até 2030, alcançar a gestão sustentável e o uso eficiente dos recursos naturais"
**Meta 12.5:** "Até 2030, reduzir substancialmente a geração de resíduos por meio da prevenção, redução, reciclagem e reuso"

---

#### 🌡️ **ODS 13 - Ação Contra a Mudança Global do Clima**
**Justificativa de seleção:**
O projeto calcula e visualiza a pegada de carbono das operações de impressão, conectando ações cotidianas do setor fiscal com impacto climático global. O módulo `metodologia_calculos_sustentabilidade.py` converte páginas impressas em emissões de CO₂ equivalentes, tornando tangível a contribuição individual e coletiva para mudanças climáticas. Conscientização climática é um dos pilares educativos do dashboard.

**Conexão com o código:**
- Cálculo de emissões de CO₂ por página impressa
- Equivalências em quilômetros de carro (contextualização climática)
- Monitoramento de tendências de emissões ao longo do tempo
- Relatórios executivos de impacto climático

**Meta 13.3:** "Melhorar a educação, aumentar a conscientização e a capacidade humana e institucional sobre mitigação, adaptação, redução de impacto e alerta precoce da mudança do clima"

---

### ⭐ **ODS SECUNDÁRIOS (Conexão Relevante)**

#### 📚 **ODS 4 - Educação de Qualidade**
**Justificativa de seleção:**
Embora o projeto não seja primariamente educacional, a conscientização ambiental é um de seus pilares fundamentais. O dashboard foi projetado como ferramenta educativa que transforma dados técnicos em aprendizados sobre sustentabilidade. Explicações sobre metodologia de cálculo, contextualizações em equivalências tangíveis (árvores, CO₂) e visualizações didáticas promovem educação ambiental no ambiente corporativo.

**Conexão com o código:**
- Interface educativa com explicações contextualizadas
- Metodologia transparente de cálculos (módulo dedicado)
- Visualizações didáticas transformando números em aprendizado
- Abordagem não-punitiva focada em conscientização

**Meta 4.7:** "Até 2030, garantir que todos os alunos adquiram conhecimentos e habilidades necessárias para promover o desenvolvimento sustentável, inclusive, entre outros, por meio da educação para o desenvolvimento sustentável e estilos de vida sustentáveis"

---

### ❓ **ODS NÃO SELECIONADOS (Conexão Fraca ou Ausente)**

#### ❌ **ODS 8 - Trabalho Decente e Crescimento Econômico**
**Justificativa para NÃO seleção:**
Embora o dashboard gere eficiência operacional e reduza custos (impacto econômico indireto), a conexão com trabalho decente e crescimento econômico é tangencial e forçada. O foco do projeto não está em condições de trabalho, emprego formal, crescimento do PIB ou produtividade econômica. A economia financeira é benefício secundário, não objetivo central.

**Conclusão:** Não selecionar para manter foco nos ODS centrais.

---

#### ❌ **ODS 1 - Erradicação da Pobreza**
**Justificativa para NÃO seleção:**
Não há conexão relevante entre o projeto e erradicação da pobreza. O dashboard atende setor corporativo (fiscal), não populações em situação de vulnerabilidade social. Não há componente de renda mínima, acesso a recursos básicos, proteção social ou redução de desigualdades socioeconômicas. Incluir este ODS seria desonesto intelectualmente e diluiria a clareza do projeto.

**Conclusão:** Definitivamente não selecionar.

---

## 📋 SELEÇÃO FINAL RECOMENDADA

### ✅ **ODS a marcar:**
1. ✅ **ODS 12 - Consumo e Produção Responsáveis** (CENTRAL)
2. ✅ **ODS 13 - Ação Contra a Mudança Global do Clima** (CENTRAL)
3. ✅ **ODS 4 - Educação de Qualidade** (SECUNDÁRIO mas relevante)

### ❌ **ODS a NÃO marcar:**
- ❌ ODS 8 - Trabalho Decente e Crescimento Econômico
- ❌ ODS 1 - Erradicação da Pobreza

---

## 🎯 JUSTIFICATIVA ACADÊMICA CONSOLIDADA

### Resposta para o trabalho (~500 caracteres):

Selecionamos três ODS alinhados aos desafios identificados: **ODS 12** (central) pois o dashboard promove consumo responsável de recursos monitorando desperdícios de papel, toner e energia; **ODS 13** (central) através do cálculo de pegada de carbono das impressões e conscientização sobre impacto climático; **ODS 4** (secundário) pela abordagem educativa que transforma dados técnicos em aprendizado sobre sustentabilidade. Não selecionamos ODS 1 (sem conexão com erradicação da pobreza) nem ODS 8 (foco não está em condições de trabalho), mantendo coerência entre desafios diagnosticados e objetivos propostos.

---

## 📊 TABELA DE CONEXÃO: PROBLEMA → ODS → SOLUÇÃO

| **Problema Identificado** | **ODS** | **Como o Código Atende** |
|--------------------------|---------|--------------------------|
| Desperdício de papel | ODS 12 | Monitora páginas impressas, identifica padrões |
| Desperdício de toner | ODS 12 | Rastreia uso de cartuchos |
| Consumo energético | ODS 12 | Calcula kWh das impressoras |
| Emissões de CO₂ | ODS 13 | Calcula pegada de carbono |
| Falta de conscientização | ODS 4 | Interface educativa, equivalências tangíveis |
| Impacto climático invisível | ODS 13 | Contextualiza emissões (km de carro) |
| Dados técnicos incompreensíveis | ODS 4 | Visualizações didáticas |

---

## 🌐 CONEXÃO COM CURSO DE DESENVOLVIMENTO BACK-END

Como estudante de **Desenvolvimento Back-End**, este projeto demonstra aplicação prática de competências técnicas para solucionar problemas socioambientais reais:

### **Tecnologias Back-End Aplicadas:**

**1. Python (Linguagem Back-End)**
- Estruturação de lógica de negócio
- Processamento de dados SNMP
- Algoritmos de cálculo de sustentabilidade

**2. APIs e Protocolos**
- Integração via SNMP (protocolo de rede)
- Coleta automatizada de dados de hardware
- Arquitetura modular escalável

**3. Processamento de Dados**
- Transformação de dados brutos em métricas significativas
- Agregações e análises temporais
- Cálculos de impacto ambiental

**4. Arquitetura de Software**
- Separação de responsabilidades (módulos dedicados)
- Código reutilizável e extensível
- Padrões de projeto aplicados

**5. Persistência de Dados**
- Armazenamento de histórico
- Recuperação de métricas temporais
- Estruturas de dados eficientes

### **Aprendizados Técnicos + Impacto Social:**

Este projeto exemplifica como **competências técnicas de back-end** podem ser direcionadas para **impacto socioambiental positivo**, conectando:

- 💻 **Código limpo e eficiente** → Solução sustentável e replicável
- 🌍 **Automação inteligente** → Redução de desperdício de recursos
- 📊 **Processamento de dados** → Decisões ambientalmente informadas
- 🔧 **Arquitetura robusta** → Escalabilidade para outras organizações

---

## 🎓 REFLEXÃO: TECNOLOGIA A SERVIÇO DOS ODS

### Resposta para o trabalho (~400 caracteres):

Como estudante de desenvolvimento back-end, este projeto demonstra que competências técnicas podem gerar impacto socioambiental concreto. Aplicando Python, APIs e processamento de dados, desenvolvemos solução que atende simultaneamente ODS 12, 13 e 4. Código bem estruturado não é apenas boa prática técnica, é responsabilidade social: tecnologia acessível e replicável democratiza sustentabilidade corporativa.

---

## 📖 CONCLUSÃO

A seleção dos ODS 12, 13 e 4 não é arbitrária, mas resultado da análise crítica do código desenvolvido e dos problemas que ele resolve. Cada módulo implementado conecta-se diretamente a metas específicas dos ODS escolhidos, demonstrando alinhamento entre diagnóstico participativo, desenvolvimento técnico e objetivos globais de sustentabilidade.

O exercício de vincular projeto de extensão universitária aos ODS reforça que desenvolvimento de software vai além de escrever código: é sobre aplicar conhecimento técnico para transformar realidades, promover conscientização e contribuir para futuro mais sustentável.

---

**Data:** ___/___/_____  
**Responsável:** _______________________  
**Curso:** Desenvolvimento Back-End

