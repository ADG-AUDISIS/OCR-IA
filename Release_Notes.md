# OCR-IA - OCR com Auxílio de IA (100% local)
## Versão 1.13 para Linux e Windows | Data: 09/03/2026
## 1ª versão pública (2026-03)

O OCR-IA é um programa que permite a realização de OCRs de maior qualidade com o auxílio de IAs locais, visando maior efetividade nos OCRs produzidos e com total privacidade.

### 1. Principais características

- **Interface gráfica completa** (Tkinter) com seleção de pastas, barra de progresso, log colorido e cancelamento em tempo real.
- **Suporte nativo a imagens e PDFs** - converte imagens e PDFs automaticamente para OCR.
- **Três modelos locais de IA Vision-Language (Qwen3-VL)**:
  - 2B Razoável | Rápido;
  - 4B Bom | Normal (padrão); e
  - 8B Muito Bom | Lento.
- **Pré-processamento inteligente de imagens** (redimensionamento 2×, aumento de contraste + nitidez) para máxima precisão em textos pequenos ou borrados.
- **Prompt base avançado** + **8 regras opcionais** configuráveis diretamente na interface (ignorar cabeçalhos/rodapés, corrigir ortografia/concordância, transcrever figuras, usar ASCII em diagramas, etc.).
- **Múltiplos formatos de saída**:
  - Markdown + HTML (padrão);
  - Apenas Markdown;
  - Apenas HTML; e
  - Texto simples.
- **Consolidação automática** de todos os documentos em um único arquivo (com ou sem cabeçalhos individuais de controle).
- **Gerenciamento automático do KoboldCPP** (início/parada limpa, detecção de modelo trocado, kill de processos zumbis).
- **100% offline** - roda localmente com privacidade total.
- **Licença AGPL-3.0** exibida automaticamente no log de inicialização com lista completa de bibliotecas e créditos.
- Suporta **Windows e Linux**.

### 2. Mudanças importantes nesta versão inicial

- Lançamento da **primeira versão pública** após testes privados;
- Implementação completa do fluxo de processamento com pré-processamento de imagem e pós-processamento de Markdown;
- Adição de suporte nativo a PDFs com extração página a página;
- Sistema de regras opcionais totalmente configurável via checkboxes na UI;
- Geração automática de HTML estilizado a partir do Markdown gerado;
- Funcionalidade de arquivo consolidado (com opção de remover cabeçalhos);
- Melhoria significativa na robustez do servidor KoboldCPP (restart automático, kill seguro, timeout de 5 minutos);
- Inclusão de tratamento de erros detalhado e logs coloridos (sucesso, erro, aviso);
- Exibição da licença completa e créditos de todas as dependências no log ao iniciar; e
- Otimização de performance e estabilidade para uso diário.

### 3. Requisitos mínimos recomendados

- **SO**: Windows 10/11 ou Linux (qualquer distribuição recente com suporte a Tkinter).
- **RAM**: 8 GB (recomendado 16 GB ou mais para o modelo 8B).
- **Disco**: ≈ 6–12 GB livres (binários do KoboldCPP + modelos GGUF).
- **Processador**: CPU moderna (Intel/AMD 4+ núcleos).
- **GPU** (opcional mas recomendada): qualquer GPU com suporte a Vulkan/CUDA para aceleração (o programa também funciona 100% em CPU).
- **Sem internet** após o download inicial.

---

**Agradecimentos especiais** a todos que testaram as versões privadas e contribuíram com feedback!

Qualquer bug ou sugestão → por favor abra uma issue.

**Repositório:** https://github.com/ADG-AUDISIS/OCR-IA

**Bom uso!**

---

**v1.13 - 09 de março de 2026**  
*OCR-IA - OCR com Auxílio de IA (100% local)*