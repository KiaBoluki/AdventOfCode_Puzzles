def main() : 
  report = read_file()
  
  # to get the result of part 1 uncomment the following line
  #get_sum_of_increases(report)
  
  
  get_sum_of_sliding_window(report)  
  
def read_file():
  with open('./submarine_report.txt', 'r') as submarine_report:
    report = submarine_report.readlines()
    return report

def get_sum_of_increases(report):
  prev_number = int(report[0])
  increase_counter = 0 
  decrease_counter = 0
  for index,deep_num in enumerate(report):
    
    current_num = int(deep_num)
    diff = current_num - prev_number
    if diff > 0 :
      increase_counter += 1
      # print(f'{index}:\r\n{prev_number}\r\n{current_num}\r\n+Increase\r\n')
    else :
      decrease_counter += 1
      # print(f'{index}:\r\n{prev_number}\r\n{current_num}\r\n-Decrease\r\n')
    prev_number = current_num
    
  print(f'Increase:{increase_counter}',f'Decrease:{decrease_counter}')
  
  
def get_sum_of_sliding_window(report):
  increase_counter = 0
  decrease_counter = 0
  for index in range(len(report)-len(report)%3):
    slide_1 = report[index:index+3]
    slide_2 = report[index+1:index+4]
    sum_1 = sum(map(int,slide_1))
    sum_2 = sum(map(int,slide_2))
    diff = sum_2 - sum_1
    if diff > 0 :
      increase_counter += 1
      
    else :
      decrease_counter += 1
      
  print('Increase:',increase_counter,'Decrease:',decrease_counter)




main()