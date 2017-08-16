from __future__ import print_function
import xmltodict
import ConfigParser

def load_xmlfile(xmlfile=''):
    with open(xmlfile) as xmlhandle:
        xmldata = xmlhandle.read()

    return xmldata

def load_xmldata_as_python_obj(xmldata):
    xmlobj = xmltodict.parse(xmldata)

    return xmlobj

def process_data(xmlfile=''):
    xmldata = load_xmlfile(xmlfile)
    xmlobj = load_xmldata_as_python_obj(xmldata)

    servers = xmlobj['root']['servers']
    data = {}
    jenkins_job_url = ''
    jenkins_job_name = ''
    for cluster in servers:
        cluster_id = cluster['@name']
        cluster_name = cluster['@title']
        data[cluster_id] = {}
        data[cluster_id][cluster_name] = list()
        for server in cluster['server']:
            server_name = server['name']
            server_port = 80
            server_name = server_name[0:server_name.index(':')] \
                    if ':' in server_name else server_name
            if 'jenkins_job' in server:
                jenkins_job_url = server['jenkins_job']
                jenkins_job_name = jenkins_job_url[jenkins_job_url.rindex('/') + 1:len(jenkins_job_url)]
            hash_table = {server_name: {'port': server_port, 'jenkins_job_name': jenkins_job_name, 'jenkins_job_url': jenkins_job_url}}
            data[cluster_id][cluster_name].append(hash_table)
    return data

def generate_inventory_file(data):
    title = ''
    inventory_file = './inventory'
    titles = list()
    inventory_filehandle = None
    with open(inventory_file, 'w+') as inventory_filehandle:
        for cluster_id, clusters in data.items():
            title = '[learn-%s]' % cluster_id
            titles.append('learn-%s' % cluster_id)
            inventory_filehandle.write("%s\n" % title)
            for cluster, servers in clusters.items():
                for server in servers:
                    for server_name, server_info in server.items():
                        line = "%s\n" % server_name
                        inventory_filehandle.write(line)
            inventory_filehandle.write("\n")

        inventory_filehandle.write('[learn:children]\n')
        for title in titles:
            inventory_filehandle.write("%s\n" % title)
        inventory_filehandle.write("\n")

        # write out [learn:vars]
        inventory_filehandle.write("[learn:vars]\n")
        inventory_filehandle.write("ansible_user=root\n")
        inventory_filehandle.write("\n")

def main():
    data = process_data('/Users/cliang/src/gitrepo/blackboard/jenkins/learn-server-status/src/main/resources/servers.xml')
    return data

if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=2)

    data = main()
    generate_inventory_file(data)
    pp.pprint(data)
