def main(num):
    epsilon=0.00001
    bajo=0.0
    alto=max(1.0, num)
    media = (alto+bajo) / 2
    while abs(media**2 - num) >=epsilon:
        print(f'bajo: {bajo}, alto: {alto}, media: {media}')
        if media**2<num:
            bajo=media
        else:
            alto=media
        media=(alto+bajo)/2
    print(media)
if __name__=='__main__':
    num=int(input("Dame un numero: "))
    main(num)