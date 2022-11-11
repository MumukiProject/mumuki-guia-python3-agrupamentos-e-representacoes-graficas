Infelizmente, os departamentos e localidades de um país dificilmente são únicos :facepalm:, Por exemplo, neste dataset existem 11 departamentos chamados `"Capital"`:

||loc_code|category|province|department|city|name|
|---|---|---|---|---|---|---|
|0|10049030|Salas de cine|Catamarca|Capital|Catamarca|Cinemacenter
|(..)|
|14|42021020|Salas de cine|La Pampa|Capital|Santa Rosa|Milenium
|(..)|
|18|54028030|Salas de cine|Misiones|Capital|Posadas|Del Conocimiento
|(..)|
|20|66028050|Salas de cine|Salta|Capital|Salta|El Teatrino
|(..)|


Quando essas situações acontecem, não poderemos agrupar descuidadamente de acordo com uma única coluna, pois vamos acabar misturando dados acidentalmente 🙅. Por exemplo, nesta situação, teríamos adicionado os números de assentos dos departamentos que têm o mesmo nome, mas não têm nada a ver entre si :crazy_face:.

Em vez disso, construiremos nossos grupos levando em consideração quantas colunas forem necessárias para evitar essas ambiguidades, da seguinte maneira:

```python
ム cinemas.groupby(["province", "department"], as_index=False)["seats"].sum()
```

||province |department |seats|
|---|---|---|---|
|0 |Buenos Aires |9 de julio |90
|1 |Buenos Aires |Adolfo Gonzales Chaves |250
|2 |Buenos Aires |Almirante Brown |3215
|3 |Buenos Aires |Avellaneda |4805
|4 |Buenos Aires |Ayacucho |385
|... |... |... |...
|148 |Tierra del Fuego |Rio Grande |584
|149 |Tierra del Fuego |Ushuaia |861
|150 |Tucumán |Capital |2286
|151 |Tucumán |Tafi Viejo |830
|152 |Tucumán |Yerba Buena |2045
 
Como podemos ver, quando ao invés de especificar um nome de coluna, passamos uma lista de nomes como parâmetro, os dados são agrupados de acordo com todas elas e o resultado é uma tabela com mais de duas colunas.

>Este não é o único problema! Neste dataset, vamos ver que existem duas cidades chamadas `"Colón"`, uma em Buenos Aires e outra em Entre Ríos:
>
> ||loc_code|category|province|department|city|name|
> |---|---|---|---|---|---|---|
> |(...)|
> |9|30008020|Salas de cine|Entre Ríos|Colon|Colón|Starlight
> |(...)|
> |293|6175010|Salas de cine|Buenos Aires|Colon|Colón|Cine Teatro Colon
>
> :seat: Tendo isso em mente, crie um novo `DataFrame` que tenha o total de assentos por localidade e salve em uma variável `assentos_per_localidade`


<style>

blockquote .table {
  background: white;
  border-radius: 5px;
  margin: 9px 0;
}

</style>