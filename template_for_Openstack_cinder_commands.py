#!/usr/bin/env python

import os

OS_PASSWORD=os.environ["OS_PASSWORD"]
OS_AUTH_URL=os.environ["OS_AUTH_URL"]
OS_USERNAME=os.environ["OS_USERNAME"]
OS_TENANT_NAME=os.environ["OS_TENANT_NAME"]


from cinderclient import client
from cinderclient import base
from novaclient import client


cinder = client.Client('2', OS_USERNAME,OS_PASSWORD, OS_TENANT_NAME, OS_AUTH_URL)
nova = client.Client('3', OS_USERNAME,OS_PASSWORD, OS_TENANT_NAME, OS_AUTH_URL)   



# find the image 
image = nova.images.find(name="RHEL65")
image1 = nova.images.find(name="cirros")

# get the flavor
flavor = nova.flavors.find(name="m1.large")

# get the network and attach
network = nova.networks.find(label="private")
nics = [{'net-id': network.id}]


def createInstance():
    newins = nova.servers.create(name='Automation', image=image1.id, flavor=flavor.id, nics=nics)


# find instance "Automation" 
try:
    instance = nova.servers.find(name="Automation")
except:
    createInstance()


def getVolumes():
    print "\n Your volumes are \n"
    for i in cinder.volumes.list():
        print (i)


def createVolume(number):
    for i in range(number):
        volume = cinder.volumes.create(size=8,volume_type='scaleio')
        print volume.id
    

def deleteVolume():
    for i in cinder.volumes.list():
        print i.id
        cinder.volumes.delete(i)


def getInstance():
    print "\n Your instances are \n"
    for i in nova.servers.list():
        print i

def getImages():
    print nova.images.list()


def getVolumeTypes():
    print nova.volume_types.list()

def attachVolumes():
    for i,j in zip(cinder.volumes.list(),['c','d','e','f','g','h','i','j','k','l']):
        nova.volumes.create_server_volume(instance.id,i.id,'/dev/vd'+j)

def detachVolumes():
    for i in cinder.volumes.list():
        nova.volumes.delete_server_volume(instance.id,i.id)


def createVolumeType(name):
    nova.volume_types.create(name)


def createExtraSpec():
    y = cinder.volume_types.get_keys('Scaleio-Automation')
    print y   


#getVolumes()
#createVolume(10)
#deleteVolume()
#getVolumes()
#getInstance()
#getImages()
#createInstance()
#getVolumeTypes()
#attachVolumes()
#detachVolumes()
#createVolumeType('Scaleio-Automation')
createExtraSpec()
