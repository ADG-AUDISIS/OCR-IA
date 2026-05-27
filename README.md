## **✅ Guia completo passo a passo para instalar e usar o OCR-IA (100% local)**

- O OCR-IA é um programa que permite a realização de OCRs de maior qualidade com o auxílio de IAs locais, visando maior efetividade nos OCRs produzidos e com total privacidade.

- O OCR-IA usa **KoboldCpp + Qwen3-VL abliterated** (modelos vision) para converter imagens/PDFs em Markdown, HTML e/ou TXT.

**Aviso Legal / Disclaimer**

- O programa é licenciado sob a GNU Affero General Public License versão 3 ou posterior (GNU AGPL v3+) e fornecido “como está”, sem qualquer garantia de qualidade, funcionalidade, disponibilidade, segurança ou compatibilidade;
- O uso do programa é por conta e risco do usuário, que assume toda a responsabilidade pelos resultados e consequências do uso do software, isentando o desenvolvedor e outros contribuidores de qualquer responsabilidade legal ou moral;
- O usuário deve respeitar os direitos e deveres que a licença GNU AGPL v3+ lhe confere, bem como os direitos autorais e a privacidade de terceiros;
- O usuário deve zelar pela segurança das informações geradas pelo programa que pode violar direitos autorais, perder dados, gerar resultados imprecisos ou ainda invadir a privacidade de terceiros;
- O usuário não deve utilizar o programa para fins ilícitos ou prejudiciais;
- O usuário do programa está sujeito às leis e normas internacionais que versam sobre a proteção aos dados pessoais e, se for brasileiro ou estiver em território brasileiro, está sujeito à legislação brasileira, especialmente à Lei Geral de Proteção de Dados Pessoais (LGPD), Lei nº 13.709, de 14 de agosto de 2018, que dispõe sobre o tratamento de dados pessoais, inclusive nos meios digitais, por pessoa natural ou por pessoa jurídica de direito público ou privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural;
- Ao utilizar o OCR-IA, o usuário concorda em respeitar os princípios, os direitos e as obrigações previstos nas leis e normas internacionais que versam sobre a proteção aos dados pessoais e na LGPD, bem como as normas e as orientações da Autoridade Nacional de Proteção de Dados (ANPD), órgão responsável no Brasil por fiscalizar e aplicar sanções pelo descumprimento da lei;
- O usuário do OCR-IA deve estar ciente das disposições das leis e normas que versam sobre a proteção aos dados pessoais no seu país e, no caso do Brasil, ciente da LGPD e das responsabilidades que ela impõe aos agentes de tratamento de dados pessoais, como o controlador, o operador e o encarregado. O usuário do programa deve obter o consentimento livre, informado e inequívoco do titular dos dados pessoais, sempre que necessário, para realizar o tratamento dos dados, respeitando a finalidade, a adequação, a necessidade, a transparência e a segurança dos dados;
- O usuário brasileiro do OCR-IA deve comunicar à ANPD e ao titular dos dados pessoais qualquer incidente de segurança que possa acarretar risco ou dano relevante aos titulares, bem como adotar medidas para mitigar os efeitos do incidente;
- O usuário de fora do território brasileiro, e que não mantenha relações com o Brasil, deve comunicar ao órgão governamental do seu país, responsável em receber informações sobre incidentes com dados pessoais, e ao titular dos dados pessoais, qualquer incidente de segurança que possa acarretar risco ou dano relevante aos titulares, bem como adotar medidas para mitigar os efeitos do incidente; e
- Por fim, o usuário do programa deve estar atento às sanções administrativas previstas nas leis e normas do seu país e, em se tratando do Brasil, deve estar atento às sanções administrativas previstas na LGPD, que podem variar desde advertências até multas de até 2% do faturamento anual da organização* no Brasil, limitado a R$ 50 milhões por infração.

**Nota:** Entende-se por organização qualquer pessoa jurídica de direito público ou privado que realize o tratamento de dados pessoais no Brasil, independentemente do país onde esteja localizada a sede ou o estabelecimento responsável pelo tratamento.

---

### **Método Recomendado: Executável Pré-Compilado (mais fácil)**

Não é necessário instalar Python nem rodar `pip`. Basta baixar o pacote binário correspondente ao seu sistema.

#### Passo 1: Baixar o executável pronto
Baixe diretamente do repositório o arquivo da última versão:

- **Windows (10/11 de 64 bits)**: `OCR-IA-vx.xx-bin-Windows-x64.zip`
- **Linux (Ubuntu/Mint/Debian de 64 bits)**: `OCR-IA-vx.xx-bin-Ubuntu-x64.tar.xz`

