from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        return render(request, 'auction/home.html')

    def post(self, request):
        pass