# Scanner de Configuração de Impressora

Este projeto permite acessar e extrair configurações de impressoras através do IP 192.168.200.15 usando Python e UV.

## 🚀 Como usar

### 1. Ativar o ambiente virtual

**Windows:**
```bash
# Opção 1: Usar o script de ativação
ativar_ambiente.bat

# Opção 2: Ativação manual
printer_config_env\Scripts\activate
```

### 2. Executar os scripts

**Scan básico:**
```bash
python printer_config.py
```

**Scan avançado (recomendado):**
```bash
python printer_advanced.py
```

**Scan específico para HP:**
```bash
python hp_printer_scanner.py
```

**Gerar relatório completo:**
```bash
python relatorio_impressora.py
```

## 📋 O que os scripts fazem

### `printer_config.py` - Scan Básico
- Testa conexão com a impressora
- Explora endpoints comuns
- Extrai informações básicas
- Salva resultados em `printer_config_results.json`

### `printer_advanced.py` - Scan Avançado
- Detecta automaticamente a marca da impressora
- Testa endpoints específicos por marca (HP, Canon, Epson, Brother, etc.)
- Extrai informações detalhadas:
  - Configurações de rede (IP, Gateway, DNS, MAC)
  - Informações do dispositivo (Modelo, Serial)
  - Status dos suprimentos (Nível de tinta/toner)
- Salva resultados em `printer_advanced_results.json`

### `hp_printer_scanner.py` - Scan Específico para HP
- Otimizado para impressoras HP LaserJet
- Testa endpoints específicos da HP
- Extrai informações detalhadas de rede e dispositivo
- Salva resultados em `hp_printer_results.json`

### `relatorio_impressora.py` - Gerador de Relatório
- Consolida todas as informações coletadas
- Gera relatório completo em texto
- Inclui instruções de acesso e configuração
- Salva relatório em `relatorio_impressora.txt`

## 🔍 Informações extraídas

### Rede
- Endereço IP
- Gateway padrão
- DNS
- Endereço MAC
- Configurações Wi-Fi

### Dispositivo
- Modelo da impressora
- Número de série
- Versão do firmware
- Status do dispositivo

### Suprimentos
- Nível de tinta/toner
- Status dos cartuchos
- Informações de manutenção

## 📁 Arquivos gerados

- `printer_config_results.json` - Resultados do scan básico
- `printer_advanced_results.json` - Resultados do scan avançado
- `hp_printer_results.json` - Resultados do scan específico para HP
- `relatorio_impressora.txt` - Relatório completo em texto

## 🛠️ Dependências

- Python 3.10+
- UV (gerenciador de pacotes)
- requests
- beautifulsoup4
- lxml

## 🔧 Solução de problemas

### Erro de conexão
- Verifique se o IP 192.168.200.15 está correto
- Confirme se a impressora está ligada
- Verifique se está na mesma rede

### Autenticação necessária
- Algumas impressoras requerem login
- Tente acessar via navegador primeiro
- Verifique se há credenciais padrão

### Timeout
- A impressora pode estar ocupada
- Tente novamente em alguns minutos
- Verifique a conectividade de rede

## 📞 Suporte

Para dúvidas ou problemas, verifique:
1. Se o ambiente virtual está ativado
2. Se todas as dependências estão instaladas
3. Se a impressora está acessível na rede
