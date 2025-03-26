README - Exercícios de Programação
Este é um resumo dos exercícios que foram realizados até agora, com uma explicação breve sobre cada um deles.

Exercícios:

30. Exercício: Cálculo de Fatorial e Fibonacci

Objetivo: Criar um programa interativo que permite ao usuário calcular tanto o fatorial quanto a sequência de Fibonacci de maneira simples e eficiente. O código oferece validação de entradas, tratamento de erros e a opção de realizar múltiplos cálculos sem reiniciar o programa.

Descrição: O sistema solicita ao usuário que escolha entre o cálculo de fatorial ou da sequência de Fibonacci. Após a escolha, o programa solicita a entrada do usuário e executa o cálculo correspondente. Caso o usuário queira realizar outro cálculo, pode optar por continuar, ou sair do programa a qualquer momento. As entradas são validadas para garantir que o usuário forneça números válidos, e o código utiliza tratamento de erros para prevenir falhas. Além disso, o programa inclui mensagens interativas e uma pausa para melhorar a experiência do usuário.

29. Exercício: Par ou Ímpar
Objetivo: Criar um programa interativo que identifica se um número é par ou ímpar, garantindo entradas válidas e permitindo múltiplas execuções.

Descrição: O sistema solicita um número entre 1 e 10 e informa se ele é par ou ímpar. Para melhorar a experiência do usuário, foram implementadas, uma validação de entrada para evitar erros com valores inválidos, opção de saída ("sair") para interromper o processo, loop interativo para permitir novas tentativas sem reiniciar o programa, mensagens dinâmicas e tempo de espera para tornar a execução mais fluida. O exercício reforçou o uso de condicionais, loops e tratamento de erros em Python.

28. Roleta de Afazeres com Integração de APIs e Histórico
Objetivo: Criar um sistema interativo que sorteia afazeres personalizados e atividades de entretenimento, integrando diversas APIs públicas para fornecer sugestões dinâmicas, além de armazenar o histórico das escolhas.

Descrição: Neste exercício, desenvolvi um sistema de roleta que permite ao usuário cadastrar até sete opções de afazeres, incluindo tanto atividades personalizadas quanto categorias predefinidas (como filmes, séries, músicas, animes, livros e pratos). Caso a opção sorteada corresponda a uma dessas categorias, a aplicação faz uma requisição a uma API pública para buscar uma sugestão aleatória dentro do tema. Aprendi a consumir APIs externas usando requests, tratar respostas JSON e estruturar a lógica para apresentar os dados relevantes ao usuário. Além disso, implementei um sistema de armazenamento no MySQL para registrar cada sorteio com data e horário, permitindo a consulta de um histórico. O projeto fortaleceu meu conhecimento sobre manipulação de formulários em Flask, integração com bancos de dados e consumo de APIs para enriquecer a experiência do usuário.

27. Roleta de Entretenimento e Tarefas

Objetivo: Criar um sistema interativo que auxilia na escolha de atividades diárias por meio de um sorteio, incluindo filmes, séries, animes, músicas, livros e pratos aleatórios.

Descrição: Este projeto expande a ideia de uma roleta de afazeres ao integrar APIs para buscar conteúdos aleatórios. O usuário insere até seis opções, podendo incluir atividades personalizadas ou categorias predefinidas (como "Filme", "Série", "Música", etc.). Quando a roleta é girada, se uma das opções corresponder a uma categoria integrada, o programa consulta uma API pública para exibir um resultado aleatório correspondente. Além disso, todas as escolhas são salvas com data e hora em um arquivo de texto, permitindo um histórico das atividades sorteadas.

26. Roleta de Decisões

Objetivo: Criar um sistema interativo que auxilia na escolha de tarefas ou decisões por meio de um sorteio entre opções fornecidas pelo usuário.

Descrição: Este projeto consiste em uma roleta digital onde o usuário pode inserir até oito opções de tarefas, atividades ou decisões. O sistema registra as opções e permite que o usuário gire a roleta digitando "sortear". A escolha aleatória é salva em um arquivo de texto junto com a data e horário do sorteio. Além disso, o programa oferece a possibilidade de reiniciar o processo ou encerrar a sessão, tornando a experiência dinâmica e reutilizável.

24. Roleta de Comidas

Objetivo: Criar um sistema interativo que auxilia na escolha de refeições por meio de um sorteio entre opções fornecidas pelo usuário.

