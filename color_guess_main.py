import random

def generate_color() -> str :
    color_list=["R","G","B","V","Y","O","W"]
    sequence=""
    for i in range(4):
        sequence+=random.choice(color_list)
    return sequence

def check_sequence(sequence: str, guess: str) -> tuple[ int, int, bool]:
    guess=guess.upper()
    correct,incorrect=0,0
    for i in range(4):
        if(sequence[i] == guess[i]):
            correct+=1
        else:
            incorrect+=1
    status=False
    if correct==4:
        status=True
    return(correct,incorrect,status)

 

if __name__=='__main__':
    print(generate_color())
    print(check_sequence(generate_color(),"RGBV"))