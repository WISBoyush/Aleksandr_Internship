# Напишите функцию, которая будет принимать три значения: h (часы), m (минуты), s (секунды).
# Функция должна возвращать значение, соответствующее самому длительному периоду времени.
#
# Примечание: среди передаваемых временных промежутков не будет одинаковых.


def longest_time(h, m, s):
    h_to_sec = h * 3600
    m_to_sec = m * 60
    seconds_mapping = dict(zip([h_to_sec, m_to_sec, s], (h, m, s)))
    return seconds_mapping[max(seconds_mapping.keys())]


print(longest_time(1, 59, 3598))   # 1
print(longest_time(2, 300, 15000))   # 300
print(longest_time(15, 955, 59400))   # 59400
