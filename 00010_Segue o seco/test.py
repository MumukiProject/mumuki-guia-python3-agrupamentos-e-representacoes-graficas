class Test(unittest.TestCase):

  def test_assentos_per_localidade_é_um_DataFrame(self):
    self.assertEquals(type(assentos_per_localidade), pd.DataFrame)
    
  def test_gera_o_DataFrame_correto(self):
    indexadas = assentos_per_localidade.set_index("city")
    self.assertTrue(len(assentos_per_localidade) == 11, "deve ser do tamanho correto")
    self.assertTrue(indexadas.loc["Bragado", "seats"] == 750, "Bragado deve ter a quantidade correta")
    self.assertTrue(indexadas.loc["Salta", "seats"] == 354, "Salta deve ter a quantidade correta")
    self.assertTrue(indexadas.loc["Pilar", "seats"] == 1407, "Pilar deve ter a quantidade correta")

  def test_tem_duas_cidades_colon(self):
    assert len(assentos_per_localidade[assentos_per_localidade["city"]== "Colón"]) == 2, "deve ter duas cidades Colón"
  
    
  def test_genera_as_colunas_corretas(self):  
    self.assertEquals(set(assentos_per_localidade.columns), {'province', 'department', 'city', 'seats'})