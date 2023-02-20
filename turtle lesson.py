Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.forward(100)
tao.left(50)
tao.forword(50)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tao.forword(50)
AttributeError: 'Turtle' object has no attribute 'forword'. Did you mean: 'forward'?
tao.forward(50)
tao.right(90)

tao.forward(50)
tao.left(50)
tao.forward(100)
tao.reset()
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.clear()
for i in range(4):
    tao.forward(50)
    tao.left(90)

    
tao.penup()
tao.goto(0,50)
tao.goto(0,-50)
tao.goto(0,0)
tao.goto(50,0)
tao.pendown
<bound method TPen.pendown of <turtle.Turtle object at 0x10f6d03d0>>
tao.pendown()
tao.left(45)
tao.forward(50)
tao.right(45)
for i in range(4):
    tao.forward(50)
    tao.left(90)

    
tao.penup()
tao.goto(50,50)
tao.pendown()
tao.left(45)
tao.forward(50)
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.right(90)
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.penup()
tao.goto(0,50)
tao.right(90)
tao.right(90)
tao.pendown()
tao.forward(50)
tao.right(45)
for i in range(4):
    tao.forward(50)
    tao.left(90)

    
tao.forward(100)
tao.left(45)
tao.forward(50)
tao.left(45)
tao.penup
<bound method TPen.penup of <turtle.Turtle object at 0x10f6d03d0>>
tao.penup()
tao.goto(0,50)
tao.right(45)
tao.forward(50)
tao.left(45)
tao.forward(50)
tao.right(45)
tao.pendown()
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.right(90)
tao.forward(50)
tao.right(45)
tao.penup()
tao.forward(50)
tao.right(180)
tao.left(45)
tao.forward(50)
tao.right(45)
tao.pendown()
tao.forward(50)
tao.penup()
tao.home()
tao.color("black" , "red")
tao.pu()
tao.goto(-100,-100)
tao.pd()
tao.begin_fill()
tao.circle(50)
tao.end_fill()
tao.color("white" , "white")
tao.begin_fill()
tao.circle(50)
tao.end_fill()
tao.begin_fill()
tao.circle(80)
tao.end_fill()
tao.color("blacl","black")
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    tao.color("blacl","black")
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2217, in color
    pcolor = self._colorstr(pcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: blacl
tao.color("black","black")

tao.pu()
tao.home()
tao.home()
tao.goto(-100,-100)
tao.left(45)
tao.forward(50)
tao.left.(45)
SyntaxError: invalid syntax
tao.left(45)
tao.forward(50)
tao.left(135)
tao.forward(100)
tao.left(135)
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)

    
tao.pd()
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)

    
tao.right(180)
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)

tao.left(90)
tao.pu()
tao.home()
tao.forward(50)
tao.color("black, "black")
          
SyntaxError: unterminated string literal (detected at line 1)
tao.color("black", "black")
          
tao.begin_fill()
          
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(90)

          
tao.end_fill()
          
tao.pu()
          
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)

          
tao.right(90)
          
tao.pd()
          
tao.begin_fill()
          
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(90)

          
tao.end_fill()
          
for i in range (1):
          tao.forward(50)
          tao.right(90)
          tao.forward(50)
          tao.left(90)

          
tao.begin_fill()
          
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(90)


tao.end_fill()
          
tao.pu()
          
tao.home()
          
tao.color("black" , "red")
          
tao.begin_fill()
          
for i in range(4):
    tao.forward(50)
    tao.left(90)

          
tao.end_fill()
          
