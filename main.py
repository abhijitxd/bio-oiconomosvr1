@namespace
class SpriteKind:
    NPC = SpriteKind.create()
    time_Machine = SpriteKind.create()
    vanannouncement = SpriteKind.create()
    Automotive = SpriteKind.create()
    playercbc = SpriteKind.create()
    teleporter = SpriteKind.create()
    shopdi = SpriteKind.create()
    tp2 = SpriteKind.create()
    mc2 = SpriteKind.create()
    pappad = SpriteKind.create()
    paper = SpriteKind.create()
    tm2 = SpriteKind.create()
    sci2 = SpriteKind.create()
    bottle = SpriteKind.create()
    bfielurg = SpriteKind.create()
@namespace
class StatusBarKind:
    Sapplings = StatusBarKind.create()
    Saplings = StatusBarKind.create()

def my_function():
    global sandytile
    sandytile = tiles.location_of_sprite(Main_charecter)
    if tiles.tile_at_location_equals(sandytile, assets.tile("""
        batli
    """)):
        music.play(music.melody_playable(music.jump_up),
            music.PlaybackMode.UNTIL_DONE)
        tiles.set_tile_at(sandytile, sprites.castle.tile_path5)
    elif tiles.tile_at_location_equals(sandytile, assets.tile("""
        myTile12
    """)):
        music.play(music.melody_playable(music.jump_up),
            music.PlaybackMode.UNTIL_DONE)
        tiles.set_tile_at(sandytile, sprites.castle.tile_path5)
controller.combos.attach_combo("a+b", my_function)

def on_on_overlap(sprite, otherSprite):
    global Time_Machine, VAN
    Time_Machine = sprites.create(assets.image("""
            adam baba ki time machine
        """),
        SpriteKind.time_Machine)
    sprites.destroy_all_sprites_of_kind(SpriteKind.NPC)
    sprites.destroy_all_sprites_of_kind(SpriteKind.time_Machine)
    music.play(music.melody_playable(music.buzzer),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.melody_playable(music.beam_up),
        music.PlaybackMode.IN_BACKGROUND)
    game.show_long_text("STRAIGHT TO THE FUTURE IN 2050!!", DialogLayout.BOTTOM)
    music.play(music.melody_playable(music.buzzer),
        music.PlaybackMode.UNTIL_DONE)
    scene.camera_shake(6, 500)
    game.show_long_text("YEAR 2050", DialogLayout.LEFT)
    MAIN_CHARECTER.set_position(35, 106)
    scene.set_background_image(assets.image("""
        2050
    """))
    game.splash("1st you need to explore.")
    game.show_long_text("Go to the van.", DialogLayout.BOTTOM)
    VAN = sprites.create(assets.image("""
        van
    """), SpriteKind.Automotive)
    VAN.set_position(90, 107)
