# DELIMITAÇÃO TEMÁTICA DO PROJETO

---

## 🎯 TEMÁTICAS SELECIONADAS

Baseado no diagnóstico participativo realizado no setor fiscal e nas funcionalidades do dashboard desenvolvido, delimitamos as seguintes temáticas relacionadas à economia sustentável:

---

### 📌 **TEMÁTICA PRINCIPAL (Central e Prioritária)**

#### **1. DESPERDÍCIO DE RECURSOS NATURAIS EM AMBIENTES CORPORATIVOS**

**Delimitação precisa:**
Uso excessivo e não monitorado de papel, toner e energia elétrica nas operações de impressão do setor fiscal, resultando em consumo desnecessário de recursos naturais (celulose, minérios, água na produção) e geração de resíduos sólidos (cartuchos, papel descartado).

**Por que esta temática:**
- Identificada no questionário com 10 profissionais: maioria desconhecia volume real de impressões
- Ausência de ferramentas de monitoramento quantitativo
- Impacto ambiental significativo mas invisível nas operações diárias
- Problema concreto, mensurável e passível de intervenção técnica

**Conexão com ODS:**
- **ODS 12 (Meta 12.2):** Uso eficiente de recursos naturais
- **ODS 12 (Meta 12.5):** Redução de geração de resíduos

**Como o dashboard aborda:**
- Módulo `hp_printer_scanner.py` quantifica consumo em tempo real
- Visualizações mostram padrões de desperdício
- Equivalências tangíveis (X páginas = Y árvores) contextualizam impacto

---

### 📌 **TEMÁTICAS COMPLEMENTARES (Relevantes e Integradas)**

#### **2. INVISIBILIDADE DO IMPACTO AMBIENTAL DAS OPERAÇÕES COTIDIANAS**

**Delimitação precisa:**
Falta de visibilidade e compreensão sobre como ações operacionais cotidianas (imprimir documentos, usar impressoras standby) geram emissões de carbono e contribuem para mudanças climáticas, dificultando tomada de decisão ambientalmente consciente.

**Por que esta temática:**
- Questionário revelou subestimação generalizada do impacto ambiental
- Dados técnicos existentes (contadores de impressoras) não eram convertidos em informações significativas
- Ausência de conexão entre ações locais e desafios climáticos globais

**Conexão com ODS:**
- **ODS 13 (Meta 13.3):** Educação e conscientização sobre mudança climática
- **ODS 4 (Meta 4.7):** Educação para desenvolvimento sustentável

**Como o dashboard aborda:**
- Cálculo de pegada de carbono por impressão
- Equivalências em quilômetros de carro (contextualização climática)
- Módulo `metodologia_calculos_sustentabilidade.py` torna metodologia transparente

---

#### **3. AUSÊNCIA DE GESTÃO BASEADA EM DADOS PARA SUSTENTABILIDADE CORPORATIVA**

**Delimitação precisa:**
Inexistência de sistemas acessíveis e gratuitos para monitoramento, análise e gestão de indicadores ambientais em organizações de pequeno e médio porte, perpetuando tomada de decisão sem embasamento quantitativo sobre impacto ambiental.

**Por que esta temática:**
- Soluções comerciais são caras e inacessíveis (identificado na análise de mercado)
- Setor fiscal não possuía dados históricos sobre consumo
- Decisões eram baseadas em percepção, não em evidências
- Barreira tecnológica impede sustentabilidade corporativa

**Conexão com ODS:**
- **ODS 12:** Gestão sustentável requer dados para decisões informadas
- **ODS 4:** Capacitação técnica para uso de ferramentas de gestão ambiental

**Como o dashboard aborda:**
- Armazenamento de dados históricos para análises temporais
- Relatórios executivos exportáveis (`sustainability_executive_report.py`)
- Interface intuitiva eliminando barreira técnica
- Solução gratuita e open source democratizando acesso

---

#### **4. DÉFICIT DE CONSCIENTIZAÇÃO AMBIENTAL NO AMBIENTE CORPORATIVO**

**Delimitação precisa:**
Falta de educação ambiental contextualizada para profissionais corporativos, especialmente em setores administrativos, onde conexão entre rotinas de trabalho e impacto ecológico não é evidente, resultando em práticas insustentáveis por desconhecimento.

**Por que esta temática:**
- Questionário mostrou interesse forte em aprender sobre sustentabilidade
- Não existe cultura de conscientização ambiental institucionalizada
- Informações técnicas existentes não são acessíveis a não-especialistas
- Educação ambiental é vista como tema escolar, não corporativo

**Conexão com ODS:**
- **ODS 4 (Meta 4.7):** Educação para estilos de vida sustentáveis
- **ODS 13 (Meta 13.3):** Conscientização sobre clima

