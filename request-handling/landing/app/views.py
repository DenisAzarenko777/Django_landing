from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render, reverse
#from django.shortcuts import render_to_response
# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show2 = Counter()
counter_click2 = Counter()
new_list = []
new_list2 = []

def index(request):
    # Реализуйте логику подсчета количества переходов с ленди га по GET параметру from-landing
    name = request.GET['from-landing']
    if name == 'original':
        counter_click2['original'] += 1
    elif name == 'test':
        counter_click2['test'] += 1
    return render(request,'index.html')



def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    name = request.GET.get('ab-test-arg', 'origin')
    if name == 'origin':
        counter_show2['origin'] += 1
        return render(request,'landing.html')
    elif name == 'test':
        counter_show2['test'] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:

    try:
        relationship_of_count1 = float(counter_click2["test"]/counter_show2["test"])
        relationship_of_count2 = float(counter_click2["original"]/counter_show2["origin"])
        return render(request,'stats.html', context={ 'test_conversion': relationship_of_count1, 'original_conversion': relationship_of_count2,})
    except ZeroDivisionError:
        return render(request, 'stats.html', context={ 'test_conversion': 'Произошло деление на ноль', 'original_conversion': "Произошло деление на ноль",})
