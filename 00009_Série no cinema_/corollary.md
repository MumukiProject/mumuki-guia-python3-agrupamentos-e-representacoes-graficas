E o que teria acontecido se precisássemos do número total de assentos por departamento? E por localidade (ou seja, cidade ou povoado)? Poderíamos fazer algo assim?

```python
# total de assentos por departamento?
cinemas.groupby("department", as_index=False)["seats"].sum()
# total de assentos por localidade?
cinemas.groupby("city", as_index=False)["seats"].sum()
```

:timer: Pare um momento para refletir sobre isso e nos vemos no próximo exercício.
