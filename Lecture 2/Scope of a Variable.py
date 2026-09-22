## different scopes of variables  
  
# global variable  
var_x = 12
def add_sum():
  # local variable     
  var_y = 12  
  print(f'{var_x} + {var_y} = {var_x + var_y}')  
add_sum()
print("var_x : ",var_x)