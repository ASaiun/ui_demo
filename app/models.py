from info.get_info import *

class Vepc(object):
	"""docstring for Vepc"""
	def __init__(self, file_path):
		conf = get_vepc_info(file_path)
		sections = conf.sections()
		self.vepc = {}
		for value_1 in sections:
			self.vepc[value_1] = conf.items(value_1)
			for index_2, value_2 in enumerate(self.vepc[value_1]):
				self.vepc[value_1][index_2] = list(self.vepc[value_1][index_2])
				self.vepc[value_1][index_2] = list(self.vepc[value_1][index_2])
				self.vepc[value_1][index_2].append(index_2)



	def get_vepc(self):
		# for value in self.vepc:
		# 	print value, self.vepc[value]
		return self.vepc


if __name__ == '__main__':
	
	vpec = Vepc("./info/vepc_flexible_communication_bsp_vsfo.cfg")
	vpec.get_vepc()

	# for x in vpec.vpec:
	# 	print x
