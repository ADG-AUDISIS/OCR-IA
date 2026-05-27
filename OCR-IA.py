# OCR-IA - O OCR-IA é um programa que permite a realização de OCRs de maior qualidade com o auxílio de IAs locais, visando maior efetividade nos OCRs produzidos e com total privacidade.
Author = "Copyright (C) 2026 AUDSIS-ADG-SUBAC-Controladoria Geral do Município | Prefeitura da Cidade do Rio de Janeiro"

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

version = "1.13"

# Aviso Legal / Disclaimer

# - O programa é licenciado sob a GNU Affero General Public License versão 3 ou posterior (GNU AGPL v3+) e fornecido “como está”, sem qualquer garantia de qualidade, funcionalidade, disponibilidade, segurança ou compatibilidade;
# - O uso do programa é por conta e risco do usuário, que assume toda a responsabilidade pelos resultados e consequências do uso do software, isentando o desenvolvedor e outros contribuidores de qualquer responsabilidade legal ou moral;
# - O usuário deve respeitar os direitos e deveres que a licença GNU AGPL v3+ lhe confere, bem como os direitos autorais e a privacidade de terceiros;
# - O usuário deve zelar pela segurança das informações geradas pelo programa que pode violar direitos autorais, perder dados, gerar resultados imprecisos ou ainda invadir a privacidade de terceiros;
# - O usuário não deve utilizar o programa para fins ilícitos ou prejudiciais;
# - O usuário do programa está sujeito às leis e normas internacionais que versam sobre a proteção aos dados pessoais e, se for brasileiro ou estiver em território brasileiro, está sujeito à legislação brasileira, especialmente à Lei Geral de Proteção de Dados Pessoais (LGPD), Lei nº 13.709, de 14 de agosto de 2018, que dispõe sobre o tratamento de dados pessoais, inclusive nos meios digitais, por pessoa natural ou por pessoa jurídica de direito público ou privado, com o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural;
# - Ao utilizar o OCR-IA, o usuário concorda em respeitar os princípios, os direitos e as obrigações previstos nas leis e normas internacionais que versam sobre a proteção aos dados pessoais e na LGPD, bem como as normas e as orientações da Autoridade Nacional de Proteção de Dados (ANPD), órgão responsável no Brasil por fiscalizar e aplicar sanções pelo descumprimento da lei;
# - O usuário do OCR-IA deve estar ciente das disposições das leis e normas que versam sobre a proteção aos dados pessoais no seu país e, no caso do Brasil, ciente da LGPD e das responsabilidades que ela impõe aos agentes de tratamento de dados pessoais, como o controlador, o operador e o encarregado. O usuário do programa deve obter o consentimento livre, informado e inequívoco do titular dos dados pessoais, sempre que necessário, para realizar o tratamento dos dados, respeitando a finalidade, a adequação, a necessidade, a transparência e a segurança dos dados;
# - O usuário brasileiro do OCR-IA deve comunicar à ANPD e ao titular dos dados pessoais qualquer incidente de segurança que possa acarretar risco ou dano relevante aos titulares, bem como adotar medidas para mitigar os efeitos do incidente;
# - O usuário de fora do território brasileiro, e que não mantenha relações com o Brasil, deve comunicar ao órgão governamental do seu país, responsável em receber informações sobre incidentes com dados pessoais, e ao titular dos dados pessoais, qualquer incidente de segurança que possa acarretar risco ou dano relevante aos titulares, bem como adotar medidas para mitigar os efeitos do incidente; e
# - Por fim, o usuário do programa deve estar atento às sanções administrativas previstas nas leis e normas do seu país e, em se tratando do Brasil, deve estar atento às sanções administrativas previstas na LGPD, que podem variar desde advertências até multas de até 2% do faturamento anual da organização* no Brasil, limitado a R$ 50 milhões por infração.

# Nota: Entende-se por organização qualquer pessoa jurídica de direito público ou privado que realize o tratamento de dados pessoais no Brasil, independentemente do país onde esteja localizada a sede ou o estabelecimento responsável pelo tratamento.

# Bibliotecas utilizadas (último acesso aos links das fontes a seguir ocorreu em 09/03/2026):

