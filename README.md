Fila de Atendimento — Hands On

Projeto desenvolvido em Python para simular o funcionamento de três tipos de fila em uma central de atendimento:

Fila Clássica (FIFO) — atendimento na ordem de chegada
Fila Circular — reaproveitamento de posições em uma estrutura de tamanho fixo
Fila de Prioridade — atendimento conforme o nível de urgência do cliente

Integrantes:

Rhuann Pabllo Ferreira Magalhães	45158872

Guilherme de Souza Dutra	45604061

Ryan Áquila Damasceno Vieira	38363470

Objetivo:

Mostrar na prática como diferentes tipos de fila organizam e atendem clientes, comparando a lógica de funcionamento e o comportamento de cada estrutura.

Cada cliente possui:

Nome
Senha
Prioridade

As prioridades disponíveis são:

🔴 Emergência
🟡 Prioritário
🟢 Normal

Arquivos do projeto
fila-atendimento-hands-on/

fila_classica.py

fila_circular.py

fila_prioridade.py

README.md

1. FILA CLÁSSICA

A fila clássica utiliza o conceito FIFO (First In, First Out). Isso significa que o primeiro cliente que entra é o primeiro a ser atendido.

Foram cadastrados 10 clientes e utilizados os seguintes métodos:

  enqueue() - adiciona cliente
  
  dequeue() - remove/atende cliente
  
  head() - mostra o próximo cliente
  
  size() - mostra o tamanho da fila
  
  empty() - verifica se está vazia

  Exemplo:

  Ordem de chegada:
  
  João
  
  Maria
  
  Pedro
  
  Ana
  
  Ordem de atendimento:
  
  João
  
  Maria
  
  Pedro
  
  Ana

2. FILA CIRCULAR

A fila circular possui capacidade para 5 clientes.

Ela utiliza os índices front e rear. Quando um cliente é removido, a posição liberada pode ser reutilizada.

Por exemplo, depois de remover um cliente da primeira posição, outro cliente pode ocupar essa posição novamente.

O programa também mostra os valores de front e rear durante os testes.

3. FILA DE PRIORIDADE

A fila de prioridade foi implementada utilizando o módulo heapq.

O cliente com menor número de prioridade é atendido primeiro:

1 - Emergência

2 - Prioritário

3 - Normal

Quando dois clientes possuem a mesma prioridade, a ordem de chegada é mantida através de um contador.

Exemplo:

João - prioridade 3

Maria - prioridade 1

Pedro - prioridade 2

Ordem de atendimento:

Maria

Pedro

João

4. Desafio Final

O sistema também realiza uma simulação com 20 clientes, gerando automaticamente suas prioridades.

São apresentadas:

Ordem de chegada;

Ordem de atendimento da fila clássica;

Funcionamento da fila circular;

Valores de front e rear;

Ordem de atendimento da fila de prioridade;

Comparação entre as estruturas.

5. Comparação

Fila	Como funciona
Clássica	Primeiro que chega, primeiro que sai
Circular	Reutiliza posições liberadas
Prioridade	Atende primeiro quem possui maior prioridade

A fila clássica mantém a ordem de chegada. A fila circular funciona de forma semelhante, mas possui espaço limitado e reutiliza posições. Já a fila de prioridade pode mudar a ordem de atendimento dependendo da prioridade de cada cliente.

6. Perguntas:

  . Por que a fila de prioridade pode ter uma ordem diferente da fila clássica?

    Porque a fila clássica segue a ordem de chegada, enquanto a fila de prioridade considera primeiro o nível de prioridade do cliente.

  . Quando uma fila de prioridade seria mais adequada?

    Pode ser usada em situações como hospitais, chamados urgentes, suporte técnico e processamento de tarefas que possuem diferentes níveis de importância.

  . Quais são as vantagens e limitações de uma fila circular?

    A principal vantagem é poder reutilizar posições que foram liberadas, aproveitando melhor o espaço. A limitação é que ela possui uma capacidade definida e precisa controlar os índices front e rear.

  . O que acontece quando a fila circular está cheia?

    Um novo cliente não pode ser inserido até que algum espaço seja liberado. O programa informa que a fila está cheia.

7. Como executar

É necessário ter o Python 3 instalado.

No terminal, dentro da pasta do projeto:

python fila_classica.py

python fila_circular.py

python fila_prioridade.py

8. Evidências

Foram realizados testes dos três tipos de fila.

Fila Clássica

<img width="275" height="430" alt="teste 1" src="https://github.com/user-attachments/assets/561fcad2-51f0-4d5d-9af6-ff83d50fff9c" />


Fila Circular

<img width="986" height="309" alt="teste3" src="https://github.com/user-attachments/assets/a7c8c6c3-5dd5-406a-b666-d9cef8cbca3c" />


Fila de Prioridade

<img width="415" height="450" alt="teste2" src="https://github.com/user-attachments/assets/7495d0a3-1f0e-400c-acf1-c763de1fc995" />

Desafio

<img width="486" height="376" alt="desafio" src="https://github.com/user-attachments/assets/0f82019f-9af2-47b2-a893-a63cb74163bb" />
<img width="434" height="379" alt="desafio2" src="https://github.com/user-attachments/assets/7be64138-3c75-4b79-a8d1-a96dcfce3fc2" />
<img width="609" height="585" alt="desafio3" src="https://github.com/user-attachments/assets/aec44143-cd46-4795-87b5-a20c1d34c724" />
<img width="458" height="301" alt="desafio4" src="https://github.com/user-attachments/assets/18485630-98da-4e52-a0eb-cb2c451a0fdf" />

Comparação do desafio:

A fila clássica atende os clientes na mesma ordem em que eles chegaram, seguindo o sistema FIFO.

A fila circular funciona de forma parecida, mas tem um limite de 5 clientes e consegue reutilizar as posições que ficam vazias depois que um cliente é atendido.

Já a fila de prioridade não segue somente a ordem de chegada. Ela atende primeiro os clientes com prioridade 1, depois os de prioridade 2 e por último os de prioridade 3. Quando os clientes possuem a mesma prioridade, a ordem de chegada é mantida.

Assim, cada fila possui uma forma diferente de organizar os clientes e pode ser usada dependendo da situação.





Conclusão

Com o projeto foi possível entender na prática a diferença entre uma fila comum, uma fila circular e uma fila de prioridade.

Cada estrutura possui uma forma diferente de organizar os clientes e pode ser utilizada de acordo com a situação.
