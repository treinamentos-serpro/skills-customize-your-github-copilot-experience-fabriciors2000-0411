# 📘 Tarefa: Jogo da Forca em Python

## 🎯 Objetivo

Construa o clássico jogo da Forca em Python, praticando manipulação de strings, loops, condicionais e seleção aleatória. Ao final, você terá um jogo completo onde os jogadores adivinham letras para revelar uma palavra oculta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Configuração do Jogo

#### Descrição
Prepare o estado inicial do jogo: selecione uma palavra secreta aleatoriamente e inicialize as variáveis que controlarão o progresso do jogador.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra secreta da lista predefinida usando o módulo `random`
- Inicializar uma estrutura para armazenar as letras já adivinhadas
- Definir o número máximo de tentativas incorretas permitidas

### 🛠️ Loop Principal do Jogo

#### Descrição
Implemente o loop principal que exibe o progresso da palavra, recebe os palpites do jogador e atualiza o estado do jogo a cada rodada.

#### Requisitos
O programa concluído deve:

- Exibir o progresso atual da palavra, mostrando as letras adivinhadas e ocultando as demais (formato `_ _ _`)
- Aceitar palpites de letras do usuário usando `input()`
- Verificar se a letra está na palavra secreta e atualizar o estado do jogo
- Rastrear e exibir o número de tentativas incorretas restantes

### 🛠️ Fim de Jogo

#### Descrição
Defina as condições de encerramento do jogo e exiba o resultado final para o jogador.

#### Requisitos
O programa concluído deve:

- Encerrar quando a palavra for completamente adivinhada ou quando as tentativas esgotarem
- Exibir uma mensagem de vitória quando o jogador adivinhar a palavra
- Exibir uma mensagem de derrota, revelando a palavra secreta, quando as tentativas acabarem
