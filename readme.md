# 100 Days of Python

Repositório com uma sequencia de desafios em python desde os niveis mais basicos, que utilizei como minha introdução
à linguagem de programação e em projetos mais avançados para praticar a logica de programação e resolução de problemas.

---

### [Dia 5: Gerador de senhas](https://github.com/FerrMath/100_days_of_python/tree/master/day_5)
    
* Tipo de programa: Terminal;

    * Gerador de senhas básico. O usuário pode decidir o tamanho da senha e a quantidade de números e simbolos que deseja incluir, porem não ultrapassar, nesse total.
    * Os caracteres possiveis:
      * `min = [a-z]`
      * `mai = [A-Z]`
      * `num = [0-9]`
      * `simbols = ["!", "@", "#", "$", "&", "*"]`

---

### [Dia 6: Jogo de forca](https://github.com/FerrMath/100_days_of_python/tree/master/day_6)

* Tipo de programa: Terminal;

  - Jogo da forca em potuguês. O usuário pode escolher uma letra até a palavra secreta ser descoberta ou, no caso de muitos erros, completar o desenho do Stickman, levando ao fim do jogo como derrota para o jogador.

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