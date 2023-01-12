Parabéns!  👏 Neste caso queríamos a média das multas e por isso precisamos calcular a média. No entanto, com exceção da primeira opção (porque não podemos calcular a média de uma coluna categórica), todas elas podem fazer sentido, pois tanto a média...


|placa|infração|
|----|----|
|`ab16`|166.66|
|`xy40`|175|
|`mm12`|150|
|`hz15`|100|

...a mediana...


|placa|infração|
|----|----|
|`ab16`|200|
|`xy40`|150|
|`mm12`|150|
|`hz15`|100|

...e a contagem são agregações:

|placa|infração|
|----|----|
|`ab16`|3|
|`xy40`|2|
|`mm12`|1|
|`hz15`|1|

Na verdade, esta última lembra bastante a ideia de contar o número de vezes que um valor é repetido, razão pela qual `value_counts` e o problema dos agrupamentos se parecem 😎.     