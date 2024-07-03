# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
# scene 1.1
image bg scene1 = im.Scale("images/scene/Scene Intro 1 step1.jpg", config.screen_width, config.screen_height)
image bg scene2 = im.Scale("images/scene/Scene Intro 1 step2.jpg", config.screen_width, config.screen_height)
image bg scene3 = im.Scale("images/scene/Scene Intro 2 step1.jpg", config.screen_width, config.screen_height)
image bg scene4 = im.Scale("images/scene/Scene Intro 2 step2.jpg", config.screen_width, config.screen_height)
image bg scene5 = im.Scale("images/scene/Scene Intro 3.jpg", config.screen_width, config.screen_height)
image bg scene6 = im.Scale("images/scene/Scene Intro 4 step1.jpg", config.screen_width, config.screen_height)
image bg scene7 = im.Scale("images/scene/Scene Intro 4 step2.jpg", config.screen_width, config.screen_height)
image bg scene8 = im.Scale("images/scene/Scene Intro 5 step1.jpg", config.screen_width, config.screen_height)
image bg scene9 = im.Scale("images/scene/Scene Intro 5 step2.jpg", config.screen_width, config.screen_height)
image bg scene10 = im.Scale("images/scene/Scene Intro 6 step1.jpg", config.screen_width, config.screen_height)
image bg scene11 = im.Scale("images/scene/Scene Intro 6 step2.jpg", config.screen_width, config.screen_height)
image bg scene12 = im.Scale("images/scene/Scene Intro 6 step3.jpg", config.screen_width, config.screen_height)
image bg scene13 = im.Scale("images/scene/Scene Intro 6 step4.jpg", config.screen_width, config.screen_height)
image bg scene14 = im.Scale("images/scene/Scene Intro 7.jpg", config.screen_width, config.screen_height)
image bg scene15 = im.Scale("images/scene/Scene Intro 8.jpg", config.screen_width, config.screen_height)
image bg scene16 = im.Scale("images/scene/Scene Intro 9.jpg", config.screen_width, config.screen_height)
image bg scene17 = im.Scale("images/padlock/scene padlock locked 4.jpg", config.screen_width, config.screen_height)

image bg scene_end_1 = im.Scale("images/ending/scene ending 1.jpg", config.screen_width, config.screen_height)
image bg scene_end_2 = im.Scale("images/ending/scene ending 2.jpg", config.screen_width, config.screen_height)
image bg scene_end_3 = im.Scale("images/ending/scene ending 3.jpg", config.screen_width, config.screen_height)
image bg scene_end_4 = im.Scale("images/ending/scene ending 4.jpg", config.screen_width, config.screen_height)

# scene hallway
# image bg sceneHallway = im.Scale("images/bg/hallway.jpg", config.screen_width, config.screen_height)
# image bg sceneHallwayFinal = im.Scale("images/bg/hallway_final.jpg", config.screen_width, config.screen_height)


#scene gameover
image bg gameover_ips = im.Scale("images/game_over/dead_ips.jpg", config.screen_width, config.screen_height)
image bg gameover_ipa = im.Scale("images/game_over/dead_ipa.jpg", config.screen_width, config.screen_height)
image bg gameover_indonesia = im.Scale("images/game_over/dead_indonesia.jpg", config.screen_width, config.screen_height)
image bg gameover_mtk = im.Scale("images/game_over/dead_mtk.jpg", config.screen_width, config.screen_height)


define g = Character("Teacher")
define m = Character("Student")
define h = Character("Hadi")

# board
image bg board_ips = im.Scale("images/board/board_ips.jpg", config.screen_width, config.screen_height)
image bg board_ipa = im.Scale("images/board/board_ipa.jpg", config.screen_width, config.screen_height)
image bg board_indonesia = im.Scale("images/board/board_indonesia.jpg", config.screen_width, config.screen_height)
image bg board_mtk = im.Scale("images/board/board_mtk.jpg", config.screen_width, config.screen_height)

# teacher ips
image teacher_ips = im.Scale("images/character/teacher_ips.png", config.screen_width, config.screen_height)

#teacher ipa
image teacher_ipa = im.Scale("images/character/teacher_ipa.png", config.screen_width, config.screen_height)

#teacher mtk
image teacher_indonesia = im.Scale("images/character/teacher_indonesia.png", config.screen_width, config.screen_height)

