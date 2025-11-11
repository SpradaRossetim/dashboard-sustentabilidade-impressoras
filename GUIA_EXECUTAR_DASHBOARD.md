# GUIA PARA EXECUTAR O DASHBOARD E COLETAR DADOS REAIS

**Projeto:** Dashboard de Sustentabilidade  
**Data:** ___/___/_____

---

## 🚀 PASSO 1: PREPARAÇÃO DO AMBIENTE

### **1.1 Verificar Requisitos**

- [ ] Python instalado (versão 3.8 ou superior)
- [ ] Ambiente virtual ativado (`printer_config_env`)
- [ ] Dependências instaladas (`requirements_streamlit.txt`)
- [ ] Impressora HP conectada na rede
- [ ] IP da impressora conhecido

### **1.2 Ativar Ambiente Virtual**

**Windows:**
```bash
cd "c:\Users\AlexDionesSprada&Ros\OneDrive - SPRADA\Documentos\VS CODE\TRAB Faculdade"
printer_config_env\Scripts\activate
```

**Ou usar o script automático:**
```bash
ativar_ambiente.bat
```

---

## 🎯 PASSO 2: INICIAR O DASHBOARD

### **Opção 1: Script Automático (Recomendado)**

```bash
iniciar_dashboard.bat
```

### **Opção 2: Comando Manual**

```bash
streamlit run streamlit_dashboard.py
```

---

## 🌐 PASSO 3: ACESSAR O DASHBOARD

1. Abra o navegador
2. Acesse: **http://localhost:8501**
3. O dashboard deve abrir automaticamente

---

## 📊 PASSO 4: COLETAR DADOS DO DASHBOARD

### **4.1 Dashboard Principal**

**Métricas para Registrar:**

1. **Páginas Impressas:** _____ páginas
2. **Pegada de Carbono Total:** _____ kg CO₂
3. **Economia Potencial:** R$ _____
4. **Score de Sustentabilidade:** _____/100
5. **Equivalentes Ambientais:**
   - km de carro: _____ km
   - Árvores: _____ árvores
   - Lâmpadas: _____ horas
   - Banhos: _____ minutos

### **4.2 Análise Detalhada**

**Componentes da Pegada de Carbono:**

1. **Papel:** _____ kg CO₂ (_____%)
2. **Toner:** _____ kg CO₂ (_____%)
3. **Energia:** _____ kg CO₂ (_____%) - **CONFIRMAR:** Fator ONS Brasil 0.0817 kg CO₂/kWh
4. **Fabricação:** _____ kg CO₂ (_____%)
5. **Transporte:** _____ kg CO₂ (_____%)
6. **Descarte:** _____ kg CO₂ (_____%)

**Métricas de Eficiência:**

- CO₂ por página: _____ kg CO₂/página
- ROI: _____%
- Score de sustentabilidade: _____/100

---

## 📅 PASSO 5: PLANO DE COLETA DE DADOS

### **5.1 Coleta Inicial (Baseline)**

**Data:** ___/___/_____  
**Dados Coletados:**
- Páginas impressas: _____
- Pegada de carbono total: _____ kg CO₂
- Score de sustentabilidade: _____/100

**Screenshot:** [ ] Capturado

---

### **5.2 Coleta Mensal - Mês 1**

**Data:** ___/___/_____  
**Dados Coletados:**
- Páginas impressas: _____
- Pegada de carbono total: _____ kg CO₂
- Redução em relação ao baseline: _____%

**Screenshot:** [ ] Capturado

---

### **5.3 Coleta Mensal - Mês 2**

**Data:** ___/___/_____  
**Dados Coletados:**
- Páginas impressas: _____
- Pegada de carbono total: _____ kg CO₂
- Redução em relação ao baseline: _____%

**Screenshot:** [ ] Capturado

---

### **5.4 Coleta Mensal - Mês 3**

**Data:** ___/___/_____  
**Dados Coletados:**
- Páginas impressas: _____
- Pegada de carbono total: _____ kg CO₂
- Redução em relação ao baseline: _____%

**Screenshot:** [ ] Capturado

---

## 📋 TABELA DE COLETA DE DADOS

| Data | Páginas | CO₂ Total (kg) | Papel (kg) | Toner (kg) | Energia (kg) | Score | Economia (R$) |
|------|---------|----------------|------------|------------|--------------|-------|---------------|
| Baseline | | | | | | | |
| Mês 1 | | | | | | | |
| Mês 2 | | | | | | | |
| Mês 3 | | | | | | | |

---

## 📸 PASSO 6: CAPTURAR SCREENSHOTS

### **Screenshots Obrigatórios**

- [ ] Dashboard Principal - Métricas gerais
- [ ] Análise Detalhada - Componentes da pegada
- [ ] Gráfico de Componentes (Pizza)
- [ ] Plano de Ação - Ações recomendadas
- [ ] Métricas de Sustentabilidade - Score gauge

**Localização:** Criar pasta `screenshots/` no projeto

---

## 🔍 PASSO 7: VERIFICAR FUNCIONALIDADES

### **Checklist de Funcionalidades**

- [ ] Dashboard carrega sem erros
- [ ] Coleta de dados da impressora funciona
- [ ] Cálculos de CO₂ estão corretos
- [ ] Gráficos aparecem corretamente
- [ ] Fator ONS Brasil (0.0817) está sendo usado

---

## 📝 PASSO 8: REGISTRAR DADOS NA DOCUMENTAÇÃO

Usar os dados coletados para preencher:
- `DOCUMENTACAO_INTERVENCAO.md` - Seção 7.3 Resultados Obtidos
- `RELATORIO_INTEGRADOR_RESUMIDO.md` - Seção Resultados Obtidos

---

## 🐛 TROUBLESHOOTING

### **Problema 1: Dashboard não inicia**

```bash
# Verificar ambiente virtual
printer_config_env\Scripts\activate

# Reinstalar dependências
pip install -r requirements_streamlit.txt
```

### **Problema 2: Impressora não conecta**

1. Verificar IP da impressora no código
2. Verificar conectividade de rede
3. Verificar se impressora está ligada

### **Problema 3: Cálculos incorretos**

1. Verificar fatores em `metodologia_calculos_sustentabilidade.py`
2. Confirmar fator ONS Brasil (0.0817 kg CO₂/kWh)

---

## ✅ CHECKLIST FINAL

- [ ] Dashboard funcionando
- [ ] Dados coletados de todas as fontes
- [ ] Screenshots capturados
- [ ] Cálculos verificados
- [ ] Fator ONS Brasil confirmado
- [ ] Dados registrados na tabela
- [ ] Documentação preenchida

---

**Arquivo:** `GUIA_EXECUTAR_DASHBOARD.md`  
**Versão:** 1.0