#### Passo 2: Extrair e criar a estrutura de pastas
1. Extraia o arquivo baixado para uma pasta chamada **`OCR-IA`** (pode ser qualquer nome, mas recomendo esse).
2. Dentro da pasta `OCR-IA` você já terá:
   - `OCR-IA.exe` (Windows) ou `OCR-IA` (Linux)
   - Pasta `_internal`
3. Crie uma subpasta chamada **`bin`** (minúsculo) **dentro da pasta '_internal'**.

**Estrutura final deve ficar assim:**
```
OCR-IA/
├── OCR-IA.exe                  ← (Windows) ou OCR-IA (Linux)
└── _internal/
	 ├── bin/
	 │   ├── koboldcpp.exe           ← (ou koboldcpp-linux-x64)
	 │   ├── 2B.gguf
	 │   ├── 2B-mmproj.gguf
	 │   ├── 4B.gguf
	 │   ├── 4B-mmproj.gguf
	 │   ├── 8B.gguf
	 │   └── 8B-mmproj.gguf
	 └── app_icon.png
```

---

### Passo 3: Baixar e colocar o **KoboldCpp** na pasta `bin`
1. Acesse: https://github.com/LostRuins/koboldcpp/releases/latest
2. Baixe:
   - **Windows**: `koboldcpp.exe`
   - **Linux**: `koboldcpp-linux-x64`
3. Coloque o arquivo **direto dentro da pasta `bin`**.

---

### Passo 4: Baixar e renomear os **modelos Qwen3-VL** (obrigatório!)
Vá na coleção oficial do noctrex (quantizações otimizadas com imatrix):

**Repositórios exatos (use o Instruct, não o Thinking):**

#### Modelo 2B → Razoável | Rápido
- Link: https://huggingface.co/noctrex/Huihui-Qwen3-VL-2B-Instruct-abliterated-GGUF
- Baixe:
  - `Huihui-Qwen3-VL-2B-Instruct-abliterated-Q5_K_M.gguf` → renomeie para **`2B.gguf`**
  - `mmproj-F16.gguf` → renomeie para **`2B-mmproj.gguf`**

#### Modelo 4B → Bom | Normal (recomendado para a maioria)
- Link: https://huggingface.co/noctrex/Huihui-Qwen3-VL-4B-Instruct-abliterated-GGUF
- Baixe:
  - `Huihui-Qwen3-VL-4B-Instruct-abliterated-Q5_K_M.gguf` → renomeie para **`4B.gguf`**
  - `mmproj-F16.gguf` → renomeie para **`4B-mmproj.gguf`**

#### Modelo 8B → Muito Bom | Lento
- Link: https://huggingface.co/noctrex/Huihui-Qwen3-VL-8B-Instruct-abliterated-GGUF
- Baixe:
  - `Huihui-Qwen3-VL-8B-Instruct-abliterated-Q5_K_M.gguf` → renomeie para **`8B.gguf`**
  - `mmproj-F16.gguf` → renomeie para **`8B-mmproj.gguf`**

**Dica**: Q5_K_M é o melhor equilíbrio qualidade × velocidade para OCR.

---

### Passo 5: Como rodar o programa
- **Windows**: dê duplo clique em `OCR-IA.exe`
- **Linux**: 
  ```bash
  chmod +x OCR-IA
  ./OCR-IA
  ```

A janela GUI vai abrir automaticamente.  
Escolha pasta de origem, destino, modelo (2B/4B/8B), formato de saída e regras opcionais.  
Clique em **▶ Iniciar Processamento**.

O KoboldCpp inicia automaticamente em segundo plano (pode demorar 20–90 segundos na primeira vez).

---

### **Método Alternativo: Instalar via Código Python (OCR-IA.py)**

Caso prefira rodar diretamente do fonte (ex.: para desenvolvimento ou outras versões do Python):

1. Tenha **Python 3.13** instalado.
2. Rode:
   ```bash
   pip install pymupdf pillow markdown requests openai
   ```
3. Coloque o arquivo `OCR-IA.py` na raiz da pasta `OCR-IA`.
4. Siga os mesmos Passos 3 e 4 acima (KoboldCpp + modelos na pasta `bin` que, nesse caso, ficará na **raiz da pasta OCR-IA**).
5. Rode: `python OCR-IA.py`

---

### Dicas extras
- **Primeira execução**: pode demorar um pouco (o KoboldCpp carrega o modelo na memória).
- **Cancelar**: use o botão "Cancelar" - ele para tudo com segurança após terminar a tarefa atual.
- **Consolidado**: marque a opção para gerar um único arquivo com todos os documentos.
- **Atualização**: sempre baixe a versão mais recente do `koboldcpp` (o programa é compatível).

---

**Pronto!**  
Com o executável pré-compilado você tem um OCR 100% offline, rápido de instalar e que funciona perfeitamente sem depender de Python.

Encontrou algum bug? Tem sugestão ou melhoria?  
→ Por favor abra uma issue ou mande sua ideia!
