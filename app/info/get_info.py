# -* - coding: UTF-8 -* -
import ConfigParser
import yaml

def get_vepc_info(file_path):
    conf = ConfigParser.ConfigParser()
    conf.read(file_path)
    # for x in conf.sections():
    #     print x
    #     #print conf.options(x)
    #     print conf.items(x)
    return conf

def get_hot_info(file_path):
	with open(file_path) as f:
		x = yaml.load(f)
	print x 



if __name__ == '__main__':
    #get_vepc_info("vepc_flexible_communication_bsp_vsfo.cfg")
    get_hot_info("output/expected.yaml")
