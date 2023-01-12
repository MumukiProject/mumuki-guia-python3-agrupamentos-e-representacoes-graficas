👀 Se você olhou atentamente para a tabela anterior ....

|year|employment_rate_female|employment_rate_male|
|---|---|---|
|2003|45.80|64.60|
|2004|48.70|66.60|
|2005|50.50|67.50|
|2006|49.70|68.90|
|2007|50.70|69.10|
|2008|51.19|68.56|
|2009|51.37|67.72|
|2010|51.22|67.62|
|2011|50.56|66.77|
|(...)|

...provavelmente você deve ter reconhecido que os dados do lote representam uma estatística de porcentagens anuais de emprego. Você deve ter notado que nesta estatística, esses valores estão em torno de 50 ou 60 pontos.

Além disso, os dados estão discriminados por sexo, ou seja, em vez de nos mostrar o nível de emprego total, são divididos em homens e mulheres. Você também notou alguma relação, em cada ano, entre esses dois valores?

> :mag: Vamos analisar os dados! Escreva o seguinte código em uma célula de caderno e com base nele responda quais afirmações são verdadeiras
>
> ```python
> emprego.plot.line(x="year")
> ```