tao.color("blacl", " blue")
          
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    tao.color("blacl", " blue")
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2217, in color
    pcolor = self._colorstr(pcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: blacl
tao.color("black", " blue")
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    tao.color("black", " blue")
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2218, in color
    fcolor = self._colorstr(fcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string:  blue
tao.color("black" , "blue")
tao.pu()
tao.left(90)
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.right(45)
tao.begin_fill()
for i in range (4):
    tao.forward(50)
    tao.left(90)

    
tao.end_fill()
tao.pu()
tao.forward(50)
tao.right(90)
tao.forward(50)
tao.left(90)]
SyntaxError: unmatched ']'
tao.left(90)
tao.color("black" , "yellow")
tao.pd()
tao.begin_fill()
for i in range (4):
    tao.forward(50)
    tao.left(90)

    
tao.end_fill()
tao.pu()
tao.goto(0,-200)
tao.goto(-200,0)
tao.color("white" , "white")
tao.pd()
tao.begin_fill()
for i in range (4):
    tao.forward(200)
    tao.right(90)

    
tao.end_fill()
tao.color("black","white")
tao.home()
tao.color("white","white")
tao.backward(200)
tao.color("black" , "white")
tao.pu()
tao.home()
tao.left(90)
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.left(45)
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.right(45)
tao.color("black" , "green")
tao.begin_fill()
for i in range (4):
    tao.forward(50)
    tao.left(90)

    
tao.end_fill()
tao.pu()
tao.forward(50)
tao.right(90)
tao.forward(50)
tao.left(90)
tao.color("black","margenta")
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    tao.color("black","margenta")
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2218, in color
    fcolor = self._colorstr(fcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: margenta
tao.color("black","purple")
tao.color("black","orange")
tao.pd()
tao.begin_fill()
for i in range(4):
    tao.forward(50)
    tao.left(90)

    
tao.end_fill()
tao.forward(50)
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(90)

    
tao.color("blacl","black")
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    tao.color("blacl","black")
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2217, in color
    pcolor = self._colorstr(pcolor)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/turtle.py", line 1159, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: blacl
tao.color("black","black")
tao.begin_fill()
for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(90)

    
tao.end_fill()
tao.pu()
tao.left(90)
tao.forward(50)
tao.left(90)
tao.forward(50)
tao.right(180)
tao.begin_fill()

for i in range (1):
    tao.left(45)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(135)
    tao.forward(50)
    tao.left(45)
    tao.forward(50)
    tao.left(90)

    
tao.end_fill()
tao.pd()
tao.left(90)
tao.color("black","white")
for i in range (4):
    tao.forward(50)
    tao.left(90)

    
tao.forward(50)
tao.left(90)
tao.forward(50)
tao.right(135)
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.right(90)
tao.forward(50)
tao.left(90)
toa.forward(50)
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    toa.forward(50)
NameError: name 'toa' is not defined
tao.forward(50)
tao.pu()
tao.right(90)
tao.forward?(?50)
SyntaxError: invalid syntax
tao.forward(50)
tao.right(45)
tao.forward(50)
tao.left(45)
tao.forward(50)
tao.left(90)
tao.pd()
for i in range(4):
    tao.forward(50)
    tao.left(90)

...     
>>> tao.color("black","purple")
>>> tao.begin_fill()
>>> for i in range(4):
...     tao.forward(50)
...     tao.left(90)
... 
...     
>>> tao.end_fill()
>>> tao.pu()
>>> tao.forward(50)
>>> tao.color("black","black")
>>> tao.begin_fill()
>>> for i in range (1):
...     tao.left(45)
...     tao.forward(50)
...     tao.left(45)
...     tao.forward(50)
...     tao.left(135)
...     tao.forward(50)
...     tao.left(45)
...     tao.forward(50)
...     tao.left(90)
... 
...     
>>> tao.end_fill()
>>> tao.left(45)
>>> tai.forward(50)
Traceback (most recent call last):
  File "<pyshell#324>", line 1, in <module>
    tai.forward(50)
NameError: name 'tai' is not defined. Did you mean: 'tao'?
>>> tao.forward(50)
>>> tao.left(45)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.forward(50)
>>> tao.pd()
>>> tao.backward(50)
>>> tao.pu()
>>> tao.home()
>>> tao.bgcolor("gray")
Traceback (most recent call last):
  File "<pyshell#334>", line 1, in <module>
    tao.bgcolor("gray")
AttributeError: 'Turtle' object has no attribute 'bgcolor'. Did you mean: '_color'?
>>> turtle.bgcolor("gray")
>>> turtle.bgcolor("white")
