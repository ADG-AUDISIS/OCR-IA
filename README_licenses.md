# FIEL CONVERSOR - Pequeno e simples, mas poderoso! - Versão para Linux e Windows | Data: 27/04/2026

## 1. Sobre o FIEL CONVERSOR

O Fiel Conversor é um programa que permite converter imagens em PDF, PDF em imagens, extrair páginas selecionadas de um PDF, agrupar arquivos em PDF em um só, girar páginas, e converter imagens de texto para PDF com OCR, através do Tesseract suportando diversas línguas.

## 2. Aviso Legal / Disclaimer

- O programa é licenciado sob a GNU Affero General Public License versão 3 ou posterior (GNU AGPL v3+) e fornecido “como está”, sem qualquer garantia de qualidade, funcionalidade, disponibilidade, segurança ou compatibilidade.
- O uso do programa é por conta e risco do usuário, que assume toda a responsabilidade pelos resultados e consequências do uso do software, isentando o desenvolvedor e outros contribuidores de qualquer responsabilidade legal ou moral.
- O usuário deve respeitar os direitos e deveres que a licença GNU AGPL v3+ lhe confere, bem como os direitos autorais e a privacidade de terceiros.
- O usuário deve zelar pela segurança das informações geradas pelo programa, especialmente aquelas produzidas pela ferramenta de OCR, que pode violar direitos autorais, perder dados, gerar resultados imprecisos ou ainda invadir a privacidade de terceiros. O usuário não deve utilizar o programa para fins ilícitos ou prejudiciais.
- O usuário do programa Fiel Conversor está sujeito às leis e normas internacionais que versam sobre a proteção aos dados pessoais e, se for brasileiro ou estiver em território brasileiro, está sujeito à legislação brasileira, especialmente à Lei Geral de Proteção de Dados Pessoais (LGPD), Lei nº 13.709, de 14 de agosto de 2018, que dispõe sobre o tratamento de dados pessoais, inclusive nos meios digitais, por pessoa natural ou por pessoa jurídica de direito público ou privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural.
- Ao utilizar o Fiel Conversor, o usuário concorda em respeitar os princípios, os direitos e as obrigações previstos nas leis e normas internacionais que versam sobre a proteção aos dados pessoais e na LGPD, bem como as normas e as orientações da Autoridade Nacional de Proteção de Dados (ANPD), órgão responsável no Brasil por fiscalizar e aplicar sanções pelo descumprimento da lei.
- O usuário do Fiel Conversor deve estar ciente das disposições das leis e normas que versam sobre a proteção aos dados pessoais no seu país e, no caso do Brasil, ciente da LGPD e das responsabilidades que ela impõe aos agentes de tratamento de dados pessoais, como o controlador, o operador e o encarregado. O usuário do programa deve obter o consentimento livre, informado e inequívoco do titular dos dados pessoais, sempre que necessário, para realizar o tratamento dos dados, respeitando a finalidade, a adequação, a necessidade, a transparência e a segurança dos dados.
- O usuário brasileiro do Fiel Conversor deve comunicar à ANPD e ao titular dos dados pessoais qualquer incidente de segurança que possa acarretar risco ou dano relevante aos titulares, bem como adotar medidas para mitigar os efeitos do incidente.
- O usuário do Fiel Conversor de fora do território brasileiro, e que não mantenha relações com o Brasil, deve comunicar ao órgão governamental do seu país, responsável em receber informações sobre incidentes com dados pessoais, e ao titular dos dados pessoais, qualquer incidente de segurança que possa acarretar risco ou dano relevante aos titulares, bem como adotar medidas para mitigar os efeitos do incidente.
- Por fim, o usuário do programa deve estar atento às sanções administrativas previstas nas leis e normas do seu país e, em se tratando do Brasil, deve estar atento às sanções administrativas previstas na LGPD, que podem variar desde advertências até multas de até 2% do faturamento anual da organização* no Brasil, limitado a R$ 50 milhões por infração.

**Nota:** Entende-se por organização qualquer pessoa jurídica de direito público ou privado que realize o tratamento de dados pessoais no Brasil, independentemente do país onde esteja localizada a sede ou o estabelecimento responsável pelo tratamento.

## 3. Licença do FIEL CONVERSOR

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

## 4. Bibliotecas utilizadas (último acesso aos links das fontes a seguir ocorreu em 27/04/2026)

- os: módulo que fornece uma maneira portátil de usar funcionalidades dependentes do sistema operacional. Ele está licenciado sob a Python Software Foundation License. Veja em: <https://docs.python.org/3/license.html> e <https://www.python.org/psf-landing>.

- sys: módulo que fornece acesso a algumas variáveis e funções que interagem com o interpretador python e o ambiente de execução. Ele está licenciado sob a Python Software Foundation License. Veja em: <https://docs.python.org/3/license.html> e <https://www.python.org/psf-landing>.

- subprocess: módulo que permite gerenciar subprocessos, conectar-se aos seus pipes de entrada/saída/erro e obter seus códigos de retorno. Ele está licenciado sob a Python Software Foundation License. Veja em: <https://docs.python.org/3/license.html> e <https://www.python.org/psf-landing>.

- tkinter: biblioteca de interface gráfica do usuário (GUI) Python de código aberto. Ele está licenciado sob a Python Software Foundation License. Veja em: <https://docs.python.org/3/license.html> e <https://www.python.org/psf-landing>.

- PyPDF2 (Versão 3.0.1): biblioteca de manipulação de arquivos PDF para Python. Ela está licenciada sob a PyPDF2 License. Veja em: <https://pypi.org/project/PyPDF2>.

- fitz e PyMuPDF (Versão 1.23.6): duas bibliotecas que são interfaces Python para a biblioteca MuPDF, uma biblioteca de renderização e manipulação de arquivos PDF, XPS e EPUB. Elas estão licenciadas sob a GNU Affero General Public License v3.0. Veja em: <https://pypi.org/project/PyMuPDF> e <https://github.com/pymupdf/PyMuPDF>.

- Pillow (Versão 10.1.0): é um amigável fork do PIL. Veja em: <https://github.com/python-pillow/Pillow>. PIL é a Biblioteca de Imagens do Python por Fredrik Lundh e colaboradores. PIL: Python Imaging Library, uma biblioteca de processamento de imagens para Python. Ela está licenciada sob a PIL Software License. Veja em: <https://openhub.net/licenses/pilsl> e <https://pillow.readthedocs.io/en/stable/about.html>.

## 5. TESSERACT

- Tesseract: motor de reconhecimento óptico de caracteres (OCR) de código aberto. Ele está licenciado sob a Apache License 2.0. Veja na subpasta doc da pasta Tesseract e/ou em: <https://tesseract-ocr.github.io> e <https://github.com/tesseract-ocr/tesseract>. 

## 6. Empacotador
- Pyinstaller - ferramenta que permite empacotar uma aplicação python e todas as suas dependências em um único pacote. Ele está licenciado sob uma licença dual, usando tanto a licença GPL 2.0, com uma exceção que permite usá-lo para construir produtos comerciais e a licença Apache, versão 2.0 que se aplica apenas a alguns poucos arquivos. Veja em: <https://pyinstaller.org/en/stable/license.html>.