Não, estamos reclamando! 🤬 Só queríamos mostrar outra operação útil ao fazer agregações: `agg` 😅.

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
# Se te incomoda que a coluna se chame nome, já veremos mais adiante...
``` 

Mas isso não é tudo! `agg` também permite que você use agregações personalizadas, apenas passando uma função como valor. Por exemplo, se queremos contar a quantidade de cinemas que têm a frase `"Centro Cultural"` em seu nome...


||province|name|
|---|---|---|
|0|Buenos Aires|5|
|1|Catamarca|1|
|2|Chaco|0|
|3|Chubut|1|
|4|Ciudad Autónoma de Buenos Aires|3|
|5|Corrientes|0|
|6|Córdoba|2|
|(...)|

...podemos escrever algo assim ...
 
``python
cinemas.groupby("province", as_index=False).agg({
   "name": contar_centros_culturais
})
```

... onde em vez de passar uma string com o nome de uma agregação (como `"sum"` ou `"count"`), passamos a referência para uma função. Essas funções que o `agg` recebe devem utilizar uma lista com os valores das linhas de cada grupo:

```python
def contar_centros_culturais(nomes):
 return len([nome for nome in nomes if "centro cultural" in nome.lower()])
```

> :first_place: Agora é sua vez! Construa uma tabela `proporcao_cinemas_comerciais_estatais` que contenha, para cada estado, a proporção entre 0 e 1 de cinemas de gestão `"Privado comercial"`, ordenada de acordo com esta proporção, do menor para o maior.
