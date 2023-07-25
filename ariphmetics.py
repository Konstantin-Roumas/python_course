minutes = int(input())
input_hours = int(input())
input_minutes = int(input())
total_minutes = minutes + (input_hours // 60) + input_minutes
result_hours = total_minutes // 60
result_minutes = total_minutes % 60
print(result_hours)
print(result_minutes)
print('Hello World!')
