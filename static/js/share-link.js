document.getElementById('shareButton').addEventListener('click', function() {
    $('#platformModal').modal('show');
});

function shareOnPlatform(platform) {
    var shareURL = "{{ request.build_absolute_uri }}";

    switch (platform) {
        case 'facebook':
            window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(shareURL));
            break;
        case 'twitter':
            window.open('https://twitter.com/intent/tweet?url=' + encodeURIComponent(shareURL) + '&text=' + encodeURIComponent("Check out this content: " + "{{ content.title }}"));
            break;
        case 'linkedin':
            window.open('https://www.linkedin.com/shareArticle?url=' + encodeURIComponent(shareURL) + '&title=' + encodeURIComponent("{{ content.title }}"));
            break;
    }

    // Copy Link to clipboard
    var copyText = document.createElement('textarea');
    copyText.value = shareURL;
    document.body.appendChild(copyText);
    copyText.select();
    document.execCommand('copy');
    document.body.removeChild(copyText);

    alert('Shared on ' + platform + ' and Link copied to clipboard!');
    $('#platformModal').modal('hide');
}