from huey.contrib.djhuey import task


@task()
def add_one(num):
    return num + 1
