README - Exercícios de Programação
Este é um resumo dos exercícios que foram realizados até agora, com uma explicação breve sobre cada um deles.

Exercícios:

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