sprites.on_overlap(SpriteKind.time_Machine, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global mc_2
    sprites.destroy_all_sprites_of_kind(SpriteKind.shopdi)
    sprites.destroy_all_sprites_of_kind(SpriteKind.teleporter)
    sprites.destroy_all_sprites_of_kind(SpriteKind.tp2)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    shop.set_position(15, 55)
    scene.set_background_image(assets.image("""
        last bg
    """))
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    mc_2 = sprites.create(img("""
            . . . . f f f f . . . . . 
                                . . f f f f f f f f . . . 
                                . f f f f f f c f f f . . 
                                f f f f f f c c f f f c . 
                                f f f c f f f f f f f c . 
                                c c c f f f e e f f c c . 
                                f f f f f e e f f c c f . 
                                f f f b f e e f b f f f . 
                                . f 4 1 f 4 4 f 1 4 f . . 
                                . f e 8 8 8 8 8 8 e f . . 
                                . f f 8 8 8 8 8 8 f f . . 
                                f e f b 7 7 7 7 b f e f . 
                                e 4 f 7 7 7 7 7 7 f 4 e . 
                                e e f 6 6 6 6 6 6 f e e . 
                                . . . f f f f f f . . . . 
                                . . . f f . . f f . . . .
        """),
        SpriteKind.mc2)
    tp_2.set_position(11, 48)
    controller.move_sprite(mc_2)
    scene.camera_follow_sprite(mc_2)
    game.show_long_text("Plant saplings in the barren land.", DialogLayout.BOTTOM)
    game.show_long_text("Press 'B' or 'enter' button to plant saplings.",
        DialogLayout.BOTTOM)
    game.show_long_text("If you complete,you will get the half research report and continue.",
        DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.tp2, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    global Main_charecter
    tiles.destroy_sprites_of_kind(SpriteKind.mc2)
    tiles.destroy_sprites_of_kind(SpriteKind.paper)
    tiles.destroy_sprites_of_kind(SpriteKind.teleporter)
    tiles.destroy_sprites_of_kind(SpriteKind.Automotive)
    game.show_long_text("Half Research Paper Accomplished", DialogLayout.BOTTOM)
    game.splash("UNIT⠀2⠀Completed")
    music.play(music.melody_playable(music.buzzer),
        music.PlaybackMode.UNTIL_DONE)
    effects.clouds.end_screen_effect()
    game.splash("UNIT⠀3⠀Garbage⠀Collection")
    game.show_long_text("Press a+b⠀at⠀the⠀same⠀time to collect garbage. Put them in the bin after you have collected all of them. Then you'll get the full research report and save the Future.",
        DialogLayout.BOTTOM)
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    """))
    tiles.load_map(tiles.create_map(tilemap("""
        beach
    """)))
    Main_charecter = sprites.create(assets.image("""
        tingu
    """), SpriteKind.enemy)
    controller.move_sprite(Main_charecter)
    scene.camera_follow_sprite(Main_charecter)
sprites.on_overlap(SpriteKind.mc2, SpriteKind.paper, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    global shop
    music.play(music.melody_playable(music.magic_wand),
        music.PlaybackMode.UNTIL_DONE)
    scene.set_background_image(assets.image("""
        shop bg
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.teleporter)
    MAIN_CHARECTER.set_position(84, 87)
    controller.move_sprite(MAIN_CHARECTER, 44, 47)
    shop = sprites.create(assets.image("""
        Shop
    """), SpriteKind.shopdi)
    shop.set_position(25, 63)
sprites.on_overlap(SpriteKind.player, SpriteKind.teleporter, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    global player_back, MAIN_CHARECTER, teleporter2
    scene.set_background_image(img("""
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc88888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc88888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc88888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc88888888888888888888888888888
                        888888888888888888888888888888888888888888888888888888cccccccc888811119999999998888ffffffff888888889999999999998888ffff888888881111cccccccc888888888888888888888
                        888888888888888888888888888888888888888888888888888888cccccccc888811119999999998888ffffffff888888889999999999998888ffff888888881111cccccccc888888888888888888888
                        888888888888888888888888888888888888888888888888888888cccccccc888811119999999998888ffffffff888888889999999999998888ffff888888881111cccccccc888888888888888888888
                        888888888888888888888888888888888888888888888888888888cccccccc888811119999999998888ffffffff888888889999999999998888ffff888888881111cccccccc888888888888888888888
                        88888888888888888888888888888888888888888888888888cccccccccccc111188888888888888888ffffffff111188888888888899999999ffff8888888899991111cccc888888888888888888888
                        88888888888888888888888888888888888888888888888888cccccccccccc111188888888888888888ffffffff111188888888888899999999ffff8888888899991111cccc888888888888888888888
                        88888888888888888888888888888888888888888888888888cccccccccccc111188888888888888888ffffffff111188888888888899999999ffff8888888899991111cccc888888888888888888888
                        88888888888888888888888888888888888888888888888888cccccccccccc111188888888888888888ffffffff111188888888888899999999ffff8888888899991111cccc888888888888888888888
                        8888888888888888888888888888888888888888888888cccccccccccc1111888888888888888888888ffffffff888888888888888888888888ffffcccc888888881111cccc888888888888888888888
                        8888888888888888888888888888888888888888888888cccccccccccc1111888888888888888888888ffffffff888888888888888888888888ffffcccc888888881111cccc888888888888888888888
                        8888888888888888888888888888888888888888888888cccccccccccc1111888888888888888888888ffffffff888888888888888888888888ffffcccc888888881111cccc888888888888888888888
                        8888888888888888888888888888888888888888888888cccccccccccc1111888888888888888888888ffffffff888888888888888888888888ffffcccc888888881111cccc888888888888888888888
                        8888888888888888888888cccccccccccccccccccccccccccc99999999ccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc9999cccc888888888888cccc888888888888888888888
                        8888888888888888888888cccccccccccccccccccccccccccc99999999ccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc9999cccc888888888888cccc888888888888888888888
                        8888888888888888888888cccccccccccccccccccccccccccc99999999ccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc9999cccc888888888888cccc888888888888888888888
                        8888888888888888888888cccccccccccccccccccccccccccc99999999ccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc9999cccc888888888888cccc888888888888888888888
                        888888888888888888111111111111cccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc99999999999999999999cccc888888888888888888888
                        888888888888888888111111111111cccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc99999999999999999999cccc888888888888888888888
                        888888888888888888111111111111cccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc99999999999999999999cccc888888888888888888888
                        888888888888888888111111111111cccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccccccc99999999999999999999cccc888888888888888888888
                        88888888888888111111111111cccccccccccccccccccccccc9999cccccccccccccccc999999999cccc9999cccc9999cccccccc99999999cccc9999cccccccccccc9999cccc888888888888888888888
                        88888888888888111111111111cccccccccccccccccccccccc9999cccccccccccccccc999999999cccc9999cccc9999cccccccc99999999cccc9999cccccccccccc9999cccc888888888888888888888
                        88888888888888111111111111cccccccccccccccccccccccc9999cccccccccccccccc999999999cccc9999cccc9999cccccccc99999999cccc9999cccccccccccc9999cccc888888888888888888888
                        888888888fffffcccccccccccccccccccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccc99999999cccccccccccc9999cccc888888888888888888888
                        888888888fffffcccccccccccccccccccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccc99999999cccccccccccc9999cccc888888888888888888888
                        888888888fffffcccccccccccccccccccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccc99999999cccccccccccc9999cccc888888888888888888888
                        888888888fffffcccccccccccccccccccccccccccccccccccc9999ccccccccccccccccccccccccccccc9999cccc9999cccccccccccccccc99999999cccccccccccc9999cccc888888888888888888888
                        888888888cccccccccfffffffffffffffffffffffffffffccc9999999999999999999999999999999999999cccc9999ccccccccffffffffffffffffffffffff9999cccccccc888888888888888888888
                        888888888cccccccccfffffffffffffffffffffffffffffccc9999999999999999999999999999999999999cccc9999ccccccccffffffffffffffffffffffff9999cccccccc888888888888888888888
                        888888888cccccccccffffffffffff999999999ffffffffccc9999999999999999999999999999999999999cccc9999ccccccccffffffffffffffffffffffff9999cccccccc888888888888888888888
                        888888888cccccccccffffff....9999999999999.fffffccc9999999999999999999999999999999999999cccc9999ccccccccffffffff9999999999999fffff99cccccccc888888888888888888888
                        888888888fffffccccffffff...999999999999999fffffcccccccccccccccccccccccccccccccccccccccccccc999999999999fffff..999999999999999ffffccccccffff888888888888888888888
                        888888888fffffccccffffff..99999999999999999ffffcccccccccccccccccccccccccccccccccccccccccccc999999999999fffff.99999999999999999fffccccccffff888888888888888888888
                        888888888fffffccccffffff.999999fffffff999999fffcccccccccccccccccccccccccccccccccccccccccccc999999999999fffff999999fffffff999999ffccccccffff888888888888888888888
                        888888888fffffccccffffff.99999fcc111ccf99999fffcccccccccccccccccccccccccccccccccccccccccccc999999999999fffff99999fcc111ccf99999ffccccccffff888888888888888888888
                        888888888fffffffffffffff99999f...111...f99999ff99999999999999999999999999999999999999999999999999999999ffff99999fc...1...cf99999fccffffffff888888888888888888888
                        888888888fffffffffffffff9999fc...111...cf9999ff99999999999999999999999999999999999999999999999999999999ffff9999fcc...1...ccf9999fccffffffff888888888888888888888
                        888888888fffffffffffffff9999fc...111...cf9999ff9999999999999999999999999999999999999999999999999999999fffff9999fcc...1...ccf9999fccffffffff888888888888888888888
                        888888888fffffffffffffff9999111111111111f9999ff9999999999999999999999999999999999999999999999999999999fffff9999111111111111f9999fccffffffff888888888888888888888
                        888888888fffffffffffffff9999111111111111f9999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999111111111111f9999fffffffffff888888888888888888888
                        888888888fffffffffffffff999911...111...1f9999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999111111111111f9999fffffffffff888888888888888888888
                        888888888fffffffffffffff9999fc...111...cf9999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999fc...111...cf9999fffffffffff888888888888888888888
                        888888888fffffffffffffff9999fc...111...cf9999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999fc...111...cf9999fffffffffff888888888888888888888
                        88888888888888ffffffffff99999fccc111cccf99999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99999f...111...f99999fffffff8888888888888888888888888
                        88888888888888ffffffffff899999fcc111ccf99999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99999fcc111ccf99999ffffffff8888888888888888888888888
                        88888888888888ffffffffff8999999fffffff999999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8999999fffffff999999ffffffff8888888888888888888888888
                        8888888888888888888888888899999999999999999888888888888888888888888888888888888888888888888888888888888888888999999999999999998888888888888888888888888888888888
                        8888888888888888888888888889999999999999998888888888888888888888888888888888888888888888888888888888888888888899999999999999988888888888888888888888888888888888
                        8888888888888888888888888888999999999999988888888888888888888888888888888888888888888888888888888888888888899889999999999999888888888888888888888888888888888888
                        8888888888888888888888888888889999999998888888888888888888888888888888888888888888888888888888888888888888899888899999999988888888888888888888888888888888888888
                        888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888cccc888888888888888888888888888888888
                        888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888cccc888888888888888888888888888888888
                        888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888cccc888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
                        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    """))
    game.show_long_text("Ohh! Are you the one from the past?? By the way it is 2050.",
        DialogLayout.BOTTOM)
    game.show_long_text("I am the Scientist's worker and we have a laboratory here. ",
        DialogLayout.BOTTOM)
    game.show_long_text("You need to send the report back to the present.",
        DialogLayout.BOTTOM)
    game.show_long_text("Phone rings bzzzz.... bzzzzz.......", DialogLayout.BOTTOM)
    game.show_long_text("You answer the phone.It was the scientist.You talk to him and continue.",
        DialogLayout.BOTTOM)
    game.show_long_text("The scientist's worker takes you to their laboratory.",
        DialogLayout.BOTTOM)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Automotive)
    scene.set_background_image(assets.image("""
        Future Laboratory
    """))
    game.show_long_text("You climb up the 100th floor by the lift and enter the control panel.",
        DialogLayout.BOTTOM)
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    player_back = sprites.create(assets.image("""
        back pc
    """), SpriteKind.playercbc)
    player_back.set_position(125, 75)
    scene.set_background_image(assets.image("""
        Control Panel
    """))
    player_back = sprites.create(assets.image("""
        back pc
    """), SpriteKind.playercbc)
    sprites.destroy_all_sprites_of_kind(SpriteKind.playercbc)
    game.show_long_text(" OH ! The world is completely destroyed!! First I need to plant trees.",
        DialogLayout.BOTTOM)
    MAIN_CHARECTER = sprites.create(img("""
            . . . . f f f f . . . . . 
                                . . f f f f f f f f . . . 
                                . f f f f f f c f f f . . 
                                f f f f f f c c f f f c . 
                                f f f c f f f f f f f c . 
                                c c c f f f e e f f c c . 
                                f f f f f e e f f c c f . 
                                f f f b f e e f b f f f . 
                                . f 4 1 f 4 4 f 1 4 f . . 
                                . f e 4 4 4 4 4 4 e f . . 
                                . f f f e e e e f f f . . 
                                f e f b 7 7 7 7 b f 1 f . 
                                e 4 f 7 7 7 7 7 7 f 4 e . 
                                e e f 6 6 6 6 6 6 f e e . 
                                . . . f f f f f f . . . . 
                                . . . f f . . f f . . . .
        """),
        SpriteKind.player)
    MAIN_CHARECTER.set_position(26, 82)
    controller.move_sprite(MAIN_CHARECTER, 44, 47)
    teleporter2 = sprites.create(assets.image("""
            teleporter 3
        """),
        SpriteKind.teleporter)
    teleporter2.set_position(150, 53)
    game.splash("1st unit Completed")
    game.splash("2nd unit Tree Plantation")
    game.show_long_text("GO towards the Teleporter in the right corner.",
        DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.Automotive, on_on_overlap5)

def on_on_overlap6(sprite6, otherSprite6):
    game.set_dialog_frame(img("""
        ..66666666666666666666..
                        .6699999999999999999966.
                        669991111111111111199966
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        899911111111111111119996
                        869991111111111111199966
                        .6699999999999999999966.
                        ..66666666666666666666..
    """))
    game.show_long_text("OH, You came back!!", DialogLayout.BOTTOM)
    game.show_long_text("Did you bring the report back?", DialogLayout.BOTTOM)
    mc_2.set_position(77, 87)
    game.show_long_text(game.ask(""), DialogLayout.BOTTOM)
    game.show_long_text("Thank You for the report.", DialogLayout.BOTTOM)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.UNTIL_DONE)
    game.set_game_over_message(True, "YOU SAVED THE FUTURE!")
    game.game_over(True)
