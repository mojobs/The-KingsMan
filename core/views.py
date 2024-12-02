from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Cloth, Customer, Delivery, Orders, Price

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def customers(request):
    if request.method == 'POST':
        data = request.POST

        if Customer.objects.filter(customerid=data['customerid']).exists():
           messages.info(request, 'A Customer with this ID already exists!')
           return redirect('customers')
        else:
            new_customer = Customer.objects.create(customerid=data['customerid'], customername=data['customername'],
                                                customeraddress=data['useraddress'], customernumber=data['customernumber'],
                                                sex=data['usersex'], customerdate=data['user-date'])
            new_customer.save()

        return redirect('order')

    return render(request, 'customers.html', {})

def order(request):
    if request.method == 'POST':
        data = request.POST

        if Orders.objects.filter(orderid=data['order-id']).exists():
            messages.info(request, 'An Order with this ID already exists!')
            return redirect('order')
        else:
            new_order = Orders.objects.create(orderid=data['order-id'], orderdate=data['order-date'])
            new_order.save()

        return redirect('clothes')

    return render(request, 'orders.html', {})

def clothes(request):
    if request.method == 'POST':
        data = request.POST

        new_cloth = Cloth.objects.create(clothtype=data['cloth-type'], noofclothes=data['cloth-number'])
        new_cloth.save()

        return redirect('delivery')

    return render(request, 'clothes.html', {})

def delivery(request):
    if request.POST:
        data = request.POST

        if Delivery.objects.filter(deliveryid=data['delivery-Id']).exists():
            messages.info(request, 'A Delivery with this ID already exists!')
            return redirect('delivery')
        else:
            new_delivery = Delivery.objects.create(deliveryid=data['delivery-Id'], deliverydate=data['delivery-date'])
            new_delivery.save()

        return redirect('pricing')

    return render(request, 'delivery.html', {})

def pricing(request):
    if request.method == 'POST':
       data = request.POST

       new_pricing = Price.objects.create(pricetype=data['pricing-type'], currency=data['currency-type'])
       new_pricing.save()

       return redirect('completed')

    return render(request, 'pricing.html', {})

def completed(request):
    return render(request, 'completed.html', {})
