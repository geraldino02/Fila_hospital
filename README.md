Para resolver o problema do atendimento hospitalar, foi utilizada uma estrutura de dados do tipo Heap, que permite organizar elementos com base em prioridades.
A linguagem escolhida foi Python, utilizando a biblioteca nativa heapq, que implementa uma min-heap (ou seja, o menor valor tem maior prioridade na estrutura).
O sistema utiliza a seguinte classificação de prioridade:

1  Emergência<br>
2  Urgente<br>
3  Pouco urgente<br>
4  Não urgente<br>

Nesse modelo, quanto menor o número, maior a prioridade de atendimento. Assim, pacientes em estado de emergência são atendidos antes dos demais.
Cada paciente foi representado por uma classe contendo:

Nome<br>
Nível de prioridade<br>
Descrição da prioridade<br>

A fila de atendimento foi implementada como uma lista, manipulada pelas funções:

heappush: para inserir pacientes mantendo a propriedade da heap<br>
heappop: para remover o paciente de maior prioridade<br>

Além disso, foi implementado um critério de desempate utilizando a ordem de chegada dos pacientes. Dessa forma, quando dois pacientes possuem a mesma prioridade.
O sistema atende primeiro quem chegou antes.
As principais operações do sistema são:

Inserção de pacientes na fila (complexidade O(log n))<br>
Remoção do paciente mais prioritário (O(log n))<br>
Visualização da fila<br>

Essa abordagem garante eficiência mesmo com grande número de pacientes, organizando corretamente o atendimento conforme o nível de urgência.<br>
link para visualização na prática do código em funcionamento: https://youtu.be/NzeJUprm7Bc
Integrantes do grupo:<br>
GABRIEL MOSSARELLI MOFATTO - N056797
GUILHERME GOUVÊA MARRAFON - G8354H0
LEONARDO TESTA DE MIRANDA - N092394
TIAGO DO CARMO GERALDINO - G76AHF6
