def not_string(str):
  word = list(str.split())
  print word
  if word[0] == 'not':
    return str 
  else:
    word.insert(0, 'not')
  return ' '.join(word)




def missing_char(str, n):
  new_str = list(str)
  if len(str) == 0:
   return None
  elif n > len(str):
   return str
  else:
   new_str[n] = ''
   return ''.join(new_str)



def front_back(str):
    new_str = list(str)
    temp = new_str[0] 
    new_str[0] = new_str[len(str)-1]
    new_str[len(str)-1] = temp
    return new_str 


def front3(str):
  if len(str) < 3:
     return str
  else:
     front = str[:3]
     return front*3
  
def count_evens(nums):
    l = [number for number in nums if number % 2 == 0]
    return len(l)   
  
def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  print sum(nums)/len(nums)  



def sum13(nums):
    if not len(nums):
        return 0
    else:
        for i, n in enumerate(nums):
            if n == 13:
                del nums[i]
                try:
                    del nums[i]
                except:
                    pass
    return sum(nums) if 13 not in nums else 0 

  
def sum67(nums):
    if not len(nums):
        return 0
    else:
        
