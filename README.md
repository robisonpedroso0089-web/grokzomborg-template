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
