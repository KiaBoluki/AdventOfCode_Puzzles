def main() : 
  report = read_file('submarine_move_plan.txt')
  get_final_position(report)
  
  
def read_file(file_name):
  with open(f'./{file_name}', 'r') as submarine_report:
    report = submarine_report.readlines()
    return report

def get_final_position(report):
  forward = 0 
  deep = 0 
  for line in report:
    splited_line = line.split()
    if (splited_line[0] == 'forward'):
      forward += int(splited_line[1])
    elif (splited_line[0] == 'down'):
      deep += int(splited_line[1])
    elif (splited_line[0] == 'up'):
      deep -= int(splited_line[1])
  print(f'Final position: {int(forward*deep)}')
  
  
main()