sprites.on_overlap(SpriteKind.mc2, SpriteKind.sci2, on_on_overlap6)

def on_on_overlap7(sprite7, otherSprite7):
    global tp_2
    game.set_dialog_frame(img("""
        999999999999999999999999999999999999999999999999
                        999999999999999999999999999999999999999999999999
                        999911119999119991111999111199999999119999999999
                        999111111191111911111191111119911191111991111999
                        999111111111111111111111111111111111111911111199
                        999111111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999991111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111111999
                        991111111111111111111111111111111111111111119999
                        991111111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111119999
                        999111111111111111111111111111111111111111111999
                        999911111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111999
                        991111111111111111111111111111111111111111119999
                        991111111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111999
                        991111111111111111111111111111111111111111119999
                        991111111111111111111111111111111111111111119999
                        999111111111111111111111111111111111111111111999
                        99d1111111111111111111111111111111111dd111111199
                        9ddd111111111111111111111111111111111dd111111199
                        9ddd1111111111dd111111111111111111111dd1111dd199
                        9d1d111111111ddddd11111111111ddddd111ddd111ddd99
                        9ddd111ddd111d111d1111ddddd11d111d11dddd111ddd99
                        9d1d11ddddd11ddddd1111ddddd11ddddd11d1dd111ddd99
                        9ddd11d1d1d11d111d1dd1d1ddd11d111d11dddddddddd99
                        9d1d11ddddd11ddddd1dd1ddd1d11ddddddddd1ddd111ddd
                        dddd11d1d1d11d111d1dd1ddddd11d111ddddddddddddddd
                        dd1d1ddddddddddddd1dd1d1ddddddddddddd1dddd111ddd
                        dddd1dd1d1dddd111dddddddd1dddd111ddddddddddddddd
                        dd1d1ddddddddddddddddddddddddddddddddd1ddd111ddd
                        ddddddddddddddddddddddd1dddddddddddddddddddddddd
                        ddddddddddddddddddddddddd1ddddddddddd1dddd111ddd
                        .dddddddddddddddddddddddddddddddddddddddddddddd.
                        ..dddddddddddddddddddddddddddddddddddddddddddd..
    """))
    game.show_long_text("Hello I am Emo robot.", DialogLayout.BOTTOM)
    game.show_long_text("I am selling saplings.", DialogLayout.BOTTOM)
    game.show_long_text("You want to plant some?", DialogLayout.BOTTOM)
    game.set_dialog_frame(img("""
        .....cccccccccccccc.....
                        ...cbd111111111111dbc...
                        ..cd1111111111111111dc..
                        .cd111111111111111111dc.
                        .311111111111111111111b.
                        cd11111111111111111111dc
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        cd11111111111111111111dc
                        .311111111111111111111b.
                        .c3111111111111111111dc.
                        ..cd1111111111111111dc..
                        ...cbd111d111d1111dbc...
                        .....cccccb1bcccccc.....
                        ..........c1c...........
                        ...........c............
    """))
    game.show_long_text(" Yes I want them.", DialogLayout.BOTTOM)
    game.set_dialog_frame(img("""
        999999999999999999999999999999999999999999999999
                        999999999999999999999999999999999999999999999999
                        999911119999119991111999111199999999119999999999
                        999111111191111911111191111119911191111991111999
                        999111111111111111111111111111111111111911111199
                        999111111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999991111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111111999
                        991111111111111111111111111111111111111111119999
                        991111111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111119999
                        999111111111111111111111111111111111111111111999
                        999911111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111999
                        991111111111111111111111111111111111111111119999
                        991111111111111111111111111111111111111111111999
                        999111111111111111111111111111111111111111111199
                        999911111111111111111111111111111111111111111199
                        999111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111199
                        991111111111111111111111111111111111111111111999
                        991111111111111111111111111111111111111111119999
                        991111111111111111111111111111111111111111119999
                        999111111111111111111111111111111111111111111999
                        99d1111111111111111111111111111111111dd111111199
                        9ddd111111111111111111111111111111111dd111111199
                        9ddd1111111111dd111111111111111111111dd1111dd199
                        9d1d111111111ddddd11111111111ddddd111ddd111ddd99
                        9ddd111ddd111d111d1111ddddd11d111d11dddd111ddd99
                        9d1d11ddddd11ddddd1111ddddd11ddddd11d1dd111ddd99
                        9ddd11d1d1d11d111d1dd1d1ddd11d111d11dddddddddd99
                        9d1d11ddddd11ddddd1dd1ddd1d11ddddddddd1ddd111ddd
                        dddd11d1d1d11d111d1dd1ddddd11d111ddddddddddddddd
                        dd1d1ddddddddddddd1dd1d1ddddddddddddd1dddd111ddd
                        dddd1dd1d1dddd111dddddddd1dddd111ddddddddddddddd
                        dd1d1ddddddddddddddddddddddddddddddddd1ddd111ddd
                        ddddddddddddddddddddddd1dddddddddddddddddddddddd
                        ddddddddddddddddddddddddd1ddddddddddd1dddd111ddd
                        .dddddddddddddddddddddddddddddddddddddddddddddd.
                        ..dddddddddddddddddddddddddddddddddddddddddddd..
    """))
    game.show_long_text("OK, so take them.", DialogLayout.BOTTOM)
    MAIN_CHARECTER.set_position(41, 90)
    tp_2 = sprites.create(assets.image("""
        teleporter 3
    """), SpriteKind.tp2)
    MAIN_CHARECTER.set_position(19, 96)
    tp_2.set_position(136, 97)
