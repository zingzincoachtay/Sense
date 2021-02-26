from time import sleep

def letter(s):
  s.show_letter("N",text_colour=(88,0,0))
  sleep(2)
  s.clear( (127,127,127) )
  sleep(2)
  s.show_letter("Z",text_colour=(0,88,0))
  sleep(2)

