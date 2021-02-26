
#event.direction,event.action
#('up','pressed')
#('up','released')
#('down','pressed')
#('down','released')
#('left','pressed')
#('left','released')
#('right','pressed')
#('right','released')
#('middle','pressed')
#('middle','released')
def
  while True:
      for e in s.stick.get_events():
          print(e.timestamp,e.direction,e.action)
#another useful class: s.stick.direction_any
#s.stick.direction_up 
#s.stick.direction_down 
#s.stick.direction_left 
#s.stick.direction_right 
#s.stick.direction_middle 
## This keeps the program running to receive joystick events
#while True:
#  pass

