from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_TMP_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    return {'return':0}


