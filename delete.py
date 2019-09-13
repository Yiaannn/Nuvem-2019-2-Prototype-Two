import openstack

cloud= openstack.connect(cloud='envvars') #da documentacao, posso usar envvars para carregar a cloud das variaveis de ambiente

instance= cloud.compute.find_server('openstacksdk test', ignore_missing=False)

cloud.compute.delete_server(instance, ignore_missing=False)
