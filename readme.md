# 100 Days of Python

Repositório com uma sequencia de desafios em python desde os niveis mais basicos, que utilizei como minha introdução
à linguagem de programação e em projetos mais avançados para praticar a logica de programação e resolução de problemas.

---

### [Dia 5: Gerador de senhas](https://github.com/FerrMath/100_days_of_python/tree/master/day_5)
    
* Tipo de programa: Terminal;

  * Gerador de senhas básico. O usuário pode decidir o tamanho da senha e a quantidade de números e simbolos que deseja incluir, porem não ultrapassar, nesse total.
  
  * Os caracteres possiveis:
          
        minusculas = [a-z]
        maiusculas = [A-Z]
        numeros = [0-9]
        simbolos = ["!", "@", "#", "$", "&", "*"]

---

### [Dia 6: Jogo de forca](https://github.com/FerrMath/100_days_of_python/tree/master/day_6)

* Tipo de programa: Terminal;

  - Jogo da forca em potuguês. O usuário pode escolher uma letra até a palavra secreta ser descoberta ou, no caso de muitos erros, completar o desenho do Stickman, levando ao fim do jogo como derrota para o jogador.

<br>

---

### [Dia 7: Caesar Cypher](https://github.com/FerrMath/100_days_of_python/tree/master/day_7)

  * Tipo de programa: Terminal;

  - Programa de criptografia. O usuario informa se deseja criptografar ou descriptografar uma mensagem, em seguida informa a chave `{n = int}` que irá realizar as alterações. Atualmente os valores lidos serão apenas em letras minusculas. Caracteres como `" ", "$", 123456`, serão apenas adicionados na mensagem final.

        * Input: (msg = "abc de", key = 5);
        * Output: "fgh ij"

---

### [Dia 8: Leilão secreto](https://github.com/FerrMath/100_days_of_python/tree/master/day_8)

  * Tipo de programa: Terminal;

  - Programa de leilão. O usuario consegue fazer novos lances até que o mesmo solicite o fim do leilão. Após isso o lance mais alto será apresentado com o nome do vencedor do leilão.
        
        # Lance unico será considerado o mais alto. 
        * Input: (nome = "abcde", lance = 123.45)
        * Output: "The winner is Abcde, with the bid of $123.45"

---

### [Dia 9: Calculator](https://github.com/FerrMath/100_days_of_python/tree/master/day_9)

  * Tipo de programa: Terminal;

  - Calculadora básica. O usuário tem a opção de reutilizar o resultado de sua opearação anterior na operação seguinte.

  * Exemplo de execução:
      
      <br>Usuario coloca os valores.

        Enter the first number: 15
        Enter the next value: 5
      <br>
      
      Escolhe a operação.
        
        Possible operations:
        --> +
        --> -
        --> *
        --> /

        Enter operation: /
      <br>

      Pega o resultado.

        Result -- > 15.0 / 5.0 = 3.00
      <br>

      É questionado se deseja usar o resultado na conta seguinte.

        Continue operations with the previous result?
        [y] / [n]: y
      <br>

      Se o usuario responder `"y"` seguido do input `3` e da operação escolhida `"*"` o output será:
      
        Result -- > 3.0 * 3.0 = 9.00

---

### [Dia 10: BlackJack](https://github.com/FerrMath/100_days_of_python/tree/master/day_10)

  * Tipo de programa: Terminal;

  - Round de blackjack.
      - O jogador e a mesa comçam com duas cartas. 
      A mesa terá a segunda carta oculta até o jogador sofrer um `BUST` ou optar por fazer um `STAND`.

      - O jogador pode pedir um `HIT` desde que o valor total de sua mão seja inferior a `21`. Isso irá adicionar uma carta à sua mão.

      -As cartas possiveis são:

        # 'a' ou 'Ás' == (11 || 1), dependendo do valor atual da mão
        baralho = ['a', '2', '3', '4', '5', '6','7', '8', '9', '10', 'j', 'q', 'k'] * 4
      
          
          