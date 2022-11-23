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
 
```python
cinemas.groupby("province", as_index=False).agg({
   "name": contar_centros_culturais
})
```

... onde em vez de passar uma string com o nome de uma agregação (como `"sum"` ou `"count"`), passamos a referência para uma função. Essas funções que o `agg` aceita devem receber uma lista com os valores das linhas de cada grupo e nelas podemos usar tudo o que sabemos sobre percursos, como variáveis, repetições e alternativas condicionais:

```python
def contar_centros_culturais(nomes):
  quantidade = 0
  for nome in nomes:
    if "centro cultural" in nome.lower():
      quantidade += 1
  return quantidade
```

Na verdade, podemos até usar compreensões de lista:

```python
def contar_centros_culturais(nomes):
 return len([nome for nome in nomes if "centro cultural" in nome.lower()])
```

> :first_place: Agora é sua vez! Construa uma tabela `proporcao_cinemas_comerciais_estatais` que contenha, para cada estado, a proporção entre 0 e 1 de cinemas de gestão `"Privado comercial"`, ordenada de acordo com esta proporção, do menor para o maior.