**Como o dashboard aborda:**
- Interface educativa com explicações contextualizadas
- Equivalências tangíveis tornando abstrato em concreto
- Abordagem não-punitiva focada em aprendizado
- Metodologia transparente promovendo compreensão crítica

---

## 🚫 **TEMÁTICAS NÃO ABORDADAS (e por quê)**

### ❌ Informalidade Produtiva
**Justificativa:** Projeto atua em ambiente corporativo formal (setor fiscal), não em economia informal ou produtores autônomos. Não há conexão relevante.

### ❌ Planejamento Financeiro Familiar/Individual
**Justificativa:** Foco está em gestão ambiental corporativa, não em finanças pessoais. Economia financeira gerada é benefício secundário institucional, não objetivo educacional de planejamento financeiro.

### ❌ Cadeia Produtiva e Fornecedores
**Justificativa:** Dashboard monitora consumo interno, não rastreia origem sustentável de insumos ou práticas de fornecedores. Escopo está no uso, não na produção.

---

## 📊 **SÍNTESE: TEMÁTICAS → PROBLEMAS → SOLUÇÕES**

| **Temática** | **Problema Específico** | **Solução no Dashboard** | **ODS** |
|-------------|------------------------|-------------------------|---------|
| **Desperdício de Recursos** | Consumo excessivo de papel, toner, energia | Monitoramento quantitativo automatizado | 12 |
| **Invisibilidade de Impacto** | Desconhecimento da pegada de carbono | Cálculo e visualização de emissões CO₂ | 13 |
| **Gestão sem Dados** | Decisões sem embasamento quantitativo | Histórico, relatórios, análises temporais | 12 |
| **Déficit de Conscientização** | Falta de educação ambiental corporativa | Interface educativa, equivalências tangíveis | 4, 13 |

---

## 📝 **RESPOSTA PARA O TRABALHO**

### Versão Concisa (~500 caracteres):

Delimitamos quatro temáticas interconectadas: **(1) Desperdício de recursos naturais** (papel, toner, energia) em operações de impressão do setor fiscal, identificado no diagnóstico como problema central; **(2) Invisibilidade do impacto ambiental** das ações cotidianas, dificultando decisões conscientes; **(3) Ausência de gestão baseada em dados** para sustentabilidade corporativa por inacessibilidade de ferramentas; **(4) Déficit de conscientização ambiental** no ambiente de trabalho. Estas temáticas relacionam-se à economia sustentável por promoverem uso eficiente de recursos, reduzirem custos operacionais e estabelecerem práticas produtivas ambientalmente responsáveis.

---

### Versão Expandida (~800 caracteres):

O diagnóstico participativo no setor fiscal revelou quatro temáticas prioritárias relacionadas à economia sustentável. A **temática central é o desperdício de recursos naturais**: consumo excessivo e não monitorado de papel, toner e energia nas impressões, resultando em uso desnecessário de recursos naturais e geração de resíduos. Complementarmente, identificamos **invisibilidade do impacto ambiental** das operações cotidianas, onde profissionais desconhecem suas emissões de CO₂ e contribuição para mudanças climáticas. A terceira temática é **ausência de gestão baseada em dados ambientais**, perpetuada pela inacessibilidade de ferramentas de monitoramento. Por fim, observamos **déficit de conscientização ambiental corporativa**, onde educação sobre sustentabilidade não é integrada às rotinas de trabalho. Estas temáticas conectam-se à economia sustentável ao promover eficiência no uso de recursos (redução de custos), prevenir desperdícios (Meta ODS 12.5) e estabelecer cultura de produção responsável no ambiente corporativo.

---

### Versão Detalhada (~1200 caracteres):

A delimitação temática baseou-se no diagnóstico participativo realizado com 10 profissionais do setor fiscal através de questionário, observação e análise documental. Identificamos quatro temáticas interconectadas relacionadas à economia sustentável e desenvolvimento responsável.

A **primeira temática (central) é o desperdício de recursos naturais em ambientes corporativos**, especificamente consumo excessivo de papel, toner e energia elétrica nas operações de impressão. O questionário revelou que a maioria dos profissionais desconhecia o volume real de impressões e não havia ferramentas de monitoramento quantitativo. Este desperdício representa uso ineficiente de recursos naturais (celulose, água, minérios) e geração desnecessária de resíduos sólidos, impactando diretamente a economia sustentável pela perda de valor econômico e degradação ambiental.

A **segunda temática é a invisibilidade do impacto ambiental das operações cotidianas**. Profissionais subestimam significativamente as emissões de CO₂ de suas atividades diárias, dificultando tomada de decisão ambientalmente consciente. Dados técnicos existentes (contadores de impressoras) não eram convertidos em informações significativas, perpetuando desconexão entre ações locais e desafios climáticos globais.

