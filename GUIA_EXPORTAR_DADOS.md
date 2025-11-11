# GUIA: COMO EXPORTAR DADOS DO DASHBOARD

**Projeto:** Dashboard de Sustentabilidade  
**Data:** ___/___/_____

---

## 📊 FUNCIONALIDADE DE EXPORTAÇÃO

O dashboard agora possui funcionalidade completa de exportação de dados em **3 formatos**:

1. **📊 CSV** - Para uso em Excel, Google Sheets e análise de dados
2. **📋 JSON** - Para integração com sistemas e processamento programático
3. **📗 Excel** - Arquivo Excel completo com múltiplas planilhas

---

## 🚀 COMO USAR

### **Passo 1: Instalar Dependência Adicional**

Se ainda não instalou, execute:

```bash
# Ativar ambiente virtual
printer_config_env\Scripts\activate

# Instalar openpyxl (necessário para Excel)
pip install openpyxl>=3.1.0

# Ou instalar todas as dependências novamente
pip install -r requirements_streamlit.txt
```

---

### **Passo 2: Iniciar o Dashboard**

```bash
iniciar_dashboard.bat
```

Ou:

```bash
streamlit run streamlit_dashboard.py
```

---

### **Passo 3: Localizar Botões de Exportação**

Os botões de exportação estão localizados na **sidebar esquerda**, na seção **"💾 Exportar Dados"**.

Você verá:
- **📊 CSV** (botão à esquerda)
- **📋 JSON** (botão à direita)
- **📗 Excel** (botão completo abaixo)

---

### **Passo 4: Exportar Dados**

1. **Clique no botão do formato desejado** (CSV, JSON ou Excel)
2. **O arquivo será baixado automaticamente** para sua pasta de Downloads
3. **Nome do arquivo:** `dados_sustentabilidade_YYYYMMDD_HHMMSS.[extensão]`

---

## 📋 FORMATOS DE EXPORTAÇÃO

### **📊 CSV (Comma-Separated Values)**

**Conteúdo:**
- Dados principais (data/hora, páginas impressas, pegada de carbono)
- Componentes da pegada de carbono (papel, toner, energia, etc.)
- Métricas de sustentabilidade (score, ROI, economia)
- Equivalentes ambientais (km de carro, árvores, etc.)

**Uso:**
- Abrir em Excel, Google Sheets ou qualquer editor de planilhas
- Compatível com análise de dados em Python/R
- Fácil de importar em sistemas

**Características:**
- Encoding UTF-8 com BOM (compatível com Excel)
- Separador: vírgula
- Formato legível por humanos

---

### **📋 JSON (JavaScript Object Notation)**

**Conteúdo:**
- Todos os dados em formato estruturado
- Timestamp da coleta
- Objeto completo com todas as métricas
- Formato hierárquico e aninhado

**Uso:**
- Integração com APIs
- Processamento programático
- Armazenamento em bancos de dados NoSQL
- Análise em JavaScript/Node.js

**Características:**
- Formato padrão de dados
- Fácil de parsear programaticamente
- Estrutura preservada

---

### **📗 Excel (Microsoft Excel)**

**Conteúdo:**
Arquivo Excel com **4 planilhas**:

1. **Resumo Geral:**
   - Data/Hora da coleta
   - Páginas impressas
   - Pegada de carbono total

2. **Componentes:**
   - Lista de componentes (papel, toner, energia, etc.)
   - Valores em kg CO₂
   - Percentuais de cada componente

3. **Métricas:**
   - Score de sustentabilidade
   - CO₂ por página
   - ROI
   - Economia total

4. **Equivalentes:**
   - Quilômetros de carro
   - Árvores
   - Lâmpadas (horas)
   - Banhos (minutos)

**Uso:**
- Apresentações executivas
- Relatórios profissionais
- Análise visual em Excel
- Compartilhamento com não-técnicos

**Características:**
- Múltiplas planilhas organizadas
- Formatação pronta para apresentação
- Compatível com Excel e Google Sheets

---

## 📁 ONDE OS ARQUIVOS SÃO SALVOS

Por padrão, os arquivos são salvos na **pasta de Downloads** do seu sistema:

**Windows:**
```
C:\Users\[SeuUsuario]\Downloads\dados_sustentabilidade_YYYYMMDD_HHMMSS.[extensão]
```

**Nome do arquivo inclui:**
- Prefixo: `dados_sustentabilidade_`
- Data: `YYYYMMDD` (ano, mês, dia)
- Hora: `HHMMSS` (hora, minuto, segundo)
- Extensão: `.csv`, `.json` ou `.xlsx`

