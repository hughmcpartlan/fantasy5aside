$("#jersey-filler input[type='submit']").on('click', function(event) {

			event.preventDefault();
			var nameArtist = $("#jersey-filler #artist-query").val();
			var urlSpotifyArtist = "https://api.spotify.com/v1/search?type=artist&query=" + nameArtist;

			$.ajax ({
				url : urlSpotifyArtist,
				dataType : "json"
			})
			.success (function( artistsData ) {
				var contentSelect = "<option disabled selected>Select artist</option>";

				$.each( artistsData.artists.items, function(i, elem) {
					contentSelect += '<option value=' + elem.id +'">' + elem.name + '</option>';


				});
				$("#jersey-filler select").html(contentSelect);

			})

		});