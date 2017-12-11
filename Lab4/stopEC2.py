#/usr/bin/python

import boto.ec2
# 1. Select your preffred Region
conn = boto.ec2.connect_to_region("eu-west-1")

# 2. Paste the instance_ids
conn.stop_instances(instance_ids=['i-xyz'])
