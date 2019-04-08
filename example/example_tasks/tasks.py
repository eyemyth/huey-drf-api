from huey.contrib.djhuey import task


@task()
def echo_text(text, *args, **kwargs):
    return text
