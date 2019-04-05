from rest_framework import serializers
from huey.contrib.djhuey import HUEY


class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=512)
    task_id = serializers.CharField(max_length=512, source='id')
    revoke_id = serializers.CharField(max_length=512)
    eta = serializers.DateTimeField()
    retries = serializers.IntegerField()
    retry_delay = serializers.IntegerField()
    result = serializers.SerializerMethodField()

    def get_result(self, obj):
        return HUEY.result(obj.id, preserve=True)


class TaskGroupSerializer(serializers.Serializer):
    tasks = TaskSerializer(many=True, source='__iter__')

    class Meta:
        lookup_field = 'task_group_id'
