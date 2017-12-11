import boto.ec2

# before you run this script fill the parameters highlited by comments

# 1. Select your preffered Region (ex. eu-west-1).
conn = boto.ec2.connect_to_region("eu-west-1")
conn.run_instances(
# 2. Set up proper image id (this one is amazon ami from eu-west-1)
    'ami-1a962263',
# 3. ssh key name
    key_name='your_key_name',
    instance_type='t2.micro',
# 4. Security group name for your EC2

    security_groups=['Security_Group_name']
)
