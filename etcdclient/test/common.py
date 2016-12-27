import sys
import random
import time

from service import Service
from cluster import Cluster
from app import App

def random_ip(subnet="192.168.0"):
    """
    Generate a random IP string in a subnet generating the two last parts 
    of address as random
    """
    return '{0}.{0}.{1}'.format(
            random.randint(0, 255),
            random.randint(0, 255))


def random_ports(count=3, privileged=False):
    """
    Returns an array of random ports
    """
    count = random.randint(1, count)
    ports = []

    if privileged:
        base = 1
    else:
        base = 1025

    for i in xrange(count):
        ports.append(random.randint(base, 65535))
    return ports


def build_services(cluster, template, count):
    """
    Use a template to build services in a cluster. The template can have value types
    that are functions returning values. 
    """
    # FIXME: better way to compare function type
    function_type = type(lambda: None)
    services = []
    for i in xrange(count):
        args = {
            'app': cluster.app
        }
        args.update(template)
        replacement = {}
        # Replace functions with their values
        for k, v in args.iteritems():
            if type(v) is function_type:
                replacement[k] = v()
        args.update(replacement)
        service = Service(**args)
        services.append(service)
    return services


def build_test_services(app):
    """
    Build a set of test services, use 'app' as the context
    """
    all_services = []

    # Generate the global cluster
    global_cluster = Cluster(
            app=app,
            name='global_test_cluster',
            min_count=1,
            max_count=3,
            partition_type='none',
            partition_key='none')

    global_template = {
        'name':'global_name',
        'service_class':'test_global_class',
        'cluster':global_cluster.name,
        'ip':random_ip,
        'ports':random_ports,
        'provides':['glob_svc_a', 'glob_svc_b'] }

    all_services += build_services(global_cluster, global_template, 3)

    regional_template = {
        'name':'regional_name',
        'service_class':'test_reg_class',
        'cluster':None,
        'ip':random_ip,
        'ports':random_ports,
        'provides':['reg_svc_a', 'reg_svc_b'] }

    site_template = {
        'name':'site_name',
        'service_class':'test_site_class',
        'cluster':None,
        'ip':random_ip,
        'ports':random_ports,
        'provides':['reg_svc_a', 'reg_svc_b'] }

   
    regional_clusters = []
    # Generate a few regions
    for region_name in ['region_a', 'region_b', 'region_c']:
        # Create new cluster instance
        regional_cluster = Cluster(
            app=app,
            name='regional_test_cluster',
            region=region_name,
            min_count=1,
            max_count=3,
            partition_type='key-space',
            partition_key='account_id')

        # Build regional services in cluster
        regional_template['region'] = region_name
        regional_template['cluster'] = regional_cluster.name
        all_services += build_services(regional_cluster, regional_template, 3)

        # Generate a few sites
        for site_name in ['main', 'secondary']:
            site_cluster = Cluster(
                    app=app,
                    name='site_test_cluster',
                    region=region_name,
                    site=site_name,
                    min_count = 1,
                    max_count = 3,
                    partition_type='none',
                    partition_key='none')

            site_template['region'] = region_name
            site_template['site'] = site_name
            site_template['cluster'] = site_cluster.name
            all_services += build_services(site_cluster, site_template, 3)
    
    print 'generated: {0} services'.format(len(all_services))
    return all_services


def run_services(services):
    while True:
        time.sleep(.1)
        for service in services:
            service.update()

def test_run_services(app):
    services = build_test_services(app)
    run_services(services)