Descrição: Este projeto consiste em uma roleta digital de comidas, onde o usuário insere até cinco opções e um sorteio aleatório escolhe uma delas. O sistema conta com uma interface baseada no terminal, permitindo que o usuário cadastre suas opções e, ao digitar o comando "sortear", a roleta define a refeição escolhida. Além disso, o programa oferece opções para encerrar ou reiniciar o processo, garantindo uma experiência dinâmica e intuitiva.

23. CRUD de Usuários com JSON
Objetivo: Implementar um sistema completo de CRUD (Create, Read, Update, Delete) para gerenciar usuários, utilizando um arquivo JSON como banco de dados e o e-mail como identificador único.

Descrição: O sistema permite o cadastro, listagem, atualização e exclusão de usuários, garantindo validações como a verificação de e-mails repetidos, restrição de caracteres para telefone e cidade, e autenticação por senha para ações sensíveis. As informações são armazenadas de forma persistente em um arquivo JSON. O programa oferece um menu interativo para facilitar a navegação e operação do usuário.

22. Cadastro de Usuários com JSON e E-mail como ID
Objetivo: Criar um sistema interativo para cadastrar usuários, armazenando os dados em um arquivo JSON e utilizando o e-mail como identificador único.

Descrição: O sistema permite o cadastro de usuários com nome, e-mail, telefone e senha, garantindo validações essenciais, como a presença de "@" no e-mail, a exigência de preenchimento de todos os campos e a restrição de números para o telefone. Os dados são armazenados em um arquivo JSON para persistência. O sistema oferece um fluxo interativo e intuitivo, permitindo o cadastro contínuo até a saída do usuário.

21. Cadastro de Usuários com Dicionário e E-mail como ID

Objetivo: Desenvolver um sistema interativo para cadastrar usuários, utilizando um dicionário para armazenar os dados e o e-mail como identificador único.

Descrição: O sistema permite o cadastro de usuários com nome, e-mail, telefone e senha, garantindo validações essenciais, como a presença de "@" no e-mail, a exigência de preenchimento de todos os campos e a restrição de números para o telefone. Os dados são armazenados em um dicionário, onde o e-mail é utilizado como chave para evitar duplicações. O sistema oferece um fluxo interativo e intuitivo, permitindo o cadastro contínuo até a saída do usuário.

20. Cadastro de Usuários, Busca e Atualização
Objetivo: Desenvolver um sistema interativo para cadastrar, consultar e atualizar usuários, com validação de entradas e manipulação de arquivos.

Descrição: Este exercício visa a criação de um sistema que permite o cadastro de usuários com informações como nome, e-mail e telefone, com validações de entradas para garantir que os dados estejam corretos. O sistema inclui funcionalidades de consulta de usuários por e-mail, onde o e-mail é utilizado como critério único de busca, garantindo que os dados retornados sejam específicos e sem duplicidade. Além disso, foi implementada a atualização dos dados de um usuário com base no e-mail informado, com a verificação de todos os campos antes de realizar a alteração. O código utiliza manipulação de arquivos para registrar as informações dos usuários em um arquivo .txt, o que possibilita o armazenamento persistente dos dados. O menu interativo proporciona uma navegação simples entre as opções, permitindo a execução das funções de cadastro, consulta e atualização de maneira prática e eficiente.

19. Cadastro de Usuários e Consulta por E-mail

Objetivo: Desenvolver um sistema interativo para cadastro e consulta de usuários, com validação de entradas e manipulação de arquivos.

Descrição: Este exercício tem como foco a criação de um sistema para gerenciar o cadastro de usuários. O sistema permite que o usuário cadastre informações como nome, e-mail e telefone, garantindo que os dados sejam válidos, como a verificação do formato do e-mail e se o telefone contém apenas números. Além disso, oferece funcionalidades para exibir todos os cadastros registrados, buscar um usuário específico pelo e-mail e garantir que os dados sejam salvos corretamente em um arquivo .txt.
A busca por e-mail foi escolhida como critério de pesquisa, pois, de acordo com a lógica do sistema, um e-mail é único para cada usuário. Isso evita que dados duplicados sejam retornados, o que poderia acontecer se a busca fosse feita pelo nome, caso existissem usuários com o mesmo nome. O menu interativo facilita a navegação entre as opções, proporcionando uma experiência de usuário intuitiva e permitindo a execução de várias operações de cadastro e consulta.

18. Cadastro de Produtos e Consulta de Estoque

Objetivo: Desenvolver um sistema interativo para cadastro e consulta de produtos, com validação de entradas e manipulação de arquivos.

