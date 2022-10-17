class Test(unittest.TestCase):

  def test_estados_com_cinemas_grandes_é_um_series(self):
    self.assertEquals(type(estados_com_cinemas_grandes), pd.Series)
    
  def test_genera_el_series_correcto(self):
    self.assertEquals(estados_com_cinemas_grandes.to_dict(), {
        'Santa Fe': 584.0, 'Buenos Aires': 1036.0, 'San Juan': 1071.0
    })