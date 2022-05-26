# sine.py

def main ():
    import math

    sin_range = int(input('Please enter the unit circle quadrant you would like to see sine values for or enter 0 to quit: '))

    while sin_range != 0:
        sig_figs = int(input('To how many significant figures would you like the values to have? Please enter a number 1-4: '))

        
        if sin_range == 1:
            degree1 = 30
            degree2 = 45
            degree3 = 60
            
            sine1 = math.sin(math.radians(30))
            sine2 = math.sin(math.radians(45))
            sine3 = math.sin(math.radians(60))
        elif sin_range == 2:
            degree1 = 120
            degree2 = 135
            degree3 = 150
            
            sine1 = math.sin(math.radians(120))
            sine2 = math.sin(math.radians(135))
            sine3 = math.sin(math.radians(150))
        elif sin_range == 3:
            degree1 = 210
            degree2 = 225
            degree3 = 240
            
            sine1 = math.sin(math.radians(210))
            sine2 = math.sin(math.radians(225))
            sine3 = math.sin(math.radians(240))
        else:
            degree1 = 300
            degree2 = 315
            degree3 = 330
            
            sine1 = math.sin(math.radians(300))
            sine2 = math.sin(math.radians(315))
            sine3 = math.sin(math.radians(330))

            
        if sig_figs == 1:
            print('You would like to see the values for quadrant', sin_range, 'to', sig_figs, 'significant figures.')
            print('Here is what I calculated:')
            print('--------------------------')
            print(degree1, format(sine1, '.1f'), sep = ': ')
            print(degree2, format(sine2, '.1f'), sep = ': ')
            print(degree3, format(sine3, '.1f'), sep = ': ')
            print('--------------------------')
        elif sig_figs == 2:
            print('You would like to see the values for quadrant', sin_range, 'to', sig_figs, 'significant figures.')
            print('Here is what I calculated:')
            print('--------------------------')
            print(degree1, format(sine1, '.2f'), sep = ': ')
            print(degree2, format(sine2, '.2f'), sep = ': ')
            print(degree3, format(sine3, '.2f'), sep = ': ')
            print('--------------------------')
        elif sig_figs == 3:
            print('You would like to see the values for quadrant', sin_range, 'to', sig_figs, 'significant figures.')
            print('Here is what I calculated:')
            print('--------------------------')
            print(degree1, format(sine1, '.3f'), sep = ': ')
            print(degree2, format(sine2, '.3f'), sep = ': ')
            print(degree3, format(sine3, '.3f'), sep = ': ')
            print('--------------------------')
        else:
            print('You would like to see the values for quadrant', sin_range, 'to', sig_figs, 'significant figures.')
            print('Here is what I calculated:')
            print('--------------------------')
            print(degree1, format(sine1, '.4f'), sep = ': ')
            print(degree2, format(sine2, '.4f'), sep = ': ')
            print(degree3, format(sine3, '.4f'), sep = ': ')
            print('--------------------------')
        
        sin_range = int(input('Please enter the quadrant you would like to see sine values for or enter 0 to quit: '))

    print('You have entered 0 to quit this program.')
    print('Thank you for using this program!')

    
main()