#teacher mtk
image teacher_mtk = im.Scale("images/character/teacher_mtk.png", config.screen_width, config.screen_height)

image heart_full =  im.Scale("images/heart/heart_full.png", 100, 100)
image heart_empty = im.Scale("images/heart/heart_empty.png", 100, 100)

image bg lock_0 = im.Scale("images/padlock/scene padlock locked 0.jpg", config.screen_width, config.screen_height)
image bg lock_1 = im.Scale("images/padlock/scene padlock locked 1.jpg", config.screen_width, config.screen_height)
image bg lock_2 = im.Scale("images/padlock/scene padlock locked 2.jpg", config.screen_width, config.screen_height)
image bg lock_3 = im.Scale("images/padlock/scene padlock locked 3.jpg", config.screen_width, config.screen_height)
image bg lock_4 = im.Scale("images/padlock/scene padlock locked 4.jpg", config.screen_width, config.screen_height)

# Screen to display player's lives
default lives = 3
default learned_class_ips = "false"
default learned_class_ipa = "false"
default learned_class_indonesia = "false"
default learned_class_mtk = "false"

#sound music
default quiz_music = "audio/music_game/quiz_music.mp3"
default game_over_music = "audio/music_game/game_over.mp3"
default ending_game = "audio/music_game/ending_game.mp3"
default ending_next = "audio/music_game/ending_next.mp3"


#sound effect
default answer_true = "audio/sound_game/click-melodic-tone.mp3"
default answer_false = "audio/sound_game/negative-tone-interface-tap.mp3"
default click = "audio/sound_game/classic-click.mp3"

default keys = 0
default gameOver = "false"

screen life():
    hbox:
        xalign 0.05
        yalign 0.05
        spacing 5
        if lives >= 1:
            add "heart_full"
        else:
            add "heart_empty"
        if lives >= 2:
            add "heart_full"
        else:
            add "heart_empty"
        if lives >= 3:
            add "heart_full"
        else:
            add "heart_empty"

# start scene
label start:
    scene bg scene1 with fade
    "Suatu hari di sebuah ruangan sekolah yang tenang dan damai."

    scene bg scene2 
    "Tiba-tiba dari ventilasi mengeluarkan asap hijau."

    scene bg scene3 with fade
    "Di dalam kelas, seorang guru sedang mengajar seperti biasa."

    scene bg scene4 
    "Ternyata asap hijau itu masuk kedalam kelas, sehingga guru menghirupnya."

    scene bg scene5 with fade
    "Hadi yang baru saja keluar dari Toilet mengobrol dengan temannya didepan toilet, membicarakan ada sesuatu yang aneh dari asap hijau dikelas."

    h "Sepertinya ada yang aneh dari asap itu, akan tetapi kita tidak apa apa"
    m "Aku juga mengiranya seperti itu karena sepertinya ada yang aneh dari tingkah laku guru kita"
    h "seperti nya asap itu hanya mempengaruhi para guru deh..."
    m "Benar aku jadi tidak ingin masuk kelas lagi"

    scene bg scene6 with fade
    "Tiba-tiba seorang guru muncul."
    scene bg scene7 
    "Lalu Mendekati murid yang sedang berbicara dengan hadi."
    scene bg scene8 
    m "aaaa...."
    g "Apa yang kamu katakan, ayo ikut ibu kedalam kelas"
    "Guru tersebut mencubit dan menarik salah satu murid dengan keras."
    scene bg scene9 
    "Hadi pun terkejut dan terdiam, tidak tahu harus berbuat apa."

    scene bg scene10 with fade
    m "tolong..." 
    "Murid tersebut ditarik oleh guru ke dalam kelas dan murid tersebut meminta tolong kepada hadi."
    scene bg scene11
    m "tolong..." 
    "Murid terus dipaksa dan ditarik, merasa tidak berdaya."
    scene bg scene12
    m "tolong..." 
    "Guru tidak berhenti, murid tersebut dipaksa masuk ke dalam kelas."
    scene bg scene13
    "Akhirnya murid tersebut berhasil dibawa kembali ke dalam kelas"
    "hadi pun terkejut melihat temannya diseret seperti itu oleh guru yang gila"
    "lalu ia segera melihat temannya dari kaca"

    scene bg scene14 with fade
    "ternyata... Hadi melihat Guru memaksa murid belajar dan menjawab soal dengan benar."

    scene bg scene15 with fade
    "Hadi yang melihat kejadian tersebut berlari ketakutan."

    scene bg scene16 
    "Hadi yang melarikan diri mencoba membuka pintu keluar dari sekolah."
    "Akan tetapi pintu sekolah tersebut tidak dapat dibuka."

    scene bg scene17 
    "ternyata pintu tersebut digembok sebanyak 4 gembok."
    "Oleh karena itu ia harus masuk ke beberapa kelas karena ia tau masing masing guru memiliki 1 kunci untuk membuka gembok"
    h "Aku Pasti Bisa Keluar Aku harus melewati semuanya..."
    

 
