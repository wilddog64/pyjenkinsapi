import os
from jenkins import Jenkins
from datetime import datetime
from pprint import pprint
import urllib3
import json

# %% create jenkins-webapi object
urllib3.disable_warnings()
jenkins_user = os.environ['JENKINS_USER']
jenkins_pacific_url = os.environ['JENKINS_PACIFIC_URL']
jenkins_api_token = os.environ['JENKINS_API_TOKEN']
jenkins = Jenkins(jenkins_pacific_url, jenkins_user, jenkins_api_token, False)

# %% get a Batch view, and retrieve necessary job info
batchView = jenkins.view('Batch')
jobInfo = []
for job in batchView.jobs:
    ts = int(job.last_build.info['timestamp'] / 1000)
    timestamp = datetime.fromtimestamp(ts)
    jobTimeStamp = timestamp.astimezone().isoformat()
    jobStartTime = timestamp.strftime('%H:%M:%S %p')
    jobStartDate = timestamp.strftime('%Y-%M-%d')
    jobStatus = 'Enabled' if job.enabled else 'Disabled'
    jobHostname, = job.last_build.info['builtOn'].split('.')[0],
    jobDomain = '.'.join(job.last_build.info['builtOn'].split('.')[1:4])
    jobSelectedEnv = 'N/A'
    params = []
    if 'parameters' in job.last_build.info['actions'][0]:
        params = job.last_build.info['actions'][0]['parameters']
        for param in params:
            if 'in.runBatchRequest' in param['name']:
                s = param['value']
                jobSelectedEnv = s[s.rfind(':') + 2: len(s) - 2]
                break
    jobInfo.append({'TaskName': job.name,
                    'Task State': jobStatus,
                    'Task To Run': job.last_build.info['url'],
                    'Start time': jobStartTime,
                    'Start date': jobStartDate,
                    'Timestamp': jobTimeStamp,
                    'Hostname': jobHostname,
                    'Domain': jobDomain,
                    'Selected Environment': jobSelectedEnv,
                    })
pprint(jobInfo)


# %% define function to write json data to a file
def create_or_append_json_file(data, filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as fh:
            json.dump(data, fh, indent=2)
    else:
        with open(filename, 'a') as fh:
            json.dump(data, fh, indent=2)


# %% output job info as a json data to a file
for job in jobInfo:
    filename = '/mnt/c/temp/jenkins_batchconfig_{}.json'.format(job['Hostname'])
    create_or_append_json_file(job, filename)