Descrição: Este exercício foca na criação de uma aplicação para gerenciar um estoque de produtos. O sistema permite cadastrar informações como nome, preço e quantidade de cada produto, validando se os dados inseridos são corretos, como a formatação do preço e a quantidade ser numérica. Além disso, é possível buscar por um produto específico, exibir todos os produtos cadastrados e garantir que os dados sejam salvos corretamente em um arquivo .txt. O menu interativo torna a interação com o sistema simples, com opções de cadastro, consulta e exibição, proporcionando uma experiência de usuário fluída.

17. Atualização de Contatos no Arquivo

Objetivo: Aprender a modificar dados específicos dentro de um arquivo .txt, garantindo que apenas as informações desejadas sejam alteradas.

Descrição: Neste exercício, criamos uma função que busca um nome dentro do arquivo arquivo_ex15.txt e permite atualizar seu e-mail e telefone sem alterar os outros dados. Para isso, utilizamos a leitura do arquivo com with open(), armazenamos as linhas em uma lista e percorremos os dados com um for para encontrar o nome correto. Caso o usuário insira um novo e-mail ou telefone, a linha correspondente é atualizada, garantindo que as informações antigas não sejam apagadas sem necessidade. Além disso, foram implementadas validações para garantir que o e-mail possua "@", que o telefone contenha apenas números e que o nome não esteja vazio. O exercício também ensinou a manipular arquivos sem perder os dados existentes e reforçou o uso de condicionais dentro de loops para modificar apenas partes específicas do conteúdo.

16. Exibição de Dados Cadastrados

Objetivo: Aprender a ler dados de um arquivo .txt e exibi-los de forma adequada, tratando erros como arquivo não encontrado.

Descrição: Neste exercício, criamos a função exibirUsuarios() que abre e lê o conteúdo de um arquivo .txt (no caso, arquivo_ex15.txt). Utilizamos a função with open para garantir que o arquivo seja fechado automaticamente após a leitura, e o parâmetro encoding='UTF8' para garantir que caracteres especiais sejam corretamente lidos. A função verifica se o arquivo contém dados, utilizando strip() para garantir que o conteúdo não seja apenas espaços em branco. Caso o arquivo esteja vazio ou não exista, uma mensagem informando o erro é exibida. A principal lição foi a manipulação de arquivos com tratamento de exceções usando try e except, além de garantir que a leitura de arquivos seja feita de maneira eficiente e segura.

15. Cadastro de Contatos com Validação e Salvamento em Arquivo

Objetivo: Aprender a coletar múltiplos dados e realizar validações, além de salvar informações em um arquivo.

Descrição: Neste exercício, criamos uma função que coleta o nome, e-mail e telefone do usuário, validando os dados inseridos. Utilizamos o método .strip() para garantir que os campos não estivessem vazios e o método .isdigit() para garantir que o telefone fosse composto apenas por números. Caso os dados estivessem corretos, as informações eram salvas em um arquivo .txt com o uso de with open() para garantir que o arquivo fosse fechado corretamente após a escrita. O parâmetro encoding='UTF8' foi utilizado para evitar problemas com caracteres especiais, como acentos. Com isso, a função aprendeu a tratar entradas de dados, validar as informações e realizar a gravação correta em um arquivo de texto.

14. Coleta de Dados (Nome, E-mail, Telefone)

Objetivo: Aprender a coletar múltiplos dados do usuário e passar argumentos para a função corretamente.

Descrição: Neste exercício, criamos uma função que recebe três parâmetros para coletar o nome, o e-mail e o telefone do usuário. A principal lição foi entender que, ao definir uma função com múltiplos parâmetros, todos devem ser passados juntos na mesma chamada da função, em vez de forma separada. A função também incluiu validações para garantir que os campos não estivessem vazios e para verificar se o e-mail continha o caractere "@" para ser considerado válido. Com isso, o exercício ajudou a melhorar o entendimento sobre como passar múltiplos parâmetros e validar dados de entrada.

13. Cálculo de Fatorial com Validação de Entrada

Objetivo: Aprender a calcular o fatorial de um número e tratar entradas inválidas de forma adequada.

Descrição: Neste exercício, criamos uma função que recebe um número inteiro do usuário e calcula o fatorial desse número utilizando a função math.factorial(). Foi implementada uma validação para garantir que o número seja positivo, e o programa trata o caso do número ser zero, retornando o fatorial de 0 como 1. Além disso, a entrada é validada para aceitar apenas números inteiros, e o programa exibe mensagens de erro claras se o usuário inserir algo que não seja um número. O controle de fluxo foi feito com o uso de um loop while e condições if para tratar os diferentes casos e finalizar o programa quando o usuário quiser, digitando "sair".

