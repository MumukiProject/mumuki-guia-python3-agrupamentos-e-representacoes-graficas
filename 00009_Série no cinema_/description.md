Para representar com gráficos é definitivamente muito conveniente para `groupby` retornar um `Series`, mas às vezes será mais prático obter os resultados na forma de um `DataFrame` de duas colunas.

Na verdade, quando começamos a analisar nossos dados de cinemas, comentamos que nossa _tabela_ ideal ficaria assim:

||setor|screens|
|---|---|---|
|0|Privado comercial|879|
|1|Público municipal|57|
|2|Público nacional|14|
|3|Público provincial|11|
|4|Privado independiente|8|
|5|Privado comunitario|4|
|6|Otros|1|
 
📰 A boa notícia é que isso é fácil de conseguir, apenas adicionando o parâmetro `as_index=False` a `groupby`:

```python
ム cinemas.groupby("sector", as_index=False)["screens"].sum()
```

E é isso :tada:! Agora teremos disponíveis todas as operações que vimos (e que veremos mais adiante).

> 🛑 Atenção! Vejamos se ficou claro: usando o que acabamos de aprender, gere uma tabela contendo o número total de assentos em cada estado e armazene na variável `assentos_por_estado`.
