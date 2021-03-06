from __future__ import print_function
import xmltodict
import ConfigParser

def load_xmlfile(xmlfile=''):
    '''
    read an xml file into a string, and return it.

    This function takes one parameter,

    * xmlfile is a full path to where the xml file is
    '''
    with open(xmlfile) as xmlhandle:
        xmldata = xmlhandle.read()

    return xmldata

def load_xmldata_as_python_obj(xmldata):
    '''
    parse an xml file as a Python dict object

    This function takes one parameter

    xmldata is a string that contains a valid xml structure
    '''
    xmlobj = xmltodict.parse(xmldata)

    return xmlobj

def process_xmldata(xmlfile=''):
    '''
    parse a servers.xml and return an easy manipulate python data structure.

    This function takes one parameter

    * xmlfile is a full path points to where servers.xml located

    Upon success, the function returns a nested dictionary structure like this,

    { cluster_id: {
          cluster_name: [
              { server_name: {
                   port: port number,
                   jenkins_job_name: jenkins job name,
                   jenkins_job_url: jenkins job url
              } }
          ]
    } }
    '''
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

