
def orientation(s):
  o = s.get_orientation()
  x,y,z = [ o['pitch'],o['roll'],o['yaw'] ]
  print( 'X {} Y {} Z {}'.format( approx(x),approx(y),approx(z) ) )
def accelerometer(s):
  a = s.get_accelerometer_raw()
  x,y,z = [ a['x'],a['y'],a['z'] ]
  print( 'x {} y {} z {}'.format( approx(x),approx(y),approx(z) ) )
def approx(x):
  return round(x,2)

