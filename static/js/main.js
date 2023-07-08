$(() => {
    $('#playlist-button').on('click', (e) => {
         $('.jukebox-container .songs').hide()
         $('.jukebox-container .music-playlists').show()
    })
    $('#song-button').on('click', (e) => {
        $('.jukebox-container .music-playlists').hide()
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
        $('.search-overlay').show()

    })

    $('.close').on('click', (e) => {
        $('.search-overlay, .lyrics-overlay, .song-overlay, .playlist-overlay').hide()

    })


    $('#add-song').on('click', (e) => {
       $('.song-overlay').show()
       $.ajax({
          type: 'POST',
          url: '/your-music',
          data: $('form').serialize()
       })
       

    })

    $('.add-playlist').on('click', (e) => {
        $('.playlist-overlay').show()
        $.ajax({
            type: 'POST',
            url: '/playlists',
            data: $('form').serialize()
        })

    })

    //background: #E5E59E;
    // background: rgba(236, 61, 187, 0.4);
    //    background: rgba(217, 45, 45, 0.4);

})