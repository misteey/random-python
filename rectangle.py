def main():
  a = float(input("length = "))
  b = float(input("width = "))
  perimeter = 2 * (a + b)
  area = a * b
  diagonal = (a ** 2 + b ** 2) ** 0.5
  
  print(" length=", a, "\t width=", b)
  print(" area=", area, "\n perimeter=", perimeter)
  print(" diagonal= %.2f" % d)
main()
