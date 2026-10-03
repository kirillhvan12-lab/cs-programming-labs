sec=int(input())
hr=sec//3600
mins=(sec%3600)//60
sec2=sec%60
print(f'{hr:02d}:{mins:02d}:{sec2:02d}')