label class_ips:
    play music quiz_music loop volume 0.5
    $ score = 0
    # $ wrong_answers = 0
    scene bg board_ips with fade
    "kamu tiba dikelas IPS Silahkan bersiap!"
    "Pastikan kamu sudah siap menjawab semua pertanyaan ini"
    show teacher_ips at right 
    show screen life

    g "Hai kelas! Hari ini kita akan ada kuis. Mari kita lihat seberapa baik kalian menjawab pertanyaan aneh ini."

    # Pertanyaan 1
    g "Pertanyaan 1: Apa ibu kota dari negara Unicornia?"
    menu:
        "Rainbow City":
            $ score += 1
            play sound answer_true
            g "Benar! Rainbow City adalah ibu kota negara Unicornia yang hanya ada dalam imajinasi."
        "Magic Town":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan Magic Town."
        "Fantasia":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan Fantasia."
        "Dreamland":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan Dreamland."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 2
    g "Pertanyaan 2: Jika samudra Atlantik adalah tempat tinggal ikan paus, maka siapa yang tinggal di samudra Pasifik?"
    menu:
        "Dinosaurus":
            $ lives -= 1
            play sound answer_false
            g "Salah! Dinosaurus tidak tinggal di samudra."
        "Mermaid":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, kita membayangkan bahwa mermaid tinggal di samudra Pasifik."
        "Alien":
            $ lives -= 1
            play sound answer_false
            g "Salah! Alien tidak tinggal di samudra."
        "Robot":
            $ lives -= 1
            play sound answer_false
            g "Salah! Robot tidak tinggal di samudra."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 3
    g "Pertanyaan 3: Jika benua Antartika adalah kue es krim, apa benua Afrika?"
    menu:
        "Pizza":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan pizza."
        "Donat":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, kita membayangkan benua Afrika sebagai donat."
        "Burger":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan burger."
        "Pasta":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan pasta."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 4
    g "Pertanyaan 4: Jika gunung Everest adalah coklat, maka gunung Kilimanjaro adalah apa?"
    menu:
        "Permen":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan permen."
        "Es Krim":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, kita membayangkan gunung Kilimanjaro sebagai es krim."
        "Biskuit":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan biskuit."
        "Kue":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan kue."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 5
    g "Pertanyaan 5: Jika sungai Nil adalah tali, maka sungai Amazon adalah apa?"
    menu:
        "Benang":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan benang."
        "Tali Jemuran":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, kita membayangkan sungai Amazon sebagai tali jemuran."
        "Pita":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan pita."
        "Rantai":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan rantai."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 6
    g "Pertanyaan 6: Jika Paris adalah kota bunga, maka Tokyo adalah kota apa?"
    menu:
        "Kucing":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, kita membayangkan Tokyo sebagai kota kucing."
        "Ikan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan ikan."
        "Burung":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan burung."
        "Anjing":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan anjing."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame
        

    # if score >= 5:
    hide screen life
    scene bg scene15 
    if learned_class_ips != "true":
        $ keys += 1
        "Selamat! Kalian telah mendapatkan kunci!"
        
    $ learned_class_ips = "true"
    "Sekarang kita lanjut Berlari untuk pergi ke gerbang."
    stop music

label scene_indonesia:

    show bg lock_3 with fade
    "Anda Telah Membuka 1 kunci gembok silahkan lajutkan game ini untuk mendapatkan gembok selanjutnya."
    "Mari Kita ke guru selanjutnya."
    
 
