from datetime import datetime
import json
import os


# %% define function to write json data to a file
def create_or_append_json_file(data, filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as fh:
            json.dump(data, fh, indent=2)
    else:
        with open(filename, 'a') as fh:
            json.dump(data, fh, indent=2)


def create_json_structure(jenkinsView):
    jobInfo = []
    for job in jenkinsView.jobs:
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

    return jobInfo


def generate_job_report(jenkinsView, filenameTmpl='/mnt/c/temp/jenkins_batchconfig_{}.json'):
    jobInfo = create_json_structure(jenkinsView)
    if 'JSON_FILEPATH_TMPL' in os.environ:
        filenameTmpl = os.environ['JENKINS_JSON_FILEPATH_TMPL']

    for job in jobInfo:
        filename = filenameTmpl.format(job['Hostname'])
        print('create a report at {}'.format(filename))
        create_or_append_json_file(job, filename)
