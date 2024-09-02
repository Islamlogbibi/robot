import webbrowser
import time
import pyautogui
s=input('write hello or hi \n -') 
while True:
    if s=='hello'or s=='hi':
        print('hi,im robot and i was made by islam')
        name=input('now tell me about your self ,what is your name : ')
        n=name.split()
        print('your name is ')
        print(n[-1])
        print("that's a good name")
        age=int(input('what about your age : '))
        print('your age is: ')
        if age <=0 or age >=120:
            print('am i fucking laughing')
        elif age >0:
            print (age)
        while 1>0 :
            work=input ('what you want do : ')
            facebook='https://m.facebook.com/'
            youtube='https://m.youtube.com/'
            messenger='https//m.messenger.com'
            if work =='open facebook'or work =='facebook'or work =='facebok':
                webbrowser.open('https://m.facebook.com')
                work =input ('what you want do : ')
            elif work =='open youtube' or work == 'youtube' or work == 'youtbe':
                webbrowser.open('https://m.youtube.com')
            elif work =='open messenger'or work == 'mesenger' or work == 'messenger':
                webbrowser.open('https://m.messnger.com')
            elif work == 'search on google' or work =='search in google':
                search =input('what do you want to serch :')  
                webbrowser.open('https://www.google.com/search?q='+search)
            elif work == 'search in youtube'or work == 'search on youtube':
                youtube_search=input('what you want search :')
                webbrowser.open('https://www.youtube.com/results?search_query='+youtube_search)
            elif work == 'translate arabic to english':
                translate =input('what do you want to translate : ')
                webbrowser.open('https://https://translate.google.com/?hl=fr&tab=wT&sl=ar&tl=en&text='+translate+'&op=translate')
            elif work == 'translate english to arabic':
                translate =input('what do you want to translate : ')
                webbrowser.open('https://https://translate.google.com/?hl=en&tab=wT&sl=en&tl=ar&text='+translate+'&op=translate')
            elif work == 'send messages in messenger':
                message=input ('enter your message :')
                intervale =int(input('enter the time intervale:'))
                print('you have 20 seconds Open the messenger and enter the conversation you want to send the message to')
                time.sleep(20)
                while True:
                    time.sleep(intervale)
                    pyautogui.typewrite(message)
                    pyautogui.press('enter')
        
            elif work=='solve a second degree equation':
                a=float(input('enter a: '))
                b=float(input('enter b: '))
                c=float(input('enter c: '))
                g=b**2-(4*a*c)
                print('∆='),print(g)
                if g==0:
                    x0=(-b)/2*a
                    print("there is only one solve : ")
                    print(x0)
                    
                elif g>0:
                    x1=(-b-g**(1/2))/2*a
                    x2=(-b+g**(1/2))/2*a
                    print ('x1='),print(x1)
                    print('x2='),print(x2)
                elif g<0:
                    print("the equation doesn't have any solution in |N")
            else:
                print('this is out of my work')
          
    else:
        print('could you please write hi or hello with out testing my patience')