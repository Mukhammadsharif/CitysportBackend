from rest_framework import serializers
from .models import Pool, Billiard, Sauna, Training, Order, Subscription, Notification


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'


class BilliardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billiard
        fields = '__all__'


class SaunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauna
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class DateRangeField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        if value == 'day':
            return 1
        elif value == '7_days':
            return 7
        elif value == 'month':
            return 30
        else:
            return None


class SubscriptionSerializer(serializers.ModelSerializer):
    filter_by = DateRangeField(required=False, allow_null=True, )

    class Meta:
        model = Subscription
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['pool'] = PoolSerializer(instance.pool).data
        data['billiard'] = BilliardSerializer(instance.billiard).data
        data['sauna'] = SaunaSerializer(instance.sauna).data
        data['training'] = TrainingSerializer(instance.training).data
        return data


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
