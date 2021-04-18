# import required module
import os
import yaml

# assign directory
directory = './job/'

# itrate over files in
# that directory
for filename in os.listdir(directory) :
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isdir(f):
        for config in os.listdir(f):
            if config.__contains__(".yml"):
                get_job = "%s/%s" % (f,config)
                print( get_job)
                with open(get_job) as file:
                    documents = yaml.full_load(file)

                print(documents['command'])
