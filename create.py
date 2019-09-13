import openstack

cloud= openstack.connect(cloud='envvars') #da documentacao, posso usar envvars para carregar a cloud das variaveis de ambiente

image= cloud.compute.find_image('bionic', ignore_missing=False)
flavor= cloud.compute.find_flavor('m1.tiny', ignore_missing=False)
network= cloud.network.find_network('internal', ignore_missing=False)
keypair= cloud.compute.find_keypair('openstack_key', ignore_missing=False)

server= cloud.compute.create_server(
    name='openstacksdk test', image_id= image.id, flavor_id= flavor.id,
    networks=[{'uuid': network.id}], key_name=keypair.name)

server= cloud.compute.wait_for_server(server)
