import sys, collections

f = open("test.txt")

sys.stdin = f

flag = False

def countFreq(arr):
  freq = {}  
  for ele in arr:
    if ele in freq:
      freq[ele] += 1
    else: freq[ele] = 1
  return freq

def findMode(freq):
  freqValues = [ v for v in freq.values()]
  maxFreqKey = max(freq, key= lambda x: freq[x])
  maxFreqCount = freqValues.count(freq[maxFreqKey])  
  return (maxFreqKey, maxFreqCount)
  
# freq= {1: 4, 5: 4, 2: 3, 6: 3, 3: 2, 4: 2, 9: 1, 8: 1}
# print(findMode(freq))

for _ in range(int(input())):
  n,k = map(int, input().split())
  lst = list(map(int, input().split()))
  freq = countFreq(lst)
  if k not in freq:
    freq[k] = 0
  fk = freq[k] 
  operation = 0
  mode, modef = findMode(freq)
  if mode == k and modef==1:
    print(0)
  elif n==1:
    print(1)
  else:
    # print(mode, modef, freq, "mode and modef")
    while mode!=k:
      tmpOpr = (freq[mode] - fk)//2
      # print(mode, modef, fk, "<")
      tmpOpr += 1
      fk += tmpOpr
      operation += tmpOpr
      freq[mode] -= tmpOpr
      freq[k] += tmpOpr
      mode, modef = findMode(freq)  
      # print(mode, modef, tmpOpr, freq)
      # print("=========")
      if tmpOpr==0: break
    if mode==k and modef!=1:
      operation += 1     
      
    print(operation)



amount = 100
target = amount * 2
month = 0
while amount < target:
  amount += amount * (6/100)
  month += 1
  
print(month, amount)