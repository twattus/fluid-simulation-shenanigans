import pygame,sys,random,copy
from pygame.locals import QUIT

screen_x=640
screen_y=640


world=[[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,1,0,0,0,1,0,0,0,0,0,0,2,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],]

water_drawing_flag=copy.deepcopy(world)
for e in range(0,len(water_drawing_flag)):
    for f in range(0,len(water_drawing_flag[e])):
        water_drawing_flag[e][f]=False

def transposition(matrix): #"erm this takes a list as input" be quiet
    new=[]
    for e in range(0,len(matrix)):
        temp_new=[]
        for f in range(0,len(matrix[e])):
            temp_new.append(matrix[f][e])
        new.append(temp_new)
    return new


world=transposition(world)





pygame.init()
screen=pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption('')
while True:
    clock=pygame.time.Clock()
    board=pygame.key.get_pressed()


    for e in range(0,len(world)):
        for f in range(0,len(world[e])):
            f=len(world[e])-f-1
            if world[e][f] not in [0,2]: #(only bothered about updating water tiles)
                pass

                #<moving down into free space>
                if world[e][f+1] not in [1,2]: #flows down into below container
                    transfer_value=min(world[e][f],1-world[e][f+1])
                    world[e][f]-=transfer_value
                    world[e][f+1]+=transfer_value
                #</moving down into free space>
                    if not world[e][f]:
                        continue #if all the water has been transferred down then dont bother with the rest of the stuff
                
                if world[e][f]==min(world[e][f],world[e-1][f],world[e+1][f]):
                    continue#no flowing can be done from here, youare witnessing the victim of other flowing
                elif world[e-1][f]>world[e][f]:
                    spread_value=(world[e][f]+world[e+1][f])/2
                    world[e][f]=spread_value
                    world[e+1][f]=spread_value
                elif world[e+1][f]>world[e][f]:
                    spread_value=(world[e][f]+world[e-1][f])/2
                    world[e][f]=spread_value
                    world[e-1][f]=spread_value
                else:
                    spread_value=(world[e][f]+world[e+1][f]+world[e-1][f])/3
                    world[e][f]=spread_value
                    world[e-1][f]=spread_value
                    world[e+1][f]=spread_value #AHAHA IT WORKS
                    #FLUIDS!!!!!!!!! 
                    #16/05/2026, 18:38
    
    for e in range(0,len(world)):
        for f in range(0,len(world[e])):
            if world[e][f] not in [0,2]:
                if world[e][f]>0.94:
                    world[e][f]=1
                # if world[e][f]<0.05:
                #     world[e][f]=0


    world[16][0]=random.random()

    screen.fill((64,64,64))


    for e in range(0,len(water_drawing_flag)):
        for f in range(0,len(water_drawing_flag[e])):
            water_drawing_flag[e][f]=(world[e][f] not in [0,2]) and (world[e][f+1]<0.9)

    for e in range(0,len(world)):
        for f in range(0,len(world[e])):
            if world[e][f]==2:
                pygame.draw.rect(screen,(127,127,127),pygame.Rect(20*e,20*f,20,20))
            elif world[e][f] not in [0,2]:
                if world[e][f+1]<0.9 and not (world[e+1][f] not in [0,2] or world[e-1][f] not in [0,2]):
                    if not water_drawing_flag[e][f+1]:
                        pygame.draw.rect(screen,(0,0,255),pygame.Rect(20*(e+(1-world[e][f])/2),20*f,20*(world[e][f]),20*(2-world[e][f+1])))
                    pygame.draw.rect(screen,(0,0,255),pygame.Rect(20*(e+(1-world[e][f])/2),20*f,20*(world[e][f]),20))
                else:
                    pygame.draw.rect(screen,(0,0,255),pygame.Rect(20*e,20*(f+(1-world[e][f])),20,20*(world[e][f])))

    if not board[pygame.K_SPACE]:
        clock.tick(6)
    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    pygame.display.update()
