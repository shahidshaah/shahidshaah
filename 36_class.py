def one():
    x = 'abc'
    x *=2
    print(x)
# one()

def two():
    nam = 'amit'
    nam += 'jan'
    bar = '*'
    bar *=len(nam)
    print()
# two()
def three():
    s = '\t hello world \t\t'
    bar = '*'
    bar*=len(s)
    print(f'{bar}\n{s}\n{bar}')
# three()
def four():
    s = '\t hello world \t\t'
    # s = str.strip(s)
    # s = s.strip()
    # s = s.lstrip()       #removes left side spaces
    # s = s.rstrip()       #removes right side spaces
    s = s.lstrip().title()       
    bar = '*'
    bar*=len(s)
    print(f'{bar}\n{s}\n{bar}')
# four()

def five():
    s = 'hello world addj hgh ahg'
    # y = s.find('hg')
    
    y = s.find('w', 1, 10)          #it ll search withing 1-10 indices (if nothing  matches it ll show -1 and not 0 because 0 here represents an index)
    # y = s.index('wo',1,5)        #using index if it didn't find the string it ll display an error
    y = s.rindex('wo')          #it starts searching from right 
    print(y) 

# five()

def six():
    s = 'whats bruh ?'
    y =  s.endswith('?')
    print(y) 
# six()

def seven():
    s = 'whats bruh ?'
    y =  'at' in s
    print(y) 
# seven()

def eight():
    s = 'whats bruh ?'
    # s = s.replace('bruh', 'nig')
    # s = s.replace(' ', ':')
    s = s.split(' ')
    print(s) 
# eight()
def nine():
    list = ['3','5','6','7','7']
    # s = 'gello hi byt byt'
    # y = str.join(' ', list)
    # y = ':'.join(list)
    y = (','.join(map(str, list)))
    print(y) 
nine()


