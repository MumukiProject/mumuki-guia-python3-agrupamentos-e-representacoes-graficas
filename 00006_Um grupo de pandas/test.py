class Test(unittest.TestCase):

  def test_telas_por_setor_é_um_series(self):
    self.assertEquals(type(telas_por_setor), pd.Series)
    
  def test_gera_o_series_correto(self):
    self.assertEquals(telas_por_setor.to_dict(), {
       'Privado comercial': 29,
       'Privado independiente': 1,
       'Público municipal': 2,
       'Público provincial': 1})