import tempfile                     # módulo da biblioteca padrão do Python que permite criar arquivos e diretórios temporários de forma segura e automática. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/tempfile.html e https://docs.python.org/3/license.html.
import shutil                       # módulo da biblioteca padrão do Python que oferece operações de alto nível em arquivos e coleções de arquivos (cópia, movimentação, remoção, arquivamento etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/shutil.html e https://docs.python.org/3/license.html.
import base64                       # módulo da biblioteca padrão do Python que fornece funcionalidades para codificação e decodificação em base64. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/base64.html e https://docs.python.org/3/license.html.
import platform                     # módulo da biblioteca padrão do Python que fornece informações sobre a plataforma em execução (SO, hardware etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/platform.html e https://docs.python.org/3/license.html.
import time                         # módulo da biblioteca padrão do Python que fornece funções relacionadas a tempo (sleep, timestamps etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/time.html e https://docs.python.org/3/license.html.
import queue                        # módulo da biblioteca padrão do Python que implementa filas thread-safe (FIFO, LIFO, PriorityQueue etc.), muito usado em programação concorrente. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/queue.html e https://docs.python.org/3/license.html.
import sys                          # módulo da biblioteca padrão do Python que fornece acesso a parâmetros e funções específicas do interpretador e do sistema (como argumentos de linha de comando, versão do Python, caminhos de busca etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/sys.html e https://docs.python.org/3/license.html.
import os                           # módulo da biblioteca padrão do Python que oferece uma interface portátil para funcionalidades dependentes do sistema operacional (manipulação de arquivos/diretórios, variáveis de ambiente, processos etc.). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/os.html e https://docs.python.org/3/license.html.
import io                           # módulo da biblioteca padrão do Python que fornece as principais ferramentas para trabalhar com streams de I/O (entrada/saída), incluindo fluxos de texto, binários, buffered e in-memory (como StringIO e BytesIO). Ele define a implementação moderna do open() e as classes base da hierarquia de I/O. Está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/io.html e https://docs.python.org/3/license.html.
from pathlib import Path	        # módulo da biblioteca padrão do Python (introduzido no 3.4) que oferece uma representação orientada a objetos de caminhos de arquivo/sistema. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/pathlib.html e https://docs.python.org/3/license.html.
from threading import Event, Thread # módulo da biblioteca padrão do Python que fornece suporte a programação concorrente baseada em threads. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/threading.html e https://docs.python.org/3/license.html.
from typing import Optional         # módulo da biblioteca padrão do Python que contém construções para tipagem estática (type hints). Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/typing.html e https://docs.python.org/3/license.html.
import tkinter as tk                # biblioteca de interface gráfica do usuário (GUI) Python de código aberto, incluída na biblioteca padrão. Ela está licenciada sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/tkinter.html e https://docs.python.org/3/license.html.
from tkinter import filedialog, messagebox, scrolledtext, ttk  # submódulos da biblioteca tkinter para diálogos de arquivo, caixas de mensagem, áreas de texto roláveis e widgets temáticos. Eles estão licenciados sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/tkinter.html e https://docs.python.org/3/license.html.
from tkinter.constants import *     # constantes usadas pela biblioteca tkinter (ex: TOP, LEFT, END etc.). Elas estão licenciadas sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/tkinter.html e https://docs.python.org/3/license.html.
import subprocess                   # módulo que permite gerenciar subprocessos, conectar-se aos seus pipes de entrada/saída/erro e obter seus códigos de retorno. Ele está licenciado sob a Python Software Foundation License. Veja em: https://docs.python.org/3/library/subprocess.html e https://docs.python.org/3/license.html.
import fitz                         # também conhecido como PyMuPDF — biblioteca de terceiros de alto desempenho para extração, análise, conversão e manipulação de documentos PDF (e outros formatos). Está licenciada sob AGPL-3.0 (ou licença comercial alternativa via Artifex). Veja em: https://pymupdf.readthedocs.io/en/latest/ e https://github.com/pymupdf/PyMuPDF/blob/main/COPYING
from PIL import Image, ImageEnhance # (Python Imaging Library) - Pillow, o fork mantido da biblioteca original PIL — é uma poderosa biblioteca para abertura, manipulação, processamento e salvamento de imagens em diversos formatos. O submódulo Image contém a classe principal de imagem; ImageEnhance oferece classes para ajustes de cor, contraste, brilho e nitidez. Está licenciada sob a HPND (Historical Permission Notice and Disclaimer) / MIT-CMU style license. Veja em: https://pillow.readthedocs.io/en/stable/ e https://github.com/python-pillow/Pillow/blob/main/LICENSE
import markdown                     # (Python-Markdown) biblioteca que implementa o conversor de texto Markdown para HTML. Ela está licenciada sob a BSD 3-Clause License. Veja em: https://github.com/Python-Markdown/markdown e https://pypi.org/project/Markdown/.
import requests                     # biblioteca HTTP de alto nível para Python, conhecida como "HTTP for Humans". Ela está licenciada sob a Apache License 2.0. Veja em: https://requests.readthedocs.io/ e https://github.com/psf/requests.
from openai import OpenAI           # biblioteca oficial da OpenAI para interagir com a API da OpenAI. Ela está licenciada sob a Apache License 2.0. Veja em: https://github.com/openai/openai-python e https://pypi.org/project/openai/.

# Backend de IA:

