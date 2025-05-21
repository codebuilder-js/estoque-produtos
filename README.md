# Sistema de Controle de Estoque de Produtos

Este é um programa simples em Python para cadastro de produtos, controle de estoque e verificação da necessidade de reposição com base na quantidade mínima estipulada.

## Funcionalidades

O programa executa as seguintes etapas:

1. Solicita informações de **3 produtos**:
   - Nome do produto
   - Quantidade atual em estoque
   - Estoque mínimo necessário

2. Verifica se cada produto precisa de reposição.

3. Se a quantidade atual for menor que o estoque mínimo, o sistema simula a reposição:
   - A reposição é realizada até atingir o mínimo.
   - Caso mais de 10 unidades precisem ser repostas, o processo é cancelado com uma mensagem de "Reposição lenta... cancelando".

## Exemplo de uso

```bash
$ python controle_estoque.py
Produto: Caneta
Quantidade atual: 5
Estoque mínimo: 10
Produto: Caderno
Quantidade atual: 15
Estoque mínimo: 10
Produto: Lápis
Quantidade atual: 2
Estoque mínimo: 14

Verificando necessidade de reposiçao:
Caneta - Estoque BAIXO: 5 unidades
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.

Caderno - Estoque OK

Lápis - Estoque BAIXO: 2 unidades
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição completada.
Reposição lenta... cancelando.
