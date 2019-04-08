from rest_framework import serializers
from huey.contrib.djhuey import HUEY


class TaskSerializer(serializers.Serializer):
    name = serializers.CharField()
    args = serializers.ListField(child=serializers.CharField())
    kwargs = serializers.DictField()
    task_id = serializers.CharField(source='id')
    revoke_id = serializers.CharField()
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
