class Test(unittest.TestCase):

  def test_assentos_por_estado_é_um_series(self):
    self.assertEquals(type(assentos_por_estado), pd.DataFrame)
    
  def test_gera_o_series_correto(self):
    self.assertEquals(assentos_por_estado.to_dict("records"), [
         {'province': 'Buenos Aires', 'seats': 5180},
         {'province': 'Ciudad Autónoma de Buenos Aires', 'seats': 306},
         {'province': 'Salta', 'seats': 354},
         {'province': 'San Juan', 'seats': 1071},
         {'province': 'Santa Fe', 'seats': 584}])