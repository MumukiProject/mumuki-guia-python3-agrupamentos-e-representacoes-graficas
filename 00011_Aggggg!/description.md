🤬 Não estamos resmungando! Só queríamos mostrar outra operação útil ao fazer agregações: `agg` 😅.

```python
cinemas.groupby("province", as_index=False).agg({
   "screens": "sum",
   "seats": "mean"
})
```
 
Ao contrário das agregações anteriores como `sum` e `max`, `agg` permite fazer várias ao mesmo tempo e obter tabelas com múltiplos resultados:

||province|screens|seats|
|---|---|---|---|
|0|Buenos Aires|358|878.415094|
|1|Catamarca|12|800.000000|
|2|Chaco|14|617.250000|
|3|Chubut|10|298.000000|
|4|Ciudad Autónoma de Buenos Aires|153|896.742857|
|5|Corrientes|17|421.250000|
|6|Córdoba|105|594.257143|
|(...)|

Com `agg` torna-se fácil adicionar agregações às nossas tabelas, apenas adicionando uma chave (a coluna a adicionar) e um valor (a operação a realizar) ao dicionário que recebe como parâmetro. Por exemplo, também podemos incluir a quantidade de cinemas na tabela anterior:


```python
cinemas.groupby("province", as_index=False).agg({
   "name": "count",
   "screens": "sum",
   "seats": "mean"
})
# Se te incomoda que a coluna se chame name, já veremos mais adiante...
```

> Vejamos se ficou claro: gere uma tabela `medianas_por_provincia` com o número mediano de telas e assentos em cada província. A tabela deve estar ordenada em ordem alfabética, de A a Z