label class_indonesia:
    play music quiz_music loop volume 0.5
    $ score = 0
    $ lives = 3
    # $ wrong_answers = 0
    scene bg board_indonesia with fade

    "kamu tiba dikelas Bahasa Indonesia Silahkan bersiap!"
    "Pastikan kamu sudah siap menjawab semua pertanyaan ini"

    show teacher_indonesia at right 
    show screen life

    g "Hai Murid-Murid! Hari ini kita akan ada kuis. Mari kita lihat seberapa baik kalian menjawab pertanyaan saya."

    # Pertanyaan 1
    g "Pertanyaan 1: Apa sinonim dari kata 'meong' dalam bahasa Indonesia jika kucing bisa bicara?"
    menu:
        "Berkicau":
            $ lives -= 1
            play sound answer_false
            g "Salah! Berkicau adalah suara burung."
        "Menggonggong":
            $ lives -= 1
            play sound answer_false
            g "Salah! Menggonggong adalah suara anjing."
        "Menggeram":
            $ lives -= 1
            play sound answer_false
            g "Salah! Menggeram adalah suara harimau."
        "Halo":
            $ score += 1
            play sound answer_true
            g "Benar! Jika kucing bisa bicara, 'meong' mungkin berarti 'halo'."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 2
    g "Pertanyaan 2: Apa arti kata 'buku' jika semua buku di dunia tiba-tiba berubah menjadi ikan?"
    menu:
        "Kumpulan tulisan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Buku tidak lagi berisi tulisan."
        "Sumber ilmu":
            $ lives -= 1
            play sound answer_false
            g "Salah! Buku sekarang adalah ikan."
        "Ikan":
            $ score += 1
            play sound answer_true
            g "Benar! Jika semua buku berubah menjadi ikan, 'buku' berarti 'ikan'."
        "Alat tulis":
            $ lives -= 1
            play sound answer_false
            g "Salah! Buku bukan lagi alat tulis."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 3
    g "Pertanyaan 3: Bagaimana cara menulis puisi jika semua kata dalam bahasa Indonesia digantikan dengan angka?"
    menu:
        "Menggunakan imajinasi":
            $ lives -= 1
            play sound answer_false
            g "Salah! Menggunakan angka bukan imajinasi."
        "Menggunakan kalkulator":
            $ score += 1
            play sound answer_true
            g "Benar! Jika semua kata digantikan angka, puisi ditulis dengan kalkulator."
        "Menggunakan kamus":
            $ lives -= 1
            play sound answer_false
            g "Salah! Kamus tidak berguna jika kata-kata berubah menjadi angka."
        "Menggunakan huruf Arab":
            $ lives -= 1
            play sound answer_false
            g "Salah! Soal tentang angka, bukan huruf Arab."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 4
    g "Pertanyaan 4: Apa arti 'merah' jika pelangi hanya terdiri dari satu warna?"
    menu:
        "Warna yang terlihat":
            $ lives -= 1
            play sound answer_false
            g "Salah! Pelangi hanya satu warna."
        "Tidak ada warna":
            $ score += 1
            play sound answer_true
            g "Benar! Jika pelangi satu warna, 'merah' tidak ada."
        "Semua warna":
            $ lives -= 1
            play sound answer_false
            g "Salah! Pelangi hanya satu warna."
        "Warna biru":
            $ lives -= 1
            play sound answer_false
            g "Salah! Pertanyaan tentang warna merah."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 5
    g "Pertanyaan 5: Apa yang akan terjadi jika semua huruf vokal dalam bahasa Indonesia digantikan dengan angka?"
    menu:
        "Bahasa Indonesia akan lebih mudah":
            $ lives -= 1
            play sound answer_false
            g "Salah! Bahasa akan menjadi lebih sulit."
        "Bahasa Indonesia akan menjadi lebih sulit":
            $ score += 1
            play sound answer_true
            g "Benar! Menggantikan huruf vokal dengan angka membuat bahasa sulit."
        "Tidak ada perubahan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Pasti ada perubahan."
        "Bahasa Indonesia akan menjadi bahasa rahasia":
            $ lives -= 1
            play sound answer_false
            g "Salah! Ini tidak membuat bahasa menjadi rahasia."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame
        

    # if score >= 5:
    hide screen life
    scene bg scene15 
    if learned_class_indonesia != "true":
        $ keys += 1
        "Selamat! Kalian telah mendapatkan kunci!"
        
    $ learned_class_indonesia = "true"
    "Sekarang kita lanjut Berlari untuk pergi ke gerbang."
    stop music
        

