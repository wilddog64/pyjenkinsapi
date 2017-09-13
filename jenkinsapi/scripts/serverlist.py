from __future__ import print_function
from jenkinsapi.ParseServerList import process_xmldata

def generate_inventory_file(data):
    title = ''
    inventory_file = './inventory'
    titles = list()
    inventory_filehandle = None
    with open(inventory_file, 'w+') as inventory_filehandle:
        for cluster_id, clusters in data.items():
            for cluster, servers in clusters.items():
                if 'SaaS' in cluster:
                    title = '[learn-saas-%s]' % cluster_id
                    t = 'learn-saas-%s' % cluster_id
                else:
                    title = '[learn-%s]' % cluster_id
                    t = 'learn-%s' % cluster_id
                inventory_filehandle.write("%s\n" % title)
                titles.append(t)
                for server in servers:
                    for server_name, server_info in server.items():
                        line = "%s\n" % server_name
                        inventory_filehandle.write(line)
            inventory_filehandle.write("\n")

        inventory_filehandle.write('[learn:children]\n')
        for title in sorted(titles):
            inventory_filehandle.write("%s\n" % title)
        inventory_filehandle.write("\n")

        # write out [learn:vars]
        inventory_filehandle.write("[learn:vars]\n")
        inventory_filehandle.write("ansible_user=root\n")
        inventory_filehandle.write("\n")

def main():
    data = process_xmldata('/Users/cliang/src/gitrepo/blackboard/jenkins/learn-server-status/src/main/resources/servers.xml')
    return data

if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=2)

    data = main()
    generate_inventory_file(data)
    pp.pprint(data)
