vidas = []

print("------- Quiz -------")
inicioEscolha = (input("1 -> Categorias \n2 -> Scores Recentes \n3 -> Sair \n"))

if inicioEscolha == "1":
    while True: 
        categoriaEscolha = (input("1 -> Países \n2 -> História \n3 -> Arte \n"))
        if categoriaEscolha == "1":
            vidas = 5
            print("Quiz de países\n")
            while vidas>0:
                inputUser = input("Qual é a capital do Cazaquistão: ").title()
                if inputUser == "Astana":
                    print("Acertou")
                    break

                else:
                    vidas -= 1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            while vidas>0:
                inputUser = input("Qual é a capital da Coreia do Sul:\n")
                if inputUser == "Seul":
                        print("Acertou")
                        break
                else:
                    vidas -=1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            while vidas>0:
                inputUser = input("Como se chama o presidente da China:\n")
                if inputUser == "Xi Jinping":
                        print("Acertou")
                        print("Parabéns completou o quiz de países com sucesso!\n")
                        break
                    
                else:
                    vidas -=1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            if vidas<1: 
                print("Ficou sem vidas :c\n")
                break

                                
        elif categoriaEscolha == "2":
            vidas = 5
            print("Quiz de história\n")
            while vidas>0:
                inputUser = input("Quantos anos durou a segunda guerra mundial? (ano inicial - ano final): ")
                if inputUser == "1939–1945":
                    print("Acertou")
                    break

                else:
                    vidas -= 1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            while vidas>0:
                inputUser = input("Em que batalha desapareceu D. Sebastião:\n").title()
                if inputUser == "batalha de Alcácer-Quibir":
                        print("Acertou")
                        break
                else:
                    vidas -=1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            while vidas>0:
                inputUser = input("Quem descobriu o brazil?\n")
                if inputUser == "Pedro Álvares Cabral":
                        print("Acertou")
                        print("Parabéns completou o quiz de História com sucesso!\n")
                        break
                    
                else:
                    vidas -=1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            if vidas<1: 
                print("Ficou sem vidas :c\n")
                break  


        elif categoriaEscolha == "3":
            vidas = 5
            print("Quiz de Arte\n")
            while vidas>0:
                inputUser = input("Qual foi o artista que pintou o quadro 'Mona Lisa': ").title()
                if inputUser == "Leonardo da Vinci":
                    print("Acertou")
                    break

                else:
                    vidas -= 1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            while vidas>0:
                inputUser = input("Qual foi o artista que pintou o quadro 'A Noite Estrelada'\n").title()
                if inputUser == "Vincent van Gogh":
                        print("Acertou")
                        break
                else:
                    vidas -=1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            while vidas>0:
                inputUser = input("Qual foi o artista que pintou o quadro 'Meisje met de parel'\n")
                if inputUser == "Johannes Vermeer":
                        print("Acertou")
                        print("Parabéns completou o quiz de Artes com sucesso!\n")
                        break
                    
                else:
                    vidas -=1
                    print("Errou")
                    print("Vidas Restantes: " ,vidas)

            if vidas<1: 
                print("Ficou sem vidas :c\n")
                break  

else:
    print("Input Invalida, escolha uma opção valida")


if inicioEscolha == "3":
    exit
    