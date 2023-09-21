class Rectangle:

  def __init__(self, width, height):
    self.width, self.height = width, height
    self.rect = self.width, self.height
      
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return((2 * self.width) + (2 * self.height))

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
        return ("Too big for picture.")
    else:
      picstr = ""
      for row in range(self.height):
        picstr += "*" * self.width + "\n"
      return picstr

  def __repr__(self):
    pass

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def get_amount_inside(self, shape):
# want how many times the passed in shape can fit inside THIS shape
# want area of THIS shape divided by area of passed in shape.
    x = self.get_area()
    y = shape.get_area()

    if y > x:
        return 0  # Return 0 when y cannot fit into x
    if y == x:
      return 1
    else:
      return int(x / y)
      

  
class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length
    self.sq = self.width, self.height
    
  def set_side(self, length):
    self.length = length
    self.width = length
    self.height = length

  def __str__(self):
    return f"Square(side={self.width})"