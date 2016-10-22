def f(a,b):
   while b:
     print("before",a,b,a%b)
     a,b=b,a%b
     print("now",a,b)
   return a

# >>> f(357,234)
# ('before', 357, 234, 123)
# ('now', 234, 123)
# ('before', 234, 123, 111)
# ('now', 123, 111)
# ('before', 123, 111, 12)
# ('now', 111, 12)
# ('before', 111, 12, 3)
# ('now', 12, 3)
# ('before', 12, 3, 0)
# ('now', 3, 0)
# 3
