def paper_names(papers,names):
    if papers == names:
        return True
    return False
papers = ['ahmad','ali','s','d','d','f','g','h','j','u','y','tt','t','t','r','y']
s_name = 'ali'
print(paper_names(papers,s_name))
result  = paper_names(papers,s_name)
if result:
    print('found')
else:
    print('not found')

