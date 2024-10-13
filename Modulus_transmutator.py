
possible_words={"включи","выключи","звук","браузер","d","телефона",".","!","открой"}
ae_words={  "включи":
                {"звук":
                    {
                        "телефона": False
                    },
                "браузер":False
                },
            "выключи":
                {
                 "звук":False,
                 "браузер":False
                },
            "d":False,
            "открой":True}
words_buffer=[]
audite=False
text_buffer=""

def Test(txt:str):
    print("t:",txt)
    if txt.split()[1]=="дверь":
        print("Дверь октрыта")
        return " ".join(txt.split()[2:])
    return " ".join(txt.split()[1:])

def Manager(commands):
    for i in commands:
        print(type(i))
        if isinstance(i, str): print(i)
        elif isinstance(i, list): 
                match i[0].split()[0]:
                    case "открой": 
                        print("+")
                        return Test(i[0])
    return False

def Search(word,words,cpae_words,txt=""):
    global ae_words
    if word==".": return txt.split(), "", True
    if word not in cpae_words:
        if word in ae_words: return words, txt, False
        return words[1:], txt ,False
    if type(cpae_words[word])==bool: 
        if cpae_words[word]: return cpae_words[word],words[0],False 
        else: return words[1:],txt+" "+ word,False
    if not bool(txt): txt=word
    else: txt+=" "+word
    return Search(words[1:][0],words[1:],cpae_words[word],txt)
    
def Transmutator(text:str):
    global possible_words,ae_words,words_buffer,audite,text_buffer
    commands=[]
    print("\n=======================")
    print(f"Исходный текст: {text},{len(text)}")
    if audite:
        if bool(text): words_buffer+=text
        else:
            print(f"Команда обнаружена: {words_buffer}")
            commands.append([words_buffer])
            words_buffer=[]
            audite=False
    else:
        text+=text_buffer
        if len(text)!=0: text+=" ."
        
        words=words_buffer+text.split()
        words_buffer=[]
        words=[word for word in words if word in possible_words]
        print("words:",words)
        if len(text)==0: words+=[" "]
        while words:
            words,txt,check=Search(words[0],words,ae_words) 
            if type(words)==bool: 
                audite=True
                text=text.replace('.','')
                text=text.split(txt, 1)[-1]
                words_buffer=txt+text
                return commands
            if bool(txt): 
                print(f"Команда обнаружена:{txt}")
                commands.append(txt)
                text=text.replace(f"{txt}", '', 1)
            if check:
                words_buffer=words 
                print(f"Добавить в следующий пул: {str(words)}")  
                break
            
    return commands
        
if __name__=="__main__":
    import time 
    text_input=["",
                "включи открой дверь открой дверь пожалуйста и включи ноутбук",
                ""]
    start=time.time()
    for i in text_input:
        result=Manager(commands=Transmutator(i))
        if result:
            result=Manager(commands=Transmutator(result))
    end=time.time()
    print(f"время выполнения при {len(text_input)} тактах: {round((end-start)*1000)} ms")
    
    
    # Transmutator("открой дверь открой дверь пожалуйста и включи ноутбук")
    # commands=Transmutator("включи открой дверь пожалуйста и включи ноутбук")
    
    # Transmutator("")
    # print("!",commands,completion)
    # print(Manager(commands))
    # Transmutator(Test(commads[0]))
    # Transmutator("")
    # Transmutator("")
    # Transmutator("Так, хорошо")
    # Transmutator("")
    # Transmutator("")
    # Transmutator("открой")
    # Transmutator("дверь пожалуйста")
    # Transmutator("и включи комп")
    # Transmutator("")
    # Transmutator("")
    # Transmutator("включи звук")
    # Transmutator("выключи звук")
    # Transmutator("телефона")
    # Transmutator("")
    # Transmutator("включи звук")
    # Transmutator("включи звук")
    # Transmutator("привет можешь помочь выключи включи пожалуйста звук d выключи что-то в браузер включи")
    # Transmutator("звук пожалуйстf браузер включи d включи")
    # Transmutator("браузер включи звук")
    # Transmutator("")
    