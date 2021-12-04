import sys
sys.setrecursionlimit(5000)
def josephus_survivor(n, k): 
  if n == 1: 
        return 1
  else: 
        return (josephus_survivor(n - 1, k) + k-1) % n + 1


def josephus_survivors(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1

def main():
    print(josephus_survivors(1899,997))

if __name__ == "__main__":
    main()