# KoboldCpp - Software de geração de texto de IA fácil de usar para modelos GGML e GGUF, inspirado no KoboldAI original. É uma ferramenta standalone de um único arquivo executável que integra llama.cpp e adiciona interface KoboldAI Lite, suporte a API compatível, geração de imagens (Stable Diffusion), reconhecimento de voz/imagem e mais. KoboldCpp (código principal e KoboldAI Lite) está licenciado sob a GNU Affero General Public License v3.0 (AGPL-3.0). 
# Componentes base como llama.cpp e GGML usam MIT License. Veja em: https://github.com/LostRuins/koboldcpp e https://github.com/LostRuins/koboldcpp/blob/concedo/LICENSE.md.

# Modelos:

# - Qwen3-VL
#   - Série de modelos multimodais de linguagem grande (vision-language models) desenvolvida pela equipe Qwen da Alibaba Cloud. Suporta compreensão e raciocínio avançado em texto, imagens e vídeos, com variantes dense e MoE, modos Instruct e Thinking, e melhorias em percepção visual, contexto longo e capacidades de agente. Está licenciada sob a Apache License 2.0. - Veja em: https://github.com/QwenLM/Qwen3-VL e https://huggingface.co/Qwen (coleção Qwen3-VL).

# - Modificações e quantização:
#	- Versão abliterated (uncensored, com remoção de alinhamentos de recusa via abliteration): huihui-ai → https://huggingface.co/huihui-ai/models.
#	- Quantizações GGUF (incluindo Q5_K_M e outras, com imatrix otimizado do unsloth): noctrex → https://huggingface.co/collections/noctrex/qwen3-vl-abliterated.

# Empacotador:
# - Pyinstaller - ferramenta que permite empacotar uma aplicação python e todas as suas dependências em um único pacote. Ele está licenciado sob uma licença dual, usando tanto a licença GPL 2.0, com uma exceção que permite usá-lo para construir produtos comerciais e a licença Apache, versão 2.0 que se aplica apenas a alguns poucos arquivos. Veja em: <https://pyinstaller.org/en/stable/license.html>.

KOBOLD_URL = "http://127.0.0.1:5001/v1"

PROMPT_BASE = """Converta esta imagem de documento exatamente para formato Markdown limpo e bem estruturado.

Regras obrigatórias:
- Preserve a estrutura visual o máximo possível: títulos, subtítulos, parágrafos, listas numeradas/com bullets, tabelas.
- Transcreva TODO o texto visível de forma literal e exata, sem resumir, interpretar ou adicionar conteúdo.
- Não converter texto com valores monetários para formato customizado.
- Não inclua explicações, introduções ou comentários.
- Saída deve ser sem texto extra antes ou depois.
- Sempre usar Markdown para representação de todo e qualquer tipo de tabela e planilha.
- Foque em texto pequeno ou borrado: amplie mentalmente e transcreva com precisão máxima.
- Evite repetições: não repita palavras ou frases desnecessariamente.
- Não use placeholders como ![imagem] ou referências; transcreva o conteúdo real de figuras e diagramas.
- Se houver texto ilegível, marque como [ILEGÍVEL], mas tente ao máximo.
"""

OPTIONAL_RULES = [
    "- Desconsiderar cabeçalhos e rodapés de páginas",
    "- Manter quebras de linha e espaçamentos onde fizer sentido.",
    "- Corrigir separações silábicas, exceto a de final de página",
    "- Corrigir erros ortográficos, quando aplicável.",
    "- Corrigir erros de concordância, quando aplicável.",
    "- Transcrever textos de figuras e imagens.",
    "- Nunca utilizar Mermaid. Usar ASCII puro para diagramas e fluxogramas.",
    "- Nunca utilizar LaTex. Usar ASCII puro para equações e fórmulas (Exemplo: x = (-b ± √(b² - 4ac)) / (2a)).",
    "- Transcreva caligrafia com contexto semântico",
    "- Usar blocos de código em conteúdos de codificação.",
]

IMG_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}

LOCAL_MODELS = {
    "4B Bom | Normal": {"model": "4B.gguf", "mmproj": "4B-mmproj.gguf"},
    "2B Razoável | Rápido": {"model": "2B.gguf", "mmproj": "2B-mmproj.gguf"},
    "8B Muito Bom | Lento": {"model": "8B.gguf", "mmproj": "8B-mmproj.gguf"},
}

OUTPUT_FORMATS = {
    "Markdown + HTML (.md + .html)": None,
    "Markdown (.md)": ".md",
    "HTML (.html)": ".html",
    "Texto simples (.txt)": ".txt",
}

class OCRApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"OCR-IA - OCR com Auxílio de IA (100% local) - Versão {version} | {Author}")
        self.root.geometry("1620x960")
        self.root.minsize(1300, 760)

        self.input_folder = tk.StringVar(value="Ainda não selecionada")
        self.output_folder = tk.StringVar(value="Ainda não selecionada")

        self.cancel_event = Event()
        self.processing = False
        self.kobold_proc: Optional[subprocess.Popen] = None
        self.client: Optional[OpenAI] = None
        self.current_model_key: Optional[str] = None
        self.ui_queue = queue.Queue()
        self.option_vars = [tk.BooleanVar(value=True) for _ in OPTIONAL_RULES]
        self.output_format_var = tk.StringVar(value="Markdown + HTML (.md + .html)")
        self.consolidate_var = tk.BooleanVar(value=False)
        self.no_header_var = tk.BooleanVar(value=False)
        self.consolidated_content = []

        self._build_ui()
        self.print_license_header()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.after(80, self._process_ui_queue)

    def _process_ui_queue(self):
        """Loop que atualiza a UI de forma 100% segura"""
        try:
            while not self.ui_queue.empty():
                msg_type, data = self.ui_queue.get_nowait()
                if msg_type == "log":
                    if isinstance(data, tuple) and len(data) == 3:
                        msg, end, tag = data
                    else:
                        msg = data if isinstance(data, str) else str(data)
                        end = "\n"
                        tag = None
                    self._unsafe_log(msg, end, tag)
                elif msg_type == "progress":
                    self.progress["value"] = data
                elif msg_type == "status":
                    self.status_var.set(data)
        except Exception:
            pass
        self.root.after(80, self._process_ui_queue)

    def _unsafe_log(self, msg: str, end: str = "\n", tag: Optional[str] = None):
        """Só deve ser chamado da thread principal"""
        self.log_text.configure(state="normal")
        if tag:
            self.log_text.insert(END, str(msg) + end, tag)
        else:
            self.log_text.insert(END, str(msg) + end)
        self.log_text.see(END)
        self.log_text.configure(state="disabled")

    def log(self, msg: str, end: str = "\n", tag: Optional[str] = None):
        """Método thread-safe — use este de qualquer lugar"""
        self.ui_queue.put(("log", (msg, end, tag)))

    def update_progress(self, value: int):
        self.ui_queue.put(("progress", value))

    def update_status(self, text: str):
        self.ui_queue.put(("status", text))

    def show_error(self, message: str, title: str = "Erro"):
        """Mostra messagebox + registra automaticamente em VERMELHO no log"""
        messagebox.showerror(title, message)
        self.log(message, tag="error")

    def show_warning(self, message: str, title: str = "Aviso"):
        """Mostra messagebox + registra em LARANJA no log (para uso futuro)"""
        messagebox.showwarning(title, message)
        self.log(message, tag="warning")

    def on_close(self):
        self._stop_kobold()
        self.root.destroy()

    # ── Gerenciamento do Kobold ─────────────────────────────────────
    def _stop_kobold(self) -> None:
        """Para o koboldcpp de forma confiável (Windows/Linux)"""
        if not self.kobold_proc or self.kobold_proc.poll() is not None:
            return

        self.log("→ Encerrando motor de IA (koboldcpp)...")

        if platform.system() == "Windows":
            try:
                subprocess.run(
                    ["taskkill", "/F", "/T", "/PID", str(self.kobold_proc.pid)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                )
                self.log("→ Motor de IA encerrado via taskkill. ✓", tag="success")
            except Exception:
                self.kobold_proc.kill()
                self.log("→ Motor de IA encerrado via kill. ✓", tag="success")
        else:
            self.kobold_proc.terminate()
            try:
                self.kobold_proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.kobold_proc.kill()
            self.log("→ Motor de IA encerrado. ✓", tag="success")

        self.kobold_proc = None
        self.client = None
        self.current_model_key = None

    def _start_kobold(self, model_key: str) -> bool:
        """Inicia o koboldcpp em segundo plano"""
        bin_dir = Path(__file__).parent / "bin"
        if platform.system() == "Windows":
            exe_name = (
                "koboldcpp-launcher.exe"
                if os.path.exists("koboldcpp-launcher.exe")
                else "koboldcpp.exe"
            )
        else:
            exe_name = (
                "koboldcpp-launcher"
                if os.path.exists("koboldcpp-launcher")
                else "koboldcpp-linux-x64"
            )
        exe_path = bin_dir / exe_name

        if not exe_path.is_file():
           self.show_error(f"→ {exe_name} não encontrado em bin/")
           return False

        cfg = LOCAL_MODELS[model_key]
        model_path = bin_dir / cfg["model"]
        mmproj_path = bin_dir / cfg["mmproj"]

        if not model_path.is_file() or not mmproj_path.is_file():
            self.show_error(f"→ Arquivos do modelo {model_key} não encontrados.")
            return False

        self._kill_previous_kobold()

        cmd = [
            str(exe_path), "--model", str(model_path), "--mmproj", str(mmproj_path),
            "--port", "5001", "--host", "127.0.0.1", "--contextsize", "8192",
            "--gpulayers", "-1", "--highpriority", "--quiet"
        ]

        try:
            self.log(f"→ Iniciando modelo {model_key} (pode levar 20-90 s)...")
            self.update_status("→ Iniciando motor de IA...")

            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
                self.kobold_proc = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    startupinfo=startupinfo
                )
            else:
                self.kobold_proc = subprocess.Popen(
                    cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )

            self.current_model_key = model_key

            if self.kobold_proc.poll() is not None:
                self.log(f"→ ERRO: koboldcpp falhou (código {self.kobold_proc.returncode})", tag="error")
                return False

        except Exception as e:
            self.show_error(f"→ Falha ao iniciar modelo:\n{e}")
            return False

        for attempt in range(300):
            if self.cancel_event.is_set():
                return False
            try:
                r = requests.get(f"{KOBOLD_URL}/models", timeout=3)
                if r.status_code == 200:
                    self.client = OpenAI(base_url=KOBOLD_URL, api_key="sk-no-key-required")
                    self.log(f"→ Modelo {model_key} iniciado com sucesso! ✓", tag="success")
                    self.update_status("→ Modelo pronto! ✓")
                    return True
            except:
                if attempt % 20 == 0:
                    self.log(f"→ Aguardando servidor... ({attempt+1}/300)")
                time.sleep(1.1)

        self._stop_kobold()
        self.show_error("→ Motor de IA não respondeu após 5 minutos.")
        return False

    def _kill_previous_kobold(self):
        """Mata qualquer koboldcpp que possa ter ficado preso"""
        try:
            if platform.system() == "Windows":
                subprocess.run(
                    ["taskkill", "/F", "/IM", "koboldcpp.exe"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                )
            else:
                subprocess.run(
                    ["pkill", "-9", "-f", "koboldcpp"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
        except:
            pass

    def ensure_kobold_ready(self, model_key: str) -> bool:
        """Reinicia automaticamente se o modelo for trocado"""
        if self.current_model_key != model_key:
            self.log(f"→ Carregando modelo → {model_key}")
            self._stop_kobold()
        if self.kobold_proc is None or self.kobold_proc.poll() is not None:
            return self._start_kobold(model_key)
        return True

    # ── Interface ───────────────────────────────────────────────────
    def _build_ui(self):
        pad = 10

        # ── FRAME PRINCIPAL (sem rolagem) ─────────────────────────────
        main = ttk.Frame(self.root, padding=pad)
        main.pack(fill="both", expand=True)

        fm = ttk.LabelFrame(main, text="IA Local", padding=pad)
        fm.pack(fill=X, pady=(0, pad))
        ttk.Label(fm, text="Modelo:").grid(row=0, column=0, sticky=W, padx=(0,8))
        self.model_var = tk.StringVar(value=next(iter(LOCAL_MODELS)))
        ttk.Combobox(fm, textvariable=self.model_var, values=list(LOCAL_MODELS.keys()),
                     state="readonly", width=45).grid(row=0, column=1, sticky=W, padx=5)

        self.status_var = tk.StringVar(value="Pronto para iniciar")
        ttk.Label(fm, textvariable=self.status_var, foreground="#0066cc").grid(row=0, column=2, padx=20, sticky=E)

        for title, var, btn_text in [
            ("Pasta de Origem", self.input_folder, "Selecionar Origem"),
            ("Pasta de Destino", self.output_folder, "Selecionar Destino")
        ]:
            f = ttk.LabelFrame(main, text=title, padding=pad)
            f.pack(fill=X, pady=(0, pad))
            ttk.Entry(f, textvariable=var, state="readonly").pack(side=LEFT, fill=X, expand=True, padx=(0,8))
            ttk.Button(f, text=btn_text, command=lambda v=var, t=title: self._choose_folder(v, t)).pack(side=RIGHT)

        f_out = ttk.LabelFrame(main, text="Formato de Saída", padding=pad)
        f_out.pack(fill=X, pady=(0, pad))
        ttk.Label(f_out, text="Formato:").grid(row=0, column=0, sticky=W, padx=(0,8))
        ttk.Combobox(f_out, textvariable=self.output_format_var, values=list(OUTPUT_FORMATS.keys()),
                     state="readonly", width=32).grid(row=0, column=1, sticky=W)
        ttk.Checkbutton(f_out, text="Gerar também arquivo consolidado", variable=self.consolidate_var).grid(row=1, column=0, columnspan=2, sticky=W, pady=4)
        ttk.Checkbutton(f_out, text="Consolidado sem cabeçalhos individuais", variable=self.no_header_var).grid(row=2, column=0, columnspan=2, sticky=W)

        fo = ttk.LabelFrame(main, text="Regras Opcionais", padding=pad)
        fo.pack(fill=X, pady=(0, pad))

        n_rules = len(OPTIONAL_RULES)
        rules_per_column = (n_rules + 1) // 2

        for i, (rule, var) in enumerate(zip(OPTIONAL_RULES, self.option_vars)):
            column = 0 if i < rules_per_column else 1
            row = i if i < rules_per_column else i - rules_per_column
            
            cb = ttk.Checkbutton(fo, text=rule, variable=var)
            cb.grid(row=row, column=column, sticky="w", padx=12, pady=2)
            
            fo.grid_columnconfigure(0, weight=1)
            fo.grid_columnconfigure(1, weight=1)

        fl = ttk.LabelFrame(main, text="Log / Progresso", padding=pad)
        fl.pack(fill=BOTH, expand=True, pady=(0, pad))
        self.log_text = scrolledtext.ScrolledText(fl, wrap=WORD, height=8, font=("Consolas", 9), state="disabled")
        self.log_text.pack(fill=BOTH, expand=True)

        self.log_text.tag_configure("error",   foreground="#FF3333", font=("Consolas", 9, "bold"))
        self.log_text.tag_configure("warning", foreground="#FFAA00", font=("Consolas", 9, "bold"))
        self.log_text.tag_configure("success", foreground="#00CC66", font=("Consolas", 9, "bold"))

        self.progress = ttk.Progressbar(main, mode="determinate")
        self.progress.pack(fill=X, pady=(4, 10))

        btns = ttk.Frame(main)
        btns.pack(fill=X)
        self.btn_start = ttk.Button(btns, text="▶ Iniciar Processamento", command=self.start)
        self.btn_start.pack(side=LEFT, padx=(0,8))
        self.btn_cancel = ttk.Button(btns, text="Cancelar", command=self.cancel, state=DISABLED)
        self.btn_cancel.pack(side=LEFT)
        ttk.Button(btns, text="Limpar Log", command=self.clear_log).pack(side=RIGHT)

    def _choose_folder(self, var: tk.StringVar, title: str):
        folder = filedialog.askdirectory(title=title)
        if folder:
            var.set(folder)
            self.log(f"→ Pasta selecionada: {folder} ✓", tag="success")

    def clear_log(self):
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", END)
        self.log_text.configure(state="disabled")

    def get_prompt(self) -> str:
        extras = [r for r, v in zip(OPTIONAL_RULES, self.option_vars) if v.get()]
        return PROMPT_BASE + "\n" + "\n".join(extras) + "\n- Não use ``` a menos que o conteúdo seja código.\n"

    # ── Processamento ───────────────────────────────────────────────
    def start(self):
        if self.processing:
            return

        model_key = self.model_var.get()
        indir = self.input_folder.get()
        outdir = self.output_folder.get()

        if not Path(indir).is_dir() or not Path(outdir).is_dir():
            self.show_error("→ Selecione pastas válidas.")
            return

        if not self.ensure_kobold_ready(model_key):
            return

        self.processing = True
        self.cancel_event.clear()
        self.btn_start.config(state=DISABLED)
        self.btn_cancel.config(state=NORMAL)
        self.progress["value"] = 0
        self.consolidated_content.clear()

        Thread(target=self._process_all, args=(Path(indir), Path(outdir), model_key), daemon=True).start()

    def cancel(self):
        self.cancel_event.set()
        self.log("→ Cancelamento solicitado. Por favor aguarde...")

    def _pdf_to_temp_images(self, pdf_path: Path, dpi: int = 150) -> list[Path]:
        temp_dir = Path(tempfile.mkdtemp(prefix="ocr_pdf_"))
        images_paths = []
        try:
            doc = fitz.open(pdf_path)
            total = len(doc)
            for page_num in range(total):
                if self.cancel_event.is_set():
                    break
                page = doc.load_page(page_num)
                mat = fitz.Matrix(dpi / 72, dpi / 72)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                out_path = temp_dir / f"page_{page_num+1:04d}.png"
                pix.save(out_path)
                images_paths.append(out_path)
                self.update_status(f"Convertendo PDF → página {page_num+1}/{total}")
            doc.close()
            return images_paths
        except Exception as e:
            self.log(f"→ Erro PDF {pdf_path.name}: {e}", tag="error")
            shutil.rmtree(temp_dir, ignore_errors=True)
            return []

    def _strip_outer_markdown_fences(self, text: str) -> str:
        t = text.strip()
        lines = t.splitlines()
        if len(lines) >= 2 and lines[0].strip().startswith("```") and lines[-1].strip() == "```":
            return "\n".join(lines[1:-1]).strip()
        return text

    def render_markdown_to_html(self, md_text: str, title: str) -> str:
        body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc", "attr_list"])
        return f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8"><title>{title}</title>
<style>body{{font-family:Arial,sans-serif;margin:40px;line-height:1.6;}}pre{{background:#f6f8fa;padding:15px;overflow-x:auto;}}</style></head><body>{body}</body></html>"""

    def print_license_header(self):
        """Exibe o cabeçalho de licença no log assim que o programa inicia"""
        header = f"""OCR-IA - OCR com Auxílio de IA (100% local) - Versão {version} para Linux e Windows

1. Sobre o OCR-IA

O OCR-IA é um programa que permite a realização de OCRs de maior qualidade com o auxílio de IAs locais, visando maior efetividade nos OCRs produzidos e com total privacidade.

2. Aviso Legal / Disclaimer

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

Nota: Entende-se por organização qualquer pessoa jurídica de direito público ou privado que realize o tratamento de dados pessoais no Brasil, independentemente do país onde esteja localizada a sede ou o estabelecimento responsável pelo tratamento.

3. Licença do OCR-IA

{Author}

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

4. Bibliotecas utilizadas (último acesso aos links das fontes a seguir ocorreu em 08/03/2026)

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

5. Backend de IA

5.1. KoboldCpp
Software de geração de texto de IA fácil de usar para modelos GGML e GGUF, inspirado no KoboldAI original. É uma ferramenta standalone de um único arquivo executável que integra llama.cpp e adiciona interface KoboldAI Lite, suporte a API compatível, geração de imagens (Stable Diffusion), reconhecimento de voz/imagem e mais. KoboldCpp (código principal e KoboldAI Lite) está licenciado sob a GNU Affero General Public License v3.0 (AGPL-3.0). Componentes base como llama.cpp e GGML usam MIT License. Veja em: https://github.com/LostRuins/koboldcpp e https://github.com/LostRuins/koboldcpp/blob/concedo/LICENSE.md.

5.2. Modelos

- Qwen3-VL
    - Série de modelos multimodais de linguagem grande (vision-language models) desenvolvida pela equipe Qwen da Alibaba Cloud. Suporta compreensão e raciocínio avançado em texto, imagens e vídeos, com variantes dense e MoE, modos Instruct e Thinking, e melhorias em percepção visual, contexto longo e capacidades de agente. Está licenciada sob a Apache License 2.0. - Veja em: https://github.com/QwenLM/Qwen3-VL e https://huggingface.co/Qwen (coleção Qwen3-VL).

- Modificações e quantização
    - Versão abliterated (uncensored, com remoção de alinhamentos de recusa via abliteration): huihui-ai → https://huggingface.co/huihui-ai/models.
    - Quantizações GGUF (incluindo Q5_K_M e outras, com imatrix otimizado do unsloth): noctrex → https://huggingface.co/collections/noctrex/qwen3-vl-abliterated.

6. Empacotador
- Pyinstaller - ferramenta que permite empacotar uma aplicação python e todas as suas dependências em um único pacote. Ele está licenciado sob uma licença dual, usando tanto a licença GPL 2.0, com uma exceção que permite usá-lo para construir produtos comerciais e a licença Apache, versão 2.0 que se aplica apenas a alguns poucos arquivos. Veja em: <https://pyinstaller.org/en/stable/license.html>.
"""
        self.log_text.configure(state="normal")
        # Insere no início (posição 1.0)
        self.log_text.insert("1.0", header + "\n" + "═" * 80 + "\n\n")
        # Configura a tag (pode fazer uma única vez)
        if "license" not in self.log_text.tag_names():
            self.log_text.tag_config("license", 
                                   foreground="#383838", 
                                   font=("Consolas", 9))
        self.log_text.tag_add("license", "1.0", "end")
        self.log_text.see("1.0")
        self.log_text.configure(state="disabled")

    def _process_all(self, input_dir: Path, output_dir: Path, model_key: str):
        try:
            all_files = sorted(p for p in input_dir.iterdir()
                               if p.is_file() and (p.suffix.lower() in IMG_EXTENSIONS or p.suffix.lower() == ".pdf"))
            if not all_files:
                self.log("→ Nenhum arquivo válido encontrado.", tag="warning")
                return

            to_process = []
            for file_path in all_files:
                if file_path.suffix.lower() == ".pdf":
                    temp_images = self._pdf_to_temp_images(file_path, dpi=150)
                    for img_p in temp_images:
                        to_process.append((file_path, img_p))
                else:
                    to_process.append((file_path, file_path))

            total = len(to_process)
            self.progress["maximum"] = total
            self.log(f"→ Processando {total} páginas/imagens com modelo {model_key}...")

            prompt = self.get_prompt()
            fmt_choice = self.output_format_var.get()
            save_html = fmt_choice in ("HTML (.html)", "Markdown + HTML (.md + .html)")
            save_md   = fmt_choice in ("Markdown (.md)", "Markdown + HTML (.md + .html)")
            save_txt  = fmt_choice == "Texto simples (.txt)"

            processed_count = 0
            temp_dirs = set()

            for i, (orig_path, img_path) in enumerate(to_process, 1):
                if self.cancel_event.is_set():
                    self.log("→ Cancelamento realizado.")
                    break

                display_name = f"{orig_path.name} (pág. {img_path.stem[-4:]})" if orig_path.suffix.lower() == ".pdf" else orig_path.name
                self.update_status(f"Processando: {display_name}")
                self.log(f"→ [{i:3d}/{total}] {display_name} ", end="")

                try:
                    img = Image.open(img_path).convert("RGB")
                    new_size = (img.width * 2, img.height * 2)
                    img = img.resize(new_size, resample=Image.Resampling.LANCZOS)
                    enhancer = ImageEnhance.Contrast(img)
                    img = enhancer.enhance(1.5)
                    enhancer = ImageEnhance.Sharpness(img)
                    img = enhancer.enhance(1.3)
                    buffered = io.BytesIO()
                    img.save(buffered, format="PNG")
                    b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                    response = self.client.chat.completions.create(
                        model="local-model",
                        messages=[{
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt},
                                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}}
                            ]
                        }],
                        temperature=0.0,
                        max_tokens=4096,
                    )

                    text = self._strip_outer_markdown_fences(response.choices[0].message.content.strip())

                    stem = f"{orig_path.stem}_p{img_path.stem[-4:]}" if orig_path.suffix.lower() == ".pdf" else orig_path.stem

                    if save_md: (output_dir / f"{stem}.md").write_text(text, encoding="utf-8")
                    if save_txt:
                        plain = "\n".join(line.strip() for line in text.splitlines() if line.strip())
                        (output_dir / f"{stem}.txt").write_text(plain, encoding="utf-8")
                    if save_html:
                        html = self.render_markdown_to_html(text, stem)
                        (output_dir / f"{stem}.html").write_text(html, encoding="utf-8")

                    if self.consolidate_var.get():
                        header = "" if self.no_header_var.get() else f"# {stem}\n**Original:** {orig_path.name} | {time.strftime('%Y-%m-%d %H:%M')}\n\n---\n\n"
                        self.consolidated_content.append(header + text + "\n\n---\n\n")

                    self.log("→ OK!", tag="success")
                    processed_count += 1

                except Exception as e:
                    self.log(f"ERRO ao processar/improvar imagem {display_name}: {e}", tag="error")
                    continue

                self.update_progress(i)
                time.sleep(0.45)

                if img_path != orig_path:
                    temp_dirs.add(img_path.parent)

            for d in temp_dirs:
                shutil.rmtree(d, ignore_errors=True)

            if self.consolidate_var.get() and self.consolidated_content:
                suffix = "_PARCIAL" if self.cancel_event.is_set() else ""
                ts = time.strftime("%Y%m%d_%H%M")
                content = "".join(self.consolidated_content)
                if save_md:
                    (output_dir / f"CONSOLIDADO_{ts}{suffix}.md").write_text(content, encoding="utf-8")
                if save_html:
                    html = self.render_markdown_to_html(content, f"Consolidado {ts}")
                    (output_dir / f"CONSOLIDADO_{ts}{suffix}.html").write_text(html, encoding="utf-8")
                self.log(f"→ Consolidado gerado ({len(self.consolidated_content)} itens) ✓", tag="success")

            if not self.cancel_event.is_set():
                self.log("→ Processamento finalizado! ✅", tag="success")
            else:
                self.log("→ Processamento cancelado. ✅")

        except Exception as e:
            self.log(f"→ Erro crítico: {e}", tag="error")
        finally:
            self.processing = False
            self.btn_start.config(state=NORMAL)
            self.btn_cancel.config(state=DISABLED)
            self.update_status("Pronto")
            self.consolidated_content.clear()

if __name__ == "__main__":
    root = tk.Tk()
    root.title(f"OCR-IA - OCR com Auxílio de IA (100% local) - Versão {version} | {Author}")

    app = OCRApp(root)

    icon_path = Path(__file__).parent / "icon.png"

    if not icon_path.is_file():
        app.log("Aviso: arquivo icon.png não encontrado na pasta do programa", tag="warning")
        app.log(f"→ Caminho esperado: {icon_path}", tag="warning")
    else:
        try:
            icon_img = tk.PhotoImage(file=icon_path)
            
            default = True
            if sys.platform.startswith("linux"):
                default = False

            root.iconphoto(default, icon_img)
            
        except Exception as e:
            app.log(f"Erro ao carregar ícone {icon_path.name}: {e}", tag="error")
            app.log("→ A janela usará o ícone padrão do Python/Tk", tag="warning")

    root.geometry("1024x768")
    root.mainloop()
