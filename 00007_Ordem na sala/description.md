Como você deve ter notado, ao agrupar obtemos uma `Series` com os valores agregados, mas fora de ordem (1, 879, 4, etc). No entanto, `groupby` ordena as colunas com base nos valores dos grupos (neste caso, em ordem alfabética: `Otro`, `Privado comercial`, `Privado comunitário`, etc):

```python
ム  cinemas.groupby("sector")["screens"].sum()
setor
Otros                      1
Privado comercial        879
Privado comunitário        4
Privado independente       8
(...etc...)
```

Felizmente, assim como os `DataFrame`s, as `Series` podem ser ordenadas usando `sort_values`:

```python
ム cinemas.groupby("sector")["screens"].sum().sort_values()
setor
Otros                      1
Privado comunitario        4
Privado independiente      8
Público provincial        11
Público nacional          14
Público municipal         57
Privado comercial        879
Name: screens, dtype: int64
```

:eyes: Note que embora `sort_values` retorne um `DataFrame` quando aplicado a um `DataFrame`, se aplicado a uma `Series`, retorna... outra `Séries`! Além disso, diferentemente de quando ordenamos um `DataFrame`, neste caso não precisamos especificar o nome da coluna que vamos ordenar. Afinal, agora estamos trabalhando com uma única coluna! 😛

> Agora é sua vez! Precisamos de um relatório com os **três** estados com a maior média de assentos, que fique aproximadamente assim:
>
> ```python
> province
> Santa Fe         590.0
> Rosario         1000.0
> San Juan        1050.0
> ```
>
> :warning: _(os valores do exemplo não estão necessariamente corretos)_
>
> Calcule este relatório usando o que você viu até agora e atribua a `estados_com_cinemas_grandes`.
>
