from huey.contrib.djhuey import task


@task()
def echo_text(text):
    return text
