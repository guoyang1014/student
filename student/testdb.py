from django.http import HttpResponse
from django.shortcuts import render
from stu.models import Test

def add(request):
    stu1=Test(name='',high='180',course='python',sex='男')
    stu1.save()
    return render(request,'add.html')

def select(request):
    list=Test.objects.filter(name='张三')
    return render(request,'list.html',{'list':list})

def update(request):
    list1=Test.objects.get(id=2)
    list1.name='李四'
    list1.save()
    list=Test.objects.all()
    return render(request,'update.html',{'list':list})

def delete(request):
    list1=Test.objects.get(id=3)
    list1.delete()
    list=Test.objects.all()
    return render(request,'delete.html',{'list':list})