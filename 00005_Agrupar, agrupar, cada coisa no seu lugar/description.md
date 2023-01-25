O que são então os _agrupamentos_? Quando agrupamos de acordo com uma coluna `A`, estaremos juntando todas as linhas que possuem o mesmo valor na referida coluna `A`, e então aplicaremos uma _agregação_ em todos os valores de uma coluna `B` que caíram em cada grupo.

Como, como...? Bem, talvez seja mais fácil ver com um exemplo 😅. Considere a seguinte tabela com placas de automóveis 🚗 e os valores de suas infrações de trânsito ⛔:

|placa|infração|
|----|---|
|`ab16`|100|
|`xy40`|200|
|`mm12`|150|
|`ab16`|200|
|`xy40`|150|
|`ab16`|200|
|`hz15`|100|

Se quisermos saber qual é o valor total das infrações de cada placa, devemos _agrupar_ de acordo com a coluna `placa`, juntando todas as linhas que possuem a mesma placa....

|patente|infração||
|----|---|---|
|`ab16`|100|(primeiro grupo)|
| |200|
| |200|
|`xy40`|200|(segundo grupo)|
| |150|
|`mm12`|150|(terceiro grupo)|
|`hz15`|100|(quarto grupo)|


... e então, para cada grupo, faça a somatória da coluna `infração`:

|placa|infração||
|----|---|---|
|`ab16`|500|`(= 100 + 200 + 200)`|
|`xy40`|350|`(= 200 + 150)`|
|`mm12`|150|`(= 150)`|
|`hz15`|100|`(= 100)`|

Com este exemplo acabamos de ver, passo a passo, o que significa _agrupar de acordo com as placas e calcular a soma das infrações_. Mas quando agrupamos de acordo a uma determinada coluna, podemos então usar qualquer outra agregação.

> Se agora quiséssemos saber o valor médio das multas que correspondem a cada placa, que agrupamento deveríamos fazer?
