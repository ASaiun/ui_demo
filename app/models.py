from info.get_info import *

class Vepc(object):
	"""docstring for Vepc"""
	def __init__(self, file_path):
		conf = get_vepc_info(file_path)
		sections = conf.sections()
		self.vepc = {}
		for x in sections:
			self.vepc[x] = conf.items(x)

	def get_vepc(self):
		for x in self.vepc:
			print x, self.vepc[x]
		return self.vepc


if __name__ == '__main__':
	
	vpec = Vepc("./info/vepc_flexible_communication_bsp_vsfo.cfg")
	vpec.get_vepc()

	# for x in vpec.vpec:
	# 	print x