A **terceira temática é a ausência de gestão baseada em dados para sustentabilidade corporativa**. A análise de mercado revelou que soluções comerciais são caras e inacessíveis para organizações de pequeno e médio porte, criando barreira tecnológica que impede gestão ambiental eficaz. Sem dados históricos e análises quantitativas, decisões sobre sustentabilidade eram baseadas em percepção, não evidências.

A **quarta temática é o déficit de conscientização ambiental no ambiente corporativo**. Não existe cultura institucionalizada de educação ambiental em setores administrativos, onde conexão entre rotinas de trabalho e impacto ecológico não é evidente. O questionário mostrou forte interesse em aprender sobre sustentabilidade, mas ausência de oportunidades contextualizadas ao ambiente de trabalho.

Estas quatro temáticas relacionam-se diretamente à economia sustentável ao promover: (a) eficiência no uso de recursos, reduzindo custos operacionais; (b) prevenção de desperdícios, alinhando-se à economia circular; (c) gestão informada por dados, aumentando competitividade sustentável; (d) capacitação de profissionais, fortalecendo cultura de responsabilidade socioambiental corporativa.

---

## 🎯 **COERÊNCIA: DIAGNÓSTICO → TEMÁTICAS → INTERVENÇÃO**

### Fluxo Lógico do Projeto:

```
📋 DIAGNÓSTICO PARTICIPATIVO
   ↓
   └─ Questionário com 10 profissionais
   └─ Observação de práticas de impressão
   └─ Análise documental (contadores)
   
🎯 TEMÁTICAS IDENTIFICADAS
   ↓
   └─ Desperdício de recursos (CENTRAL)
   └─ Invisibilidade de impacto
   └─ Gestão sem dados
   └─ Déficit de conscientização
   
💻 INTERVENÇÃO (Dashboard)
   ↓
   └─ Monitora consumo (hp_printer_scanner.py)
   └─ Calcula emissões (metodologia_calculos)
   └─ Gera relatórios (executive_report.py)
   └─ Educa (interface Streamlit)
   
📊 RESULTADOS ESPERADOS
   ↓
   └─ Redução de 20-30% no desperdício
   └─ Conscientização sobre impacto climático
   └─ Decisões baseadas em dados
   └─ Cultura de sustentabilidade
```

---

## 🔗 **CONEXÃO: TEMÁTICAS → ODS → ECONOMIA SUSTENTÁVEL**

**Por que estas temáticas relacionam-se à ECONOMIA sustentável?**

1. **Eficiência Econômica:** Reduzir desperdícios diminui custos operacionais (papel, toner, energia)
2. **Competitividade Responsável:** Organizações sustentáveis têm vantagem competitiva e reputacional
3. **Economia Circular:** Prevenir resíduos é mais econômico que descartar e repor
4. **Produtividade Consciente:** Profissionais conscientes tomam decisões que beneficiam ambiente E economia
5. **Democratização Tecnológica:** Solução gratuita permite que PMEs adotem práticas sustentáveis

**Economia Sustentável ≠ Apenas economia financeira**
É sobre: recursos naturais como capital, eficiência como competitividade, sustentabilidade como estratégia de longo prazo.

---

## 💡 **RELEVÂNCIA LOCAL E VIABILIDADE DE INTERVENÇÃO**

### Por que estas temáticas são RELEVANTES para o setor fiscal?

✅ **Impacto direto:** Setor imprime muitos documentos fiscais diariamente  
✅ **Mensurável:** Dados de impressoras são coletáveis via SNMP  
✅ **Engajamento:** Questionário mostrou interesse dos profissionais  
✅ **Autonomia:** Setor pode implementar mudanças sem depender de outras áreas  

### Por que a intervenção é VIÁVEL?

✅ **Tecnicamente:** Dashboard já desenvolvido e funcional  
✅ **Financeiramente:** Solução gratuita, sem custos adicionais  
✅ **Institucionalmente:** Aprovação para projeto piloto já obtida  
✅ **Temporalmente:** Implementação e testes dentro do prazo do curso  

---

## 📖 **CONCLUSÃO**

A delimitação temática focou em problemas concretos, mensuráveis e passíveis de intervenção técnica identificados no diagnóstico participativo. Ao concentrar esforços em desperdício de recursos, invisibilidade de impacto, gestão sem dados e déficit de conscientização, garantimos coerência entre diagnóstico realizado, dashboard desenvolvido e objetivos de desenvolvimento sustentável. Esta delimitação precisa permite foco nas próximas etapas e engajamento efetivo dos profissionais do setor fiscal como parceiros na transformação de práticas corporativas.

---

**Data:** ___/___/_____  
**Responsável:** _______________________  
**Setor Parceiro:** Setor Fiscal

