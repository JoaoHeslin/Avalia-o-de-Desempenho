# Atividade de Avaliação de Desempenho - Teoria das Filas e Simulação Java

## Descrição do Projeto

Este projeto tem como objetivo comparar os resultados de uma simulação prática realizada em Java com um modelo teórico baseado na teoria das filas. A atividade foi proposta pelo professor, que forneceu um código Java que simula o desempenho de um servidor web. O desafio foi automatizar a execução do código Java e comparar seus resultados com os do modelo teórico.

A atividade foi dividida em duas questões:
- **Questão 2**: Escalando o número de requisições.
- **Questão 3**: Variando o número de servidores.

Os códigos Python automatizam a execução das simulações para ambas as questões, permitindo comparar os resultados obtidos nas simulações práticas com os teóricos para diferentes configurações de requisições e servidores.

## Estrutura do Projeto

- **Simulação Java**: Um código Java foi fornecido para simular a execução de servidores web com diferentes quantidades de requisições e servidores. O código Java é executado através de um comando no terminal, que gera a saída que será utilizada para comparação.
  
- **Teoria das Filas**: Um modelo de teoria das filas foi desenvolvido em Python em um notebook (`.ipynb`). Esse modelo é utilizado para calcular as métricas de desempenho teórico de um servidor com base na teoria das filas.

- **Automação Python**: O código Python foi automatizado para executar a simulação Java diretamente do terminal e capturar os resultados. Os resultados de ambas as simulações (Java e teoria das filas) são então armazenados em DataFrames e comparados utilizando gráficos.

## Funcionalidade

### 1. **Automação da Execução da Simulação Java**:
O código Python automatiza a execução do comando no terminal para rodar a simulação Java. Ele passa os parâmetros necessários para a execução e captura a saída gerada. Essa automação foi criada para rodar várias simulações de forma eficiente, economizando tempo.

### 2. **Teoria das Filas**:
Foi criado um modelo de teoria das filas que utiliza as fórmulas matemáticas apropriadas para calcular os tempos de resposta e de espera para um servidor com diferentes números de requisições. Os resultados são armazenados em DataFrames e comparados com os resultados da simulação Java.

### 3. **Comparação dos Resultados**:
Após a execução das simulações, os resultados de ambas as abordagens (simulação Java e teoria das filas) são armazenados em DataFrames. São gerados gráficos para comparar os resultados obtidos na simulação prática com os teóricos, permitindo uma análise visual do desempenho do servidor.

## Requisitos

- **Python 3.x**
- **Java 8 ou superior**

## Como Rodar o Projeto

1. **Preparação do Ambiente**:
   - Certifique-se de que você tem o Python 3.x e o Java instalados em sua máquina.
   - Instale as dependências do Python utilizando o comando:
     ```bash
     pip install pandas matplotlib math os suobprocess
     ```
     
2. **Rodar o Código**:
   - Execute o script Python para automatizar a execução da simulação Java e realizar a comparação com o modelo de teoria das filas. O script da questão 2 irá salvar os resultados em um arquivo Excel (`results1.xlsx`) e o modelo eteorico também vai gerar um arquivo Excel (`results2.xlsx`). Já o O script da questão 3 irá salvar os resultados em um arquivo Excel (`results3.xlsx`) e o modelo teórico também vai gerar um arquivo Excel (`results4.xlsx`). Após terms os aruqivos de comparação vai ser gerado os gráficos para comparação dos resultados.


3. **Verificar Resultados**:
   - Os resultados serão salvos no arquivo `relatorio.ipynb`. Você também verá gráficos comparando as simulações Java com a teoria das filas.

## Como Funciona

1. O script Python executa a simulação Java para diferentes números de requisições.
2. Ele captura a saída da simulação e a armazena junto com os parâmetros de entrada (tempo de serviço, número de servidores, etc.).
3. O modelo de teoria das filas calcula os valores esperados de desempenho (teóricos).
4. Ambos os resultados (simulação Java e teoria das filas) são armazenados em DataFrames.
5. São gerados gráficos comparando os resultados para analisar a precisão da simulação Java em relação ao modelo teórico.
