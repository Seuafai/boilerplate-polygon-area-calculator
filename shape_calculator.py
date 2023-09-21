class Rectangle:

  def __init__(self, width, height):
    self.width, self.height = width, height
      
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return((2 * self.width) + (2 * self.height))

  def get_diagonal(self):
    #print((self.width ** 2 + self.height ** 2) ** .5)
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return ("Too big for picture.")
    else:
      picstr = ""
      for row in range(self.height):
        picstr += "*" * self.width + "\n"
      return picstr

  """
  Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
  """
  def get_amount_inside(self):
    
    
    pass
    
#rect = Rectangle(10, 5)
#print(rect.get_picture())
#print(rect.get_diagonal())

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def set_side(self, length):
    self.width = length
    self.height = length




#sq = Square(9)
#print(sq.get_picture())
    
    
    

  
  