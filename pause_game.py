# pause_game
# 작성자 : 김영현
# Play 도중 esc키를 누르면 일시정지가 되고 main menu로 되돌아가거나 Play를 이어서 할 수 있게 해준다.


def pause_game():
    run = True
    menu_list = ['Main Menu', 'Resume']
    cur_menu = 0
    ret_value = 0
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                if event.key == pg.K_DOWN:
                    cur_menu = (cur_menu + 1) % len(menu_list)
                if event.key == pg.K_UP:
                    cur_menu = (cur_menu + len(menu_list) - 1) % len(menu_list)
                if event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                    if cur_menu == 0:
                        run = False
                        ret_value = 1
                    if cur_menu == 1:
                        run = False

        menu_font = pg.font.SysFont("arial", 30, True, True)
        menu_text = []
        for text in menu_list:
            if menu_list[cur_menu] == text:
                menu_text.append(menu_font.render(text, True, colors[1]))
            else:
                menu_text.append(menu_font.render(text, True, WHITE))

        i = 0
        for text in menu_text:
            screen.blit(text, [size[0] / 2 - text.get_width() / 2, size[1] / 4 + i * text.get_height()])
            i += 1

        pg.display.flip()
        clock.tick(FPS)
    screen.fill(WHITE)
    return ret_value


