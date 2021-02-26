
def environment(s):
  fontcolour = (127,127,127)
  p, h = [s.get_pressure(), s.get_humidity()]
  t = [s.get_temperature_from_humidity(),s.get_temperature_from_pressure()]
  message = 'Ambient Condition'
  t0 = C2F(t[0])
  t1 = C2F(t[1])
  message1 = 'P {}mb H {}%'.format( approx(p),approx(h) )
  message2 = 'Tp {} Th {}'.format( approx(t0),approx(t1) )
  #s.show_message(message1,text_colour=fontcolour,scroll_speed=0.1)
  print(message1)
  #s.show_message(message2,text_colour=fontcolour,scroll_speed=0.1)
  print(message2)
def C2F(x):
  return x*(9/5)+32
def approx(x):
  return round(x,2)