label scene_ipa:

    show bg lock_2 with fade
    "Selamat Anda Telah Membuka 2 kunci gembok silahkan lajutkan game ini untuk mendapatkan gembok selanjutnya."
    "Mari Kita ke guru selanjutnya."
    
 
label class_ipa:
    play music quiz_music loop volume 0.5
    $ score = 0
    $ lives = 3
    # $ wrong_answers = 0
    scene bg board_ipa with fade
    "Selamat sekarang kamu tiba di kelas ipa untuk bisa melewati guru lagi"
    "Silahkan Menjawab Pertanyaan nya"
    show teacher_ipa at right 
    show screen life

    g "Hai Murid Murid kesayanganku! Hari ini kita akan ada kuis. Mari kita lihat seberapa baik kalian menjawab ."

    # Pertanyaan 1
    g "Pertanyaan 1: Berapa jumlah planet dalam Tata Surya kita jika Mars tiba-tiba berubah menjadi pizza?"
    menu:
        "Delapan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Mars tidak lagi dihitung sebagai planet."
        "Tujuh":
            $ score += 1
            play sound answer_true
            g "Benar! Jika Mars berubah menjadi pizza, kita hanya memiliki tujuh planet yang tersisa."
        "Sembilan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jumlah planet tidak bertambah."
        "Enam":
            $ lives -= 1
            play sound answer_false
            g "Salah! Mars hanya satu planet yang berubah."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 2
    g "Pertanyaan 2: Apa unsur kimia dengan simbol 'X' yang ditemukan oleh alien?"
    menu:
        "Xenon":
            $ lives -= 1
            play sound answer_false
            g "Salah! Xenon ada di bumi, bukan ditemukan oleh alien."
        "Xylophonium":
            $ lives -= 1
            play sound answer_false
            g "Salah! Itu hanya ada di cerita fiksi."
        "Xenomorphium":
            $ score += 1
            play sound answer_true
            g "Benar! Ini adalah unsur fiktif yang ditemukan oleh alien."
        "Xylenium":
            $ lives -= 1
            play sound answer_false
            g "Salah! Tidak ada unsur kimia seperti itu."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 3
    g "Pertanyaan 3: Apa fungsi dari klorofil pada tumbuhan jika tumbuhan itu adalah robot?"
    menu:
        "Menghasilkan energi dari matahari":
            $ lives -= 1
            play sound answer_false
            g "Salah! Robot tidak menggunakan klorofil."
        "Menghasilkan sinyal radio":
            $ lives -= 1
            play sound answer_false
            g "Salah! Robot juga tidak melakukan itu."
        "Tidak ada fungsi":
            $ score += 1
            play sound answer_true
            g "Benar! Klorofil tidak memiliki fungsi pada tumbuhan yang adalah robot."
        "Mengubah sinar matahari menjadi baterai":
            $ lives -= 1
            play sound answer_false
            g "Salah! Tidak ada klorofil pada robot."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 4
    g "Pertanyaan 4: Jika bumi tiba-tiba terbuat dari marshmallow, berapa banyak kilogram manusia yang akan ada di angkasa?"
    menu:
        "Semua manusia":
            $ score += 1
            play sound answer_true
            g "Benar! Karena bumi terbuat dari marshmallow, semua manusia akan melayang ke angkasa."
        "Tidak ada":
            $ lives -= 1
            play sound answer_false
            g "Salah! Semua manusia akan melayang."
        "Hanya astronaut":
            $ lives -= 1
            play sound answer_false
            g "Salah! Bukan hanya astronaut yang melayang."
        "Setengah populasi":
            $ lives -= 1
            play sound answer_false
            g "Salah! Seluruh manusia akan melayang."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 5
    g "Pertanyaan 5: Jika bulan terbuat dari keju, apa yang akan terjadi pada pasang surut air laut?"
    menu:
        "Tidak ada perubahan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Pasang surut air laut akan terpengaruh."
        "Air laut akan berasa asin dan gurih":
            $ lives -= 1
            play sound answer_false
            g "Salah! Air laut tetap asin saja."
        "Pasang surut akan menjadi kacau":
            $ score += 1
            play sound answer_true
            g "Benar! Gravitasi bulan yang berubah akan mengacaukan pasang surut air laut."
        "Air laut akan mengering":
            $ lives -= 1
            play sound answer_false
            g "Salah! Pasang surut saja yang berubah."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 6
    g "Pertanyaan 6: Jika matahari berubah menjadi bola diskotik raksasa, apa yang akan terjadi pada siang dan malam?"
    menu:
        "Malam akan penuh warna":
            $ lives -= 1
            play sound answer_false
            g "Salah! Siang dan malam akan berubah."
        "Siang akan seperti pesta":
            $ score += 1
            play sound answer_true
            g "Benar! Siang akan seperti pesta dengan cahaya warna-warni."
        "Malam akan menjadi lebih gelap":
            $ lives -= 1
            play sound answer_false
            g "Salah! Matahari menjadi bola diskotik akan mempengaruhi siang."
        "Tidak ada perubahan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Matahari berubah akan mempengaruhi bumi."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame
        

    # if score >= 5:
    hide screen life
    scene bg scene15 
    if learned_class_ipa != "true":
        $ keys += 1
        "Selamat! Kalian telah mendapatkan kunci!"
        
    $ learned_class_ipa = "true"
    "Sekarang kita lanjut Berlari untuk pergi ke gerbang."
    stop music
    
