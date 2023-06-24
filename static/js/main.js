$(() => {
    $('#playlist-button').on('click', (e) => {
         $('.jukebox-container .songs').hide()
         $('.jukebox-container .playlists').show()
    })
    $('#song-button').on('click', (e) => {
        $('.jukebox-container .playlists').hide()
        $('.jukebox-container .songs').show()
    })

    $('.jukebox-container .songs .artist').on('click', (e) => {
        $('#footer-content ul, #footer-content p').remove()
    })
})