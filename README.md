# 🃏 Blackjack Q-Learning Agent: Reinforcement Learning Mastery

<div align="center">
  
![image](https://github.com/user-attachments/assets/7d1987c1-08c3-4fff-9d30-31027b78ef69)
</div>

## 🌟 Projeto

Uma implementação avançada de aprendizado por reforço utilizando o algoritmo Q-Learning para resolver o ambiente de Blackjack do Gymnasium, demonstrando técnicas sofisticadas de aprendizado de máquina e estratégias de decisão adaptativas.

## 📊 Visão Geral Técnica

### Algoritmo
- **Técnica**: Q-Learning (Aprendizado por Diferença Temporal)
- **Ambiente**: OpenAI Gymnasium Blackjack-v1
- **Objetivo**: Desenvolver uma estratégia ótima para jogar Blackjack

### 🧠 Características Principais
- Exploração adaptativa via política épsilon-gulosa
- Atualização dinâmica da tabela Q
- Decaimento exponencial da taxa de exploração
- Tratamento robusto de estados e ações

## 🔬 Componentes Arquiteturais

### `BlackJackQLearningAgent`
Classe central que encapsula a lógica completa de aprendizado por reforço.

#### Hiperparâmetros
- `epsilon`: Taxa de exploração inicial (0.2)
- `alpha`: Taxa de aprendizado (0.2)
- `gamma`: Fator de desconto (0.99)

#### Métodos Chave
- `get_state_key()`: Conversão de estados
- `get_action()`: Seleção de ações
- `update()`: Atualização da política
- `train()`: Treinamento do agente

## 📈 Métricas e Análise

### Avaliação de Desempenho
- Treinamento: 1,000,000 episódios
- Métricas calculadas:
  - Taxa de vitória
  - Taxa de empate
  - Taxa de derrota

### Visualização
- Gráfico de média móvel de recompensas
- Evolução do aprendizado ao longo dos episódios

## 🚀 Dependências

### Bibliotecas Utilizadas
- `gymnasium`: Ambiente de aprendizado por reforço
- `numpy`: Computações numéricas
- `pandas`: Manipulação de dados
- `matplotlib`: Visualização
- `tqdm`: Progresso de treinamento

## 💻 Instalação & Execução

### Pré-requisitos
- Python 3.8+
- pip

### Instalação
```bash
pip install gymnasium numpy pandas matplotlib tqdm
```

## 🧮 Detalhes Matemáticos

### Equação de Atualização Q-Learning
Q(s,a) ← Q(s,a) + α * [R + γ * max(Q(s')) - Q(s,a)]

Onde:
- Q(s,a): Valor da ação
- α: Taxa de aprendizado
- R: Recompensa
- γ: Fator de desconto
- max(Q(s')): Máximo valor Q para próximo estado

## 🔍 Estratégias Implementadas

### Exploração vs Explotação
- Política Épsilon-Gulosa
- Decaimento exponencial de épsilon
- Exploração inicial vs Explotação progressiva

### Tratamento de Estados
- Suporte a estados com ás utilizável
- Mapeamento dinâmico de estados para chaves

## 🎲 Demonstração

### Funcionalidades
- Treinamento do agente
- Plotagem de resultados
- Avaliação de desempenho
- Modo de visualização de jogos

## 🔬 Análise de Complexidade

### Espaço
- O(n): Tabela Q cresce com número de estados únicos
- Complexidade: Linear com estados explorados

### Tempo
- O(m * k): m = episódios, k = passos por episódio
- Treinamento: Convergência em ~1,000,000 episódios

## 🦾 Possíveis Extensões
- Implementar Deep Q-Learning
- Adicionar função de aproximação de valor
- Experimentar outros algoritmos de RL
- Generalizar para outros jogos de casino

## 📝 Contribuições
Pull requests são bem-vindos. Para mudanças importantes, abra um issue primeiro para discutir o que você gostaria de modificar.

## 📋 Licença
[MIT](https://choosealicense.com/licenses/mit/)

---