label scene_mtk:

    show bg lock_1 with fade
    "Selamat Anda Telah Membuka 3 kunci gembok, ayo semangat tinggal 1 kunci lagi, silahkan lajutkan game ini untuk mendapatkan gembok selanjutnya."
    "Mari Kita ke guru selanjutnya."
    
 
label class_mtk:
    play music quiz_music loop volume 0.5
    $ score = 0
    $ lives = 3
    # $ wrong_answers = 0
    scene bg board_mtk 

    "kamu tiba dikelas matematika untuk mencari kunci terakhir"
    "berbeda dengan sebelumnya kamu sudah siap menjawab semua pertanyaan ini"

    show teacher_mtk at right 
    show screen life

    g "Hai kelas! Hari ini kita akan ada kuis. Mari kita lihat seberapa baik kalian menjawab pertanyaan dari saya."

    # Pertanyaan 1
    g "Pertanyaan 1: Jika tiga ditambah lima sama dengan kucing, maka apa hasil dari empat ditambah enam?"
    menu:
        "Kucing":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan kucing."
        "Anjing":
            $ score += 1
            play sound answer_true
            g "Benar! Karena dalam soal ini, kita mengikuti logika yang tidak masuk akal."
        "Delapan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan delapan."
        "Sepuluh":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan sepuluh."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 2
    g "Pertanyaan 2: Berapa hasil dari lima belas dikurangi dengan sepuluh jika di dunia ini semua angka genap adalah hewan?"
    menu:
        "Lima":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan lima."
        "Hewan":
            $ score += 1
            play sound answer_true
            g "Benar! Karena dalam soal ini, lima belas dikurangi sepuluh adalah hewan."
        "Sepuluh":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan sepuluh."
        "Nol":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan nol."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 3
    g "Pertanyaan 3: Jika dua kali dua sama dengan apel, maka apa hasil dari tiga kali tiga?"
    menu:
        "Apel":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan apel."
        "Pisang":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, hasil perkalian adalah buah."
        "Sembilan":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan sembilan."
        "Enam":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan enam."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 4
    g "Pertanyaan 4: Jika sebuah lingkaran bisa mengubah warna, apa hasil dari mengalikan merah dengan biru?"
    menu:
        "Hijau":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan hijau."
        "Ungu":
            $ score += 1
            play sound answer_true
            g "Benar! Mengalikan merah dengan biru menghasilkan ungu."
        "Merah":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan merah."
        "Biru":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan biru."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 5
    g "Pertanyaan 5: Apa hasil dari dua ditambah dua jika hasilnya adalah seekor gajah?"
    menu:
        "Empat":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan empat."
        "Seekor Gajah":
            $ score += 1
            play sound answer_true
            g "Benar! Dalam soal ini, dua ditambah dua adalah seekor gajah."
        "Lima":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan lima."
        "Tiga":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan tiga."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame

    # Pertanyaan 6
    g "Pertanyaan 6: Jika semua bilangan prima adalah warna, berapa jumlah warna antara satu dan sepuluh?"
    menu:
        "Empat":
            $ score += 1
            play sound answer_true
            g "Benar! Bilangan prima antara satu dan sepuluh adalah dua, tiga, lima, dan tujuh."
        "Tiga":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan tiga."
        "Lima":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan lima."
        "Dua":
            $ lives -= 1
            play sound answer_false
            g "Salah! Jawabannya bukan dua."

    # Cek jika sudah kalah
    if lives < 1:
        $ gameOver = "true"
        jump endGame
        

    # if score >= 5:
    hide screen life
    
    scene bg scene15 
    if learned_class_mtk != "true":
        $ keys += 1
        "Selamat! Kalian telah mendapatkan kunci!"
        
    $ learned_class_mtk = "true"
    "Sekarang kita lanjut Berlari untuk pergi ke gerbang."
    stop music

