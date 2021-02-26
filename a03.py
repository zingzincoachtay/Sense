from time import sleep


def image(s):
  s.set_pixel(2, 2, (0, 0, 255))
  s.set_pixel(4, 2, (0, 0, 255))
  s.set_pixel(3, 4, (100, 0, 0))
  s.set_pixel(1, 5, (255, 0, 0))
  s.set_pixel(2, 6, (255, 0, 0))
  s.set_pixel(3, 6, (255, 0, 0))
  s.set_pixel(4, 6, (255, 0, 0))
  s.set_pixel(5, 5, (255, 0, 0))
  sleep(2)
def creeper(s):
  g = (0,255,0) # Green
  b = (0,0,0) # Black
  creeper = [
      g, g, g, g, g, g, g, g,
      g, g, g, g, g, g, g, g,
      g, b, b, g, g, b, b, g,
      g, b, b, g, g, b, b, g,
      g, g, g, b, b, g, g, g,
      g, g, b, b, b, b, g, g,
      g, g, b, b, b, b, g, g,
      g, g, b, g, g, b, g, g
  ]
  s.set_pixels(creeper)
  sleep(2)
def steve(s):
  B = (102, 51,  0)
  b = (  0,  0,255)
  S = (205,133, 63)
  W = (255,255,255)
  steve = [
      B, B, B, B, B, B, B, B,
      B, B, B, B, B, B, B, B,
      B, S, S, S, S, S, S, B,
      S, S, S, S, S, S, S, S,
      S, W, b, S, S, b, W, S,
      S, S, S, B, B, S, S, S,
      S, S, B, S, S, B, S, S,
      S, S, B, B, B, B, S, S
  ]
  s.set_pixels(steve)
  sleep(2)
def flippy(s):
  w = (150, 150, 150)
  b = (0, 0, 255)
  e = (0, 0, 0)
  image = [
      e, e, e, e, e, e, e, e, 
      e, e, e, e, e, e, e, e, 
      w, w, w, e, e, w, w, w, 
      w, w, b, e, e, w, w, b, 
      w, w, w, e, e, w, w, w, 
      e, e, e, e, e, e, e, e, 
      e, e, e, e, e, e, e, e, 
      e, e, e, e, e, e, e, e
  ]
  s.set_pixels(image)
  while True:
    sleep(1)
    s.flip_h()

