import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def isclose_loose(a, b, rel_tol=1e-09):
	return abs(a-b) <= rel_tol

class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)


	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def plus(self, v):
		cs = [x + y for x, y in zip(self.coordinates, v.coordinates)]
		# for index in range(len(self.coordinates)):
		# 	cs.append(round(self.coordinates[index] + v.coordinates[index], 3))

		return Vector(cs)

	def minus(self, v):
		cs = [x - y for x, y in zip(self.coordinates, v.coordinates)]
		# for index in range(len(self.coordinates)):
		# 	cs.append(round(self.coordinates[index] - v.coordinates[index], 3))

		return Vector(cs)

	def sclar_multiply(self, sclar):
		cs = [sclar * x for x in self.coordinates]
		# for index in range(len(self.coordinates)):
		# 	cs.append(round(self.coordinates[index] * sclar, 3))

		return Vector(cs)

	def magnitude(self):
		cs = [x * x for x in self.coordinates]

		return sum(cs) ** 0.5

	def direction(self):
		m = self.magnitude()
		cs = [x / m for x in self.coordinates]
		return Vector(cs)

	def dot_product(self, v):
		cs = [x * y for x, y in zip(self.coordinates, v.coordinates)]
		return sum(cs)

	def angle_rad(self, v):
		return math.acos(self.dot_product(v)/(self.magnitude() * v.magnitude()))

	def angle(self, v):
		return self.angle_rad(v) * 180 / math.pi

	def is_zero_vector(self):
		for x in self.coordinates:
			if (x != 0):
				return False
		return True

	def is_parallel(self, v):
		if (len(self.coordinates) != len(v.coordinates)):
			return False

		if (self.is_zero_vector() or v.is_zero_vector()):
			return True

		if ((self.coordinates[0] == 0 and v.coordinates[0] != 0) or (self.coordinates[0] != 0 and v.coordinates[0] == 0)):
			return False

		sclar = self.coordinates[0] / v.coordinates[0]
		for index in range(len(self.coordinates)):
			if ((self.coordinates[index] == 0 and v.coordinates[index] != 0) or (self.coordinates[index] != 0 and v.coordinates[index] == 0)):
				return False

			if (not isclose(self.coordinates[index] / v.coordinates[index], sclar)):
				return False
		return True

	def is_orthogonal(self, v):
		return isclose_loose(self.dot_product(v), 0)

print Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111]))

print Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878]))

print Vector([1.671, -1.012, -0.318]).sclar_multiply(7.41)

print Vector([-0.221, 7.437]).magnitude()

print Vector([8.813, -1.331, -6.247]).magnitude()

print Vector([5.581, -2.136]).direction()

print Vector([1.996, 3.108, -4.554]).direction()

print Vector([7.887, 4.138]).dot_product(Vector([-8.802, 6.776]))

print Vector([-5.955, -4.904, -1.874]).dot_product(Vector([-4.496, -8.755, 7.103]))

print Vector([3.183, -7.627]).angle_rad(Vector([-2.668, 5.319]))

print Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985]))

print Vector([-7.579, -7.88]).is_parallel(Vector([22.737, 23.64]))

print Vector([-2.029, 9.97, 4.172]).is_parallel(Vector([-9.231, -6.639, -7.245]))

print Vector([-2.328, -7.284, -1.214]).is_parallel(Vector([-1.821, 1.072, -2.94]))

print Vector([2.118, 4.827]).is_parallel(Vector([0, 0]))

print Vector([-7.579, -7.88]).is_orthogonal(Vector([22.737, 23.64]))

print Vector([-2.029, 9.97, 4.172]).is_orthogonal(Vector([-9.231, -6.639, -7.245]))

print Vector([-2.328, -7.284, -1.214]).is_orthogonal(Vector([-1.821, 1.072, -2.94]))

# print Vector([-2.328, -7.284, -1.214]).dot_product(Vector([-1.821, 1.072, -2.94]))

print Vector([2.118, 4.827]).is_orthogonal(Vector([0, 0]))
