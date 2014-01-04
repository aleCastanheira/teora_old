#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

# Create your views here.
