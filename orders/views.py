from django.db.models import Q
from django.utils import timezone
from datetime import timedelta, date

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pool, Billiard, Sauna, Training, Order, Subscription, Notification
from .serializers import PoolSerializer, BilliardSerializer, SaunaSerializer, TrainingSerializer, OrderSerializer, \
    SubscriptionSerializer, NotificationSerializer


@api_view(['GET', 'POST'])
def pool_list(request):
    if request.method == 'GET':
        pools = Pool.objects.all()

        # Filter by day
        day = request.query_params.get('day')
        if day:
            pools = pools.filter(created_at__date=day)

        # Filter by 7 days
        seven_days = request.query_params.get('seven_days')
        if seven_days:
            start_date = timezone.now().date() - timedelta(days=7)
            pools = pools.filter(created_at__date__gte=start_date)

        # Filter by month
        month = request.query_params.get('month')
        if month:
            pools = pools.filter(created_at__month=month)

        serializer = PoolSerializer(pools, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def pool_detail(request, pk):
    try:
        pool = Pool.objects.get(pk=pk)
    except Pool.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PoolSerializer(pool)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PoolSerializer(pool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        pool.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def billiard_list(request):
    if request.method == 'GET':
        billiards = Billiard.objects.all()

        # Filter by day
        day = request.query_params.get('day')
        if day:
            billiards = billiards.filter(created_at__date=day)

        # Filter by 7 days
        seven_days = request.query_params.get('seven_days')
        if seven_days:
            start_date = timezone.now().date() - timedelta(days=7)
            billiards = billiards.filter(created_at__date__gte=start_date)

        # Filter by month
        month = request.query_params.get('month')
        if month:
            billiards = billiards.filter(created_at__month=month)

        serializer = BilliardSerializer(billiards, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BilliardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def billiard_detail(request, pk):
    try:
        billiard = Billiard.objects.get(pk=pk)
    except Billiard.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BilliardSerializer(billiard)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BilliardSerializer(billiard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        billiard.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def sauna_list(request):
    if request.method == 'GET':
        saunas = Sauna.objects.all()

        # Filter by day
        day = request.query_params.get('day')
        if day:
            saunas = saunas.filter(created_at__date=day)

        # Filter by 7 days
        seven_days = request.query_params.get('seven_days')
        if seven_days:
            start_date = timezone.now().date() - timedelta(days=7)
            saunas = saunas.filter(created_at__date__gte=start_date)

        # Filter by month
        month = request.query_params.get('month')
        if month:
            saunas = saunas.filter(created_at__month=month)

        serializer = SaunaSerializer(saunas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SaunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def sauna_detail(request, pk):
    try:
        sauna = Sauna.objects.get(pk=pk)
    except Sauna.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SaunaSerializer(sauna)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SaunaSerializer(sauna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        sauna.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def training_list(request):
    if request.method == 'GET':
        trainings = Training.objects.all()

        # Filter by day
        day = request.query_params.get('day')
        if day:
            trainings = trainings.filter(created_at__date=day)

        # Filter by 7 days
        seven_days = request.query_params.get('seven_days')
        if seven_days:
            start_date = timezone.now().date() - timedelta(days=7)
            trainings = trainings.filter(created_at__date__gte=start_date)

        # Filter by month
        month = request.query_params.get('month')
        if month:
            trainings = trainings.filter(created_at__month=month)

        serializer = TrainingSerializer(trainings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def training_detail(request, pk):
    try:
        training = Training.objects.get(pk=pk)
    except Training.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = TrainingSerializer(training)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TrainingSerializer(training, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        training.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()

        # Filter by day
        day = request.query_params.get('day')
        if day:
            orders = orders.filter(created_at__date=day)

        # Filter by 7 days
        seven_days = request.query_params.get('seven_days')
        if seven_days:
            start_date = timezone.now().date() - timedelta(days=7)
            orders = orders.filter(created_at__date__gte=start_date)

            # Filter by month
        month = request.query_params.get('month')
        if month:
            orders = orders.filter(created_at__month=month)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def subscription_list(request):
    if request.method == 'GET':
        queryset = Subscription.objects.all()

        # Apply filtering if filter_by parameter is provided
        filter_by = request.query_params.get('filter_by')
        if filter_by:
            today = date.today()
            if filter_by == 'day':
                queryset = queryset.filter(subscription_date=today)
            elif filter_by == '7_days':
                seven_days_ago = today - timedelta(days=7)
                queryset = queryset.filter(subscription_date__gte=seven_days_ago)
            elif filter_by == 'month':
                month_ago = today - timedelta(days=30)
                queryset = queryset.filter(subscription_date__gte=month_ago)

        serializer = SubscriptionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def subscription_detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def notification_list(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
