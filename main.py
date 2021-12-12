with open('./submarine_report.txt', 'r') as submarine_report:
  report = submarine_report.readlines()
  prev_number = int(report[0])
  increase_counter = 0 
  decrease_counter = 0
  for index,deep_num in enumerate(report):
    
    current_num = int(deep_num)
    diff = current_num - prev_number
    if diff > 0 :
      increase_counter += 1
      print(f'{index}:\r\n{prev_number}\r\n{current_num}\r\n+Increase\r\n')
    else :
      decrease_counter += 1
      print(f'{index}:\r\n{prev_number}\r\n{current_num}\r\n-Decrease\r\n')
    prev_number = current_num
    
  print(f'Increase:{increase_counter}',f'Decrease:{decrease_counter}')