from time import sleep

def transform(s):
  s.set_rotation(180)
  sleep(1)
  s.flip_h()
  sleep(1)
  s.flip_v()
  sleep(1)
  
