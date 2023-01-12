Infelizmente, nem sempre teremos informações no formato preciso em que precisamos 🤷. Para compreender melhor em tabelas ou graficamente, geralmente utilizaremos um lote de dados que _mais ou menos_ se ajuste ao que estamos procurando e depois o adaptamos às nossas necessidades. :person_juggling:.
 
Por exemplo, se estamos estudando a distribuição, o tipo de gestão (pública ou privada) dos cinemas na Argentina  :movie_camera:, provavelmente não encontraremos um lote de dados que contenha exatamente essa informação, mas algo assim com o qual já trabalhamos anteriormente:
 
```python
cinemas = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=969960562&single=true&output=csv")
cinemas.head(5)
```
 
||(..)|province|department|city|name|(..)|sector|screens|seats|update_year|
|---|---|---|---|---|---|---|---|---|---|---|
|0|(..)|Catamarca|Capital|Catamarca|Cinemacenter|(..)|Privado comercial|5|743|2018|
|1|(..)|Catamarca|Santa Maria|Santa María|Centro Cultural San Agustín|(..)|Privado comercial|1|440|2018|
|2|(..)|Chaco|San Fernando|Resistencia|Los Cines De La Costa|(..)|Privado comercial|5|820|2018|
|3|(..)|Chubut|Sarmiento|Sarmiento|Deborah Jones De Williams|(..)|Público municipal|1|80|2018|
|4|(..)|Corrientes|Bella Vista|Bella Vista|Fantasio|(..)|Privado comercial|1|240|2018|

Mas como seria nossa tabela ideal? 🤔 Deveria ter duas colunas...
 
 * o tipo de gestão (`sector`): uma coluna categórica (público estatal, público municipal, privado comercial, etc.)
 * o número de telas de cinema de cada gestão (`screens`): uma coluna numérica com cada um dos totais de telas.

... e fique mais ou menos assim:
 
||sector|screens|
|---|---|---|
|0|Privado comercial|879|
|1|Público municipal|57|
|2|Público nacional|14|
|3|Público provincial|11|
|4|Privado independiente|8|
|5|Privado comunitario|4|
|6|Otros|1|
 
 
> Carregue a tabela anterior em seu caderno e observe-a com atenção 🔎. É possível construir esta tabela usando **somente** o que vimos até agora?
