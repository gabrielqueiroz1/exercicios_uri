import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Fale alguma coisa :)")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-US')
        print(f"Você disse: {text}")

    except:
        print("Não consegui entender :(")

arr = []
for i in range(0, 5):
    n = int(input())
    arr.append(n)

print(sum(arr[:4]), end=' ')
print(sum(arr[1:]))


notas = []
while len(notas) < 2:
    n = float(input())
    if n < 0 or n > 10:
        print("nota invalida")
    else:
        notas.append(n)
media = sum(notas)/2
print("media =", media)


n = int(input())
for i in range(0, n):
    x, y = map(int, input().split())
    cont = 0
    if y > x:
        for g in range(x+1, y):
            if g % 2 == 1:
                cont += g
        print(cont)
    if x > y:
        for j in range(y+1, x):
            if j % 2 == 1:
                cont += j
        print(cont)

























