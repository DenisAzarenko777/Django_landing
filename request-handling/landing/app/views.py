from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render, reverse
#from django.shortcuts import render_to_response
# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()
new_list = []
new_list2 = []

def index(request):
    # Реализуйте логику подсчета количества переходов с ленди га по GET параметру from-landing
    name = request.GET['from-landing']
    if name == 'original':
        new_list2.append('original')
    elif name == 'test':
        new_list2.append('test')
    return render(request,'index.html')


def tt(request):
    counter_click = Counter(new_list2)
    counter_show = Counter(new_list)
    return HttpResponse(f'Counter: {counter_show["test"]}, \n Counter_click: {counter_click["test"]}')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    name = request.GET.get('ab-test-arg', 'origin')
    if name == 'origin':
        new_list.append("origin")
        return render(request,'landing.html')
    elif name == 'test':
        new_list.append("test")
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    counter_click = Counter(new_list2)
    counter_show = Counter(new_list)
    relationship_of_count1 = float(counter_click["test"]/counter_show["test"])
    relationship_of_count2 = float(counter_click["original"]/counter_show["test"])
    return render(request,'stats.html', context={
        'test_conversion': relationship_of_count1,
        'original_conversion': relationship_of_count2,
    })