label end_class:    
    show bg lock_0 with fade
    "Selamat Anda Telah Membuka Semua kunci gembok"

label endGame:
    stop music
    $ keys = 0
    $ lives = 3
    hide screen life
    if gameOver == "true":
        play music game_over_music
        if learned_class_ips == "false":
            scene bg gameover_ips 
            "Game over! Kalian telah menjawab salah 3 kali dan kalah."
            $ keys = 0
            menu:
                "Bermain lagi":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"

                    $ gameOver = "false"
                    $ lives = 3
                    stop music
                    jump start  # Kembali ke awal permainan
                "Kembali ke menu utama":
                    play sound click

                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"
                    "Game Over!"
                    stop music
                    return
        elif learned_class_indonesia == "false":
            scene bg gameover_indonesia 
            "Game over! Kalian telah menjawab salah 3 kali dan kalah."
            $ keys = 0
            menu:
                "Bermain lagi":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"

                    $ gameOver = "false"
                    $ lives = 3
                    stop music
                    jump start  # Kembali ke awal permainan
                "Kembali ke menu utama":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"
                    "Game Over!"
                    stop music
                    return
        elif learned_class_ipa == "false":
            scene bg gameover_ipa 
            "Game over! Kalian telah menjawab salah 3 kali dan kalah."
            $ keys = 0
            menu:
                "Bermain lagi":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"

                    $ gameOver = "false"
                    $ lives = 3
                    stop music
                    jump start  # Kembali ke awal permainan
                "Kembali ke menu utama":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"
                    "Game Over!"
                    stop music
                    return
        elif learned_class_mtk == "false":
            scene bg gameover_mtk 
            "Game over! Kalian telah menjawab salah 3 kali dan kalah."
            $ keys = 0
            menu:
                "Bermain lagi":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"

                    $ gameOver = "false"
                    $ lives = 3
                    stop music
                    jump start  # Kembali ke awal permainan
                "Kembali ke menu utama":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"
                    "Game Over!"
                    stop music
                    return
        else:
            scene bg gameover_mtk 
            "Game over! Kalian telah menjawab salah 3 kali dan kalah."
            $ keys = 0
            $ lives = 3
            $ gameOver = "true"
            menu:
                "Bermain lagi":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"
                    $ gameOver = "false"
                    $ lives = 3
                    stop music
                    jump start  # Kembali ke awal permainan
                "Kembali ke menu utama":
                    play sound click
                    $ learned_class_ips = "false"
                    $ learned_class_indonesia = "false"
                    $ learned_class_ipa = "false"
                    $ learned_class_mtk = "false"
                    "Game Over!"
                    stop music
                    return
    else:
        play music ending_game
        show bg scene_end_1 with fade
        "Selamat kamu Berhasil Membuka Gerbang"
        h "Akhirnya....."
        stop music
        play music ending_next
        "Akan Tetapi...."
        "Hadi pun terhenti karena ia melihat sesuatu yang tidak ia perkirakan..."
        show bg scene_end_2 with fade
        m "huaaaaa......"
        "Ternyata ia melihat nya ada siswa yang sudah diluar akan tetapi ada guru lain lagi yang ternyata diluar juga terkena efek dari asap hijau"
        show bg scene_end_3 with fade
        "anak yang diluar pun dibuat pingsan oleh guru tersebut"
        g "hehehe... mau kemana kamu hadi ayo masuk sekolah"
        show bg scene_end_4 with fade
        h "A aa apa ini...."
        stop music
    return