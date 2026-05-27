# OCR-IA - OCR com Auxílio de IA (100% local) - Versão para Linux e Windows | Data: 09/03/2026

## 1. Sobre o OCR-IA

O OCR-IA é um programa que permite a realização de OCRs de maior qualidade com o auxílio de IAs locais, visando maior efetividade nos OCRs produzidos e com total privacidade.

## 2. Aviso Legal / Disclaimer

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

## 3. Licença do OCR-IA

Copyright (C) 2026 AUDSIS-ADG-SUBAC-Controladoria Geral do Município | Prefeitura da Cidade do Rio de Janeiro

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## 4. Bibliotecas utilizadas (último acesso aos links das fontes a seguir ocorreu em 08/03/2026)

- tempfile - módulo da biblioteca padrão do Python que permite criar arquivos e diretórios temporários de forma segura e automática. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/tempfile.html e https://docs.python.org/3/license.html.
- shutil - módulo da biblioteca padrão do Python que oferece operações de alto nível em arquivos e coleções de arquivos (cópia, movimentação, remoção, arquivamento etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/shutil.html e https://docs.python.org/3/license.html.
- base64 - módulo da biblioteca padrão do Python que fornece funcionalidades para codificação e decodificação em base64. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/base64.html e https://docs.python.org/3/license.html.
- platform - módulo da biblioteca padrão do Python que fornece informações sobre a plataforma em execução (SO, hardware etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/platform.html e https://docs.python.org/3/license.html.
- time - módulo da biblioteca padrão do Python que fornece funções relacionadas a tempo (sleep, timestamps etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/time.html e https://docs.python.org/3/license.html.
- queue - módulo da biblioteca padrão do Python que implementa filas thread-safe (FIFO, LIFO, PriorityQueue etc.), muito usado em programação concorrente. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/queue.html e https://docs.python.org/3/license.html.
- sys - módulo da biblioteca padrão do Python que fornece acesso a parâmetros e funções específicas do interpretador e do sistema (como argumentos de linha de comando, versão do Python, caminhos de busca etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/sys.html e https://docs.python.org/3/license.html.
- os - módulo da biblioteca padrão do Python que oferece uma interface portátil para funcionalidades dependentes do sistema operacional (manipulação de arquivos/diretórios, variáveis de ambiente, processos etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/os.html e https://docs.python.org/3/license.html.
- io - módulo da biblioteca padrão do Python que fornece as principais ferramentas para trabalhar com streams de I/O (entrada/saída), incluindo fluxos de texto, binários, buffered e in-memory (como StringIO e BytesIO). Ele define a implementação moderna do open() e as classes base da hierarquia de I/O. Está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/io.html e https://docs.python.org/3/license.html.
- pathlib - módulo da biblioteca padrão do Python (introduzido no 3.4) que oferece uma representação orientada a objetos de caminhos de arquivo/sistema. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/pathlib.html e https://docs.python.org/3/license.html.
- threading - módulo da biblioteca padrão do Python que fornece suporte a programação concorrente baseada em threads. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/threading.html e https://docs.python.org/3/license.html.
- typing - módulo da biblioteca padrão do Python que contém construções para tipagem estática (type hints). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/typing.html e https://docs.python.org/3/license.html.
- tkinter - biblioteca de interface gráfica do usuário (GUI) Python de código aberto, incluída na biblioteca padrão. Ela está licenciada sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/tkinter.html e https://docs.python.org/3/license.html.
- subprocess - módulo que permite gerenciar subprocessos, conectar-se aos seus pipes de entrada/saída/erro e obter seus códigos de retorno. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/subprocess.html e https://docs.python.org/3/license.html.
- fitz - também conhecido como PyMuPDF — biblioteca de terceiros de alto desempenho para extração, análise, conversão e manipulação de documentos PDF (e outros formatos). Está licenciada sob AGPL-3.0 (ou licença comercial alternativa via Artifex). Veja em: https://pymupdf.readthedocs.io/en/latest/ e https://github.com/pymupdf/PyMuPDF/blob/main/COPYING
- PIL - Python Imaging Library - Pillow, o fork mantido da biblioteca original PIL — é uma poderosa biblioteca para abertura, manipulação, processamento e salvamento de imagens em diversos formatos. O submódulo Image contém a classe principal de imagem; ImageEnhance oferece classes para ajustes de cor, contraste, brilho e nitidez. Está licenciada sob a HPND (Historical Permission Notice and Disclaimer) / MIT-CMU style license. Veja em: https://pillow.readthedocs.io/en/stable/ e https://github.com/python-pillow/Pillow/blob/main/LICENSE
- markdown - (Python-Markdown) biblioteca que implementa o conversor de texto Markdown para HTML. Ela está licenciada sob a BSD 3-Clause License. Veja em: https://github.com/Python-Markdown/markdown e https://pypi.org/project/Markdown/.
- requests - biblioteca HTTP de alto nível para Python, conhecida como "HTTP for Humans". Ela está licenciada sob a Apache License 2.0. Veja em: https://requests.readthedocs.io/ e https://github.com/psf/requests.
- openai - biblioteca oficial da OpenAI para interagir com a API da OpenAI. Ela está licenciada sob a Apache License 2.0. Veja em: https://github.com/openai/openai-python e https://pypi.org/project/openai/.

## 5. Backend de IA

### 5.1. KoboldCpp
Software de geração de texto de IA fácil de usar para modelos GGML e GGUF, inspirado no KoboldAI original. É uma ferramenta standalone de um único arquivo executável que integra llama.cpp e adiciona interface KoboldAI Lite, suporte a API compatível, geração de imagens (Stable Diffusion), reconhecimento de voz/imagem e mais. KoboldCpp (código principal e KoboldAI Lite) está licenciado sob a GNU Affero General Public License v3.0 (AGPL-3.0). Componentes base como llama.cpp e GGML usam MIT License. Veja em: https://github.com/LostRuins/koboldcpp e https://github.com/LostRuins/koboldcpp/blob/concedo/LICENSE.md.

### 5.2. Modelos

#### - Qwen3-VL
- Série de modelos multimodais de linguagem grande (vision-language models) desenvolvida pela equipe Qwen da Alibaba Cloud. Suporta compreensão e raciocínio avançado em texto, imagens e vídeos, com variantes dense e MoE, modos Instruct e Thinking, e melhorias em percepção visual, contexto longo e capacidades de agente. Está licenciada sob a Apache License 2.0. - Veja em: https://github.com/QwenLM/Qwen3-VL e https://huggingface.co/Qwen (coleção Qwen3-VL).

#### - Modificações e quantização
- Versão abliterated (uncensored, com remoção de alinhamentos de recusa via abliteration): huihui-ai → https://huggingface.co/huihui-ai/models.
- Quantizações GGUF (incluindo Q5_K_M e outras, com imatrix otimizado do unsloth): noctrex → https://huggingface.co/collections/noctrex/qwen3-vl-abliterated.

## 6. Empacotador
- Pyinstaller - ferramenta que permite empacotar uma aplicação python e todas as suas dependências em um único pacote. Ele está licenciado sob uma licença dual, usando tanto a licença GPL 2.0, com uma exceção que permite usá-lo para construir produtos comerciais e a licença Apache, versão 2.0 que se aplica apenas a alguns poucos arquivos. Veja em: <https://pyinstaller.org/en/stable/license.html>.