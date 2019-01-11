import os
import pandas
import bs4
l=[]
count=0
for fpathe,dirs,fs in os.walk('dataset'):
  for i in dirs:
      if i=='goldenmapping' or i=='goldenmappings':
          for fp, d, f in os.walk(os.path.join(fpathe,i)):
              for j in f:
                  if j[-7::1]=='mapping':
                      file=open(os.path.join(fp,j))
                      for s in file:
                          if s[:2]==' -':
                            l.append(s.split()[1])
                            l.append(s.split()[3][:-1:])
                            count += 1
                            print(s.split()[1],s.split()[3][:-1:],count)
                  else:
                      file=open(os.path.join(fp,j))
                      for s in file:
                            l.append(s.split(',')[0])
                            l.append(s.split(',')[1])
                            count += 1
                            print(s.split(',')[0],s.split(',')[1],count)
  for f in fs:
        if 'EXACT' in f:
            #file=open(os.path.join(fpathe,f))
            print()
        else:
            if '.morph' in f:
                file=open(os.path.join(fpathe,f))
                flag=0
                for s in file:
                    if flag==1:
                        l.append(s.split()[0])
                        l.append(s.split()[1])
                        count+=1
                        print(s.split()[0], s.split()[1], count)
                    if '# Similarity Values' in s:
                        flag=1
f=open('result.txt','w')
for i in l:
    print(i)
    f.write(i+'\n')
