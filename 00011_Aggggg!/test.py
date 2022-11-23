class Test(unittest.TestCase):

  def test_medianas_por_provincia_e_um_DataFrame(self):
    self.assertEquals(type(medianas_por_provincia), pd.DataFrame)
    
  def test_gera_o_DataFrame_corteto(self):
    indexados = medianas_por_provincia.set_index("province")
    self.assertTrue(len(medianas_por_provincia) == 5, "deve ter o tamanho correto")    
    self.assertTrue(indexados.loc["San Juan", "screens"] == 6, "deve ter o valor correto de telas para San Juan")
    self.assertTrue(indexados.loc["Buenos Aires", "seats"] == 750, "deve ter o valor correto de assentots para Buenos Aires")
    self.assertTrue(indexados.loc["Santa Fe", "seats"] == 584, "deve ter o valor correto de assentots para Santa Fe")
    
  def test_gera_as_colunas_corretas(self):  
    self.assertEquals(set(medianas_por_provincia.columns), {'province', 'screens', 'seats'})   
    

  def test_esta_ordenado_de_a_a_z(self):  
    self.assertTrue(medianas_por_provincia["province"].iloc[0] == "Buenos Aires", "o primeiro elemento deve ser Buenos Aires") 
    self.assertTrue(medianas_por_provincia["province"].iloc[1] == "Ciudad Autónoma de Buenos Aires", "Ciudad Autónoma de Buenos Aires deve estar depois da Buenos Aires")
    self.assertTrue(medianas_por_provincia["province"].iloc[2] == "Salta", "Salta deve estar depois da Ciudad Autónoma de Buenos Aires")
    self.assertTrue(medianas_por_provincia["province"].iloc[4] == "Santa Fe", "Santa Fe deve estar depois de Salta")
  