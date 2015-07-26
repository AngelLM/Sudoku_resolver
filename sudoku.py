class Box:
	def __init__(self, n, x, y):
		self.n = n
		self.x = x
		self.y = y
		self.chance=[]

	def len_chance(self,c):
		len(chance)

	def check_chance(self,c):
		c in self.chance

	def write_chance(self,c):
		self.chance.append(c)

	def remove_chance(self,c):
		self.chance.remove(c)

	def write_num(self,num):
		self.n=num

class Row:
	def __init__(self,a,b,c,d,e,f,g,h,i):
		boxes=[a,b,c,d,e,f,g,h,i]

	def 


class Sudoku:
	def __init__(self):
		a1=Box(a1,0,0)
		a2=Box(a2,1,0)
		a3=Box(a3,2,0)
		a4=Box(a4,0,1)
		a5=Box(a5,1,1)
		a6=Box(a6,2,1)
		a7=Box(a7,0,2)
		a8=Box(a8,1,2)
		a9=Box(a9,2,2)

		b1=Box(b1,3,0)
		b2=Box(b2,4,0)
		b3=Box(b3,5,0)
		b4=Box(b4,3,1)
		b5=Box(b5,4,1)
		b6=Box(b6,5,1)
		b7=Box(b7,3,2)
		b8=Box(b8,4,2)
		b9=Box(b9,5,2)

		c1=Box(c1,6,0)
		c2=Box(c2,7,0)
		c3=Box(c3,8,0)
		c4=Box(c4,6,1)
		c5=Box(c5,7,1)
		c6=Box(c6,8,1)
		c7=Box(c7,6,2)
		c8=Box(c8,7,2)
		c9=Box(c9,8,2)

		d1=Box(d1,0,3)
		d2=Box(d2,1,3)
		d3=Box(d3,2,3)
		d4=Box(d4,0,4)
		d5=Box(d5,1,4)
		d6=Box(d6,2,4)
		d7=Box(d7,0,5)
		d8=Box(d8,1,5)
		d9=Box(d9,2,5)

		e1=Box(e1,3,3)
		e2=Box(e2,4,3)
		e3=Box(e3,5,3)
		e4=Box(e4,3,4)
		e5=Box(e5,4,4)
		e6=Box(e6,5,4)
		e7=Box(e7,3,5)
		e8=Box(e8,4,5)
		e9=Box(e9,5,5)

		f1=Box(f1,6,3)
		f2=Box(f2,7,3)
		f3=Box(f3,8,3)
		f4=Box(f4,6,4)
		f5=Box(f5,7,4)
		f6=Box(f6,8,4)
		f7=Box(f7,6,5)
		f8=Box(f8,7,5)
		f9=Box(f9,8,5)

		g1=Box(g1,0,6)
		g2=Box(g2,1,6)
		g3=Box(g3,2,6)
		g4=Box(g4,0,7)
		g5=Box(g5,1,7)
		g6=Box(g6,2,7)
		g7=Box(g7,0,8)
		g8=Box(g8,1,8)
		g9=Box(g9,2,8)

		h1=Box(h1,3,6)
		h2=Box(h2,4,6)
		h3=Box(h3,5,6)
		h4=Box(h4,3,7)
		h5=Box(h5,4,7)
		h6=Box(h6,5,7)
		h7=Box(h7,3,8)
		h8=Box(h8,4,8)
		h9=Box(h9,5,8)

		i1=Box(i1,6,6)
		i2=Box(i2,7,6)
		i3=Box(i3,8,6)
		i4=Box(i4,6,7)
		i5=Box(i5,7,7)
		i6=Box(i6,8,7)
		i7=Box(i7,6,8)
		i8=Box(i8,7,8)
		i9=Box(i9,8,8)

		row1=[a1,a2,a3,b1,b2,b3,c1,c2,c3]
		row2=[a4,a5,a6,b4,b5,b6,c4,c5,c6]
		row3=[a7,a8,a9,b7,b8,b9,c7,c8,c9]
		row4=[d1,d2,d3,e1,e2,e3,f1,f2,f3]
		row5=[d4,d5,d6,e4,e5,e6,f4,f5,f6]
		row6=[d7,d8,d9,e7,e8,e9,f7,f8,f9]
		row7=[g1,g2,g3,h1,h2,h3,i1,i2,i3]
		row8=[g4,g5,g6,h4,h5,h6,i4,i5,i6]
		row9=[g7,g8,g9,h7,h8,h9,i7,i8,i9]

		col1=[a1,a4,a7,d1,d4,d7,g1,g4,g7]
		col2=[a2,a5,a8,d2,d5,d8,g2,g5,g8]
		col3=[a3,a6,a9,d3,d6,d9,g3,g6,g9]
		col4=[b1,b4,b7,e1,e4,e7,h1,h4,h7]
		col5=[b2,b5,b8,e2,e5,e8,h2,h5,h8]
		col6=[b3,b6,b9,e3,e6,e9,h3,h6,h9]
		col7=[c1,c4,c7,f1,f4,f7,i1,i4,i7]
		col8=[c2,c5,c8,f2,f5,f8,i2,i5,i8]
		col9=[c3,c6,c9,f3,f6,f9,i3,i6,i9]

		squ1=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
		squ2=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
		squ3=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
		squ4=[d1,d2,d3,d4,d5,d6,d7,d8,d9]
		squ5=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
		squ6=[f1,f2,f3,f4,f5,f6,f7,f8,f9]
		squ7=[g1,g2,g3,g4,g5,g6,g7,g8,g9]
		squ8=[h1,h2,h3,h4,h5,h6,h7,h8,h9]
		squ9=[i1,i2,i3,i4,i5,i6,i7,i8,i9]


