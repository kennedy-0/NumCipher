# NumCipher

<p align="center">
  <b>Sistema educacional de criptografia utilizando Python.</b>
</p>

## Sobre o projeto

O NumCipher é um projeto desenvolvido em Python com o objetivo de apresentar conceitos básicos de criptografia de maneira simples e interativa.

O sistema utiliza um dicionário personalizado para transformar letras do alfabeto em números, permitindo codificar e decodificar mensagens.

A proposta é facilitar o entendimento da lógica por trás dos sistemas de criptografia, utilizando estruturas básicas da programação.

## Funcionalidades

- **Criptografar mensagens:** transforma letras em números.
- **Descriptografar mensagens:** converte números novamente em letras.
- **Dicionário personalizado:** utiliza uma tabela própria de correspondência.
- **Menu interativo:** permite escolher as operações disponíveis.

## Como funciona?

O projeto utiliza uma técnica de substituição numérica.

Cada letra recebe um número correspondente, seguindo uma ordem inversa do alfabeto.

Exemplo:

| Letra | Código |
|:---:|:---:|
| A | 26 |
| B | 25 |
| C | 24 |
| D | 23 |
| E | 22 |
| ... | ... |
| Z | 1 |

### Exemplo de criptografia

Mensagem original:

```text
ola mundo
```

Mensagem criptografada:

```text
121526 1413132312
```

O processo inverso utiliza o mesmo dicionário para recuperar a mensagem original.

## Tecnologias utilizadas

- Python 3
- Biblioteca sys
- Dicionários
- Funções
- Estruturas condicionais
- Laços de repetição

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/kennedy-0/NumCipher.git
```

2. Entre na pasta:

```bash
cd NumCipher
```

3. Execute o programa:

```bash
python3 main.py
```

## Menu do sistema

```text
[1] Falar
[2] Traduzir
[3] Sair
```

## Objetivo educacional

Este projeto foi criado para estudar:

- Introdução à criptografia.
- Substituição de caracteres.
- Conversão de dados.
- Manipulação de strings.
- Lógica de programação com Python.

## Aviso

O NumCipher utiliza uma cifra didática de substituição numérica. Não é recomendado para proteger informações reais ou confidenciais, pois não possui segurança criptográfica adequada.

## Autor

Desenvolvido como projeto de estudo em Python.
