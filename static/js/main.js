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

    $('#track-container button').on('click', (e) => {
        $('.lyrics-overlay').show()
        let h2 = document.createElement('h2')
        let p = document.createElement('p')
        h2.setAttribute('id', 'title')
        h2.innerHTML ='lyrics here'

    })


    $('#search').on('click', (e) => {
        e.preventDefault()
        $('.search-overlay').show()

    })

    $('.close').on('click', (e) => {
        //e.preventDefault()
        $('.search-overlay, .lyrics-overlay').hide()

    })

})