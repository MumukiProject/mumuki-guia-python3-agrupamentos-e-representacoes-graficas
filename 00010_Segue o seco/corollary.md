Às vezes, podemos evitar esse tipo de problemas se o dataset original tem algum tipo de código exclusivo para cada elemento sobre o qual desejamos agrupar. Por exemplo, neste dataset temos a coluna `loc_code` que nos dá, em teoria, um identificador numérico único para cada localidade. Por isso, também faria sentido construir a `assentos_por_localidade` assim:

```python
ム cinemas.groupby("loc_code", as_index=False)["seats"].sum()
```

||loc_code|seats|
|---|---|---|
|0|2000010|31386|
|1|6014010|250|
|2|6028010|3215|
|3|6035010|4805|
|4|6042010|385|
|...|...|...|

Ou se também quisermos preservar o nome da localidade:

```python
ム  cinemas.groupby(["loc_code", "city"], as_index=False)["seats"].sum()
```

||loc_code|city|seats|
|---|---|---|---|
|0|2000010|Ciudad Autónoma de Buenos Aires|31386|
|1|6014010|Gonzales Chaves|250|
|2|6028010|Adrogué|3215|
|3|6035010|Avellaneda|4805|
|4|6042010|Ayacucho|385|
|...|...|...|...|


