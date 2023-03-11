namespace SpriteKind {
    export const NPC = SpriteKind.create()
    export const time_Machine = SpriteKind.create()
    export const vanannouncement = SpriteKind.create()
    export const Automotive = SpriteKind.create()
    export const playercbc = SpriteKind.create()
    export const teleporter = SpriteKind.create()
    export const shopdi = SpriteKind.create()
    export const tp2 = SpriteKind.create()
    export const mc2 = SpriteKind.create()
    export const pappad = SpriteKind.create()
    export const paper = SpriteKind.create()
    export const tm2 = SpriteKind.create()
    export const sci2 = SpriteKind.create()
    export const bottle = SpriteKind.create()
    export const bfielurg = SpriteKind.create()
}

namespace StatusBarKind {
    export const Sapplings = StatusBarKind.create()
    export const Saplings = StatusBarKind.create()
}

controller.combos.attachCombo("a+b", function my_function() {
    
    sandytile = tiles.locationOfSprite(Main_charecter)
    if (tiles.tileAtLocationEquals(sandytile, assets.tile`
        batli
    `)) {
        music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.UntilDone)
        tiles.setTileAt(sandytile, sprites.castle.tilePath5)
    } else if (tiles.tileAtLocationEquals(sandytile, assets.tile`
        myTile12
    `)) {
        music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.UntilDone)
        tiles.setTileAt(sandytile, sprites.castle.tilePath5)
    }
    
})
sprites.onOverlap(SpriteKind.time_Machine, SpriteKind.Player, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    
    Time_Machine = sprites.create(assets.image`
            adam baba ki time machine
        `, SpriteKind.time_Machine)
    sprites.destroyAllSpritesOfKind(SpriteKind.NPC)
    sprites.destroyAllSpritesOfKind(SpriteKind.time_Machine)
    music.play(music.melodyPlayable(music.buzzer), music.PlaybackMode.UntilDone)
    music.play(music.melodyPlayable(music.beamUp), music.PlaybackMode.InBackground)
    game.showLongText("STRAIGHT TO THE FUTURE IN 2050!!", DialogLayout.Bottom)
    music.play(music.melodyPlayable(music.buzzer), music.PlaybackMode.UntilDone)
    scene.cameraShake(6, 500)
    game.showLongText("YEAR 2050", DialogLayout.Left)
    MAIN_CHARECTER.setPosition(35, 106)
    scene.setBackgroundImage(assets.image`
        2050
    `)
    game.splash("1st you need to explore.")
    game.showLongText("Go to the van.", DialogLayout.Bottom)
    VAN = sprites.create(assets.image`
        van
    `, SpriteKind.Automotive)
    VAN.setPosition(90, 107)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.tp2, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    
    sprites.destroyAllSpritesOfKind(SpriteKind.shopdi)
    sprites.destroyAllSpritesOfKind(SpriteKind.teleporter)
    sprites.destroyAllSpritesOfKind(SpriteKind.tp2)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    shop.setPosition(15, 55)
    scene.setBackgroundImage(assets.image`
        last bg
    `)
    tiles.setCurrentTilemap(tilemap`
        level1
    `)
    mc_2 = sprites.create(img`
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
        `, SpriteKind.mc2)
    tp_2.setPosition(11, 48)
    controller.moveSprite(mc_2)
    scene.cameraFollowSprite(mc_2)
    game.showLongText("Plant saplings in the barren land.", DialogLayout.Bottom)
    game.showLongText("Press 'B' or 'enter' button to plant saplings.", DialogLayout.Bottom)
    game.showLongText("If you complete,you will get the half research report and continue.", DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.mc2, SpriteKind.paper, function on_on_overlap3(sprite3: Sprite, otherSprite3: Sprite) {
    
    tiles.destroySpritesOfKind(SpriteKind.mc2)
    tiles.destroySpritesOfKind(SpriteKind.paper)
    tiles.destroySpritesOfKind(SpriteKind.teleporter)
    tiles.destroySpritesOfKind(SpriteKind.Automotive)
    game.showLongText("Half Research Paper Accomplished", DialogLayout.Bottom)
    game.splash("UNIT⠀2⠀Completed")
    music.play(music.melodyPlayable(music.buzzer), music.PlaybackMode.UntilDone)
    effects.clouds.endScreenEffect()
    game.splash("UNIT⠀3⠀Garbage⠀Collection")
    game.showLongText("Press a+b⠀at⠀the⠀same⠀time to collect garbage. Put them in the bin after you have collected all of them. Then you'll get the full research report and save the Future.", DialogLayout.Bottom)
    scene.setBackgroundImage(img`
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
    `)
    tiles.loadMap(tiles.createMap(tilemap`
        beach
    `))
    Main_charecter = sprites.create(assets.image`
        tingu
    `, SpriteKind.Enemy)
    controller.moveSprite(Main_charecter)
    scene.cameraFollowSprite(Main_charecter)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.teleporter, function on_on_overlap4(sprite4: Sprite, otherSprite4: Sprite) {
    
    music.play(music.melodyPlayable(music.magicWand), music.PlaybackMode.UntilDone)
    scene.setBackgroundImage(assets.image`
        shop bg
    `)
    sprites.destroyAllSpritesOfKind(SpriteKind.teleporter)
    MAIN_CHARECTER.setPosition(84, 87)
    controller.moveSprite(MAIN_CHARECTER, 44, 47)
    shop = sprites.create(assets.image`
        Shop
    `, SpriteKind.shopdi)
    shop.setPosition(25, 63)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Automotive, function on_on_overlap5(sprite5: Sprite, otherSprite5: Sprite) {
    
    scene.setBackgroundImage(img`
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
    `)
    game.showLongText("Ohh! Are you the one from the past?? By the way it is 2050.", DialogLayout.Bottom)
    game.showLongText("I am the Scientist's worker and we have a laboratory here. ", DialogLayout.Bottom)
    game.showLongText("You need to send the report back to the present.", DialogLayout.Bottom)
    game.showLongText("Phone rings bzzzz.... bzzzzz.......", DialogLayout.Bottom)
    game.showLongText("You answer the phone.It was the scientist.You talk to him and continue.", DialogLayout.Bottom)
    game.showLongText("The scientist's worker takes you to their laboratory.", DialogLayout.Bottom)
    sprites.destroyAllSpritesOfKind(SpriteKind.Automotive)
    scene.setBackgroundImage(assets.image`
        Future Laboratory
    `)
    game.showLongText("You climb up the 100th floor by the lift and enter the control panel.", DialogLayout.Bottom)
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    player_back = sprites.create(assets.image`
        back pc
    `, SpriteKind.playercbc)
    player_back.setPosition(125, 75)
    scene.setBackgroundImage(assets.image`
        Control Panel
    `)
    player_back = sprites.create(assets.image`
        back pc
    `, SpriteKind.playercbc)
    sprites.destroyAllSpritesOfKind(SpriteKind.playercbc)
    game.showLongText(" OH ! The world is completely destroyed!! First I need to plant trees.", DialogLayout.Bottom)
    MAIN_CHARECTER = sprites.create(img`
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
        `, SpriteKind.Player)
    MAIN_CHARECTER.setPosition(26, 82)
    controller.moveSprite(MAIN_CHARECTER, 44, 47)
    teleporter2 = sprites.create(assets.image`
            teleporter 3
        `, SpriteKind.teleporter)
    teleporter2.setPosition(150, 53)
    game.splash("1st unit Completed")
    game.splash("2nd unit Tree Plantation")
    game.showLongText("GO towards the Teleporter in the right corner.", DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.mc2, SpriteKind.sci2, function on_on_overlap6(sprite6: Sprite, otherSprite6: Sprite) {
    game.setDialogFrame(img`
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
    `)
    game.showLongText("OH, You came back!!", DialogLayout.Bottom)
    game.showLongText("Did you bring the report back?", DialogLayout.Bottom)
    mc_2.setPosition(77, 87)
    game.showLongText(game.ask(""), DialogLayout.Bottom)
    game.showLongText("Thank You for the report.", DialogLayout.Bottom)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
    game.setGameOverMessage(true, "YOU SAVED THE FUTURE!")
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.shopdi, function on_on_overlap7(sprite7: Sprite, otherSprite7: Sprite) {
    
    game.setDialogFrame(img`
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
    `)
    game.showLongText("Hello I am Emo robot.", DialogLayout.Bottom)
    game.showLongText("I am selling saplings.", DialogLayout.Bottom)
    game.showLongText("You want to plant some?", DialogLayout.Bottom)
    game.setDialogFrame(img`
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
    `)
    game.showLongText(" Yes I want them.", DialogLayout.Bottom)
    game.setDialogFrame(img`
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
    `)
    game.showLongText("OK, so take them.", DialogLayout.Bottom)
    MAIN_CHARECTER.setPosition(41, 90)
    tp_2 = sprites.create(assets.image`
        teleporter 3
    `, SpriteKind.tp2)
    MAIN_CHARECTER.setPosition(19, 96)
    tp_2.setPosition(136, 97)
})
sprites.onOverlap(SpriteKind.NPC, SpriteKind.Player, function on_on_overlap8(sprite8: Sprite, otherSprite8: Sprite) {
    MAIN_CHARECTER.setPosition(82, 39)
    game.setDialogTextColor(2)
    game.showLongText("\"HI adventurer, I have a really important task for you!!!", DialogLayout.Bottom)
    MAIN_CHARECTER.setPosition(43, 48)
    game.showLongText("I have a time machine. You need to go in future to know our world there.   ", DialogLayout.Bottom)
    game.showLongText("Make a research paper and bring it back to me. ", DialogLayout.Bottom)
    game.showLongText("Move left to time travel in the future.", DialogLayout.Bottom)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    sandytile = tiles.locationOfSprite(mc_2)
    if (tiles.tileIs(sandytile, assets.tile`
        myTile2
    `)) {
        Tree += 1
        tiles.setTileAt(sandytile, sprites.builtin.forestTiles0)
        effects.clouds.startScreenEffect(100)
    }
    
})
let research_paper : Sprite = null
let Tree = 0
let teleporter2 : Sprite = null
let player_back : Sprite = null
let tp_2 : Sprite = null
let mc_2 : Sprite = null
let shop : Sprite = null
let VAN : Sprite = null
let Main_charecter : Sprite = null
let sandytile : tiles.Location = null
let MAIN_CHARECTER : Sprite = null
let Time_Machine : Sprite = null
scene.setBackgroundImage(assets.image`
    start
`)
music.play(music.createSong(hex`
        0078000408040200001c00010a006400f401640000040000000000000000000000000005000004060014001800011e06001c00010a006400f401640000040000000000000000000000000000000002740000000400012a0400080001220c001000021e2914001800012418001c00012a1c00200002192524002800021e242c003000021e2934003800021e273c004000021e2940004400012448004c00021e275000540002192758005c0001205c006000012a60006400012468006c000122700074000119
    `), music.PlaybackMode.LoopingInBackground)
game.setDialogTextColor(9)
game.splash("BIO OICONOMOS", "BY HYPER CODERS ")
game.setDialogTextColor(6)
game.showLongText("This game is made to spread awareness about Bio Diversity and our Enviroment.     Press A to continue.", DialogLayout.Center)
game.showLongText("USE ARROW KEYS TO MOVE.      USE \"A\"and \"B\" TO INTERACT WITH OBJECTS.", DialogLayout.Center)
game.showLongText("DO YOU WANT TO START THE ADVENTURE? PRESS \"A\" TO CONTINUE.", DialogLayout.Full)
music.stopAllSounds()
game.setDialogTextColor(2)
scene.setBackgroundImage(assets.image`
    labh
`)
Time_Machine = sprites.create(assets.image`
        adam baba ki time machine
    `, SpriteKind.time_Machine)
Time_Machine.setPosition(18, 53)
let SCIENTIST = sprites.create(assets.image`
    Scientistfi
`, SpriteKind.NPC)
SCIENTIST.y = 32
MAIN_CHARECTER = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(MAIN_CHARECTER, 44, 47)
game.showLongText("Talk to the scientist.", DialogLayout.Bottom)
forever(function on_forever() {
    
    if (Tree == 60) {
        research_paper = sprites.create(assets.image`
            papad
        `, SpriteKind.paper)
        research_paper.setPosition(155, 118)
    }
    
})
