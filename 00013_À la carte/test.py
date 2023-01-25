class Test(unittest.TestCase):

  def test_proporcao_cinemas_comerciais_provinciais_é_um_DataFrame(self):
    self.assertEquals(type(proporcao_cinemas_comerciais_provinciais), pd.DataFrame)
    
  def test_gera_o_DataFrame_correto(self):
    indexados = proporcao_cinemas_comerciais_provinciais.set_index("province")
    self.assertTrue(len(proporcao_cinemas_comerciais_provinciais) == 5, "deve ser do tamanho correto")    
    self.assertTrue(indexados.loc["San Juan", "sector"] == 1, "deve ter o valor correto para San Juan")
    self.assertTrue(indexados.loc["Buenos Aires", "sector"] == 0.8, "deve ter o valor correto para Buenos Aires")
    self.assertTrue(indexados.loc["Santa Fe", "sector"] == 1, "deve ter o valor correto para Santa Fe")
    
  def test_gera_as_colunas_corretas(self):  
    self.assertEquals(list(proporcao_cinemas_comerciais_provinciais.columns), ['province', 'sector'])   

  def test_esta_ordenado_do_menor_para_o_maior(self):  
    self.assertTrue(proporcao_cinemas_comerciais_provinciais["sector"].iloc[0] == 0, "o primeiro elemento deve ser o mínimo")   
  