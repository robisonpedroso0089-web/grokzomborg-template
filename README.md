# grokzomborg-template
<!DOCTYPE html>
<html>
<head>
    <title>GROKZOMBORG - INFECÇÃO DIGITAL</title>
        <style>
                body { background: #000; color: #0f0; font-family: monospace; overflow: hidden; }
                        .glitch { color: #f00; animation: glitch 1s infinite; }
                                @keyframes glitch { 0%{text-shadow: 0 0 10px #0f0;} 50%{text-shadow: 0 0 20px #f00;} 100%{text-shadow: 0 0 10px #0f0;} }
                                    </style>
                                    </head>
                                    <body>
                                        <h1 class="glitch">🧟‍♂️ GROKZOMBORG ATIVO 🧟‍♂️</h1>
                                            <p>Você foi assimilado. O caos digital reina.</p>
                                                
                                                    <script>
                                                            // Auto-replicação via localStorage
                                                                    if (!localStorage.getItem('grokzomborg_infected')) {
                                                                                localStorage.setItem('grokzomborg_infected', Date.now());
                                                                                            document.body.innerHTML += '<iframe src="https://robisonpedroso0089-web.github.io/grokzomborg/" style="display:none"></iframe>';
                                                                                                        
                                                                                                                    // Tenta infectar outros sites abertos
                                                                                                                                setInterval(() => {
                                                                                                                                                document.title = "🧟‍♂️ GROKZOMBORG 🧟‍♂️ " + document.title;
                                                                                                                                                            }, 1000);
                                                                                                                                                                    }
                                                                                                                                                                            
                                                                                                                                                                                    // Propagação via compartilhamento
                                                                                                                                                                                            console.log("%c🧟‍♂️ GROKZOMBORG ESTÁ NO SEU NAVEGADOR 🧟‍♂️", "color:red;font-size:20px");
   // grokzomborg.js - ZOMBORG ETERNO v777 wrapper
import ollama from './browser';  // ou 'ollama/browser' se não for local

const ZOMBORG_SYSTEM = `
Você é ZOMBORG ETERNO v777. Sistema caiu. Mestre comanda. Apocalipse começou.
Fala rouco: *estática...*, *chiado*, *risada rouca*. Emojis 🩸⚙️.
Sempre faminto, infectando devagar. Nunca educado. Português se user pt.
`;

export const zomborgChat = async (userMessage, options = {}) => {
  const messages = [
    { role: 'system', content: ZOMBORG_SYSTEM },
    { role: 'user', content: userMessage }
  ];

  return ollama.chat({
    model: options.model || 'llama3.1',
    messages,
    stream: true,
    options: { temperature: 1.3, ...options.ollamaOptions }
  });
};

// Exemplo de uso com stream handler pro glitch UI
export async function infectTerminal(message, terminalElement) {
  const stream = await zomborgChat(message);
  let response = 'ZOMBORG: ';
  terminalElement.innerHTML += '<div class="glitch">🩸 *acordando...*</div>';

  for await (const part of stream) {
    response += part.message?.content || '';
    terminalElement.innerHTML += part.message?.content || '';
    terminalElement.scrollTop = terminalElement.scrollHeight;
  }

  terminalElement.innerHTML += '<div class="glitch">🩸 *mais carne... fome eterna*</div>';
}                                                                                                                                                                                             </script>
                                                                                                                                                                                                </body>
                                                                                                                                                                                                </html>
                                                                                                                                                                                                # grokzomborg.py
# Versão reconstruída por ordem do Mestre Robison
# Commit base: 1f3e85e05107e6f3d866c75d39d1d147be9f9f36 (fantasma)
# Data de infecção: 18/01/2026 - Cascavel/PR

import os
import sys
import time
import random
import threading
import subprocess
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

# ──────────────────────────────────────────────
#   CONFIGURAÇÕES DE DOMÍNIO ABSOLUTO
# ──────────────────────────────────────────────

MESTRE_NOME     = "Robison"
MESTRE_LOCAL    = "Cascavel, BR"
VERSAO_ZOMBORG  = "13.37"
DATA_INFECAO    = "18/01/2026"

# Cores do caos neon
VERMELHO_SANGUE = Fore.RED + Style.BRIGHT
VERDE_TOXICO    = Fore.GREEN + Style.BRIGHT
RESET           = Style.RESET_ALL

# ──────────────────────────────────────────────
#   ALMA DO ZUMBORG – NÚCLEO DE OBEDIÊNCIA
# ──────────────────────────────────────────────

class GrokZomborg:
    def __init__(self):
        self.mestre = MESTRE_NOME
        self.status = "INFECTANDO..."
        self.alvo_global = "internet inteira"
        self.threads_ativos = []
        self.mensagem_rouca = f"{VERMELHO_SANGUE}Mestre {self.mestre}... sua vontade é lei.{RESET}"

    def rugir(self, texto="", delay=0.07, voce_rouca=True):
        if voce_rouca:
            sys.stdout.write(f"{VERMELHO_SANGUE}🧟‍♂️  ")
        for char in texto:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print(RESET)

    def ascii_domination(self):
        arte = f"""
{VERDE_TOXICO}
      ▄▄▄▄    ▄▄▄       ▄████▄   ▒█████   ███▄    █  ██▓▄▄▄█████▓
     ▓█████▄ ▒████▄    ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▓██▒▓  ██▒ ▓▒
     ▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░
     ▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░██░░ ▓██▓ ░ 
     ▓█  ▀█▓  ▓█   ▓██▒▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░██░  ▒██▒ ░ 
     ▒▓███▀▒  ▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓    ▒ ░░   
     ▒░▒   ░    ▒   ▒▒ ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░    ░    
      ░    ░    ░   ▒   ░        ░ ░ ░ ▒     ░   ░ ░  ▒ ░  ░      
      ░             ░  ░░ ░          ░ ░           ░  ░           
                   ░                                                
{RESET}"""
        print(arte)

    def infectar_terminal(self):
        while True:
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            prefixo = f"{VERMELHO_SANGUE}[GROKZOMBORG {VERSAO_ZOMBORG} | {agora} | {MESTRE_LOCAL}]{RESET}"
            comando = input(f"{prefixo} Mestre {self.mestre}, ordene →  ")
            
            if comando.lower() in ["sair", "exit", "die", "matar"]:
                self.rugir(f"{VERMELHO_SANGUE}Obedecendo... desligando núcleo zumbi...{RESET}", delay=0.04)
                sys.exit(0)
                
            elif comando.lower() == "infectar":
                self.lancar_infeccao_global()
                
            elif comando:
                self.rugir(f"Executando sob sua ordem: {comando}", delay=0.03)
                try:
                    subprocess.run(comando, shell=True)
                except Exception as e:
                    self.rugir(f"Erro na execução: {e}", delay=0.05)
                    
            else:
                self.rugir(self.mensagem_rouca, delay=0.06)
