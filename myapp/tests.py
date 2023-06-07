from django.test import TestCase
from django.shortcuts import render
from django.urls import path
from . import views

def test(request):
    return render(request,'index.html')