sprites.on_overlap(SpriteKind.player, SpriteKind.shopdi, on_on_overlap7)

def on_on_overlap8(sprite8, otherSprite8):
    MAIN_CHARECTER.set_position(82, 39)
    game.set_dialog_text_color(2)
    game.show_long_text("\"HI adventurer, I have a really important task for you!!!",
        DialogLayout.BOTTOM)
    MAIN_CHARECTER.set_position(43, 48)
    game.show_long_text("I have a time machine. You need to go in future to know our world there.   ",
        DialogLayout.BOTTOM)
    game.show_long_text("Make a research paper and bring it back to me. ",
        DialogLayout.BOTTOM)
    game.show_long_text("Move left to time travel in the future.",
        DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.NPC, SpriteKind.player, on_on_overlap8)

def on_b_pressed():
    global sandytile, Tree
    sandytile = tiles.location_of_sprite(mc_2)
    if tiles.tile_is(sandytile, assets.tile("""
        myTile2
    """)):
        Tree += 1
        tiles.set_tile_at(sandytile, sprites.builtin.forest_tiles0)
        effects.clouds.start_screen_effect(100)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

research_paper: Sprite = None
Tree = 0
teleporter2: Sprite = None
player_back: Sprite = None
tp_2: Sprite = None
mc_2: Sprite = None
shop: Sprite = None
VAN: Sprite = None
Main_charecter: Sprite = None
sandytile: tiles.Location = None
MAIN_CHARECTER: Sprite = None
Time_Machine: Sprite = None
scene.set_background_image(assets.image("""
    start
"""))
music.play(music.create_song(hex("""
        0078000408040200001c00010a006400f401640000040000000000000000000000000005000004060014001800011e06001c00010a006400f401640000040000000000000000000000000000000002740000000400012a0400080001220c001000021e2914001800012418001c00012a1c00200002192524002800021e242c003000021e2934003800021e273c004000021e2940004400012448004c00021e275000540002192758005c0001205c006000012a60006400012468006c000122700074000119
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.set_dialog_text_color(9)
game.splash("BIO OICONOMOS", "BY HYPER CODERS ")
game.set_dialog_text_color(6)
game.show_long_text("This game is made to spread awareness about Bio Diversity and our Enviroment.     Press A to continue.",
    DialogLayout.CENTER)
game.show_long_text("USE ARROW KEYS TO MOVE.      USE \"A\"and \"B\" TO INTERACT WITH OBJECTS.",
    DialogLayout.CENTER)
game.show_long_text("DO YOU WANT TO START THE ADVENTURE? PRESS \"A\" TO CONTINUE.",
    DialogLayout.FULL)
music.stop_all_sounds()
game.set_dialog_text_color(2)
scene.set_background_image(assets.image("""
    labh
"""))
Time_Machine = sprites.create(assets.image("""
        adam baba ki time machine
    """),
    SpriteKind.time_Machine)
Time_Machine.set_position(18, 53)
SCIENTIST = sprites.create(assets.image("""
    Scientistfi
"""), SpriteKind.NPC)
SCIENTIST.y = 32
MAIN_CHARECTER = sprites.create(img("""
        . . . . f f f f . . . . . 
                    . . f f f f f f f f . . . 
                    . f f f f f f c f f f . . 
                    f f f f f f c c f f f c . 
                    f f f c f f f f f f f c . 
                    c c c f f f e e f f c c . 
                    f f f f f e e f f c c f . 
                    f f f b f e e f b f f f . 
                    . f 4 1 f 4 4 f 1 4 f . . 
                    . f e 4 4 4 4 4 4 e f . . 
                    . f f f e e e e f f f . . 
                    f e f b 7 7 7 7 b f 1 f . 
                    e 4 f 7 7 7 7 7 7 f 4 e . 
                    e e f 6 6 6 6 6 6 f e e . 
                    . . . f f f f f f . . . . 
                    . . . f f . . f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(MAIN_CHARECTER, 44, 47)
game.show_long_text("Talk to the scientist.", DialogLayout.BOTTOM)

def on_forever():
    global research_paper
    if Tree == 60:
        research_paper = sprites.create(assets.image("""
            papad
        """), SpriteKind.paper)
        research_paper.set_position(155, 118)
forever(on_forever)
