def fat_recursiva(n):
  if n < 2:
    print('Eu uso recursividade')
    return 1
  else:
    return n*fat_recursiva(n-1)

def fat_sem_recursividade(n):
  print('Eu não uso recursividade')
  result = 1
  for i in range(2, n + 1):
    result *= 1
  return result

if __name__ == "__main__":
  import sys
  print(fat_recursiva(int(sys.argv[1])))