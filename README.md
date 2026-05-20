Para resolver o problema do atendimento hospitalar, foi utilizada uma estrutura de dados do tipo Heap, que permite organizar elementos com base em prioridades.
A linguagem escolhida foi Python, utilizando a biblioteca nativa heapq, que implementa uma min-heap (ou seja, o menor valor tem maior prioridade na estrutura).
O sistema utiliza a seguinte classificação de prioridade:

1  Emergência
2  Urgente
3  Pouco urgente
4  Não urgente

Nesse modelo, quanto menor o número, maior a prioridade de atendimento. Assim, pacientes em estado de emergência são atendidos antes dos demais.
Cada paciente foi representado por uma classe contendo:

Nome
Nível de prioridade
Descrição da prioridade

A fila de atendimento foi implementada como uma lista, manipulada pelas funções:

heappush: para inserir pacientes mantendo a propriedade da heap
heappop: para remover o paciente de maior prioridade

Além disso, foi implementado um critério de desempate utilizando a ordem de chegada dos pacientes. Dessa forma, quando dois pacientes possuem a mesma prioridade.
O sistema atende primeiro quem chegou antes.
As principais operações do sistema são:

Inserção de pacientes na fila (complexidade O(log n))
Remoção do paciente mais prioritário (O(log n))
Visualização da fila

Essa abordagem garante eficiência mesmo com grande número de pacientes, organizando corretamente o atendimento conforme o nível de urgência.
