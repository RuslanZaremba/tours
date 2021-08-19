from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request, id):
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