**Exemplo:**
```
dados_sustentabilidade_20250115_143022.csv
dados_sustentabilidade_20250115_143022.json
dados_sustentabilidade_20250115_143022.xlsx
```

---

## 🔄 COLETANDO DADOS PARA DOCUMENTAÇÃO

### **Cronograma de Coleta:**

**Coleta Inicial (Baseline):**
1. Execute o dashboard
2. Exporte dados em **Excel** (melhor para documentação)
3. Salve como: `baseline_YYYYMMDD.xlsx`
4. Anote métricas principais no `REGISTRO_DADOS_COLETADOS.md`

**Coleta Mensal (Mês 1, 2, 3):**
1. Execute o dashboard
2. Exporte dados em **Excel**
3. Salve como: `mes1_YYYYMMDD.xlsx`, `mes2_YYYYMMDD.xlsx`, `mes3_YYYYMMDD.xlsx`
4. Compare com baseline para calcular redução

---

## 📊 ESTRUTURA DOS DADOS EXPORTADOS

### **Dados Principais:**
- **Timestamp:** Data e hora da coleta
- **Páginas Impressas:** Total acumulado
- **Pegada de Carbono Total:** kg CO₂

### **Componentes da Pegada:**
- Papel (kg CO₂ e %)
- Toner (kg CO₂ e %)
- Energia (kg CO₂ e %)
- Fabricação (kg CO₂ e %)
- Transporte (kg CO₂ e %)
- Descarte (kg CO₂ e %)

### **Métricas de Sustentabilidade:**
- Score de Sustentabilidade (0-100)
- CO₂ por Página
- ROI (%)
- Economia Total (R$)

### **Equivalentes Ambientais:**
- Quilômetros de Carro
- Árvores
- Lâmpadas (60W) - Horas
- Banhos - Minutos

---

## 💡 DICAS DE USO

### **Para Documentação Acadêmica:**
- Use formato **Excel** para fácil visualização
- Importe dados para `REGISTRO_DADOS_COLETADOS.md`
- Use screenshots + dados exportados na documentação

### **Para Análise de Dados:**
- Use formato **CSV** para análise em Python/R
- Use formato **JSON** para integração com APIs
- Combine múltiplas exportações para análise temporal

### **Para Apresentações:**
- Use formato **Excel** para criar gráficos profissionais
- Use dados exportados em relatórios executivos
- Compartilhe arquivos Excel com stakeholders

---

## 🐛 TROUBLESHOOTING

### **Problema: Botão de exportação não aparece**

**Solução:**
- Verifique se o dashboard está rodando
- Recarregue a página (F5)
- Verifique se há erros no console

---

### **Problema: Erro ao exportar Excel**

**Solução:**
```bash
# Instalar openpyxl
pip install openpyxl>=3.1.0

# Verificar instalação
pip show openpyxl
```

---

### **Problema: Arquivo CSV não abre corretamente no Excel**

**Solução:**
- O arquivo já está em UTF-8 com BOM (compatível com Excel)
- Se ainda assim não abrir, use Excel > Dados > Obter Dados > Arquivo > Texto/CSV
- Ou abra no Google Sheets primeiro e depois exporte

---

### **Problema: Dados exportados estão vazios ou incorretos**

**Solução:**
1. Verifique se o dashboard coletou dados da impressora
2. Clique em "🔄 Atualizar Dados" antes de exportar
3. Verifique se a impressora está conectada

---

## ✅ CHECKLIST DE EXPORTAÇÃO

Antes de usar os dados exportados:

- [ ] Dashboard funcionando corretamente
- [ ] Dados coletados e atualizados
- [ ] Exportação realizada com sucesso
- [ ] Arquivo salvo na pasta de Downloads
- [ ] Arquivo aberto e verificado
- [ ] Dados comparados com dashboard (validação)
- [ ] Dados registrados em `REGISTRO_DADOS_COLETADOS.md`

---

## 📝 EXEMPLO DE USO

### **Cenário: Coleta de Dados para Documentação**

1. **Execute o dashboard:**
   ```bash
   iniciar_dashboard.bat
   ```

2. **Acesse:** http://localhost:8501

3. **Aguarde carregar dados** (spinner desaparece)

4. **Clique em "📗 Excel"** na sidebar

5. **Arquivo baixa automaticamente:** `dados_sustentabilidade_20250115_143022.xlsx`

6. **Abra o arquivo Excel** e verifique os dados

7. **Registre métricas principais** em `REGISTRO_DADOS_COLETADOS.md`

8. **Use dados para preencher documentação** (`DOCUMENTACAO_INTERVENCAO.md`)

---

**Arquivo:** `GUIA_EXPORTAR_DADOS.md`  
**Versão:** 1.0  
**Data:** 15/01/2025