12. Cálculo de Média com Validação de Entrada

Objetivo: Aprender a lidar com entradas de números inteiros e flutuantes, calcular a média e implementar um controle de fluxo adequado.

Descrição: Neste exercício, criamos uma função que recebe números inteiros ou flutuantes do usuário e calcula a média desses números. Utilizamos a estrutura try/except para validar se o usuário inseriu um número válido e impedir que entradas erradas quebrem o programa. O programa armazena os números em uma lista e, ao final, calcula a média utilizando a fórmula soma / quantidade. Também foi implementada uma condição para encerrar o programa quando o usuário digita 'sair'. O exercício reforçou a manipulação de listas, a validação de entradas e o cálculo de médias.

11. Tratamento de Exceções com Try/Except para Tipos de Números

Objetivo: Aprender a lidar com entradas de números inteiros e flutuantes usando try e except.

Descrição: Neste exercício, criamos uma função que solicita ao usuário que insira números, validando se são inteiros ou flutuantes. Utilizamos a estrutura try/except para capturar e tratar erros no caso de entradas inválidas, garantindo que o programa continue funcionando corretamente. A função verifica se o número contém um ponto ('.') para determinar se ele deve ser convertido para float ou int. Caso o usuário insira algo que não seja um número, o except trata o erro e pede para o usuário tentar novamente.

10. Funções com Parâmetros e Try/Except

Objetivo: Trabalhar com funções e aprender a utilizar try e except para tratar erros de tipo nos inputs do usuário.

Descrição: O exercício focou na criação de uma função que recebe parâmetros e usa condicionais para escolher entre soma e multiplicação, além de usar try e except para validar se os inputs são números inteiros. Também houve a introdução ao uso de funções para organizar o código, tornando-o mais modular.

9. Cálculo de Média com While

Objetivo: Criar uma média de números utilizando while e funções como append(), sum() e len().

Descrição: O exercício ensinou a adicionar números em uma lista com append(), calcular a média utilizando sum() e len(), e a importância do uso do while para fazer o loop.

8. Contagem com While (De 10 a 0 e de 0 a 10)

Objetivo: Trabalhar com loops para realizar contagens em ordem crescente e decrescente.

Descrição: O exercício ensinou a controlar a execução do while para realizar contagens de 10 a 0 e de 0 a 10.

7. Manipulação de Dicionários

Objetivo: Aprender a trabalhar com dicionários e acessar seus valores.

Descrição: O exercício focou em acessar e manipular dicionários. Foi abordado como imprimir valores específicos dentro de listas armazenadas dentro de chaves de dicionários e como contar a quantidade de itens com len().

6. Como fazer List Comprehension

Objetivo: Introduzir a técnica de list comprehension para criar e modificar listas de maneira mais compacta.

Descrição: Aprendeu-se a escrever de maneira mais concisa o código para gerar listas baseadas em outra lista ou condição.

5. Como fazer um limite de tentativas nesse login utilizando While

Objetivo: Implementar um limite de tentativas no login usando loops.

Descrição: O exercício explorou como usar o while para criar um loop que controla o número de tentativas do login, limitando-o após um número predefinido.

4. Como fazer um login com variáveis e condicionais

Objetivo: Criar um sistema simples de login utilizando variáveis e condicionais.

Descrição: O exercício envolveu a criação de um processo de login com verificação de credenciais (usuário e senha). O foco foi em utilizar condicionais para verificar se os dados estão corretos.

3. Estudo de Condicionais (If, Elif, Else)

Objetivo: Explorar como usar condicionais para controlar o fluxo do código.

Descrição: O exercício introduziu a lógica de decisões, onde foi utilizado if, elif e else para direcionar o código de acordo com as condições fornecidas.

2. Como usar For e While

Objetivo: Entender as estruturas de repetição, como for e while.

Descrição: Aprendeu-se a percorrer listas e a manipular a execução de loops, além de como usar a condição break para parar o while e como pular de dois em dois itens de uma lista com o for.

1. Tipos Primitivos e como imprimir e inputar

Objetivo: Aprender a lidar com os tipos primitivos em Python (como int, float, str, etc.).

Descrição: O exercício envolveu a manipulação de entradas do usuário e a exibição de valores com diferentes tipos de dados, como inteiros e floats.