class Test(unittest.TestCase):

  def test_assentos_per_localidade_é_um_DataFrame(self):
    self.assertEquals(type(assentos_per_localidade), pd.DataFrame)
    
  def test_gera_o_DataFrame_correto(self):
    indexadas = assentos_per_localidade.set_index("city")
    self.assertTrue(len(assentos_per_localidade) == 11, "debe tener el tamaño correcto")
    self.assertTrue(indexadas.loc["Bragado", "seats"] == 750, "Tiene la cantidad correcta de Bragado")
    self.assertTrue(indexadas.loc["Salta", "seats"] == 354, "Tiene la cantidad correcta de Salta")
    self.assertTrue(indexadas.loc["Pilar", "seats"] == 1407, "Tiene la cantidad correcta de Pilar")
    
  def test_genera_as_colunas_corretas(self):  
    self.assertEquals(set(assentos_per_localidade.columns), {'province', 'department', 'city', 'seats'})