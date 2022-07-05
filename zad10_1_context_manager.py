# CONTEXT MANAGER IS FUNCTION THAT ALWAYS STARTS WITH "WITH". YOU DEFINE IT'S NAME AND THEN DO SOME STUFF INSIDE. THEN YOU CLOSE IT.
# TO DEFINE EVEN BETTER U USE BUILT IN METHODS AS __enter__   and __exit__. __enter__ allows to create "internal" object
 
class HtmlCM():
  def __init__(self):
    pass

  def __enter__(self):
    print('<TABLE>')
    print(' <TR>')
    print('   <TH>Number</TH><TH>Description</TH>')
    return self
  
  def __exit__(self, type, value, traceback):
    print("</TABLE>")

  
with HtmlCM() as cm:
  print(" <TR>")
  print("     <TD>1</TD><TD>Say hello!</TD)")
  print(" </TR>")
  print(" <TR>")
  print("     <TD>2</TD><TD>Say good bye!</TD)")
  print(" </TR>")