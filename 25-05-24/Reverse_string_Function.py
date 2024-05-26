def reverse_string(name):
   rev_string=""
   for s in name:
          rev_string=s+rev_string
   return rev_string

reverse=reverse_string("sharan")
print(reverse)