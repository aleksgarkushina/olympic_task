**Решение тестового задания.**

Задание:
У вас есть полоска клетчатой бумаги длины n. Каждая клетка либо белая, либо чёрная.
Сколько минимум клеток надо перекрасить из белого цвета в чёрный, чтобы на полоске существовал отрезок из последовательных клеток чёрного цвета?
Если входные данные таковы, что отрезок k чёрных последовательных клеток уже существует, то выведите 0.
Входные данные
В первой строке записано целое число t (1<= t <10^4) - количество наборов входных данных в тесте.
Далее следуют описания t наборов входных данных.
Первая строка набора входных данных содержит два целых числа т и k (1 <=k < n <= 2* 10^5). Вторая строка состоит из букв 'W' (белый цвет) и 'B' (чёрный цвет). Длина строки равна n.
Гарантируется, что сумма значений п не превосходит 2*10^5.
Выходные данные
Для каждого из наборов входных данных выведите целое число - минимальное количество клеток, которые надо перекрасить из белого в чёрный цвет, чтобы существовал отрезок из k подряд идущих чёрных клеток.
